"""Explicit and environment-based configuration shared by all services."""

from __future__ import annotations

import math
import os
import re
from collections.abc import Mapping
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import TYPE_CHECKING
from urllib.parse import urlsplit
from uuid import uuid4

if TYPE_CHECKING:
    from .auth import AsyncTokenProvider, TokenProvider


def validate_url(value: str) -> str:
    try:
        u = urlsplit(value)
        valid = u.scheme in ("http", "https") and u.hostname and u.port != 0
    except ValueError:
        valid = False
    if (
        not valid
        or u.username
        or u.password
        or u.query
        or u.fragment
        or re.search(r"[\s\x00-\x1f\x7f]", value)
    ):
        raise ValueError(
            "Endpoint must be an absolute HTTP(S) URL without credentials, query or fragment."
        )
    return value.rstrip("/")


def validate_token(value: str) -> str:
    if (
        not isinstance(value, str)
        or not value
        or not value.isascii()
        or re.search(r"[\s\x00-\x1f\x7f]", value)
    ):
        raise ValueError("A nonempty bearer token without whitespace is required.")
    return value


def positive_timeout(value: float) -> float:
    if isinstance(value, bool) or not math.isfinite(value) or value <= 0:
        raise ValueError("timeout must be a finite positive number of seconds.")
    return value


def attempt_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 10:
        raise ValueError("max_attempts must be an integer between 1 and 10.")
    return value


@dataclass(frozen=True, kw_only=True)
class RequestOptions:
    account_id: str | None = None
    idempotency_key: str | None = None
    headers: Mapping[str, str] = field(default_factory=dict)
    timeout: float | None = None
    max_attempts: int | None = None


@dataclass(frozen=True, kw_only=True)
class Config:
    access_key_id: str | None = field(default=None, repr=False)
    secret_access_key: str | None = field(default=None, repr=False)
    access_token: str | None = field(default=None, repr=False)
    token_provider: TokenProvider | AsyncTokenProvider | None = field(default=None, repr=False)
    anonymous: bool = False
    region: str | None = None
    account_id: str | None = None
    domain: str | None = None
    endpoints: Mapping[str, str] = field(default_factory=dict)
    token_url: str | None = None
    read_environment: bool = True
    timeout: float = 30.0
    max_attempts: int = 4
    base_delay: float = 0.2
    max_delay: float = 20.0

    def __post_init__(self) -> None:
        env = os.environ if self.read_environment else {}
        for key in ("region", "account_id", "domain"):
            if getattr(self, key) is None:
                object.__setattr__(
                    self,
                    key,
                    env.get("BASALTIC_" + key.upper(), "basaltic.sh" if key == "domain" else ""),
                )
        if not re.fullmatch(
            r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)*[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?",
            self.domain or "",
        ):
            raise ValueError("Invalid API domain.")
        endpoints = {
            k.removeprefix("BASALTIC_ENDPOINT_URL_").lower(): v
            for k, v in env.items()
            if k.startswith("BASALTIC_ENDPOINT_URL_") and v
        }
        endpoints.update(self.endpoints)
        endpoints = {key: validate_url(value) for key, value in endpoints.items()}
        object.__setattr__(self, "endpoints", MappingProxyType(endpoints))
        explicit_keys = self.access_key_id is not None or self.secret_access_key is not None
        if self.access_token is None:
            object.__setattr__(
                self, "access_token", "" if explicit_keys else env.get("BASALTIC_ACCESS_TOKEN", "")
            )
        for key in ("access_key_id", "secret_access_key"):
            if getattr(self, key) is None:
                object.__setattr__(self, key, env.get("BASALTIC_" + key.upper(), ""))
        if (
            not self.anonymous
            and not self.token_provider
            and not self.access_token
            and not (self.access_key_id and self.secret_access_key)
        ):
            raise ValueError(
                "Configure an access key pair, bearer token, token provider or explicit anonymous access."
            )
        if self.access_token:
            validate_token(self.access_token)
        positive_timeout(self.timeout)
        attempt_count(self.max_attempts)
        if any(not math.isfinite(v) or v < 0 for v in (self.base_delay, self.max_delay)):
            raise ValueError("Retry delays must be finite and nonnegative.")

    def endpoint(self, service: str, template: str) -> str:
        if service in self.endpoints:
            return self.endpoints[service]
        if "{region}" in template and not re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", self.region or ""
        ):
            raise ValueError(f"A valid region is required for {service}.")
        return validate_url(
            template.replace("basaltic.sh", self.domain or "").replace(
                "{region}", self.region or ""
            )
        )


def new_idempotency_key() -> str:
    """Create once per logical mutation and reuse when retrying that mutation."""
    return str(uuid4())
