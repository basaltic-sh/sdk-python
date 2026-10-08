"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import audit as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    aresolve_reference,
    iterate_pages,
    reference_scope,
    resolve_reference,
)

_OPS = {
    "getAuditLog": Operation(
        id="getAuditLog",
        method="GET",
        path="/v1/audit-logs/{log_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listAuditLogs": Operation(
        id="listAuditLogs",
        method="GET",
        path="/v1/audit-logs",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "actor": {"style": "form", "explode": True},
            "actor_type": {"style": "form", "explode": True},
            "action": {"style": "form", "explode": True},
            "resource_type": {"style": "form", "explode": True},
            "resource": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "ip_address": {"style": "form", "explode": True},
            "from": {"style": "form", "explode": True},
            "to": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="audit_logs",
    ),
}


class AuditService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_audit_log(
        self, log_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAuditLogResponse]:
        "Get audit log entry"
        return cast(
            ApiResponse[m.GetAuditLogResponse],
            self._transport.request(
                "audit",
                "https://audit.basaltic.sh",
                _OPS["getAuditLog"],
                "json",
                {"log_id": log_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_audit_log_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAuditLogScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAuditLogResource]:
        return cast(
            ApiResponse[m.GetAuditLogResource],
            resolve_reference(
                reference,
                lambda id: self.get_audit_log(id, options=options),
                lambda match: self.list_audit_logs(
                    query=cast(
                        m.ListAuditLogsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                False,
                "audit_log",
            ),
        )

    def list_audit_logs(
        self, *, query: m.ListAuditLogsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAuditLogsResponse, m.ListAuditLogsItem]:
        "List audit logs"
        return cast(
            Page[m.ListAuditLogsResponse, m.ListAuditLogsItem],
            self._transport.request(
                "audit",
                "https://audit.basaltic.sh",
                _OPS["listAuditLogs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_audit_logs_all(
        self, *, query: m.ListAuditLogsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListAuditLogsItem]:
        return iterate_pages(
            lambda marker: self.list_audit_logs(
                query=cast(m.ListAuditLogsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )


class AsyncAuditService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_audit_log(
        self, log_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAuditLogResponse]:
        "Get audit log entry"
        return cast(
            ApiResponse[m.GetAuditLogResponse],
            await self._transport.request(
                "audit",
                "https://audit.basaltic.sh",
                _OPS["getAuditLog"],
                "json",
                {"log_id": log_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_audit_log_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAuditLogScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAuditLogResource]:
        return cast(
            ApiResponse[m.GetAuditLogResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_audit_log(id, options=options),
                lambda match: self.list_audit_logs(
                    query=cast(
                        m.ListAuditLogsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                False,
                "audit_log",
            ),
        )

    async def list_audit_logs(
        self, *, query: m.ListAuditLogsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAuditLogsResponse, m.ListAuditLogsItem]:
        "List audit logs"
        return cast(
            Page[m.ListAuditLogsResponse, m.ListAuditLogsItem],
            await self._transport.request(
                "audit",
                "https://audit.basaltic.sh",
                _OPS["listAuditLogs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_audit_logs_all(
        self, *, query: m.ListAuditLogsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListAuditLogsItem]:
        return aiterate_pages(
            lambda marker: self.list_audit_logs(
                query=cast(m.ListAuditLogsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )
