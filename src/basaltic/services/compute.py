"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

import httpx

from .._common import UNSET, Operation, Unset, WebSocketConnection
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import compute as m
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
    "attachInstanceNIC": Operation(
        id="attachInstanceNIC",
        method="POST",
        path="/v1/instances/{instance_id}/nics",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachInstancePoolFloatingIp": Operation(
        id="attachInstancePoolFloatingIp",
        method="POST",
        path="/v1/instance-pools/{pool_id}/floating-ips",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachInstanceVolume": Operation(
        id="attachInstanceVolume",
        method="POST",
        path="/v1/instances/{instance_id}/volumes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createImage": Operation(
        id="createImage",
        method="POST",
        path="/v1/images",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createInstance": Operation(
        id="createInstance",
        method="POST",
        path="/v1/instances",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createInstancePool": Operation(
        id="createInstancePool",
        method="POST",
        path="/v1/instance-pools",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSerialConsoleTicket": Operation(
        id="createSerialConsoleTicket",
        method="POST",
        path="/v1/instances/{instance_id}/console/ticket",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteImage": Operation(
        id="deleteImage",
        method="DELETE",
        path="/v1/images/{image_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInstance": Operation(
        id="deleteInstance",
        method="DELETE",
        path="/v1/instances/{instance_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInstancePool": Operation(
        id="deleteInstancePool",
        method="DELETE",
        path="/v1/instance-pools/{pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachInstanceNIC": Operation(
        id="detachInstanceNIC",
        method="DELETE",
        path="/v1/instances/{instance_id}/nics/{interface_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachInstancePoolFloatingIp": Operation(
        id="detachInstancePoolFloatingIp",
        method="DELETE",
        path="/v1/instance-pools/{pool_id}/floating-ips/{floating_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachInstanceVolume": Operation(
        id="detachInstanceVolume",
        method="DELETE",
        path="/v1/instances/{instance_id}/volumes/{volume_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getConsoleOutput": Operation(
        id="getConsoleOutput",
        method="GET",
        path="/v1/instances/{instance_id}/console/output",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"max_bytes": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getConsoleScreenshot": Operation(
        id="getConsoleScreenshot",
        method="GET",
        path="/v1/instances/{instance_id}/console/screenshot",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "getFlavor": Operation(
        id="getFlavor",
        method="GET",
        path="/v1/flavors/{flavor_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getImage": Operation(
        id="getImage",
        method="GET",
        path="/v1/images/{image_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInstance": Operation(
        id="getInstance",
        method="GET",
        path="/v1/instances/{instance_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInstancePool": Operation(
        id="getInstancePool",
        method="GET",
        path="/v1/instance-pools/{pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listFlavors": Operation(
        id="listFlavors",
        method="GET",
        path="/v1/flavors",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "family": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="flavors",
    ),
    "listImageCatalog": Operation(
        id="listImageCatalog",
        method="GET",
        path="/v1/image-catalog",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "os": {"style": "form", "explode": True},
            "architecture": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="categories",
    ),
    "listImages": Operation(
        id="listImages",
        method="GET",
        path="/v1/images",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "os": {"style": "form", "explode": True},
            "architecture": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "all_versions": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="images",
    ),
    "listInstanceNICs": Operation(
        id="listInstanceNICs",
        method="GET",
        path="/v1/instances/{instance_id}/nics",
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
        itemsKey="nics",
    ),
    "listInstancePoolFloatingIps": Operation(
        id="listInstancePoolFloatingIps",
        method="GET",
        path="/v1/instance-pools/{pool_id}/floating-ips",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="floating_ips",
    ),
    "listInstancePools": Operation(
        id="listInstancePools",
        method="GET",
        path="/v1/instance-pools",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="instance_pools",
    ),
    "listInstanceVolumes": Operation(
        id="listInstanceVolumes",
        method="GET",
        path="/v1/instances/{instance_id}/volumes",
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
        itemsKey="attachments",
    ),
    "listInstances": Operation(
        id="listInstances",
        method="GET",
        path="/v1/instances",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "current_state": {"style": "form", "explode": True},
            "flavor": {"style": "form", "explode": True},
            "image": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="instances",
    ),
    "listPoolInstances": Operation(
        id="listPoolInstances",
        method="GET",
        path="/v1/instance-pools/{pool_id}/instances",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "name": {"style": "form", "explode": True},
            "current_state": {"style": "form", "explode": True},
            "flavor": {"style": "form", "explode": True},
            "image": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="instances",
    ),
    "rebootInstance": Operation(
        id="rebootInstance",
        method="POST",
        path="/v1/instances/{instance_id}/reboot",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "refreshInstancePool": Operation(
        id="refreshInstancePool",
        method="POST",
        path="/v1/instance-pools/{pool_id}/refresh",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "reinstallInstance": Operation(
        id="reinstallInstance",
        method="POST",
        path="/v1/instances/{instance_id}/reinstall",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "resizeInstance": Operation(
        id="resizeInstance",
        method="POST",
        path="/v1/instances/{instance_id}/resize",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "startInstance": Operation(
        id="startInstance",
        method="POST",
        path="/v1/instances/{instance_id}/start",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "startSerialConsole": Operation(
        id="startSerialConsole",
        method="GET",
        path="/v1/instances/{instance_id}/console/serial",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"backlog_bytes": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "stopInstance": Operation(
        id="stopInstance",
        method="POST",
        path="/v1/instances/{instance_id}/stop",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "updateImage": Operation(
        id="updateImage",
        method="PATCH",
        path="/v1/images/{image_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateInstance": Operation(
        id="updateInstance",
        method="PATCH",
        path="/v1/instances/{instance_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateInstancePool": Operation(
        id="updateInstancePool",
        method="PATCH",
        path="/v1/instance-pools/{pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateInstanceVolumeAttachment": Operation(
        id="updateInstanceVolumeAttachment",
        method="PATCH",
        path="/v1/instances/{instance_id}/volumes/{volume_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class ComputeService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach_instance_nic(
        self,
        instance_id: str,
        body: m.AttachInstanceNICBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstanceNICResponse]:
        "Attach an existing NIC to an instance"
        return cast(
            ApiResponse[m.AttachInstanceNICResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstanceNIC"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def attach_instance_pool_floating_ip(
        self,
        pool_id: str,
        body: m.AttachInstancePoolFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstancePoolFloatingIpResponse]:
        "Give the pool a shared public address"
        return cast(
            ApiResponse[m.AttachInstancePoolFloatingIpResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstancePoolFloatingIp"],
                "json",
                {"pool_id": pool_id},
                body,
                None,
                options,
            ),
        )

    def attach_instance_volume(
        self,
        instance_id: str,
        body: m.AttachInstanceVolumeBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstanceVolumeResponse]:
        "Attach a data volume to an instance"
        return cast(
            ApiResponse[m.AttachInstanceVolumeResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstanceVolume"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def create_image(
        self, body: m.CreateImageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateImageResponse]:
        "Import an image from an object URL"
        return cast(
            ApiResponse[m.CreateImageResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createImage"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_instance(
        self, body: m.CreateInstanceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInstanceResponse]:
        "Create instance"
        return cast(
            ApiResponse[m.CreateInstanceResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createInstance"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_instance_pool(
        self, body: m.CreateInstancePoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInstancePoolResponse]:
        "Create an instance pool"
        return cast(
            ApiResponse[m.CreateInstancePoolResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createInstancePool"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_serial_console_ticket(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSerialConsoleTicketResponse]:
        "Mint a ticket for the serial console"
        return cast(
            ApiResponse[m.CreateSerialConsoleTicketResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createSerialConsoleTicket"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_image(
        self, image_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DeleteImageResponse]:
        "Delete an unused image"
        return cast(
            ApiResponse[m.DeleteImageResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteImage"],
                "json",
                {"image_id": image_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_instance_pool(self, pool_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete an instance pool"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteInstancePool"],
                "discard",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_instance_nic(
        self, instance_id: str, interface_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a NIC from a running instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstanceNIC"],
                "discard",
                {"instance_id": instance_id, "interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_instance_pool_floating_ip(
        self, pool_id: str, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Take a shared address off the pool"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstancePoolFloatingIp"],
                "discard",
                {"pool_id": pool_id, "floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_instance_volume(
        self, instance_id: str, volume_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a data volume from an instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstanceVolume"],
                "discard",
                {"instance_id": instance_id, "volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_console_output(
        self,
        instance_id: str,
        *,
        query: m.GetConsoleOutputQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetConsoleOutputResponse]:
        "Get the instance's serial console output"
        return cast(
            ApiResponse[m.GetConsoleOutputResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getConsoleOutput"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    def get_console_screenshot(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Capture the instance's display"
        return cast(
            httpx.Response,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getConsoleScreenshot"],
                "binary",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_flavor(
        self, flavor_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetFlavorResponse]:
        "Get flavor"
        return cast(
            ApiResponse[m.GetFlavorResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getFlavor"],
                "json",
                {"flavor_id": flavor_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_flavor_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetFlavorScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetFlavorResource]:
        return cast(
            ApiResponse[m.GetFlavorResource],
            resolve_reference(
                reference,
                lambda id: self.get_flavor(id, options=options),
                lambda match: self.list_flavors(
                    query=cast(m.ListFlavorsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "flavor",
            ),
        )

    def get_image(
        self, image_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetImageResponse]:
        "Get an image"
        return cast(
            ApiResponse[m.GetImageResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getImage"],
                "json",
                {"image_id": image_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_image_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetImageScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetImageResource]:
        return cast(
            ApiResponse[m.GetImageResource],
            resolve_reference(
                reference,
                lambda id: self.get_image(id, options=options),
                lambda match: self.list_images(
                    query=cast(m.ListImagesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "image",
            ),
        )

    def get_instance(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInstanceResponse]:
        "Get instance"
        return cast(
            ApiResponse[m.GetInstanceResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getInstance"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_instance_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInstanceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInstanceResource]:
        return cast(
            ApiResponse[m.GetInstanceResource],
            resolve_reference(
                reference,
                lambda id: self.get_instance(id, options=options),
                lambda match: self.list_instances(
                    query=cast(
                        m.ListInstancesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "instance",
            ),
        )

    def get_instance_pool(
        self, pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInstancePoolResponse]:
        "Get an instance pool"
        return cast(
            ApiResponse[m.GetInstancePoolResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getInstancePool"],
                "json",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_instance_pool_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInstancePoolScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInstancePoolResource]:
        return cast(
            ApiResponse[m.GetInstancePoolResource],
            resolve_reference(
                reference,
                lambda id: self.get_instance_pool(id, options=options),
                lambda match: self.list_instance_pools(
                    query=cast(
                        m.ListInstancePoolsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "instance_pool",
            ),
        )

    def list_flavors(
        self, *, query: m.ListFlavorsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListFlavorsResponse, m.ListFlavorsItem]:
        "List flavors"
        return cast(
            Page[m.ListFlavorsResponse, m.ListFlavorsItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listFlavors"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_image_catalog(
        self, *, query: m.ListImageCatalogQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListImageCatalogResponse, m.ListImageCatalogItem]:
        "List the launch image catalog"
        return cast(
            Page[m.ListImageCatalogResponse, m.ListImageCatalogItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listImageCatalog"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_image_catalog_all(
        self, *, query: m.ListImageCatalogQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListImageCatalogItem]:
        return iterate_pages(
            lambda marker: self.list_image_catalog(
                query=cast(m.ListImageCatalogQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_images(
        self, *, query: m.ListImagesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListImagesResponse, m.ListImagesItem]:
        "List images"
        return cast(
            Page[m.ListImagesResponse, m.ListImagesItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listImages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_images_all(
        self, *, query: m.ListImagesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListImagesItem]:
        return iterate_pages(
            lambda marker: self.list_images(
                query=cast(m.ListImagesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_instance_ni_cs(
        self,
        instance_id: str,
        *,
        query: m.ListInstanceNICsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstanceNICsResponse, m.ListInstanceNICsItem]:
        "List the instance's network interfaces"
        return cast(
            Page[m.ListInstanceNICsResponse, m.ListInstanceNICsItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstanceNICs"],
                "page",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_instance_pool_floating_ips(
        self,
        pool_id: str,
        *,
        query: m.ListInstancePoolFloatingIpsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstancePoolFloatingIpsResponse, m.ListInstancePoolFloatingIpsItem]:
        "List the pool's shared public addresses"
        return cast(
            Page[m.ListInstancePoolFloatingIpsResponse, m.ListInstancePoolFloatingIpsItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstancePoolFloatingIps"],
                "page",
                {"pool_id": pool_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_instance_pool_floating_ips_all(
        self,
        pool_id: str,
        *,
        query: m.ListInstancePoolFloatingIpsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListInstancePoolFloatingIpsItem]:
        return iterate_pages(
            lambda marker: self.list_instance_pool_floating_ips(
                pool_id,
                query=cast(m.ListInstancePoolFloatingIpsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_instance_pools(
        self,
        *,
        query: m.ListInstancePoolsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstancePoolsResponse, m.ListInstancePoolsItem]:
        "List instance pools"
        return cast(
            Page[m.ListInstancePoolsResponse, m.ListInstancePoolsItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstancePools"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_instance_pools_all(
        self,
        *,
        query: m.ListInstancePoolsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListInstancePoolsItem]:
        return iterate_pages(
            lambda marker: self.list_instance_pools(
                query=cast(m.ListInstancePoolsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_instance_volumes(
        self,
        instance_id: str,
        *,
        query: m.ListInstanceVolumesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstanceVolumesResponse, m.ListInstanceVolumesItem]:
        "List the instance's attached volumes"
        return cast(
            Page[m.ListInstanceVolumesResponse, m.ListInstanceVolumesItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstanceVolumes"],
                "page",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_instances(
        self, *, query: m.ListInstancesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInstancesResponse, m.ListInstancesItem]:
        "List instances"
        return cast(
            Page[m.ListInstancesResponse, m.ListInstancesItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstances"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_instances_all(
        self, *, query: m.ListInstancesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListInstancesItem]:
        return iterate_pages(
            lambda marker: self.list_instances(
                query=cast(m.ListInstancesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_pool_instances(
        self,
        pool_id: str,
        *,
        query: m.ListPoolInstancesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPoolInstancesResponse, m.ListPoolInstancesItem]:
        "List a pool's instances"
        return cast(
            Page[m.ListPoolInstancesResponse, m.ListPoolInstancesItem],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listPoolInstances"],
                "page",
                {"pool_id": pool_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_pool_instances_all(
        self,
        pool_id: str,
        *,
        query: m.ListPoolInstancesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListPoolInstancesItem]:
        return iterate_pages(
            lambda marker: self.list_pool_instances(
                pool_id,
                query=cast(m.ListPoolInstancesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def reboot_instance(
        self,
        instance_id: str,
        body: m.RebootInstanceBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Reboot instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["rebootInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def refresh_instance_pool(
        self, pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RefreshInstancePoolResponse]:
        "Roll every member onto the pool's current launch template"
        return cast(
            ApiResponse[m.RefreshInstancePoolResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["refreshInstancePool"],
                "json",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def reinstall_instance(
        self,
        instance_id: str,
        body: m.ReinstallInstanceBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Reinstall instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["reinstallInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def resize_instance(
        self, instance_id: str, body: m.ResizeInstanceBody, *, options: RequestOptions | None = None
    ) -> None:
        "Resize instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["resizeInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def start_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
        "Start instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["startInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def start_serial_console(
        self,
        instance_id: str,
        *,
        query: m.StartSerialConsoleQuery | None = None,
        options: RequestOptions | None = None,
    ) -> WebSocketConnection:
        "Open an interactive serial console"
        return cast(
            WebSocketConnection,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["startSerialConsole"],
                "websocket",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    def stop_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
        "Stop instance"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["stopInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    def update_image(
        self, image_id: str, body: m.UpdateImageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateImageResponse]:
        "Update an image's metadata"
        return cast(
            ApiResponse[m.UpdateImageResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateImage"],
                "json",
                {"image_id": image_id},
                body,
                None,
                options,
            ),
        )

    def update_instance(
        self, instance_id: str, body: m.UpdateInstanceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateInstanceResponse]:
        "Update instance"
        return cast(
            ApiResponse[m.UpdateInstanceResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstance"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    def update_instance_pool(
        self, pool_id: str, body: m.UpdateInstancePoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateInstancePoolResponse]:
        "Update an instance pool's description, size, tags or launch template"
        return cast(
            ApiResponse[m.UpdateInstancePoolResponse],
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstancePool"],
                "json",
                {"pool_id": pool_id},
                body,
                None,
                options,
            ),
        )

    def update_instance_volume_attachment(
        self,
        instance_id: str,
        volume_id: str,
        body: m.UpdateInstanceVolumeAttachmentBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Update a volume attachment's settings"
        return cast(
            None,
            self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstanceVolumeAttachment"],
                "discard",
                {"instance_id": instance_id, "volume_id": volume_id},
                body,
                None,
                options,
            ),
        )


class AsyncComputeService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach_instance_nic(
        self,
        instance_id: str,
        body: m.AttachInstanceNICBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstanceNICResponse]:
        "Attach an existing NIC to an instance"
        return cast(
            ApiResponse[m.AttachInstanceNICResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstanceNIC"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def attach_instance_pool_floating_ip(
        self,
        pool_id: str,
        body: m.AttachInstancePoolFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstancePoolFloatingIpResponse]:
        "Give the pool a shared public address"
        return cast(
            ApiResponse[m.AttachInstancePoolFloatingIpResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstancePoolFloatingIp"],
                "json",
                {"pool_id": pool_id},
                body,
                None,
                options,
            ),
        )

    async def attach_instance_volume(
        self,
        instance_id: str,
        body: m.AttachInstanceVolumeBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInstanceVolumeResponse]:
        "Attach a data volume to an instance"
        return cast(
            ApiResponse[m.AttachInstanceVolumeResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["attachInstanceVolume"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def create_image(
        self, body: m.CreateImageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateImageResponse]:
        "Import an image from an object URL"
        return cast(
            ApiResponse[m.CreateImageResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createImage"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_instance(
        self, body: m.CreateInstanceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInstanceResponse]:
        "Create instance"
        return cast(
            ApiResponse[m.CreateInstanceResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createInstance"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_instance_pool(
        self, body: m.CreateInstancePoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInstancePoolResponse]:
        "Create an instance pool"
        return cast(
            ApiResponse[m.CreateInstancePoolResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createInstancePool"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_serial_console_ticket(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSerialConsoleTicketResponse]:
        "Mint a ticket for the serial console"
        return cast(
            ApiResponse[m.CreateSerialConsoleTicketResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["createSerialConsoleTicket"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_image(
        self, image_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DeleteImageResponse]:
        "Delete an unused image"
        return cast(
            ApiResponse[m.DeleteImageResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteImage"],
                "json",
                {"image_id": image_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_instance(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_instance_pool(
        self, pool_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete an instance pool"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["deleteInstancePool"],
                "discard",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_instance_nic(
        self, instance_id: str, interface_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a NIC from a running instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstanceNIC"],
                "discard",
                {"instance_id": instance_id, "interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_instance_pool_floating_ip(
        self, pool_id: str, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Take a shared address off the pool"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstancePoolFloatingIp"],
                "discard",
                {"pool_id": pool_id, "floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_instance_volume(
        self, instance_id: str, volume_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a data volume from an instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["detachInstanceVolume"],
                "discard",
                {"instance_id": instance_id, "volume_id": volume_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_console_output(
        self,
        instance_id: str,
        *,
        query: m.GetConsoleOutputQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetConsoleOutputResponse]:
        "Get the instance's serial console output"
        return cast(
            ApiResponse[m.GetConsoleOutputResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getConsoleOutput"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    async def get_console_screenshot(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Capture the instance's display"
        return cast(
            httpx.Response,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getConsoleScreenshot"],
                "binary",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_flavor(
        self, flavor_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetFlavorResponse]:
        "Get flavor"
        return cast(
            ApiResponse[m.GetFlavorResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getFlavor"],
                "json",
                {"flavor_id": flavor_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_flavor_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetFlavorScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetFlavorResource]:
        return cast(
            ApiResponse[m.GetFlavorResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_flavor(id, options=options),
                lambda match: self.list_flavors(
                    query=cast(m.ListFlavorsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "flavor",
            ),
        )

    async def get_image(
        self, image_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetImageResponse]:
        "Get an image"
        return cast(
            ApiResponse[m.GetImageResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getImage"],
                "json",
                {"image_id": image_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_image_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetImageScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetImageResource]:
        return cast(
            ApiResponse[m.GetImageResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_image(id, options=options),
                lambda match: self.list_images(
                    query=cast(m.ListImagesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "image",
            ),
        )

    async def get_instance(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInstanceResponse]:
        "Get instance"
        return cast(
            ApiResponse[m.GetInstanceResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getInstance"],
                "json",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_instance_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInstanceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInstanceResource]:
        return cast(
            ApiResponse[m.GetInstanceResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_instance(id, options=options),
                lambda match: self.list_instances(
                    query=cast(
                        m.ListInstancesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "instance",
            ),
        )

    async def get_instance_pool(
        self, pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInstancePoolResponse]:
        "Get an instance pool"
        return cast(
            ApiResponse[m.GetInstancePoolResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["getInstancePool"],
                "json",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_instance_pool_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInstancePoolScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInstancePoolResource]:
        return cast(
            ApiResponse[m.GetInstancePoolResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_instance_pool(id, options=options),
                lambda match: self.list_instance_pools(
                    query=cast(
                        m.ListInstancePoolsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "instance_pool",
            ),
        )

    async def list_flavors(
        self, *, query: m.ListFlavorsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListFlavorsResponse, m.ListFlavorsItem]:
        "List flavors"
        return cast(
            Page[m.ListFlavorsResponse, m.ListFlavorsItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listFlavors"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_image_catalog(
        self, *, query: m.ListImageCatalogQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListImageCatalogResponse, m.ListImageCatalogItem]:
        "List the launch image catalog"
        return cast(
            Page[m.ListImageCatalogResponse, m.ListImageCatalogItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listImageCatalog"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_image_catalog_all(
        self, *, query: m.ListImageCatalogQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListImageCatalogItem]:
        return aiterate_pages(
            lambda marker: self.list_image_catalog(
                query=cast(m.ListImageCatalogQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_images(
        self, *, query: m.ListImagesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListImagesResponse, m.ListImagesItem]:
        "List images"
        return cast(
            Page[m.ListImagesResponse, m.ListImagesItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listImages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_images_all(
        self, *, query: m.ListImagesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListImagesItem]:
        return aiterate_pages(
            lambda marker: self.list_images(
                query=cast(m.ListImagesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_instance_ni_cs(
        self,
        instance_id: str,
        *,
        query: m.ListInstanceNICsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstanceNICsResponse, m.ListInstanceNICsItem]:
        "List the instance's network interfaces"
        return cast(
            Page[m.ListInstanceNICsResponse, m.ListInstanceNICsItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstanceNICs"],
                "page",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_instance_pool_floating_ips(
        self,
        pool_id: str,
        *,
        query: m.ListInstancePoolFloatingIpsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstancePoolFloatingIpsResponse, m.ListInstancePoolFloatingIpsItem]:
        "List the pool's shared public addresses"
        return cast(
            Page[m.ListInstancePoolFloatingIpsResponse, m.ListInstancePoolFloatingIpsItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstancePoolFloatingIps"],
                "page",
                {"pool_id": pool_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_instance_pool_floating_ips_all(
        self,
        pool_id: str,
        *,
        query: m.ListInstancePoolFloatingIpsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListInstancePoolFloatingIpsItem]:
        return aiterate_pages(
            lambda marker: self.list_instance_pool_floating_ips(
                pool_id,
                query=cast(m.ListInstancePoolFloatingIpsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_instance_pools(
        self,
        *,
        query: m.ListInstancePoolsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstancePoolsResponse, m.ListInstancePoolsItem]:
        "List instance pools"
        return cast(
            Page[m.ListInstancePoolsResponse, m.ListInstancePoolsItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstancePools"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_instance_pools_all(
        self,
        *,
        query: m.ListInstancePoolsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListInstancePoolsItem]:
        return aiterate_pages(
            lambda marker: self.list_instance_pools(
                query=cast(m.ListInstancePoolsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_instance_volumes(
        self,
        instance_id: str,
        *,
        query: m.ListInstanceVolumesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInstanceVolumesResponse, m.ListInstanceVolumesItem]:
        "List the instance's attached volumes"
        return cast(
            Page[m.ListInstanceVolumesResponse, m.ListInstanceVolumesItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstanceVolumes"],
                "page",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_instances(
        self, *, query: m.ListInstancesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInstancesResponse, m.ListInstancesItem]:
        "List instances"
        return cast(
            Page[m.ListInstancesResponse, m.ListInstancesItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listInstances"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_instances_all(
        self, *, query: m.ListInstancesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListInstancesItem]:
        return aiterate_pages(
            lambda marker: self.list_instances(
                query=cast(m.ListInstancesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_pool_instances(
        self,
        pool_id: str,
        *,
        query: m.ListPoolInstancesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPoolInstancesResponse, m.ListPoolInstancesItem]:
        "List a pool's instances"
        return cast(
            Page[m.ListPoolInstancesResponse, m.ListPoolInstancesItem],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["listPoolInstances"],
                "page",
                {"pool_id": pool_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_pool_instances_all(
        self,
        pool_id: str,
        *,
        query: m.ListPoolInstancesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListPoolInstancesItem]:
        return aiterate_pages(
            lambda marker: self.list_pool_instances(
                pool_id,
                query=cast(m.ListPoolInstancesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def reboot_instance(
        self,
        instance_id: str,
        body: m.RebootInstanceBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Reboot instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["rebootInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def refresh_instance_pool(
        self, pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RefreshInstancePoolResponse]:
        "Roll every member onto the pool's current launch template"
        return cast(
            ApiResponse[m.RefreshInstancePoolResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["refreshInstancePool"],
                "json",
                {"pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def reinstall_instance(
        self,
        instance_id: str,
        body: m.ReinstallInstanceBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Reinstall instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["reinstallInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def resize_instance(
        self, instance_id: str, body: m.ResizeInstanceBody, *, options: RequestOptions | None = None
    ) -> None:
        "Resize instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["resizeInstance"],
                "discard",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def start_instance(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Start instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["startInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def start_serial_console(
        self,
        instance_id: str,
        *,
        query: m.StartSerialConsoleQuery | None = None,
        options: RequestOptions | None = None,
    ) -> WebSocketConnection:
        "Open an interactive serial console"
        return cast(
            WebSocketConnection,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["startSerialConsole"],
                "websocket",
                {"instance_id": instance_id},
                UNSET,
                query,
                options,
            ),
        )

    async def stop_instance(
        self, instance_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Stop instance"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["stopInstance"],
                "discard",
                {"instance_id": instance_id},
                UNSET,
                None,
                options,
            ),
        )

    async def update_image(
        self, image_id: str, body: m.UpdateImageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateImageResponse]:
        "Update an image's metadata"
        return cast(
            ApiResponse[m.UpdateImageResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateImage"],
                "json",
                {"image_id": image_id},
                body,
                None,
                options,
            ),
        )

    async def update_instance(
        self, instance_id: str, body: m.UpdateInstanceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateInstanceResponse]:
        "Update instance"
        return cast(
            ApiResponse[m.UpdateInstanceResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstance"],
                "json",
                {"instance_id": instance_id},
                body,
                None,
                options,
            ),
        )

    async def update_instance_pool(
        self, pool_id: str, body: m.UpdateInstancePoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateInstancePoolResponse]:
        "Update an instance pool's description, size, tags or launch template"
        return cast(
            ApiResponse[m.UpdateInstancePoolResponse],
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstancePool"],
                "json",
                {"pool_id": pool_id},
                body,
                None,
                options,
            ),
        )

    async def update_instance_volume_attachment(
        self,
        instance_id: str,
        volume_id: str,
        body: m.UpdateInstanceVolumeAttachmentBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Update a volume attachment's settings"
        return cast(
            None,
            await self._transport.request(
                "compute",
                "https://compute.{region}.basaltic.sh",
                _OPS["updateInstanceVolumeAttachment"],
                "discard",
                {"instance_id": instance_id, "volume_id": volume_id},
                body,
                None,
                options,
            ),
        )
