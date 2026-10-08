"""Shared wire preparation and response decisions for both HTTP drivers."""

from __future__ import annotations

import json
import math
import re
import time
from collections.abc import AsyncIterable, Iterable, Mapping
from dataclasses import dataclass
from datetime import timezone
from email.utils import parsedate_to_datetime
from typing import Any, TypeAlias
from urllib.parse import quote, urlsplit, urlunsplit

import httpx

from ._version import __version__
from .config import Config, RequestOptions, attempt_count, positive_timeout
from .errors import ApiError, ProtocolError
from .response import ApiResponse, Page

BinaryBody: TypeAlias = bytes | bytearray | memoryview | Iterable[bytes]
AsyncBinaryBody: TypeAlias = bytes | bytearray | memoryview | AsyncIterable[bytes]


class Unset:
    """Distinguishes an omitted optional body from explicit JSON null."""


UNSET = Unset()


@dataclass(frozen=True)
class WebSocketConnection:
    url: str
    headers: Mapping[str, str]


@dataclass(frozen=True)
class Operation:
    id: str
    method: str
    path: str
    authenticated: bool
    requiredQuery: tuple[str, ...] | list[str]
    requiredHeaders: tuple[str, ...] | list[str]
    queryEncoding: Mapping[str, Mapping[str, object]]
    bodyRequired: bool
    contentType: str
    accept: str
    itemsKey: str = ""


def encode_query(
    values: Mapping[str, object], encodings: Mapping[str, Mapping[str, object]] | None = None
) -> str:
    def scalar(value: object) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("Query values must be finite.")
        if not isinstance(value, (str, int, float)):
            raise TypeError("Query values must be scalars or lists of scalars.")
        return str(value)

    pairs: list[str] = []
    for key, value in values.items():
        if value is None or isinstance(value, Unset):
            continue
        prefix = quote(key, safe="") + "="
        if isinstance(value, (list, tuple)):
            items = [scalar(item) for item in value]
            encoding = (encodings or {}).get(key, {})
            if encoding.get("explode", True):
                pairs.extend(prefix + quote(item, safe="") for item in items)
            else:
                separator = {"spaceDelimited": " ", "pipeDelimited": "|"}.get(
                    str(encoding.get("style")), ","
                )
                pairs.append(prefix + quote(separator.join(items), safe=""))
        else:
            pairs.append(prefix + quote(scalar(value), safe=""))
    return "&".join(pairs)


@dataclass
class Prepared:
    operation: Operation
    url: str
    headers: dict[str, str]
    body: Any
    streaming: bool
    max_attempts: int
    timeout: float
    repeatable: bool

    def request(self, token: str) -> httpx.Request:
        headers = dict(self.headers)
        if token:
            headers["Authorization"] = "Bearer " + token
        return httpx.Request(
            self.operation.method,
            self.url,
            headers=headers,
            content=self.body,
            extensions={"timeout": httpx.Timeout(self.timeout).as_dict()},
        )

    def websocket(self, token: str) -> WebSocketConnection:
        headers = dict(self.headers)
        if token:
            headers["Authorization"] = "Bearer " + token
        u = urlsplit(self.url)
        return WebSocketConnection(
            urlunsplit(("wss" if u.scheme == "https" else "ws", u.netloc, u.path, u.query, "")),
            headers,
        )


_RESERVED = {
    "authorization",
    "host",
    "cookie",
    "content-length",
    "content-type",
    "accept",
    "user-agent",
    "x-account-id",
    "idempotency-key",
}


