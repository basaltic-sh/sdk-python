"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

RegionResponse = TypedDict("RegionResponse", {"region": "Required[Region]"}, total=False)
Region = TypedDict(
    "Region",
    {
        "state": "Required[Literal['planned', 'active', 'restricted', 'retiring', 'retired']]",
        "crn": "Required[str]",
        "code": "Required[str]",
        "name": "Required[str]",
        "location": "Required[str]",
        "country_code": "Required[str]",
    },
    total=False,
)
GetRegionResponse: TypeAlias = "RegionResponse"
GetRegionResource: TypeAlias = "Region"
GetRegionScope = TypedDict("GetRegionScope", {}, total=False)
ListRegionsParameters = TypedDict(
    "ListRegionsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListRegionsQuery: TypeAlias = "ListRegionsParameters"
ListRegionsResult = TypedDict(
    "ListRegionsResult",
    {
        "regions": "Required[list[Region]]",
        "default": "Required[str]",
        "meta": "Required[PaginationMeta]",
    },
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
ListRegionsResponse: TypeAlias = "ListRegionsResult"
ListRegionsItem: TypeAlias = "Region"
