"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

import httpx

from .._common import UNSET, AsyncBinaryBody, BinaryBody, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import storage as m
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
    "abortMultipartUpload": Operation(
        id="abortMultipartUpload",
        method="DELETE",
        path="/v1/buckets/{bucket}/multipart-uploads/{upload_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "completeMultipartUpload": Operation(
        id="completeMultipartUpload",
        method="POST",
        path="/v1/buckets/{bucket}/multipart-uploads/{upload_id}/complete",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createBucket": Operation(
        id="createBucket",
        method="POST",
        path="/v1/buckets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSnapshot": Operation(
        id="createSnapshot",
        method="POST",
        path="/v1/snapshots",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSnapshotPolicy": Operation(
        id="createSnapshotPolicy",
        method="POST",
        path="/v1/snapshot-policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createVolume": Operation(
        id="createVolume",
        method="POST",
        path="/v1/volumes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteBucket": Operation(
        id="deleteBucket",
        method="DELETE",
        path="/v1/buckets/{bucket}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketCORS": Operation(
        id="deleteBucketCORS",
        method="DELETE",
        path="/v1/buckets/{bucket}/cors",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketEncryption": Operation(
        id="deleteBucketEncryption",
        method="DELETE",
        path="/v1/buckets/{bucket}/encryption",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketLifecycle": Operation(
        id="deleteBucketLifecycle",
        method="DELETE",
        path="/v1/buckets/{bucket}/lifecycle",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=["If-Match"],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketObjectLock": Operation(
        id="deleteBucketObjectLock",
        method="DELETE",
        path="/v1/buckets/{bucket}/object-lock",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketPolicy": Operation(
        id="deleteBucketPolicy",
        method="DELETE",
        path="/v1/buckets/{bucket}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteBucketTagging": Operation(
        id="deleteBucketTagging",
        method="DELETE",
        path="/v1/buckets/{bucket}/tagging",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteObject": Operation(
        id="deleteObject",
        method="DELETE",
        path="/v1/buckets/{bucket}/objects/{key}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSnapshot": Operation(
        id="deleteSnapshot",
        method="DELETE",
        path="/v1/snapshots/{snapshot_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSnapshotPolicy": Operation(
        id="deleteSnapshotPolicy",
        method="DELETE",
        path="/v1/snapshot-policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteVolume": Operation(
        id="deleteVolume",
        method="DELETE",
        path="/v1/volumes/{volume_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "extendVolume": Operation(
        id="extendVolume",
        method="POST",
        path="/v1/volumes/{volume_id}/extend",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "getBucketCORS": Operation(
        id="getBucketCORS",
        method="GET",
        path="/v1/buckets/{bucket}/cors",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketEncryption": Operation(
        id="getBucketEncryption",
        method="GET",
        path="/v1/buckets/{bucket}/encryption",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketLifecycle": Operation(
        id="getBucketLifecycle",
        method="GET",
        path="/v1/buckets/{bucket}/lifecycle",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketObjectLock": Operation(
        id="getBucketObjectLock",
        method="GET",
        path="/v1/buckets/{bucket}/object-lock",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketPolicy": Operation(
        id="getBucketPolicy",
        method="GET",
        path="/v1/buckets/{bucket}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketTagging": Operation(
        id="getBucketTagging",
        method="GET",
        path="/v1/buckets/{bucket}/tagging",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getBucketVersioning": Operation(
        id="getBucketVersioning",
        method="GET",
        path="/v1/buckets/{bucket}/versioning",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getObject": Operation(
        id="getObject",
        method="GET",
        path="/v1/buckets/{bucket}/objects/{key}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "getSnapshot": Operation(
        id="getSnapshot",
        method="GET",
        path="/v1/snapshots/{snapshot_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSnapshotPolicy": Operation(
        id="getSnapshotPolicy",
        method="GET",
        path="/v1/snapshot-policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getVolume": Operation(
        id="getVolume",
        method="GET",
        path="/v1/volumes/{volume_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "headBucket": Operation(
        id="headBucket",
        method="HEAD",
        path="/v1/buckets/{bucket}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "headObject": Operation(
        id="headObject",
        method="HEAD",
        path="/v1/buckets/{bucket}/objects/{key}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "initiateMultipartUpload": Operation(
        id="initiateMultipartUpload",
        method="POST",
        path="/v1/buckets/{bucket}/multipart-uploads",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "listBuckets": Operation(
        id="listBuckets",
        method="GET",
        path="/v1/buckets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="buckets",
    ),
    "listMultipartUploads": Operation(
        id="listMultipartUploads",
        method="GET",
        path="/v1/buckets/{bucket}/multipart-uploads",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "prefix": {"style": "form", "explode": True},
            "max_uploads": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="uploads",
    ),
    "listObjectVersions": Operation(
        id="listObjectVersions",
        method="GET",
        path="/v1/buckets/{bucket}/object-versions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "prefix": {"style": "form", "explode": True},
            "key_marker": {"style": "form", "explode": True},
            "version_id_marker": {"style": "form", "explode": True},
            "max_keys": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="versions",
    ),
    "listObjects": Operation(
        id="listObjects",
        method="GET",
        path="/v1/buckets/{bucket}/objects",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "prefix": {"style": "form", "explode": True},
            "delimiter": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "max_keys": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listParts": Operation(
        id="listParts",
        method="GET",
        path="/v1/buckets/{bucket}/multipart-uploads/{upload_id}/parts",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="parts",
    ),
    "listSnapshotPolicies": Operation(
        id="listSnapshotPolicies",
        method="GET",
        path="/v1/snapshot-policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "volume": {"style": "form", "explode": True},
            "enabled": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="snapshot_policies",
    ),
    "listSnapshots": Operation(
        id="listSnapshots",
        method="GET",
        path="/v1/snapshots",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "volume": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "snapshot_policy": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="snapshots",
    ),
    "listVolumeTypes": Operation(
        id="listVolumeTypes",
        method="GET",
        path="/v1/volume-types",
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
        itemsKey="volume_types",
    ),
    "listVolumes": Operation(
        id="listVolumes",
        method="GET",
        path="/v1/volumes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="volumes",
    ),
    "putBucketCORS": Operation(
        id="putBucketCORS",
        method="PUT",
        path="/v1/buckets/{bucket}/cors",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketDeletionProtection": Operation(
        id="putBucketDeletionProtection",
        method="PUT",
        path="/v1/buckets/{bucket}/deletion-protection",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketEncryption": Operation(
        id="putBucketEncryption",
        method="PUT",
        path="/v1/buckets/{bucket}/encryption",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketLifecycle": Operation(
        id="putBucketLifecycle",
        method="PUT",
        path="/v1/buckets/{bucket}/lifecycle",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=["If-Match"],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketObjectLock": Operation(
        id="putBucketObjectLock",
        method="PUT",
        path="/v1/buckets/{bucket}/object-lock",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketPolicy": Operation(
        id="putBucketPolicy",
        method="PUT",
        path="/v1/buckets/{bucket}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketTagging": Operation(
        id="putBucketTagging",
        method="PUT",
        path="/v1/buckets/{bucket}/tagging",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putBucketVersioning": Operation(
        id="putBucketVersioning",
        method="PUT",
        path="/v1/buckets/{bucket}/versioning",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putObject": Operation(
        id="putObject",
        method="PUT",
        path="/v1/buckets/{bucket}/objects/{key}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/octet-stream",
        accept="application/json",
    ),
    "restoreBucket": Operation(
        id="restoreBucket",
        method="POST",
        path="/v1/buckets/{bucket}/restore",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "updateSnapshot": Operation(
        id="updateSnapshot",
        method="PATCH",
        path="/v1/snapshots/{snapshot_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateSnapshotPolicy": Operation(
        id="updateSnapshotPolicy",
        method="PATCH",
        path="/v1/snapshot-policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateVolume": Operation(
        id="updateVolume",
        method="PATCH",
        path="/v1/volumes/{volume_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateVolumePerformance": Operation(
        id="updateVolumePerformance",
        method="POST",
        path="/v1/volumes/{volume_id}/performance",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "uploadPart": Operation(
        id="uploadPart",
        method="PUT",
        path="/v1/buckets/{bucket}/multipart-uploads/{upload_id}/parts/{part_number}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/octet-stream",
        accept="application/json",
    ),
}


class StorageService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def abort_multipart_upload(
        self, bucket: str, upload_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Abort a multipart upload"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["abortMultipartUpload"],
                "discard",
                {"bucket": bucket, "upload_id": upload_id},
                UNSET,
                None,
                options,
            ),
        )

    def complete_multipart_upload(
        self,
        bucket: str,
        upload_id: str,
        body: m.CompleteMultipartUploadBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CompleteMultipartUploadResponse]:
        "Complete a multipart upload"
        return cast(
            ApiResponse[m.CompleteMultipartUploadResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["completeMultipartUpload"],
                "json",
                {"bucket": bucket, "upload_id": upload_id},
                body,
                None,
                options,
            ),
        )

    def create_bucket(
        self, body: m.CreateBucketBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateBucketResponse]:
        "Create bucket"
        return cast(
            ApiResponse[m.CreateBucketResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createBucket"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_snapshot(
        self, body: m.CreateSnapshotBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSnapshotResponse]:
        "Create snapshot"
        return cast(
            ApiResponse[m.CreateSnapshotResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createSnapshot"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_snapshot_policy(
        self, body: m.CreateSnapshotPolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSnapshotPolicyResponse]:
        "Create snapshot policy"
        return cast(
            ApiResponse[m.CreateSnapshotPolicyResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createSnapshotPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_volume(
        self, body: m.CreateVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateVolumeResponse]:
        "Create volume"
        return cast(
            ApiResponse[m.CreateVolumeResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createVolume"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_bucket(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DeleteBucketResponse]:
        "Delete bucket"
        return cast(
            ApiResponse[m.DeleteBucketResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucket"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_cors(self, bucket: str, *, options: RequestOptions | None = None) -> None:
        "Delete bucket CORS configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketCORS"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_encryption(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket encryption configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketEncryption"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_lifecycle(self, bucket: str, *, options: RequestOptions) -> None:
        "Delete bucket lifecycle configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketLifecycle"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_object_lock(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket object-lock configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketObjectLock"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_policy(self, bucket: str, *, options: RequestOptions | None = None) -> None:
        "Delete bucket policy"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketPolicy"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_bucket_tagging(self, bucket: str, *, options: RequestOptions | None = None) -> None:
        "Delete bucket tag set"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketTagging"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def delete_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete object"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteObject"],
                "discard",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    def delete_snapshot(self, snapshot_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete snapshot"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteSnapshot"],
                "discard",
                {"snapshot_id": snapshot_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_snapshot_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete snapshot policy"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteSnapshotPolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_volume(self, volume_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete volume"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteVolume"],
                "discard",
                {"volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    def extend_volume(
        self, volume_id: str, body: m.ExtendVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ExtendVolumeResponse]:
        "Extend volume"
        return cast(
            ApiResponse[m.ExtendVolumeResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["extendVolume"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    def get_bucket_cors(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketCORSResponse]:
        "Get bucket CORS configuration"
        return cast(
            ApiResponse[m.GetBucketCORSResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketCORS"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_encryption(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketEncryptionResponse]:
        "Get bucket encryption configuration"
        return cast(
            ApiResponse[m.GetBucketEncryptionResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketEncryption"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_lifecycle(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketLifecycleResponse]:
        "Get bucket lifecycle configuration"
        return cast(
            ApiResponse[m.GetBucketLifecycleResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketLifecycle"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_object_lock(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketObjectLockResponse]:
        "Get bucket object-lock configuration"
        return cast(
            ApiResponse[m.GetBucketObjectLockResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketObjectLock"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_policy(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketPolicyResponse]:
        "Get bucket policy"
        return cast(
            ApiResponse[m.GetBucketPolicyResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketPolicy"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_tagging(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketTaggingResponse]:
        "Get bucket tag set"
        return cast(
            ApiResponse[m.GetBucketTaggingResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketTagging"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_bucket_versioning(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketVersioningResponse]:
        "Get bucket versioning state"
        return cast(
            ApiResponse[m.GetBucketVersioningResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketVersioning"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def get_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download object"
        return cast(
            httpx.Response,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getObject"],
                "binary",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    def get_snapshot(
        self, snapshot_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSnapshotResponse]:
        "Get snapshot"
        return cast(
            ApiResponse[m.GetSnapshotResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getSnapshot"],
                "json",
                {"snapshot_id": snapshot_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_snapshot_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSnapshotScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSnapshotResource]:
        return cast(
            ApiResponse[m.GetSnapshotResource],
            resolve_reference(
                reference,
                lambda id: self.get_snapshot(id, options=options),
                lambda match: self.list_snapshots(
                    query=cast(
                        m.ListSnapshotsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "snapshot",
            ),
        )

    def get_snapshot_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSnapshotPolicyResponse]:
        "Get snapshot policy"
        return cast(
            ApiResponse[m.GetSnapshotPolicyResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getSnapshotPolicy"],
                "json",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_snapshot_policy_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSnapshotPolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSnapshotPolicyResource]:
        return cast(
            ApiResponse[m.GetSnapshotPolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_snapshot_policy(id, options=options),
                lambda match: self.list_snapshot_policies(
                    query=cast(
                        m.ListSnapshotPoliciesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "snapshot_policy",
            ),
        )

    def get_volume(
        self, volume_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetVolumeResponse]:
        "Get volume"
        return cast(
            ApiResponse[m.GetVolumeResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getVolume"],
                "json",
                {"volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_volume_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetVolumeScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetVolumeResource]:
        return cast(
            ApiResponse[m.GetVolumeResource],
            resolve_reference(
                reference,
                lambda id: self.get_volume(id, options=options),
                lambda match: self.list_volumes(
                    query=cast(m.ListVolumesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "volume",
            ),
        )

    def head_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> httpx.Response:
        "Head bucket"
        return cast(
            httpx.Response,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["headBucket"],
                "binary",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def head_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Head object"
        return cast(
            httpx.Response,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["headObject"],
                "binary",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    def initiate_multipart_upload(
        self,
        bucket: str,
        body: m.InitiateMultipartUploadBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.InitiateMultipartUploadResponse]:
        "Initiate a multipart upload"
        return cast(
            ApiResponse[m.InitiateMultipartUploadResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["initiateMultipartUpload"],
                "json",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def list_buckets(
        self, *, query: m.ListBucketsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListBucketsResponse, m.ListBucketsItem]:
        "List buckets"
        return cast(
            Page[m.ListBucketsResponse, m.ListBucketsItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listBuckets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_buckets_all(
        self, *, query: m.ListBucketsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListBucketsItem]:
        return iterate_pages(
            lambda marker: self.list_buckets(
                query=cast(m.ListBucketsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_multipart_uploads(
        self,
        bucket: str,
        *,
        query: m.ListMultipartUploadsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListMultipartUploadsResponse, m.ListMultipartUploadsItem]:
        "List in-flight multipart uploads"
        return cast(
            Page[m.ListMultipartUploadsResponse, m.ListMultipartUploadsItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listMultipartUploads"],
                "page",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    def list_object_versions(
        self,
        bucket: str,
        *,
        query: m.ListObjectVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListObjectVersionsResponse, m.ListObjectVersionsItem]:
        "List object versions"
        return cast(
            Page[m.ListObjectVersionsResponse, m.ListObjectVersionsItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listObjectVersions"],
                "page",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    def list_objects(
        self,
        bucket: str,
        *,
        query: m.ListObjectsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ListObjectsResponse]:
        "List objects"
        return cast(
            ApiResponse[m.ListObjectsResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listObjects"],
                "json",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    def list_parts(
        self, bucket: str, upload_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListPartsResponse, m.ListPartsItem]:
        "List uploaded parts"
        return cast(
            Page[m.ListPartsResponse, m.ListPartsItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listParts"],
                "page",
                {"bucket": bucket, "upload_id": upload_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_snapshot_policies(
        self,
        *,
        query: m.ListSnapshotPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSnapshotPoliciesResponse, m.ListSnapshotPoliciesItem]:
        "List snapshot policies"
        return cast(
            Page[m.ListSnapshotPoliciesResponse, m.ListSnapshotPoliciesItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listSnapshotPolicies"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_snapshot_policies_all(
        self,
        *,
        query: m.ListSnapshotPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListSnapshotPoliciesItem]:
        return iterate_pages(
            lambda marker: self.list_snapshot_policies(
                query=cast(m.ListSnapshotPoliciesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_snapshots(
        self, *, query: m.ListSnapshotsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSnapshotsResponse, m.ListSnapshotsItem]:
        "List snapshots"
        return cast(
            Page[m.ListSnapshotsResponse, m.ListSnapshotsItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listSnapshots"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_snapshots_all(
        self, *, query: m.ListSnapshotsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSnapshotsItem]:
        return iterate_pages(
            lambda marker: self.list_snapshots(
                query=cast(m.ListSnapshotsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_volume_types(
        self, *, query: m.ListVolumeTypesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVolumeTypesResponse, m.ListVolumeTypesItem]:
        "List volume types"
        return cast(
            Page[m.ListVolumeTypesResponse, m.ListVolumeTypesItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listVolumeTypes"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_volumes(
        self, *, query: m.ListVolumesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVolumesResponse, m.ListVolumesItem]:
        "List volumes"
        return cast(
            Page[m.ListVolumesResponse, m.ListVolumesItem],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listVolumes"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_volumes_all(
        self, *, query: m.ListVolumesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListVolumesItem]:
        return iterate_pages(
            lambda marker: self.list_volumes(
                query=cast(m.ListVolumesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def put_bucket_cors(
        self, bucket: str, body: m.PutBucketCORSBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket CORS configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketCORS"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_deletion_protection(
        self,
        bucket: str,
        body: m.PutBucketDeletionProtectionBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set bucket deletion protection"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketDeletionProtection"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_encryption(
        self, bucket: str, body: m.PutBucketEncryptionBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket encryption configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketEncryption"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_lifecycle(
        self, bucket: str, body: m.PutBucketLifecycleBody, *, options: RequestOptions
    ) -> None:
        "Put bucket lifecycle configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketLifecycle"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_object_lock(
        self, bucket: str, body: m.PutBucketObjectLockBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket object-lock configuration"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketObjectLock"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_policy(
        self, bucket: str, body: m.PutBucketPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket policy"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketPolicy"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_tagging(
        self, bucket: str, body: m.PutBucketTaggingBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket tag set"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketTagging"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_bucket_versioning(
        self, bucket: str, body: m.PutBucketVersioningBody, *, options: RequestOptions | None = None
    ) -> None:
        "Set bucket versioning state"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketVersioning"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    def put_object(
        self, bucket: str, key: str, body: BinaryBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutObjectResponse]:
        "Upload object"
        return cast(
            ApiResponse[m.PutObjectResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putObject"],
                "json",
                {"bucket": bucket, "key": key},
                body,
                None,
                options,
            ),
        )

    def restore_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> None:
        "Restore a bucket pending deletion"
        return cast(
            None,
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["restoreBucket"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    def update_snapshot(
        self, snapshot_id: str, body: m.UpdateSnapshotBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSnapshotResponse]:
        "Update snapshot metadata"
        return cast(
            ApiResponse[m.UpdateSnapshotResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateSnapshot"],
                "json",
                {"snapshot_id": snapshot_id},
                body,
                None,
                options,
            ),
        )

    def update_snapshot_policy(
        self,
        policy_id: str,
        body: m.UpdateSnapshotPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSnapshotPolicyResponse]:
        "Update snapshot policy"
        return cast(
            ApiResponse[m.UpdateSnapshotPolicyResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateSnapshotPolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )

    def update_volume(
        self, volume_id: str, body: m.UpdateVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateVolumeResponse]:
        "Update volume metadata"
        return cast(
            ApiResponse[m.UpdateVolumeResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateVolume"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    def update_volume_performance(
        self,
        volume_id: str,
        body: m.UpdateVolumePerformanceBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateVolumePerformanceResponse]:
        "Update provisioned performance"
        return cast(
            ApiResponse[m.UpdateVolumePerformanceResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateVolumePerformance"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    def upload_part(
        self,
        bucket: str,
        upload_id: str,
        part_number: str,
        body: BinaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UploadPartResponse]:
        "Upload a part"
        return cast(
            ApiResponse[m.UploadPartResponse],
            self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["uploadPart"],
                "json",
                {"bucket": bucket, "upload_id": upload_id, "part_number": part_number},
                body,
                None,
                options,
            ),
        )


class AsyncStorageService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def abort_multipart_upload(
        self, bucket: str, upload_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Abort a multipart upload"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["abortMultipartUpload"],
                "discard",
                {"bucket": bucket, "upload_id": upload_id},
                UNSET,
                None,
                options,
            ),
        )

    async def complete_multipart_upload(
        self,
        bucket: str,
        upload_id: str,
        body: m.CompleteMultipartUploadBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CompleteMultipartUploadResponse]:
        "Complete a multipart upload"
        return cast(
            ApiResponse[m.CompleteMultipartUploadResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["completeMultipartUpload"],
                "json",
                {"bucket": bucket, "upload_id": upload_id},
                body,
                None,
                options,
            ),
        )

    async def create_bucket(
        self, body: m.CreateBucketBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateBucketResponse]:
        "Create bucket"
        return cast(
            ApiResponse[m.CreateBucketResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createBucket"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_snapshot(
        self, body: m.CreateSnapshotBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSnapshotResponse]:
        "Create snapshot"
        return cast(
            ApiResponse[m.CreateSnapshotResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createSnapshot"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_snapshot_policy(
        self, body: m.CreateSnapshotPolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSnapshotPolicyResponse]:
        "Create snapshot policy"
        return cast(
            ApiResponse[m.CreateSnapshotPolicyResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createSnapshotPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_volume(
        self, body: m.CreateVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateVolumeResponse]:
        "Create volume"
        return cast(
            ApiResponse[m.CreateVolumeResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["createVolume"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_bucket(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DeleteBucketResponse]:
        "Delete bucket"
        return cast(
            ApiResponse[m.DeleteBucketResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucket"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_cors(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket CORS configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketCORS"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_encryption(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket encryption configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketEncryption"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_lifecycle(self, bucket: str, *, options: RequestOptions) -> None:
        "Delete bucket lifecycle configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketLifecycle"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_object_lock(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket object-lock configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketObjectLock"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_policy(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket policy"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketPolicy"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_bucket_tagging(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete bucket tag set"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteBucketTagging"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete object"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteObject"],
                "discard",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_snapshot(
        self, snapshot_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete snapshot"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteSnapshot"],
                "discard",
                {"snapshot_id": snapshot_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_snapshot_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete snapshot policy"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteSnapshotPolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_volume(self, volume_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete volume"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["deleteVolume"],
                "discard",
                {"volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    async def extend_volume(
        self, volume_id: str, body: m.ExtendVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ExtendVolumeResponse]:
        "Extend volume"
        return cast(
            ApiResponse[m.ExtendVolumeResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["extendVolume"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    async def get_bucket_cors(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketCORSResponse]:
        "Get bucket CORS configuration"
        return cast(
            ApiResponse[m.GetBucketCORSResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketCORS"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_encryption(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketEncryptionResponse]:
        "Get bucket encryption configuration"
        return cast(
            ApiResponse[m.GetBucketEncryptionResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketEncryption"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_lifecycle(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketLifecycleResponse]:
        "Get bucket lifecycle configuration"
        return cast(
            ApiResponse[m.GetBucketLifecycleResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketLifecycle"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_object_lock(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketObjectLockResponse]:
        "Get bucket object-lock configuration"
        return cast(
            ApiResponse[m.GetBucketObjectLockResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketObjectLock"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_policy(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketPolicyResponse]:
        "Get bucket policy"
        return cast(
            ApiResponse[m.GetBucketPolicyResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketPolicy"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_tagging(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketTaggingResponse]:
        "Get bucket tag set"
        return cast(
            ApiResponse[m.GetBucketTaggingResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketTagging"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_bucket_versioning(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBucketVersioningResponse]:
        "Get bucket versioning state"
        return cast(
            ApiResponse[m.GetBucketVersioningResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getBucketVersioning"],
                "json",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def get_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download object"
        return cast(
            httpx.Response,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getObject"],
                "binary",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    async def get_snapshot(
        self, snapshot_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSnapshotResponse]:
        "Get snapshot"
        return cast(
            ApiResponse[m.GetSnapshotResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getSnapshot"],
                "json",
                {"snapshot_id": snapshot_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_snapshot_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSnapshotScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSnapshotResource]:
        return cast(
            ApiResponse[m.GetSnapshotResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_snapshot(id, options=options),
                lambda match: self.list_snapshots(
                    query=cast(
                        m.ListSnapshotsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "snapshot",
            ),
        )

    async def get_snapshot_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSnapshotPolicyResponse]:
        "Get snapshot policy"
        return cast(
            ApiResponse[m.GetSnapshotPolicyResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getSnapshotPolicy"],
                "json",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_snapshot_policy_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSnapshotPolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSnapshotPolicyResource]:
        return cast(
            ApiResponse[m.GetSnapshotPolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_snapshot_policy(id, options=options),
                lambda match: self.list_snapshot_policies(
                    query=cast(
                        m.ListSnapshotPoliciesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "snapshot_policy",
            ),
        )

    async def get_volume(
        self, volume_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetVolumeResponse]:
        "Get volume"
        return cast(
            ApiResponse[m.GetVolumeResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["getVolume"],
                "json",
                {"volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_volume_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetVolumeScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetVolumeResource]:
        return cast(
            ApiResponse[m.GetVolumeResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_volume(id, options=options),
                lambda match: self.list_volumes(
                    query=cast(m.ListVolumesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "volume",
            ),
        )

    async def head_bucket(
        self, bucket: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Head bucket"
        return cast(
            httpx.Response,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["headBucket"],
                "binary",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def head_object(
        self, bucket: str, key: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Head object"
        return cast(
            httpx.Response,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["headObject"],
                "binary",
                {"bucket": bucket, "key": key},
                UNSET,
                None,
                options,
            ),
        )

    async def initiate_multipart_upload(
        self,
        bucket: str,
        body: m.InitiateMultipartUploadBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.InitiateMultipartUploadResponse]:
        "Initiate a multipart upload"
        return cast(
            ApiResponse[m.InitiateMultipartUploadResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["initiateMultipartUpload"],
                "json",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def list_buckets(
        self, *, query: m.ListBucketsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListBucketsResponse, m.ListBucketsItem]:
        "List buckets"
        return cast(
            Page[m.ListBucketsResponse, m.ListBucketsItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listBuckets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_buckets_all(
        self, *, query: m.ListBucketsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListBucketsItem]:
        return aiterate_pages(
            lambda marker: self.list_buckets(
                query=cast(m.ListBucketsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_multipart_uploads(
        self,
        bucket: str,
        *,
        query: m.ListMultipartUploadsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListMultipartUploadsResponse, m.ListMultipartUploadsItem]:
        "List in-flight multipart uploads"
        return cast(
            Page[m.ListMultipartUploadsResponse, m.ListMultipartUploadsItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listMultipartUploads"],
                "page",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    async def list_object_versions(
        self,
        bucket: str,
        *,
        query: m.ListObjectVersionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListObjectVersionsResponse, m.ListObjectVersionsItem]:
        "List object versions"
        return cast(
            Page[m.ListObjectVersionsResponse, m.ListObjectVersionsItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listObjectVersions"],
                "page",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    async def list_objects(
        self,
        bucket: str,
        *,
        query: m.ListObjectsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ListObjectsResponse]:
        "List objects"
        return cast(
            ApiResponse[m.ListObjectsResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listObjects"],
                "json",
                {"bucket": bucket},
                UNSET,
                query,
                options,
            ),
        )

    async def list_parts(
        self, bucket: str, upload_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListPartsResponse, m.ListPartsItem]:
        "List uploaded parts"
        return cast(
            Page[m.ListPartsResponse, m.ListPartsItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listParts"],
                "page",
                {"bucket": bucket, "upload_id": upload_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_snapshot_policies(
        self,
        *,
        query: m.ListSnapshotPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSnapshotPoliciesResponse, m.ListSnapshotPoliciesItem]:
        "List snapshot policies"
        return cast(
            Page[m.ListSnapshotPoliciesResponse, m.ListSnapshotPoliciesItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listSnapshotPolicies"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_snapshot_policies_all(
        self,
        *,
        query: m.ListSnapshotPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListSnapshotPoliciesItem]:
        return aiterate_pages(
            lambda marker: self.list_snapshot_policies(
                query=cast(m.ListSnapshotPoliciesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_snapshots(
        self, *, query: m.ListSnapshotsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSnapshotsResponse, m.ListSnapshotsItem]:
        "List snapshots"
        return cast(
            Page[m.ListSnapshotsResponse, m.ListSnapshotsItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listSnapshots"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_snapshots_all(
        self, *, query: m.ListSnapshotsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSnapshotsItem]:
        return aiterate_pages(
            lambda marker: self.list_snapshots(
                query=cast(m.ListSnapshotsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_volume_types(
        self, *, query: m.ListVolumeTypesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVolumeTypesResponse, m.ListVolumeTypesItem]:
        "List volume types"
        return cast(
            Page[m.ListVolumeTypesResponse, m.ListVolumeTypesItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listVolumeTypes"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_volumes(
        self, *, query: m.ListVolumesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVolumesResponse, m.ListVolumesItem]:
        "List volumes"
        return cast(
            Page[m.ListVolumesResponse, m.ListVolumesItem],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["listVolumes"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_volumes_all(
        self, *, query: m.ListVolumesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListVolumesItem]:
        return aiterate_pages(
            lambda marker: self.list_volumes(
                query=cast(m.ListVolumesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def put_bucket_cors(
        self, bucket: str, body: m.PutBucketCORSBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket CORS configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketCORS"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_deletion_protection(
        self,
        bucket: str,
        body: m.PutBucketDeletionProtectionBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set bucket deletion protection"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketDeletionProtection"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_encryption(
        self, bucket: str, body: m.PutBucketEncryptionBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket encryption configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketEncryption"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_lifecycle(
        self, bucket: str, body: m.PutBucketLifecycleBody, *, options: RequestOptions
    ) -> None:
        "Put bucket lifecycle configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketLifecycle"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_object_lock(
        self, bucket: str, body: m.PutBucketObjectLockBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket object-lock configuration"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketObjectLock"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_policy(
        self, bucket: str, body: m.PutBucketPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket policy"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketPolicy"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_tagging(
        self, bucket: str, body: m.PutBucketTaggingBody, *, options: RequestOptions | None = None
    ) -> None:
        "Put bucket tag set"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketTagging"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_bucket_versioning(
        self, bucket: str, body: m.PutBucketVersioningBody, *, options: RequestOptions | None = None
    ) -> None:
        "Set bucket versioning state"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putBucketVersioning"],
                "discard",
                {"bucket": bucket},
                body,
                None,
                options,
            ),
        )

    async def put_object(
        self, bucket: str, key: str, body: AsyncBinaryBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutObjectResponse]:
        "Upload object"
        return cast(
            ApiResponse[m.PutObjectResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["putObject"],
                "json",
                {"bucket": bucket, "key": key},
                body,
                None,
                options,
            ),
        )

    async def restore_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> None:
        "Restore a bucket pending deletion"
        return cast(
            None,
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["restoreBucket"],
                "discard",
                {"bucket": bucket},
                UNSET,
                None,
                options,
            ),
        )

    async def update_snapshot(
        self, snapshot_id: str, body: m.UpdateSnapshotBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSnapshotResponse]:
        "Update snapshot metadata"
        return cast(
            ApiResponse[m.UpdateSnapshotResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateSnapshot"],
                "json",
                {"snapshot_id": snapshot_id},
                body,
                None,
                options,
            ),
        )

    async def update_snapshot_policy(
        self,
        policy_id: str,
        body: m.UpdateSnapshotPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSnapshotPolicyResponse]:
        "Update snapshot policy"
        return cast(
            ApiResponse[m.UpdateSnapshotPolicyResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateSnapshotPolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )

    async def update_volume(
        self, volume_id: str, body: m.UpdateVolumeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateVolumeResponse]:
        "Update volume metadata"
        return cast(
            ApiResponse[m.UpdateVolumeResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateVolume"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    async def update_volume_performance(
        self,
        volume_id: str,
        body: m.UpdateVolumePerformanceBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateVolumePerformanceResponse]:
        "Update provisioned performance"
        return cast(
            ApiResponse[m.UpdateVolumePerformanceResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["updateVolumePerformance"],
                "json",
                {"volume_id": volume_id},
                body,
                None,
                options,
            ),
        )

    async def upload_part(
        self,
        bucket: str,
        upload_id: str,
        part_number: str,
        body: AsyncBinaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UploadPartResponse]:
        "Upload a part"
        return cast(
            ApiResponse[m.UploadPartResponse],
            await self._transport.request(
                "storage",
                "https://storage.{region}.basaltic.sh",
                _OPS["uploadPart"],
                "json",
                {"bucket": bucket, "upload_id": upload_id, "part_number": part_number},
                body,
                None,
                options,
            ),
        )
