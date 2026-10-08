"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import secrets as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    iterate_pages,
)

_OPS = {
    "createSecret": Operation(
        id="createSecret",
        method="POST",
        path="/v1/secrets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteSecret": Operation(
        id="deleteSecret",
        method="DELETE",
        path="/v1/secrets/{secret_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "describeSecret": Operation(
        id="describeSecret",
        method="GET",
        path="/v1/secrets/{secret_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSecretValue": Operation(
        id="getSecretValue",
        method="GET",
        path="/v1/secrets/{secret_id}/value",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"version": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listSecrets": Operation(
        id="listSecrets",
        method="GET",
        path="/v1/secrets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "include_deleted": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="secrets",
    ),
    "listVersions": Operation(
        id="listVersions",
        method="GET",
        path="/v1/secrets/{secret_id}/versions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="versions",
    ),
    "putSecretValue": Operation(
        id="putSecretValue",
        method="POST",
        path="/v1/secrets/{secret_id}/value",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "restoreSecret": Operation(
        id="restoreSecret",
        method="POST",
        path="/v1/secrets/{secret_id}/restore",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "updateSecret": Operation(
        id="updateSecret",
        method="PATCH",
        path="/v1/secrets/{secret_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class SecretsService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create_secret(
        self, body: m.CreateSecretBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSecretResponse]:
        "Create a new secret with an initial value"
        return cast(
            ApiResponse[m.CreateSecretResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["createSecret"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_secret(
        self,
        secret_id: str,
        body: m.DeleteSecretBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DeleteSecretResponse]:
        "Schedule deletion (soft delete with recovery window)"
        return cast(
            ApiResponse[m.DeleteSecretResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["deleteSecret"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )

    def describe_secret(
        self, secret_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSecretResponse]:
        "Describe a secret (no value)"
        return cast(
            ApiResponse[m.DescribeSecretResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["describeSecret"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_secret_value(
        self,
        secret_id: str,
        *,
        query: m.GetSecretValueQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecretValueResponse]:
        "Read the current value (or a specific version)"
        return cast(
            ApiResponse[m.GetSecretValueResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["getSecretValue"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_secrets(
        self, *, query: m.ListSecretsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSecretsResponse, m.ListSecretsItem]:
        "List secrets"
        return cast(
            Page[m.ListSecretsResponse, m.ListSecretsItem],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["listSecrets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_secrets_all(
        self, *, query: m.ListSecretsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSecretsItem]:
        return iterate_pages(
            lambda marker: self.list_secrets(
                query=cast(m.ListSecretsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_versions(
        self,
        secret_id: str,
        *,
        query: m.ListVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListVersionsResponse, m.ListVersionsItem]:
        "List versions"
        return cast(
            Page[m.ListVersionsResponse, m.ListVersionsItem],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["listVersions"],
                "page",
                {"secret_id": secret_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_versions_all(
        self,
        secret_id: str,
        *,
        query: m.ListVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListVersionsItem]:
        return iterate_pages(
            lambda marker: self.list_versions(
                secret_id,
                query=cast(m.ListVersionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def put_secret_value(
        self, secret_id: str, body: m.PutSecretValueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutSecretValueResponse]:
        "Store a new version (becomes current)"
        return cast(
            ApiResponse[m.PutSecretValueResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["putSecretValue"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )

    def restore_secret(
        self, secret_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RestoreSecretResponse]:
        "Restore a secret from the recovery window"
        return cast(
            ApiResponse[m.RestoreSecretResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["restoreSecret"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                None,
                options,
            ),
        )

    def update_secret(
        self, secret_id: str, body: m.UpdateSecretBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSecretResponse]:
        "Update mutable metadata"
        return cast(
            ApiResponse[m.UpdateSecretResponse],
            self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["updateSecret"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )


class AsyncSecretsService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_secret(
        self, body: m.CreateSecretBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSecretResponse]:
        "Create a new secret with an initial value"
        return cast(
            ApiResponse[m.CreateSecretResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["createSecret"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_secret(
        self,
        secret_id: str,
        body: m.DeleteSecretBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DeleteSecretResponse]:
        "Schedule deletion (soft delete with recovery window)"
        return cast(
            ApiResponse[m.DeleteSecretResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["deleteSecret"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )

    async def describe_secret(
        self, secret_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSecretResponse]:
        "Describe a secret (no value)"
        return cast(
            ApiResponse[m.DescribeSecretResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["describeSecret"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_secret_value(
        self,
        secret_id: str,
        *,
        query: m.GetSecretValueQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecretValueResponse]:
        "Read the current value (or a specific version)"
        return cast(
            ApiResponse[m.GetSecretValueResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["getSecretValue"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_secrets(
        self, *, query: m.ListSecretsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSecretsResponse, m.ListSecretsItem]:
        "List secrets"
        return cast(
            Page[m.ListSecretsResponse, m.ListSecretsItem],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["listSecrets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_secrets_all(
        self, *, query: m.ListSecretsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSecretsItem]:
        return aiterate_pages(
            lambda marker: self.list_secrets(
                query=cast(m.ListSecretsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_versions(
        self,
        secret_id: str,
        *,
        query: m.ListVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListVersionsResponse, m.ListVersionsItem]:
        "List versions"
        return cast(
            Page[m.ListVersionsResponse, m.ListVersionsItem],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["listVersions"],
                "page",
                {"secret_id": secret_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_versions_all(
        self,
        secret_id: str,
        *,
        query: m.ListVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListVersionsItem]:
        return aiterate_pages(
            lambda marker: self.list_versions(
                secret_id,
                query=cast(m.ListVersionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def put_secret_value(
        self, secret_id: str, body: m.PutSecretValueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutSecretValueResponse]:
        "Store a new version (becomes current)"
        return cast(
            ApiResponse[m.PutSecretValueResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["putSecretValue"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )

    async def restore_secret(
        self, secret_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RestoreSecretResponse]:
        "Restore a secret from the recovery window"
        return cast(
            ApiResponse[m.RestoreSecretResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["restoreSecret"],
                "json",
                {"secret_id": secret_id},
                UNSET,
                None,
                options,
            ),
        )

    async def update_secret(
        self, secret_id: str, body: m.UpdateSecretBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSecretResponse]:
        "Update mutable metadata"
        return cast(
            ApiResponse[m.UpdateSecretResponse],
            await self._transport.request(
                "secrets",
                "https://secrets.{region}.basaltic.sh",
                _OPS["updateSecret"],
                "json",
                {"secret_id": secret_id},
                body,
                None,
                options,
            ),
        )
