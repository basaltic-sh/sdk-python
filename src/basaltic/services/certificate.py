"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import certificate as m
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
    "createCertificate": Operation(
        id="createCertificate",
        method="POST",
        path="/v1/certificates",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteCertificate": Operation(
        id="deleteCertificate",
        method="DELETE",
        path="/v1/certificates/{certificate_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getCertificate": Operation(
        id="getCertificate",
        method="GET",
        path="/v1/certificates/{certificate_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getCertificateMaterial": Operation(
        id="getCertificateMaterial",
        method="GET",
        path="/v1/certificates/{certificate_id}/material",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listCertificates": Operation(
        id="listCertificates",
        method="GET",
        path="/v1/certificates",
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
        itemsKey="certificates",
    ),
    "revokeCertificate": Operation(
        id="revokeCertificate",
        method="POST",
        path="/v1/certificates/{certificate_id}/revoke",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
}


class CertificateService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create_certificate(
        self, body: m.CreateCertificateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateCertificateResponse]:
        "Create certificate"
        return cast(
            ApiResponse[m.CreateCertificateResponse],
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["createCertificate"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete certificate"
        return cast(
            None,
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["deleteCertificate"],
                "discard",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCertificateResponse]:
        "Get certificate"
        return cast(
            ApiResponse[m.GetCertificateResponse],
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["getCertificate"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_certificate_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetCertificateScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetCertificateResource]:
        return cast(
            ApiResponse[m.GetCertificateResource],
            resolve_reference(
                reference,
                lambda id: self.get_certificate(id, options=options),
                lambda match: self.list_certificates(
                    query=cast(
                        m.ListCertificatesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "certificate",
            ),
        )

    def get_certificate_material(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCertificateMaterialResponse]:
        "Fetch certificate material (leaf, chain, private key)"
        return cast(
            ApiResponse[m.GetCertificateMaterialResponse],
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["getCertificateMaterial"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_certificates(
        self, *, query: m.ListCertificatesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCertificatesResponse, m.ListCertificatesItem]:
        "List certificates"
        return cast(
            Page[m.ListCertificatesResponse, m.ListCertificatesItem],
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["listCertificates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_certificates_all(
        self, *, query: m.ListCertificatesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListCertificatesItem]:
        return iterate_pages(
            lambda marker: self.list_certificates(
                query=cast(m.ListCertificatesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def revoke_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RevokeCertificateResponse]:
        "Revoke certificate"
        return cast(
            ApiResponse[m.RevokeCertificateResponse],
            self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["revokeCertificate"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )


class AsyncCertificateService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_certificate(
        self, body: m.CreateCertificateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateCertificateResponse]:
        "Create certificate"
        return cast(
            ApiResponse[m.CreateCertificateResponse],
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["createCertificate"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete certificate"
        return cast(
            None,
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["deleteCertificate"],
                "discard",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCertificateResponse]:
        "Get certificate"
        return cast(
            ApiResponse[m.GetCertificateResponse],
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["getCertificate"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_certificate_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetCertificateScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetCertificateResource]:
        return cast(
            ApiResponse[m.GetCertificateResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_certificate(id, options=options),
                lambda match: self.list_certificates(
                    query=cast(
                        m.ListCertificatesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "certificate",
            ),
        )

    async def get_certificate_material(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCertificateMaterialResponse]:
        "Fetch certificate material (leaf, chain, private key)"
        return cast(
            ApiResponse[m.GetCertificateMaterialResponse],
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["getCertificateMaterial"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_certificates(
        self, *, query: m.ListCertificatesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCertificatesResponse, m.ListCertificatesItem]:
        "List certificates"
        return cast(
            Page[m.ListCertificatesResponse, m.ListCertificatesItem],
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["listCertificates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_certificates_all(
        self, *, query: m.ListCertificatesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListCertificatesItem]:
        return aiterate_pages(
            lambda marker: self.list_certificates(
                query=cast(m.ListCertificatesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def revoke_certificate(
        self, certificate_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RevokeCertificateResponse]:
        "Revoke certificate"
        return cast(
            ApiResponse[m.RevokeCertificateResponse],
            await self._transport.request(
                "certificate",
                "https://certificate.{region}.basaltic.sh",
                _OPS["revokeCertificate"],
                "json",
                {"certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )
