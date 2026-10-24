"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

ListQuotasParameters = TypedDict(
    "ListQuotasParameters", {"region": "NotRequired[str]"}, total=False
)
ListQuotasQuery: TypeAlias = "ListQuotasParameters"
QuotaListResponse = TypedDict(
    "QuotaListResponse",
    {"quotas": "Required[list[QuotaItem]]", "policies": "NotRequired[list[QuotaPolicy]]"},
    total=False,
)
QuotaItem = TypedDict(
    "QuotaItem",
    {
        "service": "Required[str]",
        "resource_type": "Required[str]",
        "scope": "Required[Literal['regional', 'global', 'per_resource']]",
        "limit": "Required[int]",
        "in_use": "Required[int]",
        "reserved": "Required[int]",
        "available": "Required[int]",
        "is_default": "Required[bool]",
        "description": "Required[str]",
    },
    total=False,
)
QuotaPolicy = TypedDict(
    "QuotaPolicy",
    {
        "service": "Required[Literal['email']]",
        "resource_type": "Required[Literal['message_size_bytes', 'sent_recipients_per_second', 'sent_recipients_per_day', 'received_recipients_per_second']]",
        "scope": "Required[Literal['regional']]",
        "region": "Required[str]",
        "limit": "Required[int]",
        "unit": "Required[Literal['bytes', 'recipients']]",
        "window_seconds": "NotRequired[Literal[1, 86400]]",
        "limit_source": "Required[Literal['default', 'organization', 'region']]",
        "description": "Required[str]",
    },
    total=False,
)
ListQuotasResponse: TypeAlias = "QuotaListResponse"
