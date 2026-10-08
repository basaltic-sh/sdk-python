"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

ListQuotasParameters = TypedDict(
    "ListQuotasParameters", {"region": "NotRequired[str]"}, total=False
)
ListQuotasQuery: TypeAlias = "ListQuotasParameters"
QuotaListResponse = TypedDict(
    "QuotaListResponse", {"quotas": "Required[list[QuotaItem]]"}, total=False
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
ListQuotasResponse: TypeAlias = "QuotaListResponse"
ListQuotasItem: TypeAlias = "QuotaItem"
