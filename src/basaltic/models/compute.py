"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachInstanceNICRequest = TypedDict(
    "AttachInstanceNICRequest", {"interface": "Required[str]"}, total=False
)
AttachInstanceNICBody: TypeAlias = "AttachInstanceNICRequest"
AttachInstanceNICResult = TypedDict(
    "AttachInstanceNICResult",
    {"attachment": "NotRequired[AttachInstanceNICResultAttachment]"},
    total=False,
)
AttachInstanceNICResultAttachment = TypedDict(
    "AttachInstanceNICResultAttachment",
    {
        "interface_id": "NotRequired[str]",
        "mac": "NotRequired[str]",
        "boot_index": "NotRequired[int]",
        "external": "NotRequired[bool]",
        "restart_required": "NotRequired[bool]",
        "addresses": "NotRequired[list[InterfaceAddress]]",
    },
    total=False,
)
InterfaceAddress = TypedDict(
    "InterfaceAddress",
    {
        "id": "Required[str]",
        "family": "Required[Literal['ipv4', 'ipv6']]",
        "address": "Required[str]",
        "prefix": "Required[str]",
        "primary": "Required[bool]",
        "floating_ips": "Required[list[AddressFloatingIp]]",
    },
    total=False,
)
AddressFloatingIp = TypedDict(
    "AddressFloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "address": "Required[str]",
    },
    total=False,
)
AttachInstanceNICResponse: TypeAlias = "AttachInstanceNICResult"
InstancePoolFloatingIpAttachRequestInput = TypedDict(
    "InstancePoolFloatingIpAttachRequestInput", {"floating_ip": "Required[str]"}, total=False
)
AttachInstancePoolFloatingIpBody: TypeAlias = "InstancePoolFloatingIpAttachRequestInput"
InstancePoolFloatingIpResponse = TypedDict(
    "InstancePoolFloatingIpResponse", {"floating_ip": "NotRequired[FloatingIp]"}, total=False
)
FloatingIp = TypedDict(
    "FloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "description": "NotRequired[str]",
        "family": "Required[IpFamily]",
        "attached_to": "Required[str | None]",
        "members": "Required[list[FloatingIpMember]]",
        "tags": "Required[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheck]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "address": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "subnet_id": "NotRequired[str | None]",
        "vpc_id": "NotRequired[str]",
    },
    total=False,
)
IpFamily: TypeAlias = "Literal['ipv4', 'ipv6']"
FloatingIpMember = TypedDict(
    "FloatingIpMember",
    {
        "interface": "Required[FloatingIpMemberInterfaceObject | None]",
        "health": "Required[Literal['unknown', 'healthy', 'unhealthy']]",
        "reason": "Required[Literal['unprobed', 'booting', 'probe_failed', 'passing']]",
        "created_at": "Required[str]",
        "address_id": "NotRequired[str | None]",
    },
    total=False,
)
FloatingIpMemberInterfaceObject = TypedDict(
    "FloatingIpMemberInterfaceObject",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "instance": "Required[FloatingIpMemberInterfaceObjectInstanceObject | None]",
    },
    total=False,
)
FloatingIpMemberInterfaceObjectInstanceObject = TypedDict(
    "FloatingIpMemberInterfaceObjectInstanceObject",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
)
FloatingIpHealthCheck = TypedDict(
    "FloatingIpHealthCheck",
    {
        "protocol": "Required[Literal['tcp', 'http', 'https']]",
        "path": "NotRequired[str]",
        "port": "Required[int]",
        "interval_sec": "Required[int]",
        "timeout_sec": "Required[int]",
        "healthy_threshold": "Required[int]",
        "unhealthy_threshold": "Required[int]",
        "matcher": "NotRequired[str]",
    },
    total=False,
)
AttachInstancePoolFloatingIpResponse: TypeAlias = "InstancePoolFloatingIpResponse"
AttachInstanceVolumeRequest = TypedDict(
    "AttachInstanceVolumeRequest",
    {
        "volume": "Required[str]",
        "device": "NotRequired[str]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[Literal['ext4', 'xfs']]",
    },
    total=False,
)
AttachInstanceVolumeBody: TypeAlias = "AttachInstanceVolumeRequest"
AttachInstanceVolumeResult = TypedDict(
    "AttachInstanceVolumeResult",
    {"attachment": "NotRequired[AttachInstanceVolumeResultAttachment]"},
    total=False,
)
AttachInstanceVolumeResultAttachment = TypedDict(
    "AttachInstanceVolumeResultAttachment",
    {
        "instance_id": "NotRequired[str]",
        "volume_id": "NotRequired[str]",
        "device": "NotRequired[str]",
    },
    total=False,
)
AttachInstanceVolumeResponse: TypeAlias = "AttachInstanceVolumeResult"
ImageCreateRequestInput = TypedDict(
    "ImageCreateRequestInput",
    {
        "name": "Required[str]",
        "source_url": "Required[str]",
        "description": "NotRequired[str]",
        "os": "NotRequired[Literal['almalinux', 'alpine', 'arch', 'centos', 'debian', 'fedora', 'opensuse', 'rhel', 'rocky', 'ubuntu', 'linux']]",
        "os_version": "NotRequired[str]",
        "architecture": "NotRequired[Literal['amd64']]",
        "version": "NotRequired[str]",
        "current": "NotRequired[bool]",
        "eol_date": "NotRequired[str]",
        "min_disk_gb": "NotRequired[int]",
        "min_ram_mb": "NotRequired[int]",
        "tags": "NotRequired[TagsInput]",
        "attributes": "NotRequired[dict[str, str]]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateImageBody: TypeAlias = "ImageCreateRequestInput"
ImageResponse = TypedDict("ImageResponse", {"image": "Required[Image]"}, total=False)
Image = TypedDict(
    "Image",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "os": "NotRequired[str]",
        "os_version": "NotRequired[str]",
        "architecture": "Required[str]",
        "version": "Required[str]",
        "is_current": "NotRequired[bool]",
        "eol_date": "NotRequired[str]",
        "size_bytes": "NotRequired[int]",
        "min_disk_gb": "NotRequired[int]",
        "min_ram_mb": "NotRequired[int]",
        "status": "Required[Literal['pending', 'importing', 'active', 'error', 'deleting', 'withdrawn']]",
        "withdrawal_reason": "NotRequired[str]",
        "deletion_retention": "NotRequired[ImageDeletionRetention]",
        "faults": "Required[list[Fault]]",
        "tags": "NotRequired[Tags]",
        "attributes": "NotRequired[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
ImageDeletionRetention = TypedDict(
    "ImageDeletionRetention",
    {
        "reason": "Required[Literal['in_use']]",
        "instances": "Required[int]",
        "instance_pools": "Required[int]",
    },
    total=False,
)
Fault = TypedDict(
    "Fault",
    {
        "code": "Required[str]",
        "severity": "Required[Literal['error', 'warning']]",
        "message": "Required[str]",
        "details": "Required[dict[str, object] | None]",
        "first_at": "Required[str]",
        "last_at": "Required[str]",
        "occurrences": "Required[int]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
CreateImageResponse: TypeAlias = "ImageResponse"
InstanceCreateRequestInput = TypedDict(
    "InstanceCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "flavor": "Required[str]",
        "architecture": "NotRequired[str]",
        "image": "NotRequired[str]",
        "networks": "Required[list[NetworkConfigInput]]",
        "volumes": "NotRequired[list[InstanceLaunchVolumeInput]]",
        "metadata": "NotRequired[MetadataInput]",
        "tags": "NotRequired[TagsInput]",
        "user_data": "NotRequired[str]",
        "iam_role": "NotRequired[str]",
    },
    total=False,
)
NetworkConfigInput = TypedDict(
    "NetworkConfigInput",
    {
        "subnet": "Required[str]",
        "mac": "NotRequired[str]",
        "security_groups": "NotRequired[list[str]]",
        "floating_ip_assignment": "NotRequired[Literal['none', 'ipv4', 'ipv6', 'dual_stack', 'auto']]",
        "addresses": "NotRequired[list[AddressRequestInput]]",
    },
    total=False,
)
AddressRequestInput = TypedDict(
    "AddressRequestInput",
    {"family": "Required[Literal['ipv4', 'ipv6']]", "address": "NotRequired[str]"},
    total=False,
)
InstanceLaunchVolumeInput: TypeAlias = (
    "InstanceLaunchVolumeInputVariant1 | InstanceLaunchVolumeInputVariant2"
)
InstanceLaunchVolumeInputVariant1 = TypedDict(
    "InstanceLaunchVolumeInputVariant1",
    {
        "boot": "NotRequired[bool]",
        "volume": "Required[str]",
        "size_gb": "NotRequired[int]",
        "volume_type": "NotRequired[Literal['ssd', 'nvme']]",
        "performance": "NotRequired[VolumePerformanceRequestInput]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[Literal[False]]",
        "snapshot_schedules": "NotRequired[list[SnapshotScheduleSettingsInput]]",
    },
    total=False,
)
VolumePerformanceRequestInput = TypedDict(
    "VolumePerformanceRequestInput",
    {"iops": "NotRequired[int]", "throughput_mib_s": "NotRequired[float]"},
    total=False,
)
SnapshotScheduleSettingsInput = TypedDict(
    "SnapshotScheduleSettingsInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "interval_minutes": "Required[SnapshotIntervalMinutesInput]",
        "retention_count": "Required[SnapshotRetentionCountInput]",
        "retention_days": "NotRequired[SnapshotRetentionDaysInput]",
        "enabled": "NotRequired[bool]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
SnapshotIntervalMinutesInput: TypeAlias = "int"
SnapshotRetentionCountInput: TypeAlias = "int"
SnapshotRetentionDaysInput: TypeAlias = "int"
InstanceLaunchVolumeInputVariant2 = TypedDict(
    "InstanceLaunchVolumeInputVariant2",
    {
        "boot": "NotRequired[bool]",
        "volume": "NotRequired[str]",
        "size_gb": "NotRequired[int]",
        "volume_type": "NotRequired[Literal['ssd', 'nvme']]",
        "performance": "NotRequired[VolumePerformanceRequestInput]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[bool]",
        "snapshot_schedules": "NotRequired[list[SnapshotScheduleSettingsInput]]",
    },
    total=False,
)
MetadataInput: TypeAlias = "dict[str, str]"
CreateInstanceBody: TypeAlias = "InstanceCreateRequestInput"
CreateInstanceResult = TypedDict(
    "CreateInstanceResult", {"instance": "NotRequired[Instance]"}, total=False
)
Instance = TypedDict(
    "Instance",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "task_state": "NotRequired[str | None]",
        "flavor": "NotRequired[Flavor]",
        "image": "NotRequired[Image]",
        "user_data": "NotRequired[str]",
        "iam_role": "NotRequired[InstanceRole]",
        "metadata": "NotRequired[Metadata]",
        "tags": "NotRequired[Tags]",
        "faults": "Required[list[Fault]]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "launched_at": "NotRequired[str | None]",
        "terminated_at": "NotRequired[str | None]",
        "desired_state": "NotRequired[Literal['running', 'stopped', 'deleted']]",
        "current_state": "NotRequired[CurrentState]",
    },
    total=False,
)
Flavor = TypedDict(
    "Flavor",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "vcpus": "NotRequired[int]",
        "ram_mb": "NotRequired[int]",
        "class": "NotRequired[Literal['shared', 'dedicated']]",
        "family": "NotRequired[Literal['general', 'loadbalancer', 'database']]",
        "status": "NotRequired[Literal['active', 'disabled']]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
InstanceRole = TypedDict(
    "InstanceRole",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
)
Metadata: TypeAlias = "dict[str, str]"
CurrentState: TypeAlias = "Literal['pending', 'building', 'running', 'stopping', 'stopped', 'rebooting', 'migrating', 'deleting', 'deleted', 'error', 'crashed', 'paused', 'suspended']"
CreateInstanceResponse: TypeAlias = "CreateInstanceResult"
InstancePoolCreateRequestInput = TypedDict(
    "InstancePoolCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "template": "Required[InstancePoolTemplateRequestInput]",
        "desired_count": "NotRequired[int]",
        "min_count": "NotRequired[int]",
        "max_count": "NotRequired[int]",
    },
    total=False,
)
InstancePoolTemplateRequestInput = TypedDict(
    "InstancePoolTemplateRequestInput",
    {
        "flavor": "Required[str]",
        "architecture": "NotRequired[str]",
        "image": "NotRequired[str]",
        "networks": "Required[list[NetworkConfigInput]]",
        "user_data": "NotRequired[str]",
        "metadata": "NotRequired[MetadataInput]",
        "tags": "NotRequired[TagsInput]",
        "iam_role": "NotRequired[str]",
        "volumes": "NotRequired[list[InstanceVolumeInput]]",
    },
    total=False,
)
InstanceVolumeInput = TypedDict(
    "InstanceVolumeInput",
    {
        "boot": "NotRequired[bool]",
        "size_gb": "Required[int]",
        "volume_type": "NotRequired[str]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[bool]",
    },
    total=False,
)
CreateInstancePoolBody: TypeAlias = "InstancePoolCreateRequestInput"
InstancePoolResponse = TypedDict(
    "InstancePoolResponse", {"instance_pool": "NotRequired[InstancePool]"}, total=False
)
InstancePool = TypedDict(
    "InstancePool",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "desired_count": "NotRequired[int]",
        "min_count": "NotRequired[int]",
        "max_count": "NotRequired[int]",
        "live_count": "NotRequired[int]",
        "member_count": "NotRequired[int]",
        "refresh_in_progress": "NotRequired[bool]",
        "stale_instance_count": "NotRequired[int]",
        "status": "NotRequired[Literal['active', 'scaling', 'error', 'deleting']]",
        "faults": "Required[list[Fault]]",
        "managed_by": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "template": "NotRequired[InstancePoolTemplate]",
    },
    total=False,
)
InstancePoolTemplate = TypedDict(
    "InstancePoolTemplate",
    {
        "flavor_id": "NotRequired[str]",
        "image_id": "NotRequired[str]",
        "networks": "NotRequired[list[NetworkConfigResponse]]",
        "user_data": "NotRequired[str]",
        "metadata": "NotRequired[Metadata]",
        "tags": "NotRequired[Tags]",
        "iam_role": "NotRequired[InstanceRole]",
        "volumes": "NotRequired[list[InstanceVolume]]",
    },
    total=False,
)
NetworkConfigResponse = TypedDict(
    "NetworkConfigResponse",
    {
        "subnet": "Required[Subnet | Literal[None] | None]",
        "mac": "NotRequired[str]",
        "security_group_ids": "NotRequired[list[str]]",
        "floating_ip_assignment": "NotRequired[Literal['none', 'ipv4', 'ipv6', 'dual_stack', 'auto']]",
        "addresses": "NotRequired[list[AddressRequest]]",
    },
    total=False,
)
Subnet = TypedDict(
    "Subnet",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "vpc": "Required[Vpc]",
        "route_table": "Required[RouteTableSummary]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "gateway_ipv4": "Required[str]",
        "cidr_ipv6": "NotRequired[str | None]",
        "gateway_ipv6": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
Vpc = TypedDict(
    "Vpc",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "cidr_ipv6": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
RouteTableSummary: TypeAlias = "RouteTableSummaryObject | None"
RouteTableSummaryObject = TypedDict(
    "RouteTableSummaryObject",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
)
AddressRequest = TypedDict(
    "AddressRequest",
    {"family": "Required[Literal['ipv4', 'ipv6']]", "address": "NotRequired[str]"},
    total=False,
)
InstanceVolume = TypedDict(
    "InstanceVolume",
    {
        "boot": "NotRequired[bool]",
        "size_gb": "Required[int]",
        "volume_type": "NotRequired[str]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[bool]",
    },
    total=False,
)
CreateInstancePoolResponse: TypeAlias = "InstancePoolResponse"
SerialConsoleTicket = TypedDict(
    "SerialConsoleTicket",
    {"ticket": "Required[str]", "expires_at": "Required[str]", "expires_in": "Required[int]"},
    total=False,
)
CreateSerialConsoleTicketResponse: TypeAlias = "SerialConsoleTicket"
DeleteImageResponse: TypeAlias = "ImageResponse"
GetConsoleOutputParameters = TypedDict(
    "GetConsoleOutputParameters", {"max_bytes": "NotRequired[int]"}, total=False
)
GetConsoleOutputQuery: TypeAlias = "GetConsoleOutputParameters"
GetConsoleOutputResult = TypedDict(
    "GetConsoleOutputResult",
    {"output": "Required[str]", "truncated": "Required[bool]"},
    total=False,
)
GetConsoleOutputResponse: TypeAlias = "GetConsoleOutputResult"
GetFlavorResult = TypedDict("GetFlavorResult", {"flavor": "NotRequired[Flavor]"}, total=False)
GetFlavorResponse: TypeAlias = "GetFlavorResult"
GetFlavorResource: TypeAlias = "Flavor"
GetFlavorScope = TypedDict(
    "GetFlavorScope",
    {"family": "NotRequired[Literal['general', 'loadbalancer', 'database']]"},
    total=False,
)
GetImageResponse: TypeAlias = "ImageResponse"
GetImageResource: TypeAlias = "Image"
GetImageScope = TypedDict(
    "GetImageScope",
    {
        "limit": "NotRequired[int]",
        "os": "NotRequired[str]",
        "architecture": "NotRequired[str]",
        "status": "NotRequired[Literal['pending', 'importing', 'active', 'error', 'deleting', 'withdrawn']]",
        "all_versions": "NotRequired[bool]",
    },
    total=False,
)
GetInstanceResult = TypedDict(
    "GetInstanceResult", {"instance": "NotRequired[Instance]"}, total=False
)
GetInstanceResponse: TypeAlias = "GetInstanceResult"
GetInstanceResource: TypeAlias = "Instance"
GetInstanceScope = TypedDict(
    "GetInstanceScope",
    {
        "limit": "NotRequired[int]",
        "current_state": "NotRequired[CurrentStateInput]",
        "flavor": "NotRequired[str]",
        "image": "NotRequired[str]",
    },
    total=False,
)
CurrentStateInput: TypeAlias = "Literal['pending', 'building', 'running', 'stopping', 'stopped', 'rebooting', 'migrating', 'deleting', 'deleted', 'error', 'crashed', 'paused', 'suspended']"
GetInstancePoolResponse: TypeAlias = "InstancePoolResponse"
GetInstancePoolResource: TypeAlias = "InstancePool"
GetInstancePoolScope = TypedDict("GetInstancePoolScope", {"limit": "NotRequired[int]"}, total=False)
ListFlavorsParameters = TypedDict(
    "ListFlavorsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "family": "NotRequired[Literal['general', 'loadbalancer', 'database']]",
    },
    total=False,
)
ListFlavorsQuery: TypeAlias = "ListFlavorsParameters"
FlavorListResponse = TypedDict(
    "FlavorListResponse", {"flavors": "NotRequired[list[Flavor]]"}, total=False
)
ListFlavorsResponse: TypeAlias = "FlavorListResponse"
ListFlavorsItem: TypeAlias = "Flavor"
ListImageCatalogParameters = TypedDict(
    "ListImageCatalogParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "os": "NotRequired[str]",
        "architecture": "NotRequired[str]",
    },
    total=False,
)
ListImageCatalogQuery: TypeAlias = "ListImageCatalogParameters"
ImageCatalogResponse = TypedDict(
    "ImageCatalogResponse",
    {"categories": "Required[list[ImageCatalogCategory]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ImageCatalogCategory = TypedDict(
    "ImageCatalogCategory",
    {"name": "Required[str]", "images": "Required[list[CatalogImage]]"},
    total=False,
)
CatalogImage = TypedDict(
    "CatalogImage",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "os": "NotRequired[str]",
        "os_version": "NotRequired[str]",
        "architecture": "Required[str]",
        "min_disk_gb": "Required[int]",
        "min_ram_mb": "Required[int]",
        "eol_date": "NotRequired[str]",
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
ListImageCatalogResponse: TypeAlias = "ImageCatalogResponse"
ListImageCatalogItem: TypeAlias = "ImageCatalogCategory"
ListImagesParameters = TypedDict(
    "ListImagesParameters",
    {
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "os": "NotRequired[str]",
        "architecture": "NotRequired[str]",
        "name": "NotRequired[str]",
        "status": "NotRequired[Literal['pending', 'importing', 'active', 'error', 'deleting', 'withdrawn']]",
        "all_versions": "NotRequired[bool]",
    },
    total=False,
)
ListImagesQuery: TypeAlias = "ListImagesParameters"
ImageListResponse = TypedDict(
    "ImageListResponse",
    {"images": "Required[list[Image]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListImagesResponse: TypeAlias = "ImageListResponse"
ListImagesItem: TypeAlias = "Image"
ListInstanceNICsParameters = TypedDict(
    "ListInstanceNICsParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListInstanceNICsQuery: TypeAlias = "ListInstanceNICsParameters"
ListInstanceNICsResult = TypedDict(
    "ListInstanceNICsResult",
    {"nics": "NotRequired[list[ListInstanceNICsResultNicsItem]]"},
    total=False,
)
ListInstanceNICsResultNicsItem = TypedDict(
    "ListInstanceNICsResultNicsItem",
    {
        "interface_id": "Required[str]",
        "boot_index": "Required[int]",
        "primary": "Required[bool]",
        "external": "Required[bool]",
        "name": "NotRequired[str]",
        "mac": "NotRequired[str]",
        "subnet": "Required[Subnet | Literal[None] | None]",
        "addresses": "Required[list[InterfaceAddress]]",
        "routed_prefixes": "Required[list[RoutedPrefix]]",
    },
    total=False,
)
RoutedPrefix = TypedDict(
    "RoutedPrefix",
    {
        "id": "Required[str]",
        "pool_id": "Required[str]",
        "family": "Required[Literal['ipv4']]",
        "prefix": "Required[str]",
    },
    total=False,
)
ListInstanceNICsResponse: TypeAlias = "ListInstanceNICsResult"
ListInstanceNICsEntry = TypedDict(
    "ListInstanceNICsEntry",
    {
        "interface_id": "Required[str]",
        "boot_index": "Required[int]",
        "primary": "Required[bool]",
        "external": "Required[bool]",
        "name": "NotRequired[str]",
        "mac": "NotRequired[str]",
        "subnet": "Required[Subnet | Literal[None] | None]",
        "addresses": "Required[list[InterfaceAddress]]",
        "routed_prefixes": "Required[list[RoutedPrefix]]",
    },
    total=False,
)
ListInstanceNICsItem: TypeAlias = "ListInstanceNICsEntry"
ListInstancePoolFloatingIpsParameters = TypedDict(
    "ListInstancePoolFloatingIpsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInstancePoolFloatingIpsQuery: TypeAlias = "ListInstancePoolFloatingIpsParameters"
FloatingIpListResponse = TypedDict(
    "FloatingIpListResponse",
    {"floating_ips": "Required[list[FloatingIp]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInstancePoolFloatingIpsResponse: TypeAlias = "FloatingIpListResponse"
ListInstancePoolFloatingIpsItem: TypeAlias = "FloatingIp"
ListInstancePoolsParameters = TypedDict(
    "ListInstancePoolsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInstancePoolsQuery: TypeAlias = "ListInstancePoolsParameters"
InstancePoolListResponse = TypedDict(
    "InstancePoolListResponse",
    {"instance_pools": "NotRequired[list[InstancePool]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListInstancePoolsResponse: TypeAlias = "InstancePoolListResponse"
ListInstancePoolsItem: TypeAlias = "InstancePool"
ListInstanceVolumesParameters = TypedDict(
    "ListInstanceVolumesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListInstanceVolumesQuery: TypeAlias = "ListInstanceVolumesParameters"
ListInstanceVolumesResult = TypedDict(
    "ListInstanceVolumesResult",
    {"attachments": "NotRequired[list[ListInstanceVolumesResultAttachmentsItem]]"},
    total=False,
)
ListInstanceVolumesResultAttachmentsItem = TypedDict(
    "ListInstanceVolumesResultAttachmentsItem",
    {
        "volume_id": "NotRequired[str]",
        "device": "NotRequired[str]",
        "boot_index": "NotRequired[int]",
        "delete_on_termination": "NotRequired[bool]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[Literal['ext4', 'xfs']]",
        "name": "NotRequired[str]",
        "volume_type": "NotRequired[str]",
        "size_gb": "NotRequired[int]",
        "status": "NotRequired[str]",
        "bootable": "NotRequired[bool]",
        "mount": "NotRequired[VolumeMount]",
    },
    total=False,
)
VolumeMount = TypedDict(
    "VolumeMount",
    {
        "state": "Required[Literal['unknown', 'pending', 'mounted', 'failed']]",
        "code": "NotRequired[Literal['unsafe_serial', 'device_absent', 'probe_failed', 'signatures_no_filesystem', 'unsupported_fstype', 'mkfs_failed', 'unsafe_mount_path', 'mkdir_failed', 'mount_failed', 'fstab_write_failed', 'unknown_error']]",
        "message": "NotRequired[str]",
        "since": "NotRequired[str]",
        "reported_at": "NotRequired[str]",
    },
    total=False,
)
ListInstanceVolumesResponse: TypeAlias = "ListInstanceVolumesResult"
ListInstanceVolumesEntry = TypedDict(
    "ListInstanceVolumesEntry",
    {
        "volume_id": "NotRequired[str]",
        "device": "NotRequired[str]",
        "boot_index": "NotRequired[int]",
        "delete_on_termination": "NotRequired[bool]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[Literal['ext4', 'xfs']]",
        "name": "NotRequired[str]",
        "volume_type": "NotRequired[str]",
        "size_gb": "NotRequired[int]",
        "status": "NotRequired[str]",
        "bootable": "NotRequired[bool]",
        "mount": "NotRequired[VolumeMount]",
    },
    total=False,
)
ListInstanceVolumesItem: TypeAlias = "ListInstanceVolumesEntry"
ListInstancesParameters = TypedDict(
    "ListInstancesParameters",
    {
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "current_state": "NotRequired[CurrentStateInput]",
        "flavor": "NotRequired[str]",
        "image": "NotRequired[str]",
    },
    total=False,
)
ListInstancesQuery: TypeAlias = "ListInstancesParameters"
InstanceListResponse = TypedDict(
    "InstanceListResponse",
    {"instances": "NotRequired[list[Instance]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListInstancesResponse: TypeAlias = "InstanceListResponse"
ListInstancesItem: TypeAlias = "Instance"
ListPoolInstancesParameters = TypedDict(
    "ListPoolInstancesParameters",
    {
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "current_state": "NotRequired[CurrentStateInput]",
        "flavor": "NotRequired[str]",
        "image": "NotRequired[str]",
    },
    total=False,
)
ListPoolInstancesQuery: TypeAlias = "ListPoolInstancesParameters"
ListPoolInstancesResponse: TypeAlias = "InstanceListResponse"
ListPoolInstancesItem: TypeAlias = "Instance"
InstanceRebootRequestInput = TypedDict(
    "InstanceRebootRequestInput", {"hard": "NotRequired[bool]"}, total=False
)
RebootInstanceBody: TypeAlias = "InstanceRebootRequestInput"
RefreshInstancePoolResponse: TypeAlias = "InstancePoolResponse"
ReinstallInstanceRequest = TypedDict(
    "ReinstallInstanceRequest",
    {
        "image": "NotRequired[str]",
        "size_gb": "NotRequired[int]",
        "volume_type": "NotRequired[Literal['ssd', 'nvme']]",
    },
    total=False,
)
ReinstallInstanceBody: TypeAlias = "ReinstallInstanceRequest"
ResizeInstanceRequest = TypedDict("ResizeInstanceRequest", {"flavor": "Required[str]"}, total=False)
ResizeInstanceBody: TypeAlias = "ResizeInstanceRequest"
StartSerialConsoleParameters = TypedDict(
    "StartSerialConsoleParameters", {"backlog_bytes": "NotRequired[int]"}, total=False
)
StartSerialConsoleQuery: TypeAlias = "StartSerialConsoleParameters"
ImageUpdateRequestInput = TypedDict(
    "ImageUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "current": "NotRequired[bool]",
        "eol_date": "NotRequired[str | None]",
        "tags": "NotRequired[TagsInput]",
        "attributes": "NotRequired[dict[str, str]]",
    },
    total=False,
)
UpdateImageBody: TypeAlias = "ImageUpdateRequestInput"
UpdateImageResponse: TypeAlias = "ImageResponse"
InstanceUpdateRequestInput = TypedDict(
    "InstanceUpdateRequestInput",
    {
        "iam_role": "NotRequired[str]",
        "description": "NotRequired[str]",
        "metadata": "NotRequired[MetadataInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateInstanceBody: TypeAlias = "InstanceUpdateRequestInput"
UpdateInstanceResult = TypedDict(
    "UpdateInstanceResult", {"instance": "NotRequired[Instance]"}, total=False
)
UpdateInstanceResponse: TypeAlias = "UpdateInstanceResult"
InstancePoolUpdateRequestInput = TypedDict(
    "InstancePoolUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "desired_count": "NotRequired[int]",
        "min_count": "NotRequired[int]",
        "max_count": "NotRequired[int]",
        "template": "NotRequired[InstancePoolTemplateRequestInput]",
    },
    total=False,
)
UpdateInstancePoolBody: TypeAlias = "InstancePoolUpdateRequestInput"
UpdateInstancePoolResponse: TypeAlias = "InstancePoolResponse"
UpdateInstanceVolumeAttachmentRequest = TypedDict(
    "UpdateInstanceVolumeAttachmentRequest",
    {"delete_on_termination": "Required[bool]"},
    total=False,
)
UpdateInstanceVolumeAttachmentBody: TypeAlias = "UpdateInstanceVolumeAttachmentRequest"
