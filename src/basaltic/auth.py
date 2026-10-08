"""Cached credentials with thread-safe and asyncio single-flight refresh."""

from __future__ import annotations

import asyncio
import base64
import json
import math
import threading
import time
from collections.abc import Callable
from typing import Protocol

import httpx

from .config import positive_timeout, validate_token, validate_url
from .errors import AuthenticationError


class TokenProvider(Protocol):
    def get_token(self) -> str: ...


class AsyncTokenProvider(Protocol):
    async def get_token(self) -> str: ...


class StaticToken:
    def __init__(self, token: str) -> None:
        self.__token = validate_token(token)

    def get_token(self) -> str:
        return self.__token


class AsyncStaticToken:
    def __init__(self, token: str) -> None:
        self.__token = validate_token(token)

    async def get_token(self) -> str:
        return self.__token


def _token_response(status: int, raw: bytes) -> tuple[str, float]:
    data: object = None
    try:
        data = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        pass
    if status != 200 or not isinstance(data, dict):
        code = data.get("error", "") if isinstance(data, dict) else ""
        raise AuthenticationError(
            status,
            code if code in ("invalid_client", "invalid_grant", "temporarily_unavailable") else "",
        )
    token, lifetime, kind = (
        data.get("access_token"),
        data.get("expires_in", 900),
        data.get("token_type", "Bearer"),
    )
    valid = isinstance(token, str) and isinstance(kind, str) and kind.lower() == "bearer"
    try:
        seconds = float(lifetime)
        if not math.isfinite(seconds) or seconds <= 0 or isinstance(lifetime, bool):
            valid = False
        if valid and isinstance(token, str):
            validate_token(token)
    except (ValueError, TypeError, OverflowError):
        valid = False
    if not valid or not isinstance(token, str):
        raise AuthenticationError(status)
    return token, seconds - min(300, seconds * 0.1)


def _request(key: str, secret: str, url: str, timeout: float) -> httpx.Request:
    if not key or ":" in key or not secret:
        raise ValueError("A valid access key ID and secret are required.")
    encoded = base64.b64encode((key + ":" + secret).encode()).decode()
    return httpx.Request(
        "POST",
        validate_url(url),
        content=b"grant_type=client_credentials",
        headers={
            "Authorization": "Basic " + encoded,
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        extensions={"timeout": httpx.Timeout(positive_timeout(timeout)).as_dict()},
    )


class ClientCredentials:
    def __init__(
        self,
        *,
        access_key_id: str,
        secret_access_key: str,
        token_url: str,
        http_client: httpx.Client,
        timeout: float = 30,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        # Validate without retaining the prepared request, whose repr may expose headers.
        _request(access_key_id, secret_access_key, token_url, timeout)
        self.__key, self.__secret, self.__url = access_key_id, secret_access_key, token_url
        self._http, self._timeout, self._clock = http_client, timeout, clock
        self._lock = threading.Lock()
        self.__cached, self._refresh_at = "", 0.0

    def get_token(self) -> str:
        with self._lock:
            if self.__cached and self._clock() < self._refresh_at:
                return self.__cached
            now = self._clock()
            failure: AuthenticationError | None = None
            response: httpx.Response | None = None
            try:
                response = self._http.send(
                    _request(self.__key, self.__secret, self.__url, self._timeout),
                    auth=None,
                    follow_redirects=False,
                    stream=True,
                )
                raw = bytearray()
                for chunk in response.iter_bytes():
                    raw.extend(chunk[: 1048577 - len(raw)])
                    if len(raw) > 1048576:
                        break
                if len(raw) > 1048576:
                    raise AuthenticationError(response.status_code)
                token, ttl = _token_response(response.status_code, bytes(raw))
            except (httpx.HTTPError, AuthenticationError) as error:
                failure = (
                    AuthenticationError(error.status_code, error.error_code)
                    if isinstance(error, AuthenticationError)
                    else AuthenticationError()
                )
            finally:
                if response is not None:
                    response.close()
            if failure is not None:
                raise failure
            self.__cached, self._refresh_at = token, now + ttl
            return token

    def invalidate(self, rejected_token: str | None = None) -> None:
        with self._lock:
            if rejected_token is None or rejected_token == self.__cached:
                self.__cached, self._refresh_at = "", 0.0


class AsyncClientCredentials:
    def __init__(
        self,
        *,
        access_key_id: str,
        secret_access_key: str,
        token_url: str,
        http_client: httpx.AsyncClient,
        timeout: float = 30,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        _request(access_key_id, secret_access_key, token_url, timeout)
        self.__key, self.__secret, self.__url = access_key_id, secret_access_key, token_url
        self._http, self._timeout, self._clock = http_client, timeout, clock
        self.__cached, self._refresh_at = "", 0.0
        self._pending: asyncio.Task[str] | None = None

    async def get_token(self) -> str:
        if self.__cached and self._clock() < self._refresh_at:
            return self.__cached
        # There is no await between checking and assigning the task; creation is
        # atomic within the client's event loop. A caller's cancellation is isolated.
        if self._pending is None:
            task = asyncio.create_task(self._refresh())
            self._pending = task

            def done(finished: asyncio.Task[str]) -> None:
                if self._pending is finished:
                    self._pending = None
                if not finished.cancelled():
                    finished.exception()

            task.add_done_callback(done)
        return await asyncio.shield(self._pending)

    def invalidate(self, rejected_token: str | None = None) -> None:
        if rejected_token is None or rejected_token == self.__cached:
            self.__cached, self._refresh_at = "", 0.0

    async def aclose(self) -> None:
        if self._pending is not None:
            pending = self._pending
            pending.cancel()
            try:
                await pending
            except asyncio.CancelledError:
                pass

    async def _refresh(self) -> str:
        now = self._clock()
        failure: AuthenticationError | None = None
        response: httpx.Response | None = None
        try:
            response = await self._http.send(
                _request(self.__key, self.__secret, self.__url, self._timeout),
                auth=None,
                follow_redirects=False,
                stream=True,
            )
            raw = bytearray()
            async for chunk in response.aiter_bytes():
                raw.extend(chunk[: 1048577 - len(raw)])
                if len(raw) > 1048576:
                    break
            if len(raw) > 1048576:
                raise AuthenticationError(response.status_code)
            token, ttl = _token_response(response.status_code, bytes(raw))
        except (httpx.HTTPError, AuthenticationError) as error:
            failure = (
                AuthenticationError(error.status_code, error.error_code)
                if isinstance(error, AuthenticationError)
                else AuthenticationError()
            )
        finally:
            if response is not None:
                await response.aclose()
        if failure is not None:
            raise failure
        self.__cached, self._refresh_at = token, now + ttl
        return token
