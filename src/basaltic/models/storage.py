"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

CompleteMultipartUploadRequestInput = TypedDict(
    "CompleteMultipartUploadRequestInput",
    {"parts": "Required[list[CompleteMultipartUploadRequestInputPartsItem]]"},
    total=False,
)
CompleteMultipartUploadRequestInputPartsItem = TypedDict(
    "CompleteMultipartUploadRequestInputPartsItem",
    {"part_number": "Required[int]", "etag": "Required[str]"},
    total=False,
)
CompleteMultipartUploadBody: TypeAlias = "CompleteMultipartUploadRequestInput"
CompleteMultipartUploadResponse2 = TypedDict(
    "CompleteMultipartUploadResponse2",
    {
        "etag": "Required[str]",
        "size": "Required[int]",
        "version_id": "NotRequired[str]",
        "storage_class": "NotRequired[str]",
    },
    total=False,
)
CompleteMultipartUploadResponse: TypeAlias = "CompleteMultipartUploadResponse2"
CreateBucketRequestInput = TypedDict(
    "CreateBucketRequestInput",
    {"name": "Required[str]", "object_lock_enabled": "NotRequired[bool]"},
    total=False,
)
CreateBucketBody: TypeAlias = "CreateBucketRequestInput"
BucketResponse = TypedDict("BucketResponse", {"bucket": "NotRequired[Bucket]"}, total=False)
Bucket = TypedDict(
    "Bucket",
    {
        "id": "Required[str]",
        "name": "Required[str]",
        "crn": "Required[str]",
        "acl": "Required[str]",
        "versioning": "Required[Literal['disabled', 'enabled', 'suspended']]",
        "deletion_protection": "Required[bool]",
        "recovery_window_days": "Required[int]",
        "deleted_at": "Required[str | None]",
        "scheduled_purge_at": "NotRequired[str]",
        "created_at": "Required[str]",
    },
    total=False,
)
CreateBucketResponse: TypeAlias = "BucketResponse"
SnapshotCreateRequestInput = TypedDict(
    "SnapshotCreateRequestInput",
    {
        "volume": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateSnapshotBody: TypeAlias = "SnapshotCreateRequestInput"
SnapshotResponse = TypedDict("SnapshotResponse", {"snapshot": "NotRequired[Snapshot]"}, total=False)
Snapshot = TypedDict(
    "Snapshot",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "volume_id": "NotRequired[str]",
        "snapshot_policy_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "size_gb": "NotRequired[int]",
        "status": "NotRequired[SnapshotStatus]",
        "faults": "Required[list[Fault]]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
SnapshotStatus: TypeAlias = "Literal['creating', 'available', 'deleting', 'error']"
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
CreateSnapshotResponse: TypeAlias = "SnapshotResponse"
SnapshotPolicyCreateRequestInput = TypedDict(
    "SnapshotPolicyCreateRequestInput",
    {
        "volume": "Required[str]",
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
CreateSnapshotPolicyBody: TypeAlias = "SnapshotPolicyCreateRequestInput"
SnapshotPolicyResponse = TypedDict(
    "SnapshotPolicyResponse", {"snapshot_policy": "NotRequired[SnapshotPolicy]"}, total=False
)
SnapshotPolicy = TypedDict(
    "SnapshotPolicy",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "volume_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "enabled": "NotRequired[bool]",
        "interval_minutes": "NotRequired[SnapshotIntervalMinutes]",
        "retention_count": "NotRequired[SnapshotRetentionCount]",
        "retention_days": "NotRequired[SnapshotRetentionDays]",
        "next_run_at": "NotRequired[str]",
        "last_run_at": "NotRequired[str]",
        "faults": "Required[list[Fault]]",
        "tags": "NotRequired[Tags]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
SnapshotIntervalMinutes: TypeAlias = "int"
SnapshotRetentionCount: TypeAlias = "int"
SnapshotRetentionDays: TypeAlias = "int"
CreateSnapshotPolicyResponse: TypeAlias = "SnapshotPolicyResponse"
VolumeCreateRequestInput = TypedDict(
    "VolumeCreateRequestInput",
    {
        "performance": "NotRequired[VolumePerformanceRequestInput]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "volume_type": "Required[CreatableVolumeTypeNameInput]",
        "size_gb": "Required[int]",
        "architecture": "NotRequired[str]",
        "source_image": "NotRequired[str]",
        "source_snapshot": "NotRequired[str]",
        "bootable": "NotRequired[bool]",
    },
    total=False,
)
VolumePerformanceRequestInput = TypedDict(
    "VolumePerformanceRequestInput",
    {"iops": "NotRequired[int]", "throughput_mib_s": "NotRequired[float]"},
    total=False,
)
CreatableVolumeTypeNameInput: TypeAlias = "Literal['ssd', 'nvme']"
CreateVolumeBody: TypeAlias = "VolumeCreateRequestInput"
VolumeResponse = TypedDict("VolumeResponse", {"volume": "NotRequired[Volume]"}, total=False)
Volume = TypedDict(
    "Volume",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "volume_type": "NotRequired[VolumeTypeName]",
        "size_gb": "NotRequired[int]",
        "performance": "NotRequired[VolumePerformance]",
        "included_io_limits": "NotRequired[IncludedIOLimits]",
        "status": "NotRequired[VolumeStatus]",
        "bootable": "NotRequired[bool]",
        "source_image_id": "NotRequired[str | None]",
        "source_snapshot_id": "NotRequired[str | None]",
        "faults": "Required[list[Fault]]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
VolumeTypeName: TypeAlias = "Literal['hdd', 'ssd', 'nvme']"
VolumePerformance = TypedDict(
    "VolumePerformance",
    {
        "requested": "Required[IncludedIOLimits]",
        "applied": "Required[IncludedIOLimits]",
        "state": "Required[Literal['creating', 'pending', 'applied']]",
        "operation_id": "NotRequired[str]",
        "applied_at": "NotRequired[str]",
        "last_error": "NotRequired[str]",
    },
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
    "Literal['creating', 'available', 'in_use', 'extending', 'deleting', 'error']"
)
CreateVolumeResponse: TypeAlias = "VolumeResponse"
DeleteBucketResult = TypedDict(
    "DeleteBucketResult", {"scheduled_purge_at": "Required[str]"}, total=False
)
DeleteBucketResponse: TypeAlias = "DeleteBucketResult | dict[str, object]"
VolumeExtendRequestInput = TypedDict(
    "VolumeExtendRequestInput", {"new_size_gb": "Required[int]"}, total=False
)
ExtendVolumeBody: TypeAlias = "VolumeExtendRequestInput"
ExtendVolumeResponse: TypeAlias = "VolumeResponse"
BucketCORSResponse = TypedDict("BucketCORSResponse", {"cors": "Required[CORSConfig]"}, total=False)
CORSConfig = TypedDict("CORSConfig", {"rules": "Required[list[CORSRule]]"}, total=False)
CORSRule = TypedDict(
    "CORSRule",
    {
        "id": "NotRequired[str]",
        "allowed_origins": "Required[list[str]]",
        "allowed_methods": "Required[list[Literal['GET', 'PUT', 'POST', 'DELETE', 'HEAD']]]",
        "allowed_headers": "NotRequired[list[str]]",
        "expose_headers": "NotRequired[list[str]]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
GetBucketCORSResponse: TypeAlias = "BucketCORSResponse"
BucketEncryptionResponse = TypedDict(
    "BucketEncryptionResponse", {"encryption": "Required[EncryptionConfig]"}, total=False
)
EncryptionConfig = TypedDict(
    "EncryptionConfig", {"rules": "Required[list[EncryptionRule]]"}, total=False
)
EncryptionRule = TypedDict(
    "EncryptionRule",
    {"default": "NotRequired[EncryptionRuleDefault]", "bucket_key_enabled": "NotRequired[bool]"},
    total=False,
)
EncryptionRuleDefault = TypedDict(
    "EncryptionRuleDefault",
    {"sse_algorithm": "Required[str]", "kms_master_key_id": "NotRequired[str]"},
    total=False,
)
GetBucketEncryptionResponse: TypeAlias = "BucketEncryptionResponse"
BucketLifecycleResponse = TypedDict(
    "BucketLifecycleResponse",
    {"revision": "Required[str]", "lifecycle": "Required[LifecycleConfig]"},
    total=False,
)
LifecycleConfig = TypedDict(
    "LifecycleConfig", {"rules": "Required[list[LifecycleRule]]"}, total=False
)
LifecycleRule = TypedDict(
    "LifecycleRule",
    {
        "id": "NotRequired[str]",
        "status": "Required[Literal['enabled', 'disabled']]",
        "filter": "NotRequired[LifecycleRuleFilter]",
        "transition": "NotRequired[LifecycleRuleTransition]",
        "expiration": "NotRequired[LifecycleRuleExpiration]",
        "noncurrent_version_expiration": "NotRequired[LifecycleRuleNoncurrentVersionExpiration]",
        "abort_incomplete_multipart_upload": "NotRequired[LifecycleRuleAbortIncompleteMultipartUpload]",
    },
    total=False,
)
LifecycleRuleFilter = TypedDict("LifecycleRuleFilter", {"prefix": "NotRequired[str]"}, total=False)
LifecycleRuleTransition = TypedDict(
    "LifecycleRuleTransition",
    {
        "days": "NotRequired[int]",
        "date": "NotRequired[str]",
        "storage_class": "Required[Literal['STANDARD', 'COLD']]",
    },
    total=False,
)
LifecycleRuleExpiration = TypedDict(
    "LifecycleRuleExpiration", {"days": "NotRequired[int]", "date": "NotRequired[str]"}, total=False
)
LifecycleRuleNoncurrentVersionExpiration = TypedDict(
    "LifecycleRuleNoncurrentVersionExpiration",
    {"noncurrent_days": "NotRequired[int]", "newer_noncurrent_versions": "NotRequired[int]"},
    total=False,
)
LifecycleRuleAbortIncompleteMultipartUpload = TypedDict(
    "LifecycleRuleAbortIncompleteMultipartUpload",
    {"days_after_initiation": "NotRequired[int]"},
    total=False,
)
GetBucketLifecycleResponse: TypeAlias = "BucketLifecycleResponse"
BucketObjectLockResponse = TypedDict(
    "BucketObjectLockResponse", {"object_lock": "Required[ObjectLockConfig]"}, total=False
)
ObjectLockConfig = TypedDict(
    "ObjectLockConfig",
    {"object_lock_enabled": "NotRequired[str]", "rule": "NotRequired[ObjectLockConfigRule]"},
    total=False,
)
ObjectLockConfigRule = TypedDict(
    "ObjectLockConfigRule",
    {"default_retention": "NotRequired[ObjectLockConfigRuleDefaultRetention]"},
    total=False,
)
ObjectLockConfigRuleDefaultRetention = TypedDict(
    "ObjectLockConfigRuleDefaultRetention",
    {
        "mode": "NotRequired[Literal['GOVERNANCE', 'COMPLIANCE']]",
        "days": "NotRequired[int]",
        "years": "NotRequired[int]",
    },
    total=False,
)
GetBucketObjectLockResponse: TypeAlias = "BucketObjectLockResponse"
BucketPolicyResponse = TypedDict(
    "BucketPolicyResponse", {"document": "NotRequired[BucketPolicy]"}, total=False
)
BucketPolicy: TypeAlias = "dict[str, object]"
GetBucketPolicyResponse: TypeAlias = "BucketPolicyResponse"
BucketTaggingResponse = TypedDict(
    "BucketTaggingResponse", {"tags": "Required[TagSet]"}, total=False
)
TagSet: TypeAlias = "dict[str, str]"
GetBucketTaggingResponse: TypeAlias = "BucketTaggingResponse"
BucketVersioningResponse = TypedDict(
    "BucketVersioningResponse",
    {"status": "Required[Literal['disabled', 'enabled', 'suspended']]"},
    total=False,
)
GetBucketVersioningResponse: TypeAlias = "BucketVersioningResponse"
GetSnapshotResponse: TypeAlias = "SnapshotResponse"
GetSnapshotResource: TypeAlias = "Snapshot"
GetSnapshotScope = TypedDict(
    "GetSnapshotScope",
    {
        "limit": "NotRequired[int]",
        "volume": "NotRequired[str]",
        "status": "NotRequired[SnapshotStatusInput]",
        "snapshot_policy": "NotRequired[str]",
    },
    total=False,
)
SnapshotStatusInput: TypeAlias = "Literal['creating', 'available', 'deleting', 'error']"
GetSnapshotPolicyResponse: TypeAlias = "SnapshotPolicyResponse"
GetSnapshotPolicyResource: TypeAlias = "SnapshotPolicy"
GetSnapshotPolicyScope = TypedDict(
    "GetSnapshotPolicyScope",
    {"limit": "NotRequired[int]", "volume": "NotRequired[str]", "enabled": "NotRequired[bool]"},
    total=False,
)
GetVolumeResponse: TypeAlias = "VolumeResponse"
GetVolumeResource: TypeAlias = "Volume"
GetVolumeScope = TypedDict(
    "GetVolumeScope",
    {"limit": "NotRequired[int]", "status": "NotRequired[VolumeStatusInput]"},
    total=False,
)
VolumeStatusInput: TypeAlias = (
    "Literal['creating', 'available', 'in_use', 'extending', 'deleting', 'error']"
)
InitiateMultipartUploadRequestInput = TypedDict(
    "InitiateMultipartUploadRequestInput",
    {
        "key": "Required[str]",
        "content_type": "NotRequired[str]",
        "storage_class": "NotRequired[str]",
        "metadata": "NotRequired[dict[str, str]]",
    },
    total=False,
)
InitiateMultipartUploadBody: TypeAlias = "InitiateMultipartUploadRequestInput"
MultipartUploadResponse = TypedDict(
    "MultipartUploadResponse", {"upload": "Required[MultipartUpload]"}, total=False
)
MultipartUpload = TypedDict(
    "MultipartUpload",
    {
        "upload_id": "Required[str]",
        "bucket": "Required[str]",
        "key": "Required[str]",
        "content_type": "NotRequired[str]",
        "storage_class": "NotRequired[str]",
        "metadata": "NotRequired[dict[str, str]]",
        "created_at": "Required[str]",
    },
    total=False,
)
InitiateMultipartUploadResponse: TypeAlias = "MultipartUploadResponse"
ListBucketsParameters = TypedDict(
    "ListBucketsParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
ListBucketsQuery: TypeAlias = "ListBucketsParameters"
BucketListResponse = TypedDict(
    "BucketListResponse",
    {"buckets": "NotRequired[list[Bucket]]", "meta": "NotRequired[PaginationMeta]"},
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
ListBucketsResponse: TypeAlias = "BucketListResponse"
ListBucketsItem: TypeAlias = "Bucket"
ListMultipartUploadsParameters = TypedDict(
    "ListMultipartUploadsParameters",
    {"prefix": "NotRequired[str]", "max_uploads": "NotRequired[int]"},
    total=False,
)
ListMultipartUploadsQuery: TypeAlias = "ListMultipartUploadsParameters"
ListMultipartUploadsResponse2 = TypedDict(
    "ListMultipartUploadsResponse2", {"uploads": "Required[list[MultipartUpload]]"}, total=False
)
ListMultipartUploadsResponse: TypeAlias = "ListMultipartUploadsResponse2"
ListMultipartUploadsItem: TypeAlias = "MultipartUpload"
ListObjectVersionsParameters = TypedDict(
    "ListObjectVersionsParameters",
    {
        "prefix": "NotRequired[str]",
        "key_marker": "NotRequired[str]",
        "version_id_marker": "NotRequired[str]",
        "max_keys": "NotRequired[int]",
    },
    total=False,
)
ListObjectVersionsQuery: TypeAlias = "ListObjectVersionsParameters"
ListObjectVersionsResponse2 = TypedDict(
    "ListObjectVersionsResponse2",
    {
        "versions": "Required[list[ObjectVersion]]",
        "is_truncated": "Required[bool]",
        "next_key_marker": "NotRequired[str]",
        "next_version_id_marker": "NotRequired[str]",
    },
    total=False,
)
ObjectVersion = TypedDict(
    "ObjectVersion",
    {
        "key": "Required[str]",
        "version_id": "Required[str]",
        "size": "Required[int]",
        "etag": "Required[str]",
        "content_type": "NotRequired[str]",
        "storage_class": "NotRequired[str]",
        "last_modified": "Required[str]",
        "is_latest": "Required[bool]",
        "is_delete_marker": "Required[bool]",
    },
    total=False,
)
ListObjectVersionsResponse: TypeAlias = "ListObjectVersionsResponse2"
ListObjectVersionsItem: TypeAlias = "ObjectVersion"
ListObjectsParameters = TypedDict(
    "ListObjectsParameters",
    {
        "prefix": "NotRequired[str]",
        "delimiter": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "max_keys": "NotRequired[int]",
    },
    total=False,
)
ListObjectsQuery: TypeAlias = "ListObjectsParameters"
ObjectListResponse = TypedDict(
    "ObjectListResponse",
    {
        "objects": "NotRequired[list[ObjectEntry]]",
        "common_prefixes": "NotRequired[list[str]]",
        "is_truncated": "NotRequired[bool]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
ObjectEntry = TypedDict(
    "ObjectEntry",
    {
        "key": "Required[str]",
        "size": "Required[int]",
        "etag": "Required[str]",
        "content_type": "NotRequired[str]",
        "last_modified": "Required[str]",
    },
    total=False,
)
ListObjectsResponse: TypeAlias = "ObjectListResponse"
ListPartsResponse2 = TypedDict(
    "ListPartsResponse2",
    {"upload": "Required[MultipartUpload]", "parts": "Required[list[MultipartPart]]"},
    total=False,
)
MultipartPart = TypedDict(
    "MultipartPart",
    {"part_number": "Required[int]", "size": "Required[int]", "etag": "Required[str]"},
    total=False,
)
ListPartsResponse: TypeAlias = "ListPartsResponse2"
ListPartsItem: TypeAlias = "MultipartPart"
ListSnapshotPoliciesParameters = TypedDict(
    "ListSnapshotPoliciesParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "volume": "NotRequired[str]",
        "enabled": "NotRequired[bool]",
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
ListSnapshotPoliciesQuery: TypeAlias = "ListSnapshotPoliciesParameters"
SnapshotPolicyListResponse = TypedDict(
    "SnapshotPolicyListResponse",
    {
        "snapshot_policies": "NotRequired[list[SnapshotPolicy]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
ListSnapshotPoliciesResponse: TypeAlias = "SnapshotPolicyListResponse"
ListSnapshotPoliciesItem: TypeAlias = "SnapshotPolicy"
ListSnapshotsParameters = TypedDict(
    "ListSnapshotsParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "volume": "NotRequired[str]",
        "name": "NotRequired[str]",
        "status": "NotRequired[SnapshotStatusInput]",
        "crn": "NotRequired[str]",
        "snapshot_policy": "NotRequired[str]",
    },
    total=False,
)
ListSnapshotsQuery: TypeAlias = "ListSnapshotsParameters"
SnapshotListResponse = TypedDict(
    "SnapshotListResponse",
    {"snapshots": "NotRequired[list[Snapshot]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListSnapshotsResponse: TypeAlias = "SnapshotListResponse"
ListSnapshotsItem: TypeAlias = "Snapshot"
ListVolumeTypesParameters = TypedDict(
    "ListVolumeTypesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListVolumeTypesQuery: TypeAlias = "ListVolumeTypesParameters"
VolumeTypeListResponse = TypedDict(
    "VolumeTypeListResponse", {"volume_types": "NotRequired[list[VolumeType]]"}, total=False
)
VolumeType = TypedDict(
    "VolumeType",
    {
        "included_iops": "NotRequired[int]",
        "included_throughput_mib_s": "NotRequired[int]",
        "max_iops": "NotRequired[int]",
        "max_throughput_mib_s": "NotRequired[int]",
        "crn": "NotRequired[str]",
        "id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
    },
    total=False,
)
ListVolumeTypesResponse: TypeAlias = "VolumeTypeListResponse"
ListVolumeTypesItem: TypeAlias = "VolumeType"
ListVolumesParameters = TypedDict(
    "ListVolumesParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "status": "NotRequired[VolumeStatusInput]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
ListVolumesQuery: TypeAlias = "ListVolumesParameters"
VolumeListResponse = TypedDict(
    "VolumeListResponse",
    {"volumes": "NotRequired[list[Volume]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListVolumesResponse: TypeAlias = "VolumeListResponse"
ListVolumesItem: TypeAlias = "Volume"
PutBucketCORSRequestInput = TypedDict(
    "PutBucketCORSRequestInput", {"cors": "Required[CORSConfigInput]"}, total=False
)
CORSConfigInput = TypedDict(
    "CORSConfigInput", {"rules": "Required[list[CORSRuleInput]]"}, total=False
)
CORSRuleInput = TypedDict(
    "CORSRuleInput",
    {
        "id": "NotRequired[str]",
        "allowed_origins": "Required[list[str]]",
        "allowed_methods": "Required[list[Literal['GET', 'PUT', 'POST', 'DELETE', 'HEAD']]]",
        "allowed_headers": "NotRequired[list[str]]",
        "expose_headers": "NotRequired[list[str]]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
PutBucketCORSBody: TypeAlias = "PutBucketCORSRequestInput"
PutBucketDeletionProtectionRequestInput = TypedDict(
    "PutBucketDeletionProtectionRequestInput",
    {"enabled": "Required[bool]", "recovery_window_days": "NotRequired[int]"},
    total=False,
)
PutBucketDeletionProtectionBody: TypeAlias = "PutBucketDeletionProtectionRequestInput"
PutBucketEncryptionRequestInput = TypedDict(
    "PutBucketEncryptionRequestInput",
    {"encryption": "Required[EncryptionConfigInput]"},
    total=False,
)
EncryptionConfigInput = TypedDict(
    "EncryptionConfigInput", {"rules": "Required[list[EncryptionRuleInput]]"}, total=False
)
EncryptionRuleInput = TypedDict(
    "EncryptionRuleInput",
    {
        "default": "NotRequired[EncryptionRuleInputDefault]",
        "bucket_key_enabled": "NotRequired[bool]",
    },
    total=False,
)
EncryptionRuleInputDefault = TypedDict(
    "EncryptionRuleInputDefault",
    {"sse_algorithm": "Required[str]", "kms_master_key_id": "NotRequired[str]"},
    total=False,
)
PutBucketEncryptionBody: TypeAlias = "PutBucketEncryptionRequestInput"
PutBucketLifecycleRequestInput = TypedDict(
    "PutBucketLifecycleRequestInput", {"lifecycle": "Required[LifecycleConfigInput]"}, total=False
)
LifecycleConfigInput = TypedDict(
    "LifecycleConfigInput", {"rules": "Required[list[LifecycleRuleInput]]"}, total=False
)
LifecycleRuleInput = TypedDict(
    "LifecycleRuleInput",
    {
        "id": "NotRequired[str]",
        "status": "Required[Literal['enabled', 'disabled']]",
        "filter": "NotRequired[LifecycleRuleInputFilter]",
        "transition": "NotRequired[LifecycleRuleInputTransition]",
        "expiration": "NotRequired[LifecycleRuleInputExpiration]",
        "noncurrent_version_expiration": "NotRequired[LifecycleRuleInputNoncurrentVersionExpiration]",
        "abort_incomplete_multipart_upload": "NotRequired[LifecycleRuleInputAbortIncompleteMultipartUpload]",
    },
    total=False,
)
LifecycleRuleInputFilter = TypedDict(
    "LifecycleRuleInputFilter", {"prefix": "NotRequired[str]"}, total=False
)
LifecycleRuleInputTransition = TypedDict(
    "LifecycleRuleInputTransition",
    {
        "days": "NotRequired[int]",
        "date": "NotRequired[str]",
        "storage_class": "Required[Literal['STANDARD', 'COLD']]",
    },
    total=False,
)
LifecycleRuleInputExpiration = TypedDict(
    "LifecycleRuleInputExpiration",
    {"days": "NotRequired[int]", "date": "NotRequired[str]"},
    total=False,
)
LifecycleRuleInputNoncurrentVersionExpiration = TypedDict(
    "LifecycleRuleInputNoncurrentVersionExpiration",
    {"noncurrent_days": "NotRequired[int]", "newer_noncurrent_versions": "NotRequired[int]"},
    total=False,
)
LifecycleRuleInputAbortIncompleteMultipartUpload = TypedDict(
    "LifecycleRuleInputAbortIncompleteMultipartUpload",
    {"days_after_initiation": "NotRequired[int]"},
    total=False,
)
PutBucketLifecycleBody: TypeAlias = "PutBucketLifecycleRequestInput"
PutBucketObjectLockRequestInput = TypedDict(
    "PutBucketObjectLockRequestInput",
    {"object_lock": "Required[ObjectLockConfigInput]"},
    total=False,
)
ObjectLockConfigInput = TypedDict(
    "ObjectLockConfigInput",
    {"object_lock_enabled": "NotRequired[str]", "rule": "NotRequired[ObjectLockConfigInputRule]"},
    total=False,
)
ObjectLockConfigInputRule = TypedDict(
    "ObjectLockConfigInputRule",
    {"default_retention": "NotRequired[ObjectLockConfigInputRuleDefaultRetention]"},
    total=False,
)
ObjectLockConfigInputRuleDefaultRetention = TypedDict(
    "ObjectLockConfigInputRuleDefaultRetention",
    {
        "mode": "NotRequired[Literal['GOVERNANCE', 'COMPLIANCE']]",
        "days": "NotRequired[int]",
        "years": "NotRequired[int]",
    },
    total=False,
)
PutBucketObjectLockBody: TypeAlias = "PutBucketObjectLockRequestInput"
PutBucketPolicyRequestInput = TypedDict(
    "PutBucketPolicyRequestInput", {"document": "Required[BucketPolicyInput]"}, total=False
)
BucketPolicyInput: TypeAlias = "dict[str, object]"
PutBucketPolicyBody: TypeAlias = "PutBucketPolicyRequestInput"
PutBucketTaggingRequestInput = TypedDict(
    "PutBucketTaggingRequestInput", {"tags": "Required[TagSetInput]"}, total=False
)
TagSetInput: TypeAlias = "dict[str, str]"
PutBucketTaggingBody: TypeAlias = "PutBucketTaggingRequestInput"
PutBucketVersioningRequestInput = TypedDict(
    "PutBucketVersioningRequestInput",
    {"status": "Required[Literal['enabled', 'suspended']]"},
    total=False,
)
PutBucketVersioningBody: TypeAlias = "PutBucketVersioningRequestInput"
PutObjectResponse2 = TypedDict(
    "PutObjectResponse2",
    {"key": "Required[str]", "etag": "Required[str]", "size": "Required[int]"},
    total=False,
)
PutObjectResponse: TypeAlias = "PutObjectResponse2 | dict[str, object]"
SnapshotUpdateRequestInput = TypedDict(
    "SnapshotUpdateRequestInput",
    {"description": "NotRequired[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
UpdateSnapshotBody: TypeAlias = "SnapshotUpdateRequestInput"
UpdateSnapshotResponse: TypeAlias = "SnapshotResponse"
SnapshotPolicyUpdateRequestInput = TypedDict(
    "SnapshotPolicyUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "enabled": "NotRequired[bool]",
        "interval_minutes": "NotRequired[SnapshotIntervalMinutesInput]",
        "retention_count": "NotRequired[SnapshotRetentionCountInput]",
        "retention_days": "NotRequired[SnapshotRetentionDaysInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateSnapshotPolicyBody: TypeAlias = "SnapshotPolicyUpdateRequestInput"
UpdateSnapshotPolicyResponse: TypeAlias = "SnapshotPolicyResponse"
VolumeUpdateRequestInput = TypedDict(
    "VolumeUpdateRequestInput",
    {"description": "NotRequired[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
UpdateVolumeBody: TypeAlias = "VolumeUpdateRequestInput"
UpdateVolumeResponse: TypeAlias = "VolumeResponse"
UpdateVolumePerformanceBody: TypeAlias = "VolumePerformanceRequestInput"
UpdateVolumePerformanceResponse: TypeAlias = "VolumeResponse"
UploadPartResponse2 = TypedDict(
    "UploadPartResponse2",
    {"part_number": "Required[int]", "etag": "Required[str]", "size": "Required[int]"},
    total=False,
)
UploadPartResponse: TypeAlias = "UploadPartResponse2"
