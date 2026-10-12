"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

GetCountryResult = TypedDict(
    "GetCountryResult", {"country": "Required[CountryDetail]"}, total=False
)
CountryDetail = TypedDict(
    "CountryDetail",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "code": "Required[str]",
        "iso3": "Required[str]",
        "name": "Required[str]",
        "calling_code": "Required[str]",
        "rules": "Required[CountryRules]",
        "postal_lookup": "Required[bool]",
    },
    total=False,
)
CountryRules = TypedDict(
    "CountryRules",
    {
        "customer_types": "Required[list[Literal['individual', 'company']]]",
        "name_labels": "Required[dict[str, str]]",
        "tax_ids": "Required[dict[str, list[TaxIDRule]]]",
        "fields": "Required[list[AddressField]]",
    },
    total=False,
)
TaxIDRule = TypedDict(
    "TaxIDRule",
    {
        "kind": "Required[str]",
        "label": "Required[str]",
        "mask": "NotRequired[str]",
        "pattern": "NotRequired[str]",
        "validator": "NotRequired[Literal['br_cpf', 'br_cnpj', 'ar_cuit', 'cl_rut']]",
        "example": "NotRequired[str]",
        "required": "Required[bool]",
    },
    total=False,
)
AddressField = TypedDict(
    "AddressField",
    {
        "key": "Required[Literal['street_name', 'street_number', 'complement', 'neighborhood', 'city', 'state', 'postal_code']]",
        "label": "Required[str]",
        "required": "Required[bool]",
        "max": "NotRequired[int]",
        "mask": "NotRequired[str]",
        "pattern": "NotRequired[str]",
        "example": "NotRequired[str]",
        "source": "NotRequired[Literal['list', 'free']]",
        "require_metadata": "NotRequired[str]",
    },
    total=False,
)
GetCountryResponse: TypeAlias = "GetCountryResult"
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
ListCitiesParameters = TypedDict(
    "ListCitiesParameters",
    {
        "state": "NotRequired[str]",
        "country": "NotRequired[str]",
        "q": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListCitiesQuery: TypeAlias = "ListCitiesParameters"
ListCitiesResult = TypedDict(
    "ListCitiesResult", {"cities": "Required[list[City]]", "meta": "Required[GeoPage]"}, total=False
)
City = TypedDict(
    "City",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "country": "Required[ResourceRef]",
        "state": "Required[ResourceRef | Literal[None] | None]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
GeoPage = TypedDict(
    "GeoPage",
    {"total": "Required[int]", "limit": "Required[int]", "has_more": "Required[bool]"},
    total=False,
)
ListCitiesResponse: TypeAlias = "ListCitiesResult"
ListCitiesItem: TypeAlias = "City"
ListCountriesResult = TypedDict(
    "ListCountriesResult",
    {"countries": "Required[list[Country]]", "meta": "Required[GeoPage]"},
    total=False,
)
Country = TypedDict(
    "Country",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "code": "Required[str]",
        "iso3": "Required[str]",
        "name": "Required[str]",
        "calling_code": "Required[str]",
    },
    total=False,
)
ListCountriesResponse: TypeAlias = "ListCountriesResult"
ListCountriesItem: TypeAlias = "Country"
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
ListStatesParameters = TypedDict("ListStatesParameters", {"country": "Required[str]"}, total=False)
ListStatesQuery: TypeAlias = "ListStatesParameters"
ListStatesResult = TypedDict(
    "ListStatesResult",
    {"states": "Required[list[State]]", "meta": "Required[GeoPage]"},
    total=False,
)
State = TypedDict(
    "State",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "code": "Required[str]",
        "name": "Required[str]",
        "country": "Required[ResourceRef]",
    },
    total=False,
)
ListStatesResponse: TypeAlias = "ListStatesResult"
ListStatesItem: TypeAlias = "State"
LookupPostalCodeParameters = TypedDict(
    "LookupPostalCodeParameters", {"country": "Required[str]"}, total=False
)
LookupPostalCodeQuery: TypeAlias = "LookupPostalCodeParameters"
LookupPostalCodeResult = TypedDict(
    "LookupPostalCodeResult", {"postal_code": "Required[PostalCode]"}, total=False
)
PostalCode = TypedDict(
    "PostalCode",
    {
        "code": "Required[str]",
        "country": "Required[ResourceRef]",
        "state": "Required[ResourceRef | Literal[None] | None]",
        "city": "Required[ResourceRef | Literal[None] | None]",
        "address": "Required[dict[str, str]]",
        "source": "Required[str]",
    },
    total=False,
)
LookupPostalCodeResponse: TypeAlias = "LookupPostalCodeResult"
