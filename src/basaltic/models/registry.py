"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

BatchDeleteImageRequestInput = TypedDict(
    "BatchDeleteImageRequestInput",
    {"digests": "NotRequired[list[str]]", "tags": "NotRequired[list[str]]"},
    total=False,
)
BatchDeleteImageBody: TypeAlias = "BatchDeleteImageRequestInput"
BatchDeleteResult = TypedDict(
    "BatchDeleteResult",
    {
        "deleted": "Required[list[BatchDeleteResultDeletedItem]]",
        "failed": "Required[list[BatchDeleteResultFailedItem]]",
    },
    total=False,
)
BatchDeleteResultDeletedItem = TypedDict(
    "BatchDeleteResultDeletedItem",
    {"digest": "Required[str]", "tags": "NotRequired[list[str]]"},
    total=False,
)
BatchDeleteResultFailedItem = TypedDict(
    "BatchDeleteResultFailedItem",
    {
        "digest": "NotRequired[str]",
        "tag": "NotRequired[str]",
        "code": "Required[str]",
        "reason": "Required[str]",
    },
    total=False,
)
BatchDeleteImageResponse: TypeAlias = "BatchDeleteResult"
CreatePullThroughCacheRuleRequestInput = TypedDict(
    "CreatePullThroughCacheRuleRequestInput",
    {
        "prefix": "Required[str]",
        "upstream_registry": "Required[str]",
        "upstream_prefix": "NotRequired[str]",
        "upstream_username": "NotRequired[str]",
        "upstream_secret": "NotRequired[str]",
    },
    total=False,
)
CreatePullThroughCacheRuleBody: TypeAlias = "CreatePullThroughCacheRuleRequestInput"
PullThroughCacheRuleResponse = TypedDict(
    "PullThroughCacheRuleResponse",
    {"pull_through_cache_rule": "Required[PullThroughCacheRule]"},
    total=False,
)
PullThroughCacheRule = TypedDict(
    "PullThroughCacheRule",
    {
        "crn": "Required[str]",
        "prefix": "Required[str]",
        "uri_prefix": "Required[str]",
        "upstream_registry": "Required[str]",
        "upstream_prefix": "NotRequired[str]",
        "upstream_username": "NotRequired[str]",
        "has_credential": "Required[bool]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreatePullThroughCacheRuleResponse: TypeAlias = "PullThroughCacheRuleResponse"
CreateRepositoryRequestInput = TypedDict(
    "CreateRepositoryRequestInput",
    {
        "name": "Required[str]",
        "tag_mutability": "NotRequired[Literal['mutable', 'immutable']]",
        "deletion_protection": "NotRequired[bool]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateRepositoryBody: TypeAlias = "CreateRepositoryRequestInput"
RepositoryResponse = TypedDict(
    "RepositoryResponse",
    {"repository": "Required[Repository]", "push_commands": "NotRequired[list[str]]"},
    total=False,
)
Repository = TypedDict(
    "Repository",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "uri": "Required[str]",
        "tag_mutability": "Required[Literal['mutable', 'immutable']]",
        "deletion_protection": "Required[bool]",
        "tags": "NotRequired[dict[str, str]]",
        "stats": "NotRequired[RepositoryStats]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
RepositoryStats = TypedDict(
    "RepositoryStats",
    {
        "image_count": "NotRequired[int]",
        "tag_count": "NotRequired[int]",
        "size_bytes": "NotRequired[int]",
        "last_pushed_at": "NotRequired[str | None]",
    },
    total=False,
)
CreateRepositoryResponse: TypeAlias = "RepositoryResponse"
DeleteRepositoryParameters = TypedDict(
    "DeleteRepositoryParameters", {"force": "NotRequired[bool]"}, total=False
)
DeleteRepositoryQuery: TypeAlias = "DeleteRepositoryParameters"
ImageResponse = TypedDict(
    "ImageResponse",
    {"image": "Required[Image]", "manifest": "NotRequired[dict[str, object]]"},
    total=False,
)
Image = TypedDict(
    "Image",
    {
        "id": "Required[str]",
        "digest": "Required[str]",
        "media_type": "Required[str]",
        "tags": "Required[list[str]]",
        "artifact_type": "NotRequired[str]",
        "config_digest": "NotRequired[str]",
        "subject": "NotRequired[str]",
        "manifest_size_bytes": "NotRequired[int]",
        "size_bytes": "Required[int]",
        "is_index": "Required[bool]",
        "pushed_at": "Required[str]",
        "last_pulled_at": "NotRequired[str | None]",
    },
    total=False,
)
DescribeImageResponse: TypeAlias = "ImageResponse"
DescribeImagesParameters = TypedDict(
    "DescribeImagesParameters",
    {
        "tag_status": "NotRequired[Literal['tagged', 'untagged', 'any']]",
        "tag_prefix": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
DescribeImagesQuery: TypeAlias = "DescribeImagesParameters"
ImageListResponse = TypedDict(
    "ImageListResponse",
    {"images": "Required[list[Image]]", "meta": "NotRequired[PaginationMeta]"},
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
DescribeImagesResponse: TypeAlias = "ImageListResponse"
DescribePullThroughCacheRuleResponse: TypeAlias = "PullThroughCacheRuleResponse"
DescribePullThroughCacheRulesParameters = TypedDict(
    "DescribePullThroughCacheRulesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
DescribePullThroughCacheRulesQuery: TypeAlias = "DescribePullThroughCacheRulesParameters"
PullThroughCacheRuleListResponse = TypedDict(
    "PullThroughCacheRuleListResponse",
    {"pull_through_cache_rules": "Required[list[PullThroughCacheRule]]"},
    total=False,
)
DescribePullThroughCacheRulesResponse: TypeAlias = "PullThroughCacheRuleListResponse"
DescribeRepositoriesParameters = TypedDict(
    "DescribeRepositoriesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
DescribeRepositoriesQuery: TypeAlias = "DescribeRepositoriesParameters"
RepositoryListResponse = TypedDict(
    "RepositoryListResponse",
    {"repositories": "Required[list[Repository]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
DescribeRepositoriesResponse: TypeAlias = "RepositoryListResponse"
DescribeRepositoryResponse: TypeAlias = "RepositoryResponse"
AuthorizationTokenResponse = TypedDict(
    "AuthorizationTokenResponse",
    {"authorization_data": "Required[AuthorizationTokenResponseAuthorizationData]"},
    total=False,
)
AuthorizationTokenResponseAuthorizationData = TypedDict(
    "AuthorizationTokenResponseAuthorizationData",
    {
        "authorization_token": "Required[str]",
        "username": "Required[str]",
        "password": "Required[str]",
        "endpoint": "Required[str]",
        "expires_at": "Required[str]",
    },
    total=False,
)
GetAuthorizationTokenResponse: TypeAlias = "AuthorizationTokenResponse"
EncryptionConfigurationResponse = TypedDict(
    "EncryptionConfigurationResponse",
    {"encryption_configuration": "Required[EncryptionConfiguration]"},
    total=False,
)
EncryptionConfiguration = TypedDict(
    "EncryptionConfiguration",
    {
        "encryption_type": "Required[Literal['platform_managed', 'kms']]",
        "kms_key": "NotRequired[ResourceRef]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
GetEncryptionConfigurationResponse: TypeAlias = "EncryptionConfigurationResponse"
LifecyclePolicyResponse = TypedDict(
    "LifecyclePolicyResponse", {"policy": "Required[LifecyclePolicyResponsePolicy]"}, total=False
)
LifecyclePolicyResponsePolicy = TypedDict(
    "LifecyclePolicyResponsePolicy",
    {
        "rules": "Required[list[LifecycleRule]]",
        "updated_at": "Required[str]",
        "last_evaluated_at": "NotRequired[str | None]",
    },
    total=False,
)
LifecycleRule = TypedDict(
    "LifecycleRule",
    {
        "priority": "Required[int]",
        "description": "NotRequired[str]",
        "selection": "Required[LifecycleSelection]",
        "action": "Required[Literal['expire']]",
    },
    total=False,
)
LifecycleSelection = TypedDict(
    "LifecycleSelection",
    {
        "tag_status": "Required[Literal['tagged', 'untagged', 'any']]",
        "tag_prefixes": "NotRequired[list[str]]",
        "tag_patterns": "NotRequired[list[str]]",
        "count_type": "Required[Literal['image_count_more_than', 'since_image_pushed', 'since_image_pulled']]",
        "count_unit": "NotRequired[Literal['days']]",
        "count_number": "Required[int]",
    },
    total=False,
)
GetLifecyclePolicyResponse: TypeAlias = "LifecyclePolicyResponse"
RepositoryPolicyResponse = TypedDict(
    "RepositoryPolicyResponse", {"policy": "Required[RepositoryPolicyResponsePolicy]"}, total=False
)
RepositoryPolicyResponsePolicy = TypedDict(
    "RepositoryPolicyResponsePolicy",
    {"document": "Required[RepositoryPolicyDocument]", "updated_at": "NotRequired[str]"},
    total=False,
)
RepositoryPolicyDocument = TypedDict(
    "RepositoryPolicyDocument",
    {
        "version": "Required[str]",
        "statements": "Required[list[RepositoryPolicyDocumentStatementsItem]]",
    },
    total=False,
)
RepositoryPolicyDocumentStatementsItem = TypedDict(
    "RepositoryPolicyDocumentStatementsItem",
    {
        "sid": "NotRequired[str]",
        "effect": "Required[Literal['allow', 'deny']]",
        "principals": "Required[list[str]]",
        "actions": "Required[list[str]]",
        "resources": "Required[list[str]]",
        "conditions": "NotRequired[list[PolicyCondition]]",
    },
    total=False,
)
PolicyCondition = TypedDict(
    "PolicyCondition",
    {
        "operator": "Required[str]",
        "key": "Required[str]",
        "values": "Required[list[str]]",
        "set_operator": "NotRequired[Literal['for_all_values', 'for_any_value']]",
    },
    total=False,
)
GetRepositoryPolicyResponse: TypeAlias = "RepositoryPolicyResponse"
GetRetainedRegistryPresenceResult = TypedDict(
    "GetRetainedRegistryPresenceResult", {"has_resources": "Required[bool]"}, total=False
)
GetRetainedRegistryPresenceResponse: TypeAlias = "GetRetainedRegistryPresenceResult"
ListTagsParameters = TypedDict(
    "ListTagsParameters", {"marker": "NotRequired[str]", "limit": "NotRequired[int]"}, total=False
)
ListTagsQuery: TypeAlias = "ListTagsParameters"
TagListResponse = TypedDict(
    "TagListResponse",
    {"tags": "Required[list[Tag]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
Tag = TypedDict(
    "Tag",
    {
        "name": "Required[str]",
        "digest": "Required[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
ListTagsResponse: TypeAlias = "TagListResponse"
ListTagsItem: TypeAlias = "Tag"
EncryptionConfigurationRequestInput = TypedDict(
    "EncryptionConfigurationRequestInput",
    {
        "encryption_type": "Required[Literal['platform_managed', 'kms']]",
        "kms_key": "NotRequired[str]",
    },
    total=False,
)
PutEncryptionConfigurationBody: TypeAlias = "EncryptionConfigurationRequestInput"
PutEncryptionConfigurationResponse: TypeAlias = "EncryptionConfigurationResponse"
LifecyclePolicyRequestInput = TypedDict(
    "LifecyclePolicyRequestInput", {"rules": "Required[list[LifecycleRuleInput]]"}, total=False
)
LifecycleRuleInput = TypedDict(
    "LifecycleRuleInput",
    {
        "priority": "Required[int]",
        "description": "NotRequired[str]",
        "selection": "Required[LifecycleSelectionInput]",
        "action": "Required[Literal['expire']]",
    },
    total=False,
)
LifecycleSelectionInput = TypedDict(
    "LifecycleSelectionInput",
    {
        "tag_status": "Required[Literal['tagged', 'untagged', 'any']]",
        "tag_prefixes": "NotRequired[list[str]]",
        "tag_patterns": "NotRequired[list[str]]",
        "count_type": "Required[Literal['image_count_more_than', 'since_image_pushed', 'since_image_pulled']]",
        "count_unit": "NotRequired[Literal['days']]",
        "count_number": "Required[int]",
    },
    total=False,
)
PutLifecyclePolicyBody: TypeAlias = "LifecyclePolicyRequestInput"
PutLifecyclePolicyResponse: TypeAlias = "LifecyclePolicyResponse"
RepositoryPolicyRequestInput = TypedDict(
    "RepositoryPolicyRequestInput",
    {"document": "Required[RepositoryPolicyDocumentInput]"},
    total=False,
)
RepositoryPolicyDocumentInput = TypedDict(
    "RepositoryPolicyDocumentInput",
    {
        "version": "Required[str]",
        "statements": "Required[list[RepositoryPolicyDocumentInputStatementsItem]]",
    },
    total=False,
)
RepositoryPolicyDocumentInputStatementsItem = TypedDict(
    "RepositoryPolicyDocumentInputStatementsItem",
    {
        "sid": "NotRequired[str]",
        "effect": "Required[Literal['allow', 'deny']]",
        "principals": "Required[list[str]]",
        "actions": "Required[list[str]]",
        "resources": "Required[list[str]]",
        "conditions": "NotRequired[list[PolicyConditionInput]]",
    },
    total=False,
)
PolicyConditionInput = TypedDict(
    "PolicyConditionInput",
    {
        "operator": "Required[str]",
        "key": "Required[str]",
        "values": "Required[list[str]]",
        "set_operator": "NotRequired[Literal['for_all_values', 'for_any_value']]",
    },
    total=False,
)
SetRepositoryPolicyBody: TypeAlias = "RepositoryPolicyRequestInput"
SetRepositoryPolicyResponse: TypeAlias = "RepositoryPolicyResponse"
StartLifecyclePolicyPreviewBody: TypeAlias = "LifecyclePolicyRequestInput"
LifecyclePreviewResponse = TypedDict(
    "LifecyclePreviewResponse",
    {"preview": "Required[LifecyclePreviewResponsePreview]"},
    total=False,
)
LifecyclePreviewResponsePreview = TypedDict(
    "LifecyclePreviewResponsePreview",
    {
        "matches": "Required[list[LifecyclePreviewResponsePreviewMatchesItem]]",
        "total_images": "Required[int]",
        "size_bytes": "Required[int]",
    },
    total=False,
)
LifecyclePreviewResponsePreviewMatchesItem = TypedDict(
    "LifecyclePreviewResponsePreviewMatchesItem",
    {
        "digest": "Required[str]",
        "tags": "NotRequired[list[str]]",
        "pushed_at": "Required[str]",
        "last_pulled_at": "NotRequired[str | None]",
        "rule_priority": "Required[int]",
    },
    total=False,
)
StartLifecyclePolicyPreviewResponse: TypeAlias = "LifecyclePreviewResponse"
UpdatePullThroughCacheRuleRequestInput = TypedDict(
    "UpdatePullThroughCacheRuleRequestInput",
    {
        "upstream_registry": "NotRequired[str]",
        "upstream_prefix": "NotRequired[str]",
        "upstream_username": "NotRequired[str]",
        "upstream_secret": "NotRequired[str]",
    },
    total=False,
)
UpdatePullThroughCacheRuleBody: TypeAlias = "UpdatePullThroughCacheRuleRequestInput"
UpdatePullThroughCacheRuleResponse: TypeAlias = "PullThroughCacheRuleResponse"
UpdateRepositoryRequestInput = TypedDict(
    "UpdateRepositoryRequestInput",
    {
        "tag_mutability": "NotRequired[Literal['mutable', 'immutable']]",
        "deletion_protection": "NotRequired[bool]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
UpdateRepositoryBody: TypeAlias = "UpdateRepositoryRequestInput"
UpdateRepositoryResponse: TypeAlias = "RepositoryResponse"
