"""HTTP drivers. Shared preparation keeps synchronous and asyncio semantics aligned."""

from __future__ import annotations

import asyncio
import random
import time
from collections.abc import Awaitable, Callable, Mapping
from typing import Any

import httpx

from ._common import UNSET, Operation, api_error, backoff, decoded, prepare, retry_delay
from .auth import AsyncTokenProvider, TokenProvider
from .config import Config, RequestOptions, validate_token
from .errors import RequestTimeoutError, TransportError


class SyncTransport:
    def __init__(self, config: Config, http: httpx.Client, provider: TokenProvider | None) -> None:
        self.config, self.http, self.provider = config, http, provider
        self.sleep: Callable[[float], None] = time.sleep
        self.random: Callable[[], float] = random.random

    def _token(self, authenticated: bool) -> str:
        if not authenticated:
            return ""
        if self.provider is None:
            raise ValueError("Anonymous access cannot call an authenticated operation.")
        return validate_token(self.provider.get_token())

    def request(
        self,
        service: str,
        endpoint: str,
        op: Operation,
        kind: str,
        path: Mapping[str, str],
        body: object = UNSET,
        query: Mapping[str, object] | None = None,
        options: RequestOptions | None = None,
    ) -> Any:
        prepared = prepare(self.config, service, endpoint, op, path, body, query, options)
        if kind == "websocket":
            return prepared.websocket(self._token(op.authenticated))
        refreshed = False
        for attempt in range(1, prepared.max_attempts + 1):
            response: httpx.Response | None = None
            returned_stream = False
            delay: float | None = None
            failure: TransportError | None = None
            try:
                token = self._token(op.authenticated)
                response = self.http.send(
                    prepared.request(token), auth=None, stream=True, follow_redirects=False
                )
                if response.is_success:
                    if kind == "binary":
                        returned_stream = True
                        return response
                    if kind == "discard":
                        return None
                    return decoded(response, response.read(), op, kind)
                invalidate = getattr(self.provider, "invalidate", None)
                if (
                    response.status_code == 401
                    and op.authenticated
                    and not refreshed
                    and attempt < prepared.max_attempts
                    and callable(invalidate)
                ):
                    invalidate(token)
                    refreshed, delay = True, 0.0
                elif (
                    prepared.repeatable
                    and attempt < prepared.max_attempts
                    and response.status_code in (429, 500, 502, 503, 504)
                ):
                    delay = retry_delay(
                        self.config, attempt, response.headers.get("Retry-After"), self.random()
                    )
                if delay is None:
                    raw = bytearray()
                    for chunk in response.iter_bytes():
                        raw.extend(chunk[: 1048576 - len(raw)])
                        if len(raw) >= 1048576:
                            break
                    raise api_error(response, bytes(raw), op.id)
            except httpx.HTTPError as error:
                failure = (
                    RequestTimeoutError(f"{op.id}: HTTP timeout.")
                    if isinstance(error, httpx.TimeoutException)
                    else TransportError(f"{op.id}: HTTP transport failed.")
                )
            finally:
                if response is not None and not returned_stream:
                    response.close()
            # Raise outside the HTTP exception handler so no credential-bearing
            # request or exception survives through __context__ or __cause__.
            if failure is not None:
                if not prepared.repeatable or attempt == prepared.max_attempts:
                    raise failure
                delay = backoff(self.config, attempt, self.random())
            self.sleep(delay or 0.0)
        raise TransportError("Request attempts exhausted.")


class AsyncTransport:
    def __init__(
        self, config: Config, http: httpx.AsyncClient, provider: AsyncTokenProvider | None
    ) -> None:
        self.config, self.http, self.provider = config, http, provider
        self.sleep: Callable[[float], Awaitable[None]] = asyncio.sleep
        self.random: Callable[[], float] = random.random

    async def _token(self, authenticated: bool) -> str:
        if not authenticated:
            return ""
        if self.provider is None:
            raise ValueError("Anonymous access cannot call an authenticated operation.")
        return validate_token(await self.provider.get_token())

    async def request(
        self,
        service: str,
        endpoint: str,
        op: Operation,
        kind: str,
        path: Mapping[str, str],
        body: object = UNSET,
        query: Mapping[str, object] | None = None,
        options: RequestOptions | None = None,
    ) -> Any:
        prepared = prepare(
            self.config, service, endpoint, op, path, body, query, options, asynchronous=True
        )
        if kind == "websocket":
            return prepared.websocket(await self._token(op.authenticated))
        refreshed = False
        for attempt in range(1, prepared.max_attempts + 1):
            response: httpx.Response | None = None
            returned_stream = False
            delay: float | None = None
            failure: TransportError | None = None
            try:
                token = await self._token(op.authenticated)
                response = await self.http.send(
                    prepared.request(token), auth=None, stream=True, follow_redirects=False
                )
                if response.is_success:
                    if kind == "binary":
                        returned_stream = True
                        return response
                    if kind == "discard":
                        return None
                    return decoded(response, await response.aread(), op, kind)
                invalidate = getattr(self.provider, "invalidate", None)
                if (
                    response.status_code == 401
                    and op.authenticated
                    and not refreshed
                    and attempt < prepared.max_attempts
                    and callable(invalidate)
                ):
                    invalidate(token)
                    refreshed, delay = True, 0.0
                elif (
                    prepared.repeatable
                    and attempt < prepared.max_attempts
                    and response.status_code in (429, 500, 502, 503, 504)
                ):
                    delay = retry_delay(
                        self.config, attempt, response.headers.get("Retry-After"), self.random()
                    )
                if delay is None:
                    raw = bytearray()
                    async for chunk in response.aiter_bytes():
                        raw.extend(chunk[: 1048576 - len(raw)])
                        if len(raw) >= 1048576:
                            break
                    raise api_error(response, bytes(raw), op.id)
            except httpx.HTTPError as error:
                failure = (
                    RequestTimeoutError(f"{op.id}: HTTP timeout.")
                    if isinstance(error, httpx.TimeoutException)
                    else TransportError(f"{op.id}: HTTP transport failed.")
                )
            finally:
                if response is not None and not returned_stream:
                    await response.aclose()
            if failure is not None:
                if not prepared.repeatable or attempt == prepared.max_attempts:
                    raise failure
                delay = backoff(self.config, attempt, self.random())
            await self.sleep(delay or 0.0)
        raise TransportError("Request attempts exhausted.")
