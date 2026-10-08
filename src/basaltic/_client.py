"""HTTP client lifetime and shared credential configuration."""

from __future__ import annotations

from collections.abc import Mapping
from types import TracebackType
from typing import Self, TypedDict, Unpack, cast

import httpx

from ._transport import AsyncTransport, SyncTransport
from .auth import (
    AsyncClientCredentials,
    AsyncStaticToken,
    AsyncTokenProvider,
    ClientCredentials,
    StaticToken,
    TokenProvider,
)
from .config import Config


class ClientOptions(TypedDict, total=False):
    access_key_id: str
    secret_access_key: str
    access_token: str
    anonymous: bool
    region: str
    account_id: str
    domain: str
    endpoints: Mapping[str, str]
    token_url: str
    read_environment: bool
    timeout: float
    max_attempts: int
    base_delay: float
    max_delay: float


class SyncClientBase:
    def __init__(
        self,
        config: Config | None = None,
        *,
        http_client: httpx.Client | None = None,
        token_provider: TokenProvider | None = None,
        **options: Unpack[ClientOptions],
    ) -> None:
        if config is not None and (options or token_provider is not None):
            raise ValueError("Pass either Config or configuration keywords.")
        self.config = config or Config(token_provider=token_provider, **options)
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.Client(trust_env=False)
        provider = cast(TokenProvider | None, self.config.token_provider)
        if self.config.anonymous:
            provider = None
        elif provider is None:
            if self.config.access_token:
                provider = StaticToken(self.config.access_token)
            else:
                provider = ClientCredentials(
                    access_key_id=self.config.access_key_id or "",
                    secret_access_key=self.config.secret_access_key or "",
                    token_url=self.config.token_url
                    or self.config.endpoint("iam", "https://iam.basaltic.sh") + "/v1/oauth/token",
                    http_client=self._http,
                    timeout=self.config.timeout,
                )
        self._transport = SyncTransport(self.config, self._http, provider)

    def close(self) -> None:
        if self._owns_http:
            self._http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncClientBase:
    def __init__(
        self,
        config: Config | None = None,
        *,
        http_client: httpx.AsyncClient | None = None,
        token_provider: AsyncTokenProvider | None = None,
        **options: Unpack[ClientOptions],
    ) -> None:
        if config is not None and (options or token_provider is not None):
            raise ValueError("Pass either Config or configuration keywords.")
        self.config = config or Config(token_provider=token_provider, **options)
        self._owns_http = http_client is None
        self._http = http_client if http_client is not None else httpx.AsyncClient(trust_env=False)
        provider = cast(AsyncTokenProvider | None, self.config.token_provider)
        self._owns_provider = False
        if self.config.anonymous:
            provider = None
        elif provider is None:
            if self.config.access_token:
                provider = AsyncStaticToken(self.config.access_token)
            else:
                provider = AsyncClientCredentials(
                    access_key_id=self.config.access_key_id or "",
                    secret_access_key=self.config.secret_access_key or "",
                    token_url=self.config.token_url
                    or self.config.endpoint("iam", "https://iam.basaltic.sh") + "/v1/oauth/token",
                    http_client=self._http,
                    timeout=self.config.timeout,
                )
                self._owns_provider = True
        self._transport = AsyncTransport(self.config, self._http, provider)

    async def aclose(self) -> None:
        provider = self._transport.provider
        if self._owns_provider and isinstance(provider, AsyncClientCredentials):
            await provider.aclose()
        if self._owns_http:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()
