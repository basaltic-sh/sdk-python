"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachInstanceInterfaceRequest = TypedDict(
    "AttachInstanceInterfaceRequest", {"interface": "Required[str]"}, total=False
)
AttachInstanceInterfaceBody: TypeAlias = "AttachInstanceInterfaceRequest"
InstanceInterfaceResponse = TypedDict(
    "InstanceInterfaceResponse", {"interface": "Required[AttachedInterface]"}, total=False
)
AttachedInterface = TypedDict(
    "AttachedInterface",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "subnet": "Required[ResourceRef]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "mac": "Required[str]",
        "attached_to": "Required[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "boot_index": "Required[int]",
        "primary": "Required[bool]",
        "external": "Required[bool]",
        "restart_required": "NotRequired[bool]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
AttachInstanceInterfaceResponse: TypeAlias = "InstanceInterfaceResponse"
InstancePoolFloatingIpAttachRequestInput = TypedDict(
    "InstancePoolFloatingIpAttachRequestInput", {"floating_ip": "Required[str]"}, total=False
)
AttachInstancePoolFloatingIpBody: TypeAlias = "InstancePoolFloatingIpAttachRequestInput"
InstancePoolFloatingIpResponse = TypedDict(
    "InstancePoolFloatingIpResponse", {"floating_ip": "Required[FloatingIp]"}, total=False
)
FloatingIp = TypedDict(
    "FloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "description": "NotRequired[str]",
        "family": "Required[IpFamily]",
        "attached_to": "Required[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheck]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "address": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "subnet": "Required[ResourceRef | Literal[None] | None]",
        "vpc": "Required[ResourceRef | Literal[None] | None]",
    },
    total=False,
)
IpFamily: TypeAlias = "Literal['ipv4', 'ipv6']"
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
InstanceVolumeResponse = TypedDict(
    "InstanceVolumeResponse", {"volume": "Required[AttachedVolume]"}, total=False
)
AttachedVolume = TypedDict(
    "AttachedVolume",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "Required[Tags]",
        "volume_type": "Required[VolumeTypeName]",
        "size_gb": "Required[int]",
        "performance": "Required[VolumePerformance]",
        "included_io_limits": "Required[IncludedIOLimits]",
        "status": "Required[VolumeStatus]",
        "bootable": "Required[bool]",
        "faults": "Required[list[Fault]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "source_image": "Required[ResourceRef | Literal[None] | None]",
        "source_snapshot": "Required[ResourceRef | Literal[None] | None]",
        "device": "Required[str]",
        "boot_index": "Required[int]",
        "delete_on_termination": "Required[bool]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[Literal['ext4', 'xfs']]",
        "mount": "NotRequired[VolumeMount]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
VolumeTypeName: TypeAlias = "Literal['hdd', 'ssd', 'nvme']"
VolumePerformance = TypedDict(
    "VolumePerformance",
    {"requested": "Required[IncludedIOLimits]", "applied": "Required[IncludedIOLimits]"},
    total=False,
)
IncludedIOLimits = TypedDict(
    "IncludedIOLimits",
    {
        "iops": "Required[int]",
        "bytes_per_sec": "Required[int]",
        "burst_iops": "Required[int]",
        "burst_bytes_per_sec": "Required[int]",
        "burst_seconds": "Required[int]",
    },
    total=False,
)
VolumeStatus: TypeAlias = (
    "Literal['creating', 'available', 'in_use', 'extending', 'updating', 'deleting', 'error']"
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
AttachInstanceVolumeResponse: TypeAlias = "InstanceVolumeResponse"
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
    "CreateInstanceResult", {"instance": "Required[Instance]"}, total=False
)
Instance = TypedDict(
    "Instance",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "task_state": "NotRequired[str | None]",
        "flavor": "Required[ResourceRef]",
        "image": "Required[ResourceRef | Literal[None] | None]",
        "user_data": "NotRequired[str]",
        "iam_role": "Required[ResourceRef | Literal[None] | None]",
        "metadata": "NotRequired[Metadata]",
        "tags": "NotRequired[Tags]",
        "faults": "Required[list[Fault]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "launched_at": "NotRequired[str | None]",
        "terminated_at": "NotRequired[str | None]",
        "desired_state": "Required[Literal['running', 'stopped', 'deleted']]",
        "current_state": "Required[CurrentState]",
    },
    total=False,
)
Metadata: TypeAlias = "dict[str, str]"
CurrentState: TypeAlias = "Literal['pending', 'building', 'running', 'stopping', 'stopped', 'rebooting', 'migrating', 'deleting', 'deleted', 'error', 'crashed', 'paused', 'suspended']"
CreateInstanceResponse: TypeAlias = "CreateInstanceResult"
InstancePoolCreateRequestInput = TypedDict(
    "InstancePoolCreateRequestInput",
    {
        "subnets": "Required[list[str]]",
        "autoscaling": "NotRequired[AutoscalingPolicyInput]",
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
AutoscalingPolicyInput = TypedDict(
    "AutoscalingPolicyInput",
    {
        "enabled": "Required[bool]",
        "metrics": "Required[list[ScalingMetricInput]]",
        "warmup_seconds": "NotRequired[int]",
        "cooldown_seconds": "NotRequired[int]",
        "scale_down_stabilization_seconds": "NotRequired[int]",
        "max_scale_out_step": "NotRequired[int]",
        "max_scale_in_step": "NotRequired[int]",
        "drain_seconds": "NotRequired[int]",
    },
    total=False,
)
ScalingMetricInput = TypedDict(
    "ScalingMetricInput",
    {
        "source": "Required[Literal['cpu', 'telemetry']]",
        "target_type": "Required[Literal['utilization', 'average_value']]",
        "target_value": "Required[float]",
        "name": "NotRequired[str]",
        "labels": "NotRequired[dict[str, str]]",
        "sample_aggregation": "NotRequired[Literal['last', 'avg', 'max', 'rate']]",
        "series_aggregation": "NotRequired[Literal['sum', 'avg', 'max']]",
        "expected_series": "NotRequired[int]",
        "window_seconds": "NotRequired[int]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
InstancePoolTemplateRequestInput = TypedDict(
    "InstancePoolTemplateRequestInput",
    {
        "flavor": "Required[str]",
        "architecture": "NotRequired[str]",
        "image": "NotRequired[str]",
        "addresses": "NotRequired[list[AddressRequestInput]]",
        "security_groups": "NotRequired[list[str]]",
        "floating_ip_assignment": "NotRequired[Literal['none', 'ipv4', 'ipv6', 'dual_stack', 'auto']]",
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
        "performance": "NotRequired[VolumePerformanceRequestInput]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[bool]",
    },
    total=False,
)
CreateInstancePoolBody: TypeAlias = "InstancePoolCreateRequestInput"
InstancePoolResponse = TypedDict(
    "InstancePoolResponse", {"instance_pool": "Required[InstancePool]"}, total=False
)
InstancePool = TypedDict(
    "InstancePool",
    {
        "subnets": "Required[list[ResourceRef]]",
        "vpc": "Required[ResourceRef | Literal[None] | None]",
        "autoscaling": "NotRequired[AutoscalingPolicy]",
        "autoscaling_status": "NotRequired[AutoscalingStatus]",
        "rollout_surge": "NotRequired[bool]",
        "scale_in_protected_instances": "NotRequired[list[str]]",
        "scale_in_blocked_reason": "NotRequired[str]",
        "retiring_instances": "NotRequired[list[RetiringPoolMember]]",
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
AutoscalingPolicy = TypedDict(
    "AutoscalingPolicy",
    {
        "enabled": "Required[bool]",
        "metrics": "Required[list[ScalingMetric]]",
        "warmup_seconds": "NotRequired[int]",
        "cooldown_seconds": "NotRequired[int]",
        "scale_down_stabilization_seconds": "NotRequired[int]",
        "max_scale_out_step": "NotRequired[int]",
        "max_scale_in_step": "NotRequired[int]",
        "drain_seconds": "NotRequired[int]",
    },
    total=False,
)
ScalingMetric = TypedDict(
    "ScalingMetric",
    {
        "source": "Required[Literal['cpu', 'telemetry']]",
        "target_type": "Required[Literal['utilization', 'average_value']]",
        "target_value": "Required[float]",
        "name": "NotRequired[str]",
        "labels": "NotRequired[dict[str, str]]",
        "sample_aggregation": "NotRequired[Literal['last', 'avg', 'max', 'rate']]",
        "series_aggregation": "NotRequired[Literal['sum', 'avg', 'max']]",
        "expected_series": "NotRequired[int]",
        "window_seconds": "NotRequired[int]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
AutoscalingStatus = TypedDict(
    "AutoscalingStatus",
    {
        "status": "Required[Literal['pending', 'disabled', 'stable', 'scaling', 'waiting', 'warming_up', 'metrics_unavailable', 'stabilizing', 'cooldown', 'draining', 'scale_in_blocked']]",
        "reason": "Required[str]",
        "evaluated_at": "NotRequired[str]",
        "last_scaled_at": "NotRequired[str]",
        "history": "Required[list[AutoscalingStatusHistoryItem]]",
    },
    total=False,
)
AutoscalingStatusHistoryItem = TypedDict(
    "AutoscalingStatusHistoryItem",
    {
        "at": "Required[str]",
        "from": "Required[int]",
        "to": "Required[int]",
        "reason": "Required[str]",
    },
    total=False,
)
RetiringPoolMember = TypedDict(
    "RetiringPoolMember",
    {
        "requested_at": "Required[str]",
        "drain_seconds": "Required[int]",
        "agent_acknowledged_at": "NotRequired[str]",
        "drain_until": "NotRequired[str]",
        "instance_id": "Required[str]",
    },
    total=False,
)
InstancePoolTemplate = TypedDict(
    "InstancePoolTemplate",
    {
        "addresses": "NotRequired[list[AddressRequest]]",
        "security_groups": "Required[list[ResourceRef]]",
        "floating_ip_assignment": "Required[Literal['none', 'ipv4', 'ipv6', 'dual_stack', 'auto']]",
        "user_data": "NotRequired[str]",
        "metadata": "NotRequired[Metadata]",
        "tags": "NotRequired[Tags]",
        "iam_role": "Required[ResourceRef | Literal[None] | None]",
        "volumes": "NotRequired[list[InstanceVolume]]",
        "flavor": "Required[ResourceRef]",
        "image": "Required[ResourceRef | Literal[None] | None]",
    },
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
        "performance": "NotRequired[VolumePerformanceRequest]",
        "mount_path": "NotRequired[str]",
        "fstype": "NotRequired[str]",
        "delete_on_termination": "NotRequired[bool]",
    },
    total=False,
)
VolumePerformanceRequest = TypedDict(
    "VolumePerformanceRequest",
    {"iops": "NotRequired[int]", "throughput_mib_s": "NotRequired[float]"},
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
GetFlavorResult = TypedDict("GetFlavorResult", {"flavor": "Required[Flavor]"}, total=False)
Flavor = TypedDict(
    "Flavor",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "vcpus": "Required[int]",
        "ram_mb": "Required[int]",
        "class": "Required[Literal['shared', 'dedicated']]",
        "family": "Required[Literal['general', 'loadbalancer', 'database']]",
        "net_mbps": "NotRequired[int]",
        "cpu_baseline_pct": "NotRequired[int]",
        "cpu_burst_pct": "NotRequired[int]",
        "status": "Required[Literal['active', 'unavailable']]",
    },
    total=False,
)
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
GetInstanceResult = TypedDict("GetInstanceResult", {"instance": "Required[Instance]"}, total=False)
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
    "FlavorListResponse",
    {"flavors": "Required[list[Flavor]]", "meta": "Required[PaginationMeta]"},
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
ListInstanceInterfacesParameters = TypedDict(
    "ListInstanceInterfacesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListInstanceInterfacesQuery: TypeAlias = "ListInstanceInterfacesParameters"
InstanceInterfaceListResponse = TypedDict(
    "InstanceInterfaceListResponse",
    {"interfaces": "Required[list[AttachedInterface]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInstanceInterfacesResponse: TypeAlias = "InstanceInterfaceListResponse"
ListInstanceInterfacesItem: TypeAlias = "AttachedInterface"
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
    {"instance_pools": "Required[list[InstancePool]]", "meta": "Required[PaginationMeta]"},
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
InstanceVolumeListResponse = TypedDict(
    "InstanceVolumeListResponse",
    {"volumes": "Required[list[AttachedVolume]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInstanceVolumesResponse: TypeAlias = "InstanceVolumeListResponse"
ListInstanceVolumesItem: TypeAlias = "AttachedVolume"
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
    {"instances": "Required[list[Instance]]", "meta": "Required[PaginationMeta]"},
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
    "UpdateInstanceResult", {"instance": "Required[Instance]"}, total=False
)
UpdateInstanceResponse: TypeAlias = "UpdateInstanceResult"
InstancePoolUpdateRequestInput = TypedDict(
    "InstancePoolUpdateRequestInput",
    {
        "scale_in_instances": "NotRequired[list[str]]",
        "subnets": "NotRequired[list[str]]",
        "autoscaling": "NotRequired[AutoscalingPolicyInput]",
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
InstancePoolMemberProtectionRequestInput = TypedDict(
    "InstancePoolMemberProtectionRequestInput",
    {"scale_in_protected": "Required[bool]"},
    total=False,
)
UpdateInstancePoolMemberProtectionBody: TypeAlias = "InstancePoolMemberProtectionRequestInput"
UpdateInstancePoolMemberProtectionResponse: TypeAlias = "InstancePoolResponse"
UpdateInstanceVolumeAttachmentRequest = TypedDict(
    "UpdateInstanceVolumeAttachmentRequest",
    {"delete_on_termination": "Required[bool]"},
    total=False,
)
UpdateInstanceVolumeAttachmentBody: TypeAlias = "UpdateInstanceVolumeAttachmentRequest"
