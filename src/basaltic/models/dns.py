"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

VPCAssociationRequestInput = TypedDict(
    "VPCAssociationRequestInput", {"vpc": "Required[str]"}, total=False
)
AssociateZoneVPCBody: TypeAlias = "VPCAssociationRequestInput"
VPCAssociationAccepted = TypedDict(
    "VPCAssociationAccepted", {"zone_id": "Required[str]", "vpc_id": "Required[str]"}, total=False
)
AssociateZoneVPCResponse: TypeAlias = "VPCAssociationAccepted"
RecordCreateRequestInput = TypedDict(
    "RecordCreateRequestInput",
    {
        "name": "Required[str]",
        "type": "Required[RecordTypeInput]",
        "ttl": "NotRequired[int]",
        "values": "Required[list[RecordValueInput]]",
    },
    total=False,
)
RecordTypeInput: TypeAlias = "Literal['A', 'AAAA', 'AFSDB', 'APL', 'CAA', 'CERT', 'CNAME', 'CSYNC', 'DHCID', 'DNAME', 'EUI48', 'EUI64', 'HINFO', 'HTTPS', 'IPSECKEY', 'KX', 'L32', 'L64', 'LOC', 'LP', 'MX', 'NAPTR', 'NID', 'NS', 'OPENPGPKEY', 'PTR', 'RKEY', 'RP', 'SMIMEA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT', 'URI']"
RecordValueInput = TypedDict(
    "RecordValueInput", {"content": "Required[str]", "disabled": "NotRequired[bool]"}, total=False
)
CreateRecordBody: TypeAlias = "RecordCreateRequestInput"
RecordResponse = TypedDict("RecordResponse", {"record": "NotRequired[Record]"}, total=False)
Record = TypedDict(
    "Record",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "zone_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "type": "NotRequired[str]",
        "ttl": "NotRequired[int]",
        "managed": "NotRequired[bool]",
        "values": "NotRequired[list[RecordValue]]",
    },
    total=False,
)
RecordValue = TypedDict(
    "RecordValue", {"content": "Required[str]", "disabled": "NotRequired[bool]"}, total=False
)
CreateRecordResponse: TypeAlias = "RecordResponse"
ZoneCreateRequestInput = TypedDict(
    "ZoneCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "visibility": "NotRequired[Literal['public', 'private']]",
        "dnssec": "NotRequired[bool]",
        "import_existing_records": "NotRequired[bool]",
        "vpcs": "NotRequired[list[str]]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateZoneBody: TypeAlias = "ZoneCreateRequestInput"
ZoneResponse = TypedDict("ZoneResponse", {"zone": "NotRequired[Zone]"}, total=False)
Zone = TypedDict(
    "Zone",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "nameservers": "NotRequired[list[str]]",
        "soa": "NotRequired[SOA]",
        "visibility": "NotRequired[Literal['public', 'private']]",
        "dnssec": "NotRequired[ZoneDNSSEC]",
        "tags": "NotRequired[Tags]",
        "ownership": "NotRequired[ZoneOwnership]",
    },
    total=False,
)
SOA = TypedDict(
    "SOA",
    {
        "primary_ns": "NotRequired[str]",
        "admin_email": "NotRequired[str]",
        "refresh": "NotRequired[int]",
        "retry": "NotRequired[int]",
        "expire": "NotRequired[int]",
        "minimum": "NotRequired[int]",
    },
    total=False,
)
ZoneDNSSEC = TypedDict(
    "ZoneDNSSEC",
    {
        "enabled": "Required[bool]",
        "ksk_key_tag": "NotRequired[int]",
        "zsk_key_tag": "NotRequired[int]",
        "algorithm": "NotRequired[int]",
        "ds_records": "NotRequired[list[ZoneDSRecord]]",
    },
    total=False,
)
ZoneDSRecord = TypedDict(
    "ZoneDSRecord",
    {
        "key_tag": "Required[int]",
        "algorithm": "Required[int]",
        "digest_type": "Required[int]",
        "digest": "Required[str]",
        "rdata": "Required[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
ZoneOwnership = TypedDict(
    "ZoneOwnership",
    {
        "verified": "NotRequired[bool]",
        "verified_at": "NotRequired[str | None]",
        "checked_at": "NotRequired[str]",
        "recheck_deadline": "NotRequired[str]",
    },
    total=False,
)
CreateZoneResponse: TypeAlias = "ZoneResponse"
GetRecordResponse: TypeAlias = "RecordResponse"
GetRecordResource: TypeAlias = "Record"
GetRecordScope = TypedDict(
    "GetRecordScope",
    {
        "type": "NotRequired[str]",
        "include_managed": "NotRequired[bool]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
GetZoneResponse: TypeAlias = "ZoneResponse"
GetZoneResource: TypeAlias = "Zone"
GetZoneScope = TypedDict("GetZoneScope", {"limit": "NotRequired[int]"}, total=False)
ZoneRecordImportResponse = TypedDict(
    "ZoneRecordImportResponse", {"record_import": "NotRequired[ZoneRecordImport]"}, total=False
)
ZoneRecordImport = TypedDict(
    "ZoneRecordImport",
    {
        "state": "NotRequired[Literal['pending', 'complete', 'failed']]",
        "source": "NotRequired[Literal['axfr', 'nsec-walk', 'query']]",
        "complete": "NotRequired[bool]",
        "found": "NotRequired[int]",
        "imported": "NotRequired[int]",
        "notes": "NotRequired[list[str]]",
        "error": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
GetZoneRecordImportResponse: TypeAlias = "ZoneRecordImportResponse"
ZoneImportRequestInput = TypedDict(
    "ZoneImportRequestInput", {"zone_file": "Required[str]"}, total=False
)
ImportZoneFileBody: TypeAlias = "ZoneImportRequestInput"
ZoneImportResponse = TypedDict(
    "ZoneImportResponse", {"import": "NotRequired[ZoneImportResult]"}, total=False
)
ZoneImportResult = TypedDict(
    "ZoneImportResult",
    {
        "records_created": "NotRequired[int]",
        "records_replaced": "NotRequired[int]",
        "records_by_type": "NotRequired[dict[str, int]]",
        "skipped": "NotRequired[list[ZoneImportSkipped]]",
        "warnings": "NotRequired[list[str]]",
    },
    total=False,
)
ZoneImportSkipped = TypedDict(
    "ZoneImportSkipped",
    {"name": "NotRequired[str]", "type": "NotRequired[str]", "reason": "NotRequired[str]"},
    total=False,
)
ImportZoneFileResponse: TypeAlias = "ZoneImportResponse"
ListRecordsParameters = TypedDict(
    "ListRecordsParameters",
    {
        "type": "NotRequired[str]",
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "include_managed": "NotRequired[bool]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListRecordsQuery: TypeAlias = "ListRecordsParameters"
RecordListResponse = TypedDict(
    "RecordListResponse",
    {"records": "NotRequired[list[Record]]", "meta": "NotRequired[PaginationMeta]"},
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
ListRecordsResponse: TypeAlias = "RecordListResponse"
ListRecordsItem: TypeAlias = "Record"
ListZoneVPCAssociationsParameters = TypedDict(
    "ListZoneVPCAssociationsParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListZoneVPCAssociationsQuery: TypeAlias = "ListZoneVPCAssociationsParameters"
VPCAssociationsResponse = TypedDict(
    "VPCAssociationsResponse", {"vpc_ids": "Required[list[str]]"}, total=False
)
ListZoneVPCAssociationsResponse: TypeAlias = "VPCAssociationsResponse"
ListZoneVPCAssociationsItem: TypeAlias = "str"
ListZonesParameters = TypedDict(
    "ListZonesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListZonesQuery: TypeAlias = "ListZonesParameters"
ZoneListResponse = TypedDict(
    "ZoneListResponse",
    {"zones": "NotRequired[list[Zone]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListZonesResponse: TypeAlias = "ZoneListResponse"
ListZonesItem: TypeAlias = "Zone"
RecordUpdateRequestInput = TypedDict(
    "RecordUpdateRequestInput",
    {"ttl": "NotRequired[int]", "values": "NotRequired[list[RecordValueInput]]"},
    total=False,
)
UpdateRecordBody: TypeAlias = "RecordUpdateRequestInput"
UpdateRecordResponse: TypeAlias = "RecordResponse"
ZoneUpdateRequestInput = TypedDict(
    "ZoneUpdateRequestInput",
    {"description": "NotRequired[str]", "tags": "NotRequired[dict[str, object]]"},
    total=False,
)
UpdateZoneBody: TypeAlias = "ZoneUpdateRequestInput"
UpdateZoneResponse: TypeAlias = "ZoneResponse"
VerifyZoneOwnershipResponse: TypeAlias = "ZoneResponse"
