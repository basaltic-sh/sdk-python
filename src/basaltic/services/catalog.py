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
}


class CatalogService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

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


class AsyncCatalogService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

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