def prepare(
    config: Config,
    service: str,
    endpoint: str,
    operation: Operation,
    path: Mapping[str, str],
    body: object,
    query: Mapping[str, object] | None,
    options: RequestOptions | None,
    *,
    asynchronous: bool = False,
) -> Prepared:
    opts = options or RequestOptions()
    values = query or {}
    if operation.bodyRequired and (isinstance(body, Unset) or body is None):
        raise ValueError(f"{operation.id}: request body is required.")
    for key in operation.requiredQuery:
        if values.get(key) is None:
            raise ValueError(f"{operation.id}: missing required query parameter {key}.")

    def replace(match: re.Match[str]) -> str:
        value = path.get(match[1], "")
        if not isinstance(value, str) or value in ("", ".", ".."):
            raise ValueError(f"{operation.id}: invalid path parameter {match[1]}.")
        return quote(value, safe="")

    route = re.sub(r"\{([^}]+)\}", replace, operation.path)
    qs = encode_query(values, operation.queryEncoding)
    url = config.endpoint(service, endpoint) + route + ("?" + qs if qs else "")
    headers = httpx.Headers(
        {"Accept": operation.accept, "User-Agent": f"basaltic-python/{__version__}"}
    )
    account = opts.account_id if opts.account_id is not None else config.account_id
    if account:
        headers["X-Account-Id"] = account
    if opts.idempotency_key is not None:
        if not opts.idempotency_key.strip():
            raise ValueError("idempotency_key must not be empty.")
        headers["Idempotency-Key"] = opts.idempotency_key
    for key, value in opts.headers.items():
        if key.lower() in _RESERVED:
            raise ValueError(f"Cannot override managed header {key}.")
        if re.search(r"[\r\n\x00]", key + value):
            raise ValueError("Invalid HTTP header.")
        headers[key] = value
    for key, value in headers.items():
        if re.search(r"[\x00-\x1f\x7f]", key + value):
            raise ValueError("Invalid HTTP header.")
    for key in operation.requiredHeaders:
        if not headers.get(key):
            raise ValueError(f"{operation.id}: missing required header {key}.")
    content: object = None
    streaming = False
    if not isinstance(body, Unset):
        if operation.contentType == "application/json":
            content = json.dumps(
                body, ensure_ascii=False, separators=(",", ":"), allow_nan=False
            ).encode()
        elif operation.contentType == "application/x-www-form-urlencoded":
            if not isinstance(body, Mapping):
                raise TypeError("Form body must be a mapping.")
            content = encode_query(body).encode()
        elif isinstance(body, (bytes, bytearray, memoryview)):
            content = bytes(body)
        elif isinstance(body, str):
            content = body.encode()
        elif not isinstance(body, Mapping) and isinstance(
            body, AsyncIterable if asynchronous else Iterable
        ):
            content, streaming = body, True
        else:
            raise TypeError("Binary body must be bytes or a matching sync/async byte iterable.")
        if operation.contentType:
            headers["Content-Type"] = operation.contentType
    limit = attempt_count(
        opts.max_attempts if opts.max_attempts is not None else config.max_attempts
    )
    return Prepared(
        operation,
        url,
        dict(headers),
        content,
        streaming,
        1 if streaming else limit,
        positive_timeout(opts.timeout if opts.timeout is not None else config.timeout),
        operation.method in ("GET", "HEAD", "OPTIONS", "PUT", "DELETE")
        or opts.idempotency_key is not None,
    )


def backoff(config: Config, attempt: int, random_value: float) -> float:
    if not math.isfinite(random_value):
        raise ValueError("Random source must return a finite number.")
    return min(1, max(0, random_value)) * min(
        config.max_delay, float(config.base_delay * 2 ** (attempt - 1))
    )


def retry_delay(
    config: Config, attempt: int, value: str | None, random_value: float, now: float | None = None
) -> float | None:
    if not value:
        return backoff(config, attempt, random_value)
    parsed = 0.0
    try:
        if value.isdigit():
            parsed = float(value)
        else:
            date = parsedate_to_datetime(value)
            if date.tzinfo is None:
                date = date.replace(tzinfo=timezone.utc)
            parsed = date.timestamp() - (time.time() if now is None else now)
    except (ValueError, OverflowError, TypeError):
        return backoff(config, attempt, random_value)
    return max(0, parsed) if parsed <= config.max_delay else None


def api_error(response: httpx.Response, raw: bytes, operation_id: str) -> ApiError:
    data: object = None
    try:
        data = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        pass
    error = data.get("error", {}) if isinstance(data, dict) else {}
    if not isinstance(error, dict):
        error = {}
    code, message, request_id = error.get("code"), error.get("message"), error.get("request_id")
    return ApiError(
        response.status_code,
        code if isinstance(code, str) else "",
        message if isinstance(message, str) else "Unexpected API response",
        request_id if isinstance(request_id, str) else response.headers.get("X-Request-Id", ""),
        operation_id,
        dict(response.headers),
    )


def decoded(response: httpx.Response, raw: bytes, op: Operation, kind: str) -> object:
    data: object = None
    valid = True
    try:
        data = json.loads(raw) if raw.strip() else {}
    except (ValueError, UnicodeDecodeError):
        valid = False
    if not valid or not isinstance(data, (dict, list)):
        raise ProtocolError(f"{op.id}: expected a JSON object or array.")
    if kind == "page":
        page: Page[Any, Any] = Page(data, response, op.itemsKey)
        _ = page.items
        return page
    return ApiResponse(data, response)
