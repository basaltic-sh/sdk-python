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
