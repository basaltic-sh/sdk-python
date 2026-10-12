"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import kms as m
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
    "cancelKeyDeletion": Operation(
        id="cancelKeyDeletion",
        method="POST",
        path="/v1/keys/{key_id}/cancel-deletion",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "createKey": Operation(
        id="createKey",
        method="POST",
        path="/v1/keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "decrypt": Operation(
        id="decrypt",
        method="POST",
        path="/v1/keys/{key_id}/decrypt",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "disableKey": Operation(
        id="disableKey",
        method="POST",
        path="/v1/keys/{key_id}/disable",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "enableKey": Operation(
        id="enableKey",
        method="POST",
        path="/v1/keys/{key_id}/enable",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "encrypt": Operation(
        id="encrypt",
        method="POST",
        path="/v1/keys/{key_id}/encrypt",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "generateDataKey": Operation(
        id="generateDataKey",
        method="POST",
        path="/v1/keys/{key_id}/generate-data-key",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "getKey": Operation(
        id="getKey",
        method="GET",
        path="/v1/keys/{key_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getKeyRotation": Operation(
        id="getKeyRotation",
        method="GET",
        path="/v1/keys/{key_id}/rotations/{rotation_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getKeyRotationStatus": Operation(
        id="getKeyRotationStatus",
        method="GET",
        path="/v1/keys/{key_id}/rotation",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getPublicKey": Operation(
        id="getPublicKey",
        method="GET",
        path="/v1/keys/{key_id}/public-key",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"key_version": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listKeyRotations": Operation(
        id="listKeyRotations",
        method="GET",
        path="/v1/keys/{key_id}/rotations",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="rotations",
    ),
    "listKeys": Operation(
        id="listKeys",
        method="GET",
        path="/v1/keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "state": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="keys",
    ),
    "rewrap": Operation(
        id="rewrap",
        method="POST",
        path="/v1/keys/{key_id}/rewrap",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "rotateKeyOnDemand": Operation(
        id="rotateKeyOnDemand",
        method="POST",
        path="/v1/keys/{key_id}/rotate",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "scheduleKeyDeletion": Operation(
        id="scheduleKeyDeletion",
        method="POST",
        path="/v1/keys/{key_id}/schedule-deletion",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "setKeyRotation": Operation(
        id="setKeyRotation",
        method="PUT",
        path="/v1/keys/{key_id}/rotation",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "sign": Operation(
        id="sign",
        method="POST",
        path="/v1/keys/{key_id}/sign",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateKey": Operation(
        id="updateKey",
        method="PATCH",
        path="/v1/keys/{key_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "verify": Operation(
        id="verify",
        method="POST",
        path="/v1/keys/{key_id}/verify",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class KmsService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def cancel_key_deletion(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CancelKeyDeletionResponse]:
        "Cancel a scheduled deletion"
        return cast(
            ApiResponse[m.CancelKeyDeletionResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["cancelKeyDeletion"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def create_key(
        self, body: m.CreateKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateKeyResponse]:
        "Create a KMS key"
        return cast(
            ApiResponse[m.CreateKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["createKey"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def decrypt(
        self, key_id: str, body: m.DecryptBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DecryptResponse]:
        "Decrypt a ciphertext"
        return cast(
            ApiResponse[m.DecryptResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["decrypt"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def disable_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DisableKeyResponse]:
        "Disable a key"
        return cast(
            ApiResponse[m.DisableKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["disableKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def enable_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.EnableKeyResponse]:
        "Enable a disabled key"
        return cast(
            ApiResponse[m.EnableKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["enableKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def encrypt(
        self, key_id: str, body: m.EncryptBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.EncryptResponse]:
        "Encrypt a payload"
        return cast(
            ApiResponse[m.EncryptResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["encrypt"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def generate_data_key(
        self,
        key_id: str,
        body: m.GenerateDataKeyBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GenerateDataKeyResponse]:
        "Generate a fresh data key"
        return cast(
            ApiResponse[m.GenerateDataKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["generateDataKey"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def get_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyResponse]:
        "Get a KMS key"
        return cast(
            ApiResponse[m.GetKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_key_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetKeyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetKeyResource]:
        return cast(
            ApiResponse[m.GetKeyResource],
            resolve_reference(
                reference,
                lambda id: self.get_key(id, options=options),
                lambda match: self.list_keys(
                    query=cast(m.ListKeysQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "key",
            ),
        )

    def get_key_rotation(
        self, key_id: str, rotation_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyRotationResponse]:
        "Get a key rotation"
        return cast(
            ApiResponse[m.GetKeyRotationResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKeyRotation"],
                "json",
                {"key_id": key_id, "rotation_id": rotation_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_key_rotation_status(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyRotationStatusResponse]:
        "Get key rotation status"
        return cast(
            ApiResponse[m.GetKeyRotationStatusResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKeyRotationStatus"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_public_key(
        self,
        key_id: str,
        *,
        query: m.GetPublicKeyQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetPublicKeyResponse]:
        "Get a versioned public key"
        return cast(
            ApiResponse[m.GetPublicKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getPublicKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_key_rotations(
        self,
        key_id: str,
        *,
        query: m.ListKeyRotationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListKeyRotationsResponse, m.ListKeyRotationsItem]:
        "List key rotation history"
        return cast(
            Page[m.ListKeyRotationsResponse, m.ListKeyRotationsItem],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["listKeyRotations"],
                "page",
                {"key_id": key_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_key_rotations_all(
        self,
        key_id: str,
        *,
        query: m.ListKeyRotationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListKeyRotationsItem]:
        return iterate_pages(
            lambda marker: self.list_key_rotations(
                key_id,
                query=cast(m.ListKeyRotationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_keys(
        self, *, query: m.ListKeysQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListKeysResponse, m.ListKeysItem]:
        "List KMS keys"
        return cast(
            Page[m.ListKeysResponse, m.ListKeysItem],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["listKeys"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_keys_all(
        self, *, query: m.ListKeysQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListKeysItem]:
        return iterate_pages(
            lambda marker: self.list_keys(
                query=cast(m.ListKeysQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def rewrap(
        self, key_id: str, body: m.RewrapBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RewrapResponse]:
        "Rewrap ciphertext with current key material"
        return cast(
            ApiResponse[m.RewrapResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["rewrap"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def rotate_key_on_demand(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RotateKeyOnDemandResponse]:
        "Rotate key material now"
        return cast(
            ApiResponse[m.RotateKeyOnDemandResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["rotateKeyOnDemand"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    def schedule_key_deletion(
        self,
        key_id: str,
        body: m.ScheduleKeyDeletionBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ScheduleKeyDeletionResponse]:
        "Schedule key for deletion"
        return cast(
            ApiResponse[m.ScheduleKeyDeletionResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["scheduleKeyDeletion"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def set_key_rotation(
        self, key_id: str, body: m.SetKeyRotationBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SetKeyRotationResponse]:
        "Configure automatic key rotation"
        return cast(
            ApiResponse[m.SetKeyRotationResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["setKeyRotation"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def sign(
        self, key_id: str, body: m.SignBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SignResponse]:
        "Sign a message"
        return cast(
            ApiResponse[m.SignResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["sign"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def update_key(
        self, key_id: str, body: m.UpdateKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateKeyResponse]:
        "Update key metadata"
        return cast(
            ApiResponse[m.UpdateKeyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["updateKey"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    def verify(
        self, key_id: str, body: m.VerifyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyResponse]:
        "Verify a signature"
        return cast(
            ApiResponse[m.VerifyResponse],
            self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["verify"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )


class AsyncKmsService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def cancel_key_deletion(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CancelKeyDeletionResponse]:
        "Cancel a scheduled deletion"
        return cast(
            ApiResponse[m.CancelKeyDeletionResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["cancelKeyDeletion"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def create_key(
        self, body: m.CreateKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateKeyResponse]:
        "Create a KMS key"
        return cast(
            ApiResponse[m.CreateKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["createKey"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def decrypt(
        self, key_id: str, body: m.DecryptBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DecryptResponse]:
        "Decrypt a ciphertext"
        return cast(
            ApiResponse[m.DecryptResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["decrypt"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def disable_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DisableKeyResponse]:
        "Disable a key"
        return cast(
            ApiResponse[m.DisableKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["disableKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def enable_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.EnableKeyResponse]:
        "Enable a disabled key"
        return cast(
            ApiResponse[m.EnableKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["enableKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def encrypt(
        self, key_id: str, body: m.EncryptBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.EncryptResponse]:
        "Encrypt a payload"
        return cast(
            ApiResponse[m.EncryptResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["encrypt"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def generate_data_key(
        self,
        key_id: str,
        body: m.GenerateDataKeyBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GenerateDataKeyResponse]:
        "Generate a fresh data key"
        return cast(
            ApiResponse[m.GenerateDataKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["generateDataKey"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def get_key(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyResponse]:
        "Get a KMS key"
        return cast(
            ApiResponse[m.GetKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_key_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetKeyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetKeyResource]:
        return cast(
            ApiResponse[m.GetKeyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_key(id, options=options),
                lambda match: self.list_keys(
                    query=cast(m.ListKeysQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "key",
            ),
        )

    async def get_key_rotation(
        self, key_id: str, rotation_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyRotationResponse]:
        "Get a key rotation"
        return cast(
            ApiResponse[m.GetKeyRotationResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKeyRotation"],
                "json",
                {"key_id": key_id, "rotation_id": rotation_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_key_rotation_status(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetKeyRotationStatusResponse]:
        "Get key rotation status"
        return cast(
            ApiResponse[m.GetKeyRotationStatusResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getKeyRotationStatus"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_public_key(
        self,
        key_id: str,
        *,
        query: m.GetPublicKeyQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetPublicKeyResponse]:
        "Get a versioned public key"
        return cast(
            ApiResponse[m.GetPublicKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["getPublicKey"],
                "json",
                {"key_id": key_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_key_rotations(
        self,
        key_id: str,
        *,
        query: m.ListKeyRotationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListKeyRotationsResponse, m.ListKeyRotationsItem]:
        "List key rotation history"
        return cast(
            Page[m.ListKeyRotationsResponse, m.ListKeyRotationsItem],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["listKeyRotations"],
                "page",
                {"key_id": key_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_key_rotations_all(
        self,
        key_id: str,
        *,
        query: m.ListKeyRotationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListKeyRotationsItem]:
        return aiterate_pages(
            lambda marker: self.list_key_rotations(
                key_id,
                query=cast(m.ListKeyRotationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_keys(
        self, *, query: m.ListKeysQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListKeysResponse, m.ListKeysItem]:
        "List KMS keys"
        return cast(
            Page[m.ListKeysResponse, m.ListKeysItem],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["listKeys"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_keys_all(
        self, *, query: m.ListKeysQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListKeysItem]:
        return aiterate_pages(
            lambda marker: self.list_keys(
                query=cast(m.ListKeysQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def rewrap(
        self, key_id: str, body: m.RewrapBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RewrapResponse]:
        "Rewrap ciphertext with current key material"
        return cast(
            ApiResponse[m.RewrapResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["rewrap"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def rotate_key_on_demand(
        self, key_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RotateKeyOnDemandResponse]:
        "Rotate key material now"
        return cast(
            ApiResponse[m.RotateKeyOnDemandResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["rotateKeyOnDemand"],
                "json",
                {"key_id": key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def schedule_key_deletion(
        self,
        key_id: str,
        body: m.ScheduleKeyDeletionBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ScheduleKeyDeletionResponse]:
        "Schedule key for deletion"
        return cast(
            ApiResponse[m.ScheduleKeyDeletionResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["scheduleKeyDeletion"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def set_key_rotation(
        self, key_id: str, body: m.SetKeyRotationBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SetKeyRotationResponse]:
        "Configure automatic key rotation"
        return cast(
            ApiResponse[m.SetKeyRotationResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["setKeyRotation"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def sign(
        self, key_id: str, body: m.SignBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SignResponse]:
        "Sign a message"
        return cast(
            ApiResponse[m.SignResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["sign"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def update_key(
        self, key_id: str, body: m.UpdateKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateKeyResponse]:
        "Update key metadata"
        return cast(
            ApiResponse[m.UpdateKeyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["updateKey"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )

    async def verify(
        self, key_id: str, body: m.VerifyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyResponse]:
        "Verify a signature"
        return cast(
            ApiResponse[m.VerifyResponse],
            await self._transport.request(
                "kms",
                "https://kms.{region}.basaltic.sh",
                _OPS["verify"],
                "json",
                {"key_id": key_id},
                body,
                None,
                options,
            ),
        )
