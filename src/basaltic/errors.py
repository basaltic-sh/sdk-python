"""Structured SDK errors; transport and OAuth failures never retain raw requests."""

import re


class BasalticError(Exception):
    """Base class for SDK failures."""


class ProtocolError(BasalticError):
    pass


class TransportError(BasalticError):
    pass


class RequestTimeoutError(TransportError):
    pass


class AuthenticationError(BasalticError):
    def __init__(self, status_code: int = 0, error_code: str = "") -> None:
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(f"Token exchange failed (HTTP {status_code}, code {error_code}).")


class AmbiguousReferenceError(BasalticError):
    def __init__(self) -> None:
        super().__init__("Reference matches multiple resources; narrow its parent scope.")


class ApiError(BasalticError):
    def __init__(
        self,
        status_code: int,
        error_code: str,
        message: str,
        request_id: str,
        operation_id: str,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self.error_code = error_code
        self.request_id = request_id
        self.operation_id = operation_id
        self.headers = dict(headers or {})
        super().__init__(f"{operation_id}: {message} (HTTP {status_code}, request {request_id})")

    def is_not_found(self) -> bool:
        return self.status_code in (404, 410)

    def is_unauthorized(self) -> bool:
        return self.status_code == 401

    def is_quota_exceeded(self) -> bool:
        return bool(re.search(r"(?:^|_)(?:QUOTA|LIMIT)_EXCEEDED$", self.error_code))

    def is_access_denied(self) -> bool:
        return self.status_code == 403 and not self.is_quota_exceeded()

    def is_conflict(self) -> bool:
        return self.status_code == 409

    def is_invalid_input(self) -> bool:
        return self.status_code in (400, 422)

    def is_rate_limited(self) -> bool:
        return self.status_code == 429

    def is_transient(self) -> bool:
        return self.status_code == 429 or self.status_code >= 500
