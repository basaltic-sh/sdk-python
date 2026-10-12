"""Generated typed API methods; do not edit."""

from __future__ import annotations

from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import catalog as m
from ..response import (
    ApiResponse,
    Page,
    aresolve_reference,
    reference_scope,
    resolve_reference,
)

_OPS = {
    "getCountry": Operation(
        id="getCountry",
        method="GET",
        path="/v1/countries/{country}",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRegion": Operation(
        id="getRegion",
        method="GET",
        path="/v1/regions/{code}",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listCities": Operation(
        id="listCities",
        method="GET",
        path="/v1/cities",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "state": {"style": "form", "explode": True},
            "country": {"style": "form", "explode": True},
            "q": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="cities",
    ),
    "listCountries": Operation(
        id="listCountries",
        method="GET",
        path="/v1/countries",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="countries",
    ),
    "listRegions": Operation(
        id="listRegions",
        method="GET",
        path="/v1/regions",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="regions",
    ),
    "listStates": Operation(
        id="listStates",
        method="GET",
        path="/v1/states",
        authenticated=False,
        requiredQuery=["country"],
        requiredHeaders=[],
        queryEncoding={"country": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="states",
    ),
    "lookupPostalCode": Operation(
        id="lookupPostalCode",
        method="GET",
        path="/v1/postal-codes/{code}",
        authenticated=False,
        requiredQuery=["country"],
        requiredHeaders=[],
        queryEncoding={"country": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
}


class CatalogService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_country(
        self, country: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCountryResponse]:
        "Get a country and its address rules"
        return cast(
            ApiResponse[m.GetCountryResponse],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["getCountry"],
                "json",
                {"country": country},
                UNSET,
                None,
                options,
            ),
        )

    def get_region(
        self, code: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRegionResponse]:
        "Get a region"
        return cast(
            ApiResponse[m.GetRegionResponse],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["getRegion"],
                "json",
                {"code": code},
                UNSET,
                None,
                options,
            ),
        )

    def get_region_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRegionScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRegionResource]:
        return cast(
            ApiResponse[m.GetRegionResource],
            resolve_reference(
                reference,
                lambda id: self.get_region(id, options=options),
                lambda match: self.list_regions(
                    query=cast(m.ListRegionsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                None,
            ),
        )

    def list_cities(
        self, *, query: m.ListCitiesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCitiesResponse, m.ListCitiesItem]:
        "List cities"
        return cast(
            Page[m.ListCitiesResponse, m.ListCitiesItem],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listCities"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_countries(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListCountriesResponse, m.ListCountriesItem]:
        "List countries"
        return cast(
            Page[m.ListCountriesResponse, m.ListCountriesItem],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listCountries"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def list_regions(
        self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
        "List regions"
        return cast(
            Page[m.ListRegionsResponse, m.ListRegionsItem],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listRegions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_states(
        self, *, query: m.ListStatesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListStatesResponse, m.ListStatesItem]:
        "List a country's states"
        return cast(
            Page[m.ListStatesResponse, m.ListStatesItem],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listStates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def lookup_postal_code(
        self, code: str, *, query: m.LookupPostalCodeQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.LookupPostalCodeResponse]:
        "Look up a postal code"
        return cast(
            ApiResponse[m.LookupPostalCodeResponse],
            self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["lookupPostalCode"],
                "json",
                {"code": code},
                UNSET,
                query,
                options,
            ),
        )


class AsyncCatalogService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_country(
        self, country: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCountryResponse]:
        "Get a country and its address rules"
        return cast(
            ApiResponse[m.GetCountryResponse],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["getCountry"],
                "json",
                {"country": country},
                UNSET,
                None,
                options,
            ),
        )

    async def get_region(
        self, code: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRegionResponse]:
        "Get a region"
        return cast(
            ApiResponse[m.GetRegionResponse],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["getRegion"],
                "json",
                {"code": code},
                UNSET,
                None,
                options,
            ),
        )

    async def get_region_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRegionScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRegionResource]:
        return cast(
            ApiResponse[m.GetRegionResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_region(id, options=options),
                lambda match: self.list_regions(
                    query=cast(m.ListRegionsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                None,
            ),
        )

    async def list_cities(
        self, *, query: m.ListCitiesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCitiesResponse, m.ListCitiesItem]:
        "List cities"
        return cast(
            Page[m.ListCitiesResponse, m.ListCitiesItem],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listCities"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_countries(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListCountriesResponse, m.ListCountriesItem]:
        "List countries"
        return cast(
            Page[m.ListCountriesResponse, m.ListCountriesItem],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listCountries"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def list_regions(
        self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
        "List regions"
        return cast(
            Page[m.ListRegionsResponse, m.ListRegionsItem],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listRegions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_states(
        self, *, query: m.ListStatesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListStatesResponse, m.ListStatesItem]:
        "List a country's states"
        return cast(
            Page[m.ListStatesResponse, m.ListStatesItem],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["listStates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def lookup_postal_code(
        self, code: str, *, query: m.LookupPostalCodeQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.LookupPostalCodeResponse]:
        "Look up a postal code"
        return cast(
            ApiResponse[m.LookupPostalCodeResponse],
            await self._transport.request(
                "catalog",
                "https://catalog.basaltic.sh",
                _OPS["lookupPostalCode"],
                "json",
                {"code": code},
                UNSET,
                query,
                options,
            ),
        )
