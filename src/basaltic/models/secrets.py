"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import NotRequired, Required, TypeAlias, TypedDict

CreateSecretRequestInput = TypedDict(
    "CreateSecretRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "value": "Required[str]",
        "recovery_window_days": "NotRequired[int]",
        "kms_key": "NotRequired[str]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateSecretBody: TypeAlias = "CreateSecretRequestInput"
SecretResponse = TypedDict("SecretResponse", {"secret": "Required[Secret]"}, total=False)
Secret = TypedDict(
    "Secret",
    {
        "id": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "crn": "Required[str]",
        "kms_key_unavailable": "NotRequired[bool]",
        "kms_key_crn": "NotRequired[str | None]",
        "managed": "Required[bool]",
        "deleted_at": "NotRequired[str | None]",
        "scheduled_purge_at": "NotRequired[str | None]",
        "recovery_window_days": "Required[int]",
        "current_version": "NotRequired[int]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
CreateSecretResponse: TypeAlias = "SecretResponse"
DeleteSecretRequestInput = TypedDict(
    "DeleteSecretRequestInput", {"recovery_window_days": "NotRequired[int]"}, total=False
)
DeleteSecretBody: TypeAlias = "DeleteSecretRequestInput"
DeleteSecretResponse: TypeAlias = "SecretResponse"
DescribeSecretResponse: TypeAlias = "SecretResponse"
GetSecretValueParameters = TypedDict(
    "GetSecretValueParameters", {"version": "NotRequired[int]"}, total=False
)
GetSecretValueQuery: TypeAlias = "GetSecretValueParameters"
SecretValueResponse = TypedDict(
    "SecretValueResponse", {"secret": "Required[SecretValue]"}, total=False
)
SecretValue = TypedDict(
    "SecretValue",
    {
        "secret_id": "Required[str]",
        "name": "Required[str]",
        "version": "Required[int]",
        "value": "Required[str]",
        "created_at": "Required[str]",
    },
    total=False,
)
GetSecretValueResponse: TypeAlias = "SecretValueResponse"
ListSecretsParameters = TypedDict(
    "ListSecretsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "include_deleted": "NotRequired[bool]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListSecretsQuery: TypeAlias = "ListSecretsParameters"
SecretListResponse = TypedDict(
    "SecretListResponse",
    {"secrets": "Required[list[Secret]]", "meta": "NotRequired[PaginationMeta]"},
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
ListSecretsResponse: TypeAlias = "SecretListResponse"
ListSecretsItem: TypeAlias = "Secret"
ListVersionsParameters = TypedDict(
    "ListVersionsParameters",
    {"crn": "NotRequired[str]", "marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListVersionsQuery: TypeAlias = "ListVersionsParameters"
VersionListResponse = TypedDict(
    "VersionListResponse",
    {"versions": "Required[list[SecretVersion]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
SecretVersion = TypedDict(
    "SecretVersion",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "version": "Required[int]",
        "is_current": "Required[bool]",
        "created_by": "NotRequired[str]",
        "created_at": "Required[str]",
    },
    total=False,
)
ListVersionsResponse: TypeAlias = "VersionListResponse"
ListVersionsItem: TypeAlias = "SecretVersion"
PutSecretValueRequestInput = TypedDict(
    "PutSecretValueRequestInput", {"value": "Required[str]"}, total=False
)
PutSecretValueBody: TypeAlias = "PutSecretValueRequestInput"
VersionResponse = TypedDict("VersionResponse", {"version": "Required[SecretVersion]"}, total=False)
PutSecretValueResponse: TypeAlias = "VersionResponse"
RestoreSecretResponse: TypeAlias = "SecretResponse"
UpdateSecretRequestInput = TypedDict(
    "UpdateSecretRequestInput",
    {"description": "NotRequired[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
UpdateSecretBody: TypeAlias = "UpdateSecretRequestInput"
UpdateSecretResponse: TypeAlias = "SecretResponse"
