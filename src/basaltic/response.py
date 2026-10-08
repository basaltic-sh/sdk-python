"""Response envelopes, pagination and resource reference helpers."""

from __future__ import annotations

import re
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, cast

import httpx

from .errors import AmbiguousReferenceError, ApiError, ProtocolError

T = TypeVar("T", covariant=True)
Item = TypeVar("Item", covariant=True)


@dataclass(frozen=True)
class ApiResponse(Generic[T]):
    data: T
    response: httpx.Response

    @property
    def request_id(self) -> str:
        return str(self.response.headers.get("X-Request-Id", ""))

    @property
    def status_code(self) -> int:
        return self.response.status_code


@dataclass(frozen=True)
class Page(ApiResponse[T], Generic[T, Item]):
    items_key: str

    @property
    def items(self) -> list[Item]:
        if not isinstance(self.data, dict) or not isinstance(self.data.get(self.items_key), list):
            raise ProtocolError("List response is missing its items array.")
        return cast(list[Item], self.data[self.items_key])

    @property
    def has_more(self) -> bool:
        meta = self.data.get("meta") if isinstance(self.data, dict) else None
        return isinstance(meta, dict) and meta.get("has_more") is True

    @property
    def marker(self) -> str:
        meta = self.data.get("meta") if isinstance(self.data, dict) else None
        value = meta.get("marker") if isinstance(meta, dict) else None
        return value if isinstance(value, str) else ""


def iterate_pages(fetch: Callable[[str], Page[Any, Item]], marker: str = "") -> Iterator[Item]:
    seen = {marker}
    while True:
        page = fetch(marker)
        yield from page.items
        if not page.has_more:
            return
        marker = next_marker(page, seen)


async def aiterate_pages(
    fetch: Callable[[str], Awaitable[Page[Any, Item]]], marker: str = ""
) -> AsyncIterator[Item]:
    seen = {marker}
    while True:
        page = await fetch(marker)
        for item in page.items:
            yield item
        if not page.has_more:
            return
        marker = next_marker(page, seen)


def next_marker(page: Page[Any, Any], seen: set[str]) -> str:
    marker = page.marker
    if not marker or marker in seen:
        raise ProtocolError("Pagination did not advance; refusing a truncated or repeated walk.")
    seen.add(marker)
    return marker


def reference_scope(scope: Mapping[str, object] | None) -> dict[str, object]:
    return {k: v for k, v in (scope or {}).items() if k not in ("name", "crn", "marker")}


def reference_filter(reference: str, has_name: bool) -> dict[str, str] | None:
    if not reference:
        raise ValueError("A nonempty resource reference is required.")
    if re.fullmatch(r"[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}", reference):
        return None
    kind = "crn" if reference.startswith("crn:") else "name"
    if kind == "crn" and len(reference.split(":")) != 5:
        raise ValueError("A CRN must have five colon-separated segments.")
    if kind == "name" and not has_name:
        raise ValueError("This resource requires a UUID or CRN.")
    return {kind: reference}


def unwrap_reference(result: ApiResponse[Any], envelope: str | None) -> ApiResponse[Any]:
    data = result.data.get(envelope) if envelope and isinstance(result.data, dict) else result.data
    if not isinstance(data, dict):
        raise ProtocolError("Reference lookup is missing its resource envelope.")
    return ApiResponse(data, result.response)


def select_reference(page: Page[Any, Any]) -> ApiResponse[Any]:
    if len(page.items) > 1 or page.has_more:
        raise AmbiguousReferenceError()
    if not page.items:
        raise ApiError(
            404,
            "REFERENCE_NOT_FOUND",
            "No resource matches the reference.",
            page.request_id,
            "resolve_reference",
        )
    if not isinstance(page.items[0], dict):
        raise ProtocolError("Reference lookup returned a non-object resource.")
    return ApiResponse(page.items[0], page.response)


def resolve_reference(
    reference: str,
    get: Callable[[str], ApiResponse[Any]],
    listing: Callable[[dict[str, str]], Page[Any, Any]],
    has_name: bool,
    envelope: str | None = None,
) -> ApiResponse[Any]:
    match = reference_filter(reference, has_name)
    return (
        unwrap_reference(get(reference), envelope)
        if match is None
        else select_reference(listing(match))
    )


async def aresolve_reference(
    reference: str,
    get: Callable[[str], Awaitable[ApiResponse[Any]]],
    listing: Callable[[dict[str, str]], Awaitable[Page[Any, Any]]],
    has_name: bool,
    envelope: str | None = None,
) -> ApiResponse[Any]:
    match = reference_filter(reference, has_name)
    return (
        unwrap_reference(await get(reference), envelope)
        if match is None
        else select_reference(await listing(match))
    )
