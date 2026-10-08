"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

Region = TypedDict(
    "Region",
    {
        "state": "Required[Literal['planned', 'active', 'restricted', 'retiring', 'retired']]",
        "accepting_new_resources": "Required[bool]",
        "crn": "Required[str]",
        "code": "Required[str]",
        "name": "Required[str]",
        "location": "Required[str]",
        "country_code": "Required[str]",
        "available": "Required[bool]",
        "coming_soon": "Required[bool]",
    },
    total=False,
)
GetRegionResponse: TypeAlias = "Region"
GetRegionResource: TypeAlias = "GetRegionResponse"
GetRegionScope = TypedDict("GetRegionScope", {}, total=False)
ListRegionsParameters = TypedDict(
    "ListRegionsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListRegionsQuery: TypeAlias = "ListRegionsParameters"
ListRegionsResult = TypedDict(
    "ListRegionsResult",
    {"regions": "Required[list[Region]]", "default": "Required[str]"},
    total=False,
)
ListRegionsResponse: TypeAlias = "ListRegionsResult"
ListRegionsItem: TypeAlias = "Region"
