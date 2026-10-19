"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import registry as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    iterate_pages,
)

_OPS = {
    "batchDeleteImage": Operation(
        id="batchDeleteImage",
        method="POST",
        path="/v1/repositories/{repository_id}/images/batch-delete",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createPullThroughCacheRule": Operation(
        id="createPullThroughCacheRule",
        method="POST",
        path="/v1/pull-through-cache-rules",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRepository": Operation(
        id="createRepository",
        method="POST",
        path="/v1/repositories",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteEncryptionConfiguration": Operation(
        id="deleteEncryptionConfiguration",
        method="DELETE",
        path="/v1/encryption-configuration",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteLifecyclePolicy": Operation(
        id="deleteLifecyclePolicy",
        method="DELETE",
        path="/v1/repositories/{repository_id}/lifecycle-policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deletePullThroughCacheRule": Operation(
        id="deletePullThroughCacheRule",
        method="DELETE",
        path="/v1/pull-through-cache-rules/{prefix}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRepository": Operation(
        id="deleteRepository",
        method="DELETE",
        path="/v1/repositories/{repository_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"force": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRepositoryPolicy": Operation(
        id="deleteRepositoryPolicy",
        method="DELETE",
        path="/v1/repositories/{repository_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeImage": Operation(
        id="describeImage",
        method="GET",
        path="/v1/repositories/{repository_id}/images/{image_reference}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeImages": Operation(
        id="describeImages",
        method="GET",
        path="/v1/repositories/{repository_id}/images",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "tag_status": {"style": "form", "explode": True},
            "tag_prefix": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describePullThroughCacheRule": Operation(
        id="describePullThroughCacheRule",
        method="GET",
        path="/v1/pull-through-cache-rules/{prefix}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describePullThroughCacheRules": Operation(
        id="describePullThroughCacheRules",
        method="GET",
        path="/v1/pull-through-cache-rules",
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
    ),
    "describeRepositories": Operation(
        id="describeRepositories",
        method="GET",
        path="/v1/repositories",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeRepository": Operation(
        id="describeRepository",
        method="GET",
        path="/v1/repositories/{repository_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getAuthorizationToken": Operation(
        id="getAuthorizationToken",
        method="POST",
        path="/v1/authorization-token",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getEncryptionConfiguration": Operation(
        id="getEncryptionConfiguration",
        method="GET",
        path="/v1/encryption-configuration",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getLifecyclePolicy": Operation(
        id="getLifecyclePolicy",
        method="GET",
        path="/v1/repositories/{repository_id}/lifecycle-policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRepositoryPolicy": Operation(
        id="getRepositoryPolicy",
        method="GET",
        path="/v1/repositories/{repository_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRetainedRegistryPresence": Operation(
        id="getRetainedRegistryPresence",
        method="GET",
        path="/v1/encryption-configuration/retained-data",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listTags": Operation(
        id="listTags",
        method="GET",
        path="/v1/repositories/{repository_id}/tags",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="tags",
    ),
    "putEncryptionConfiguration": Operation(
        id="putEncryptionConfiguration",
        method="PUT",
        path="/v1/encryption-configuration",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putLifecyclePolicy": Operation(
        id="putLifecyclePolicy",
        method="PUT",
        path="/v1/repositories/{repository_id}/lifecycle-policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "setRepositoryPolicy": Operation(
        id="setRepositoryPolicy",
        method="PUT",
        path="/v1/repositories/{repository_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "startLifecyclePolicyPreview": Operation(
        id="startLifecyclePolicyPreview",
        method="POST",
        path="/v1/repositories/{repository_id}/lifecycle-policy/preview",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "updatePullThroughCacheRule": Operation(
        id="updatePullThroughCacheRule",
        method="PATCH",
        path="/v1/pull-through-cache-rules/{prefix}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRepository": Operation(
        id="updateRepository",
        method="PATCH",
        path="/v1/repositories/{repository_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class RegistryService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def batch_delete_image(
        self,
        repository_id: str,
        body: m.BatchDeleteImageBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.BatchDeleteImageResponse]:
        "Delete images"
        return cast(
            ApiResponse[m.BatchDeleteImageResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["batchDeleteImage"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    def create_pull_through_cache_rule(
        self, body: m.CreatePullThroughCacheRuleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePullThroughCacheRuleResponse]:
        "Create a pull-through cache rule"
        return cast(
            ApiResponse[m.CreatePullThroughCacheRuleResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["createPullThroughCacheRule"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_repository(
        self, body: m.CreateRepositoryBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRepositoryResponse]:
        "Create a repository"
        return cast(
            ApiResponse[m.CreateRepositoryResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["createRepository"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_encryption_configuration(self, *, options: RequestOptions | None = None) -> None:
        "Delete encryption configuration"
        return cast(
            None,
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteEncryptionConfiguration"],
                "discard",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def delete_lifecycle_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete the lifecycle policy"
        return cast(
            None,
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteLifecyclePolicy"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_pull_through_cache_rule(
        self, prefix: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a pull-through cache rule"
        return cast(
            None,
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deletePullThroughCacheRule"],
                "discard",
                {"prefix": prefix},
                UNSET,
                None,
                options,
            ),
        )

    def delete_repository(
        self,
        repository_id: str,
        *,
        query: m.DeleteRepositoryQuery | None = None,
        options: RequestOptions | None = None,
    ) -> None:
        "Delete a repository"
        return cast(
            None,
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteRepository"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    def delete_repository_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete the repository policy"
        return cast(
            None,
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteRepositoryPolicy"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_image(
        self, repository_id: str, image_reference: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeImageResponse]:
        "Describe an image"
        return cast(
            ApiResponse[m.DescribeImageResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeImage"],
                "json",
                {"repository_id": repository_id, "image_reference": image_reference},
                UNSET,
                None,
                options,
            ),
        )

    def describe_images(
        self,
        repository_id: str,
        *,
        query: m.DescribeImagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribeImagesResponse]:
        "List images"
        return cast(
            ApiResponse[m.DescribeImagesResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeImages"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    def describe_pull_through_cache_rule(
        self, prefix: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribePullThroughCacheRuleResponse]:
        "Get a pull-through cache rule"
        return cast(
            ApiResponse[m.DescribePullThroughCacheRuleResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describePullThroughCacheRule"],
                "json",
                {"prefix": prefix},
                UNSET,
                None,
                options,
            ),
        )

    def describe_pull_through_cache_rules(
        self,
        *,
        query: m.DescribePullThroughCacheRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribePullThroughCacheRulesResponse]:
        "List pull-through cache rules"
        return cast(
            ApiResponse[m.DescribePullThroughCacheRulesResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describePullThroughCacheRules"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def describe_repositories(
        self,
        *,
        query: m.DescribeRepositoriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribeRepositoriesResponse]:
        "List repositories"
        return cast(
            ApiResponse[m.DescribeRepositoriesResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeRepositories"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def describe_repository(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeRepositoryResponse]:
        "Describe a repository"
        return cast(
            ApiResponse[m.DescribeRepositoryResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeRepository"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_authorization_token(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAuthorizationTokenResponse]:
        "Get a docker login credential"
        return cast(
            ApiResponse[m.GetAuthorizationTokenResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getAuthorizationToken"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_encryption_configuration(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetEncryptionConfigurationResponse]:
        "Get the encryption configuration"
        return cast(
            ApiResponse[m.GetEncryptionConfigurationResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getEncryptionConfiguration"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_lifecycle_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLifecyclePolicyResponse]:
        "Get the lifecycle policy"
        return cast(
            ApiResponse[m.GetLifecyclePolicyResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getLifecyclePolicy"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_repository_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRepositoryPolicyResponse]:
        "Get the repository policy"
        return cast(
            ApiResponse[m.GetRepositoryPolicyResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getRepositoryPolicy"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_retained_registry_presence(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRetainedRegistryPresenceResponse]:
        "Check retained registry data presence"
        return cast(
            ApiResponse[m.GetRetainedRegistryPresenceResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getRetainedRegistryPresence"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def list_tags(
        self,
        repository_id: str,
        *,
        query: m.ListTagsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTagsResponse, m.ListTagsItem]:
        "List tags"
        return cast(
            Page[m.ListTagsResponse, m.ListTagsItem],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["listTags"],
                "page",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_tags_all(
        self,
        repository_id: str,
        *,
        query: m.ListTagsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListTagsItem]:
        return iterate_pages(
            lambda marker: self.list_tags(
                repository_id,
                query=cast(m.ListTagsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def put_encryption_configuration(
        self, body: m.PutEncryptionConfigurationBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutEncryptionConfigurationResponse]:
        "Set the encryption configuration"
        return cast(
            ApiResponse[m.PutEncryptionConfigurationResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["putEncryptionConfiguration"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def put_lifecycle_policy(
        self,
        repository_id: str,
        body: m.PutLifecyclePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutLifecyclePolicyResponse]:
        "Set the lifecycle policy"
        return cast(
            ApiResponse[m.PutLifecyclePolicyResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["putLifecyclePolicy"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    def set_repository_policy(
        self,
        repository_id: str,
        body: m.SetRepositoryPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetRepositoryPolicyResponse]:
        "Set the repository policy"
        return cast(
            ApiResponse[m.SetRepositoryPolicyResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["setRepositoryPolicy"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    def start_lifecycle_policy_preview(
        self,
        repository_id: str,
        body: m.StartLifecyclePolicyPreviewBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.StartLifecyclePolicyPreviewResponse]:
        "Preview a lifecycle policy"
        return cast(
            ApiResponse[m.StartLifecyclePolicyPreviewResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["startLifecyclePolicyPreview"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    def update_pull_through_cache_rule(
        self,
        prefix: str,
        body: m.UpdatePullThroughCacheRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdatePullThroughCacheRuleResponse]:
        "Update a pull-through cache rule"
        return cast(
            ApiResponse[m.UpdatePullThroughCacheRuleResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["updatePullThroughCacheRule"],
                "json",
                {"prefix": prefix},
                body,
                None,
                options,
            ),
        )

    def update_repository(
        self,
        repository_id: str,
        body: m.UpdateRepositoryBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRepositoryResponse]:
        "Update repository settings"
        return cast(
            ApiResponse[m.UpdateRepositoryResponse],
            self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["updateRepository"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )


class AsyncRegistryService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def batch_delete_image(
        self,
        repository_id: str,
        body: m.BatchDeleteImageBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.BatchDeleteImageResponse]:
        "Delete images"
        return cast(
            ApiResponse[m.BatchDeleteImageResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["batchDeleteImage"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    async def create_pull_through_cache_rule(
        self, body: m.CreatePullThroughCacheRuleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePullThroughCacheRuleResponse]:
        "Create a pull-through cache rule"
        return cast(
            ApiResponse[m.CreatePullThroughCacheRuleResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["createPullThroughCacheRule"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_repository(
        self, body: m.CreateRepositoryBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRepositoryResponse]:
        "Create a repository"
        return cast(
            ApiResponse[m.CreateRepositoryResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["createRepository"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_encryption_configuration(
        self, *, options: RequestOptions | None = None
    ) -> None:
        "Delete encryption configuration"
        return cast(
            None,
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteEncryptionConfiguration"],
                "discard",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_lifecycle_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete the lifecycle policy"
        return cast(
            None,
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteLifecyclePolicy"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_pull_through_cache_rule(
        self, prefix: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a pull-through cache rule"
        return cast(
            None,
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deletePullThroughCacheRule"],
                "discard",
                {"prefix": prefix},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_repository(
        self,
        repository_id: str,
        *,
        query: m.DeleteRepositoryQuery | None = None,
        options: RequestOptions | None = None,
    ) -> None:
        "Delete a repository"
        return cast(
            None,
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteRepository"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    async def delete_repository_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete the repository policy"
        return cast(
            None,
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["deleteRepositoryPolicy"],
                "discard",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_image(
        self, repository_id: str, image_reference: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeImageResponse]:
        "Describe an image"
        return cast(
            ApiResponse[m.DescribeImageResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeImage"],
                "json",
                {"repository_id": repository_id, "image_reference": image_reference},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_images(
        self,
        repository_id: str,
        *,
        query: m.DescribeImagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribeImagesResponse]:
        "List images"
        return cast(
            ApiResponse[m.DescribeImagesResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeImages"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    async def describe_pull_through_cache_rule(
        self, prefix: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribePullThroughCacheRuleResponse]:
        "Get a pull-through cache rule"
        return cast(
            ApiResponse[m.DescribePullThroughCacheRuleResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describePullThroughCacheRule"],
                "json",
                {"prefix": prefix},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_pull_through_cache_rules(
        self,
        *,
        query: m.DescribePullThroughCacheRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribePullThroughCacheRulesResponse]:
        "List pull-through cache rules"
        return cast(
            ApiResponse[m.DescribePullThroughCacheRulesResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describePullThroughCacheRules"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def describe_repositories(
        self,
        *,
        query: m.DescribeRepositoriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DescribeRepositoriesResponse]:
        "List repositories"
        return cast(
            ApiResponse[m.DescribeRepositoriesResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeRepositories"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def describe_repository(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeRepositoryResponse]:
        "Describe a repository"
        return cast(
            ApiResponse[m.DescribeRepositoryResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["describeRepository"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_authorization_token(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAuthorizationTokenResponse]:
        "Get a docker login credential"
        return cast(
            ApiResponse[m.GetAuthorizationTokenResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getAuthorizationToken"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_encryption_configuration(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetEncryptionConfigurationResponse]:
        "Get the encryption configuration"
        return cast(
            ApiResponse[m.GetEncryptionConfigurationResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getEncryptionConfiguration"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_lifecycle_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLifecyclePolicyResponse]:
        "Get the lifecycle policy"
        return cast(
            ApiResponse[m.GetLifecyclePolicyResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getLifecyclePolicy"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_repository_policy(
        self, repository_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRepositoryPolicyResponse]:
        "Get the repository policy"
        return cast(
            ApiResponse[m.GetRepositoryPolicyResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getRepositoryPolicy"],
                "json",
                {"repository_id": repository_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_retained_registry_presence(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRetainedRegistryPresenceResponse]:
        "Check retained registry data presence"
        return cast(
            ApiResponse[m.GetRetainedRegistryPresenceResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["getRetainedRegistryPresence"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def list_tags(
        self,
        repository_id: str,
        *,
        query: m.ListTagsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTagsResponse, m.ListTagsItem]:
        "List tags"
        return cast(
            Page[m.ListTagsResponse, m.ListTagsItem],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["listTags"],
                "page",
                {"repository_id": repository_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_tags_all(
        self,
        repository_id: str,
        *,
        query: m.ListTagsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListTagsItem]:
        return aiterate_pages(
            lambda marker: self.list_tags(
                repository_id,
                query=cast(m.ListTagsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def put_encryption_configuration(
        self, body: m.PutEncryptionConfigurationBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutEncryptionConfigurationResponse]:
        "Set the encryption configuration"
        return cast(
            ApiResponse[m.PutEncryptionConfigurationResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["putEncryptionConfiguration"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def put_lifecycle_policy(
        self,
        repository_id: str,
        body: m.PutLifecyclePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutLifecyclePolicyResponse]:
        "Set the lifecycle policy"
        return cast(
            ApiResponse[m.PutLifecyclePolicyResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["putLifecyclePolicy"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    async def set_repository_policy(
        self,
        repository_id: str,
        body: m.SetRepositoryPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetRepositoryPolicyResponse]:
        "Set the repository policy"
        return cast(
            ApiResponse[m.SetRepositoryPolicyResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["setRepositoryPolicy"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    async def start_lifecycle_policy_preview(
        self,
        repository_id: str,
        body: m.StartLifecyclePolicyPreviewBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.StartLifecyclePolicyPreviewResponse]:
        "Preview a lifecycle policy"
        return cast(
            ApiResponse[m.StartLifecyclePolicyPreviewResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["startLifecyclePolicyPreview"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )

    async def update_pull_through_cache_rule(
        self,
        prefix: str,
        body: m.UpdatePullThroughCacheRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdatePullThroughCacheRuleResponse]:
        "Update a pull-through cache rule"
        return cast(
            ApiResponse[m.UpdatePullThroughCacheRuleResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["updatePullThroughCacheRule"],
                "json",
                {"prefix": prefix},
                body,
                None,
                options,
            ),
        )

    async def update_repository(
        self,
        repository_id: str,
        body: m.UpdateRepositoryBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRepositoryResponse]:
        "Update repository settings"
        return cast(
            ApiResponse[m.UpdateRepositoryResponse],
            await self._transport.request(
                "registry",
                "https://registry.{region}.basaltic.sh",
                _OPS["updateRepository"],
                "json",
                {"repository_id": repository_id},
                body,
                None,
                options,
            ),
        )
