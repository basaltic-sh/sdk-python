"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, TypeAlias, TypedDict

AuditLogResponse = TypedDict(
    "AuditLogResponse", {"audit_log": "NotRequired[AuditLog]"}, total=False
)
AuditLog = TypedDict(
    "AuditLog",
    {
        "crn": "NotRequired[str]",
        "id": "NotRequired[str]",
        "timestamp": "NotRequired[str]",
        "actor_crn": "NotRequired[str | None]",
        "resource_crn": "NotRequired[str | None]",
        "actor_name": "NotRequired[str | None]",
        "actor_email": "NotRequired[str | None]",
        "action": "NotRequired[str]",
        "status": "NotRequired[Literal['success', 'failure', 'denied']]",
        "resource_name": "NotRequired[str | None]",
        "ip_address": "NotRequired[str | None]",
        "user_agent": "NotRequired[str | None]",
        "request_id": "NotRequired[str | None]",
        "details": "NotRequired[dict[str, object]]",
        "error_code": "NotRequired[str | None]",
        "error_message": "NotRequired[str | None]",
    },
    total=False,
)
GetAuditLogResponse: TypeAlias = "AuditLogResponse"
GetAuditLogResource: TypeAlias = "AuditLog"
GetAuditLogScope = TypedDict(
    "GetAuditLogScope",
    {
        "actor": "NotRequired[str]",
        "actor_type": "NotRequired[Literal['user', 'service_account', 'system']]",
        "action": "NotRequired[str]",
        "resource_type": "NotRequired[str]",
        "resource": "NotRequired[str]",
        "status": "NotRequired[Literal['success', 'failure', 'denied']]",
        "ip_address": "NotRequired[str]",
        "from": "NotRequired[str]",
        "to": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListAuditLogsParameters = TypedDict(
    "ListAuditLogsParameters",
    {
        "crn": "NotRequired[str]",
        "actor": "NotRequired[str]",
        "actor_type": "NotRequired[Literal['user', 'service_account', 'system']]",
        "action": "NotRequired[str]",
        "resource_type": "NotRequired[str]",
        "resource": "NotRequired[str]",
        "status": "NotRequired[Literal['success', 'failure', 'denied']]",
        "ip_address": "NotRequired[str]",
        "from": "NotRequired[str]",
        "to": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListAuditLogsQuery: TypeAlias = "ListAuditLogsParameters"
AuditLogListResponse = TypedDict(
    "AuditLogListResponse",
    {"audit_logs": "NotRequired[list[AuditLog]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
PaginationMeta = TypedDict(
    "PaginationMeta",
    {
        "total": "NotRequired[int]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "has_more": "NotRequired[bool]",
    },
    total=False,
)
ListAuditLogsResponse: TypeAlias = "AuditLogListResponse"
ListAuditLogsItem: TypeAlias = "AuditLog"
