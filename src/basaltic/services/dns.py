"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

import httpx

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import dns as m
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
    "associateZoneVPC": Operation(
        id="associateZoneVPC",
        method="POST",
        path="/v1/zones/{zone_id}/vpc-associations",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRecord": Operation(
        id="createRecord",
        method="POST",
        path="/v1/zones/{zone_id}/records",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createZone": Operation(
        id="createZone",
        method="POST",
        path="/v1/zones",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteRecord": Operation(
        id="deleteRecord",
        method="DELETE",
        path="/v1/zones/{zone_id}/records/{record_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteZone": Operation(
        id="deleteZone",
        method="DELETE",
        path="/v1/zones/{zone_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteZoneRecordImport": Operation(
        id="deleteZoneRecordImport",
        method="DELETE",
        path="/v1/zones/{zone_id}/record-import",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "dissociateZoneVPC": Operation(
        id="dissociateZoneVPC",
        method="DELETE",
        path="/v1/zones/{zone_id}/vpc-associations/{vpc_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "exportZoneFile": Operation(
        id="exportZoneFile",
        method="GET",
        path="/v1/zones/{zone_id}/export",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "getRecord": Operation(
        id="getRecord",
        method="GET",
        path="/v1/zones/{zone_id}/records/{record_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getZone": Operation(
        id="getZone",
        method="GET",
        path="/v1/zones/{zone_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getZoneRecordImport": Operation(
        id="getZoneRecordImport",
        method="GET",
        path="/v1/zones/{zone_id}/record-import",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "importZoneFile": Operation(
        id="importZoneFile",
        method="POST",
        path="/v1/zones/{zone_id}/import",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "listRecords": Operation(
        id="listRecords",
        method="GET",
        path="/v1/zones/{zone_id}/records",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "type": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "include_managed": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="records",
    ),
    "listZoneVPCAssociations": Operation(
        id="listZoneVPCAssociations",
        method="GET",
        path="/v1/zones/{zone_id}/vpc-associations",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="vpc_ids",
    ),
    "listZones": Operation(
        id="listZones",
        method="GET",
        path="/v1/zones",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="zones",
    ),
    "updateRecord": Operation(
        id="updateRecord",
        method="PATCH",
        path="/v1/zones/{zone_id}/records/{record_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateZone": Operation(
        id="updateZone",
        method="PATCH",
        path="/v1/zones/{zone_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "verifyZoneOwnership": Operation(
        id="verifyZoneOwnership",
        method="POST",
        path="/v1/zones/{zone_id}/verify-ownership",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
}


class DnsService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def associate_zone_vpc(
        self, zone_id: str, body: m.AssociateZoneVPCBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssociateZoneVPCResponse]:
        "Associate a VPC with a private zone"
        return cast(
            ApiResponse[m.AssociateZoneVPCResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["associateZoneVPC"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    def create_record(
        self, zone_id: str, body: m.CreateRecordBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRecordResponse]:
        "Create record"
        return cast(
            ApiResponse[m.CreateRecordResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["createRecord"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    def create_zone(
        self, body: m.CreateZoneBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateZoneResponse]:
        "Create zone"
        return cast(
            ApiResponse[m.CreateZoneResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["createZone"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_record(
        self, zone_id: str, record_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete record"
        return cast(
            None,
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteRecord"],
                "discard",
                {"zone_id": zone_id, "record_id": record_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_zone(self, zone_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete zone"
        return cast(
            None,
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteZone"],
                "discard",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_zone_record_import(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Discard the record-import outcome"
        return cast(
            None,
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteZoneRecordImport"],
                "discard",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    def dissociate_zone_vpc(
        self, zone_id: str, vpc_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Dissociate a VPC from a private zone"
        return cast(
            None,
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["dissociateZoneVPC"],
                "discard",
                {"zone_id": zone_id, "vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    def export_zone_file(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Export the zone as a zone file"
        return cast(
            httpx.Response,
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["exportZoneFile"],
                "binary",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_record(
        self, zone_id: str, record_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRecordResponse]:
        "Get record"
        return cast(
            ApiResponse[m.GetRecordResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getRecord"],
                "json",
                {"zone_id": zone_id, "record_id": record_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_record_by_reference(
        self,
        zone_id: str,
        reference: str,
        *,
        scope: m.GetRecordScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRecordResource]:
        return cast(
            ApiResponse[m.GetRecordResource],
            resolve_reference(
                reference,
                lambda id: self.get_record(zone_id, id, options=options),
                lambda match: self.list_records(
                    zone_id,
                    query=cast(m.ListRecordsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "record",
            ),
        )

    def get_zone(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetZoneResponse]:
        "Get zone"
        return cast(
            ApiResponse[m.GetZoneResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getZone"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_zone_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetZoneScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetZoneResource]:
        return cast(
            ApiResponse[m.GetZoneResource],
            resolve_reference(
                reference,
                lambda id: self.get_zone(id, options=options),
                lambda match: self.list_zones(
                    query=cast(m.ListZonesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "zone",
            ),
        )

    def get_zone_record_import(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetZoneRecordImportResponse]:
        "Get the record-import outcome"
        return cast(
            ApiResponse[m.GetZoneRecordImportResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getZoneRecordImport"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    def import_zone_file(
        self, zone_id: str, body: m.ImportZoneFileBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ImportZoneFileResponse]:
        "Import a zone file"
        return cast(
            ApiResponse[m.ImportZoneFileResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["importZoneFile"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    def list_records(
        self,
        zone_id: str,
        *,
        query: m.ListRecordsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRecordsResponse, m.ListRecordsItem]:
        "List records"
        return cast(
            Page[m.ListRecordsResponse, m.ListRecordsItem],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listRecords"],
                "page",
                {"zone_id": zone_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_records_all(
        self,
        zone_id: str,
        *,
        query: m.ListRecordsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListRecordsItem]:
        return iterate_pages(
            lambda marker: self.list_records(
                zone_id,
                query=cast(m.ListRecordsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_zone_vpc_associations(
        self,
        zone_id: str,
        *,
        query: m.ListZoneVPCAssociationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListZoneVPCAssociationsResponse, m.ListZoneVPCAssociationsItem]:
        "List VPC associations"
        return cast(
            Page[m.ListZoneVPCAssociationsResponse, m.ListZoneVPCAssociationsItem],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listZoneVPCAssociations"],
                "page",
                {"zone_id": zone_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_zones(
        self, *, query: m.ListZonesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListZonesResponse, m.ListZonesItem]:
        "List zones"
        return cast(
            Page[m.ListZonesResponse, m.ListZonesItem],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listZones"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_zones_all(
        self, *, query: m.ListZonesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListZonesItem]:
        return iterate_pages(
            lambda marker: self.list_zones(
                query=cast(m.ListZonesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def update_record(
        self,
        zone_id: str,
        record_id: str,
        body: m.UpdateRecordBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRecordResponse]:
        "Update record"
        return cast(
            ApiResponse[m.UpdateRecordResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["updateRecord"],
                "json",
                {"zone_id": zone_id, "record_id": record_id},
                body,
                None,
                options,
            ),
        )

    def update_zone(
        self, zone_id: str, body: m.UpdateZoneBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateZoneResponse]:
        "Update zone"
        return cast(
            ApiResponse[m.UpdateZoneResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["updateZone"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    def verify_zone_ownership(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyZoneOwnershipResponse]:
        "Verify zone ownership"
        return cast(
            ApiResponse[m.VerifyZoneOwnershipResponse],
            self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["verifyZoneOwnership"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )


class AsyncDnsService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def associate_zone_vpc(
        self, zone_id: str, body: m.AssociateZoneVPCBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssociateZoneVPCResponse]:
        "Associate a VPC with a private zone"
        return cast(
            ApiResponse[m.AssociateZoneVPCResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["associateZoneVPC"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    async def create_record(
        self, zone_id: str, body: m.CreateRecordBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRecordResponse]:
        "Create record"
        return cast(
            ApiResponse[m.CreateRecordResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["createRecord"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    async def create_zone(
        self, body: m.CreateZoneBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateZoneResponse]:
        "Create zone"
        return cast(
            ApiResponse[m.CreateZoneResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["createZone"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_record(
        self, zone_id: str, record_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete record"
        return cast(
            None,
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteRecord"],
                "discard",
                {"zone_id": zone_id, "record_id": record_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_zone(self, zone_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete zone"
        return cast(
            None,
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteZone"],
                "discard",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_zone_record_import(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Discard the record-import outcome"
        return cast(
            None,
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["deleteZoneRecordImport"],
                "discard",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    async def dissociate_zone_vpc(
        self, zone_id: str, vpc_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Dissociate a VPC from a private zone"
        return cast(
            None,
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["dissociateZoneVPC"],
                "discard",
                {"zone_id": zone_id, "vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    async def export_zone_file(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Export the zone as a zone file"
        return cast(
            httpx.Response,
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["exportZoneFile"],
                "binary",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_record(
        self, zone_id: str, record_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRecordResponse]:
        "Get record"
        return cast(
            ApiResponse[m.GetRecordResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getRecord"],
                "json",
                {"zone_id": zone_id, "record_id": record_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_record_by_reference(
        self,
        zone_id: str,
        reference: str,
        *,
        scope: m.GetRecordScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRecordResource]:
        return cast(
            ApiResponse[m.GetRecordResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_record(zone_id, id, options=options),
                lambda match: self.list_records(
                    zone_id,
                    query=cast(m.ListRecordsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "record",
            ),
        )

    async def get_zone(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetZoneResponse]:
        "Get zone"
        return cast(
            ApiResponse[m.GetZoneResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getZone"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_zone_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetZoneScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetZoneResource]:
        return cast(
            ApiResponse[m.GetZoneResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_zone(id, options=options),
                lambda match: self.list_zones(
                    query=cast(m.ListZonesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "zone",
            ),
        )

    async def get_zone_record_import(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetZoneRecordImportResponse]:
        "Get the record-import outcome"
        return cast(
            ApiResponse[m.GetZoneRecordImportResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["getZoneRecordImport"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )

    async def import_zone_file(
        self, zone_id: str, body: m.ImportZoneFileBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ImportZoneFileResponse]:
        "Import a zone file"
        return cast(
            ApiResponse[m.ImportZoneFileResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["importZoneFile"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    async def list_records(
        self,
        zone_id: str,
        *,
        query: m.ListRecordsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRecordsResponse, m.ListRecordsItem]:
        "List records"
        return cast(
            Page[m.ListRecordsResponse, m.ListRecordsItem],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listRecords"],
                "page",
                {"zone_id": zone_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_records_all(
        self,
        zone_id: str,
        *,
        query: m.ListRecordsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListRecordsItem]:
        return aiterate_pages(
            lambda marker: self.list_records(
                zone_id,
                query=cast(m.ListRecordsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_zone_vpc_associations(
        self,
        zone_id: str,
        *,
        query: m.ListZoneVPCAssociationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListZoneVPCAssociationsResponse, m.ListZoneVPCAssociationsItem]:
        "List VPC associations"
        return cast(
            Page[m.ListZoneVPCAssociationsResponse, m.ListZoneVPCAssociationsItem],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listZoneVPCAssociations"],
                "page",
                {"zone_id": zone_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_zones(
        self, *, query: m.ListZonesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListZonesResponse, m.ListZonesItem]:
        "List zones"
        return cast(
            Page[m.ListZonesResponse, m.ListZonesItem],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["listZones"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_zones_all(
        self, *, query: m.ListZonesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListZonesItem]:
        return aiterate_pages(
            lambda marker: self.list_zones(
                query=cast(m.ListZonesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def update_record(
        self,
        zone_id: str,
        record_id: str,
        body: m.UpdateRecordBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRecordResponse]:
        "Update record"
        return cast(
            ApiResponse[m.UpdateRecordResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["updateRecord"],
                "json",
                {"zone_id": zone_id, "record_id": record_id},
                body,
                None,
                options,
            ),
        )

    async def update_zone(
        self, zone_id: str, body: m.UpdateZoneBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateZoneResponse]:
        "Update zone"
        return cast(
            ApiResponse[m.UpdateZoneResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["updateZone"],
                "json",
                {"zone_id": zone_id},
                body,
                None,
                options,
            ),
        )

    async def verify_zone_ownership(
        self, zone_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyZoneOwnershipResponse]:
        "Verify zone ownership"
        return cast(
            ApiResponse[m.VerifyZoneOwnershipResponse],
            await self._transport.request(
                "dns",
                "https://dns.basaltic.sh",
                _OPS["verifyZoneOwnership"],
                "json",
                {"zone_id": zone_id},
                UNSET,
                None,
                options,
            ),
        )
