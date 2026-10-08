"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

import httpx

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import billing as m
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
    "getBillingProfile": Operation(
        id="getBillingProfile",
        method="GET",
        path="/v1/profile",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getCurrentUsage": Operation(
        id="getCurrentUsage",
        method="GET",
        path="/v1/usage",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getFiscalInvoiceXml": Operation(
        id="getFiscalInvoiceXml",
        method="GET",
        path="/v1/fiscal-invoices/{document_id}/xml",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "getInvoice": Operation(
        id="getInvoice",
        method="GET",
        path="/v1/invoices/{invoice_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInvoicePdf": Operation(
        id="getInvoicePdf",
        method="GET",
        path="/v1/invoices/{invoice_id}/pdf",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "listCredits": Operation(
        id="listCredits",
        method="GET",
        path="/v1/credits",
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
        itemsKey="credits",
    ),
    "listFiscalInvoices": Operation(
        id="listFiscalInvoices",
        method="GET",
        path="/v1/fiscal-invoices",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"invoice": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="fiscal_documents",
    ),
    "listInvoices": Operation(
        id="listInvoices",
        method="GET",
        path="/v1/invoices",
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
        itemsKey="invoices",
    ),
    "listPayments": Operation(
        id="listPayments",
        method="GET",
        path="/v1/payments",
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
        itemsKey="payments",
    ),
    "listPrices": Operation(
        id="listPrices",
        method="GET",
        path="/v1/prices",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "service": {"style": "form", "explode": True},
            "resource_type": {"style": "form", "explode": True},
            "sku": {"style": "form", "explode": True},
            "family": {"style": "form", "explode": True},
            "at": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="prices",
    ),
    "listTransactions": Operation(
        id="listTransactions",
        method="GET",
        path="/v1/transactions",
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
        itemsKey="transactions",
    ),
    "updateBillingProfile": Operation(
        id="updateBillingProfile",
        method="PUT",
        path="/v1/profile",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class BillingService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_billing_profile(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBillingProfileResponse]:
        "Read the organization billing profile"
        return cast(
            ApiResponse[m.GetBillingProfileResponse],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getBillingProfile"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_current_usage(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCurrentUsageResponse]:
        "Get month-to-date usage total"
        return cast(
            ApiResponse[m.GetCurrentUsageResponse],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getCurrentUsage"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_fiscal_invoice_xml(
        self, document_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download issued NFS-e XML"
        return cast(
            httpx.Response,
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getFiscalInvoiceXml"],
                "binary",
                {"document_id": document_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_invoice(
        self, invoice_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInvoiceResponse]:
        "Get an invoice with its line items"
        return cast(
            ApiResponse[m.GetInvoiceResponse],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getInvoice"],
                "json",
                {"invoice_id": invoice_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_invoice_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInvoiceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInvoiceResource]:
        return cast(
            ApiResponse[m.GetInvoiceResource],
            resolve_reference(
                reference,
                lambda id: self.get_invoice(id, options=options),
                lambda match: self.list_invoices(
                    query=cast(
                        m.ListInvoicesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                False,
                None,
            ),
        )

    def get_invoice_pdf(
        self, invoice_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download an invoice as a PDF statement"
        return cast(
            httpx.Response,
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getInvoicePdf"],
                "binary",
                {"invoice_id": invoice_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_credits(
        self, *, query: m.ListCreditsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCreditsResponse, m.ListCreditsItem]:
        "List credit grants"
        return cast(
            Page[m.ListCreditsResponse, m.ListCreditsItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listCredits"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_credits_all(
        self, *, query: m.ListCreditsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListCreditsItem]:
        return iterate_pages(
            lambda marker: self.list_credits(
                query=cast(m.ListCreditsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_fiscal_invoices(
        self,
        *,
        query: m.ListFiscalInvoicesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListFiscalInvoicesResponse, m.ListFiscalInvoicesItem]:
        "List fiscal invoice issuance and delivery status"
        return cast(
            Page[m.ListFiscalInvoicesResponse, m.ListFiscalInvoicesItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listFiscalInvoices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_invoices(
        self, *, query: m.ListInvoicesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInvoicesResponse, m.ListInvoicesItem]:
        "List invoices"
        return cast(
            Page[m.ListInvoicesResponse, m.ListInvoicesItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listInvoices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_invoices_all(
        self, *, query: m.ListInvoicesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListInvoicesItem]:
        return iterate_pages(
            lambda marker: self.list_invoices(
                query=cast(m.ListInvoicesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_payments(
        self, *, query: m.ListPaymentsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPaymentsResponse, m.ListPaymentsItem]:
        "List invoice payments"
        return cast(
            Page[m.ListPaymentsResponse, m.ListPaymentsItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listPayments"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_payments_all(
        self, *, query: m.ListPaymentsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListPaymentsItem]:
        return iterate_pages(
            lambda marker: self.list_payments(
                query=cast(m.ListPaymentsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_prices(
        self, *, query: m.ListPricesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPricesResponse, m.ListPricesItem]:
        "List catalog prices"
        return cast(
            Page[m.ListPricesResponse, m.ListPricesItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listPrices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_transactions(
        self, *, query: m.ListTransactionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTransactionsResponse, m.ListTransactionsItem]:
        "List ledger transactions"
        return cast(
            Page[m.ListTransactionsResponse, m.ListTransactionsItem],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listTransactions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_transactions_all(
        self, *, query: m.ListTransactionsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListTransactionsItem]:
        return iterate_pages(
            lambda marker: self.list_transactions(
                query=cast(m.ListTransactionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def update_billing_profile(
        self, body: m.UpdateBillingProfileBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateBillingProfileResponse]:
        "Save organization billing details"
        return cast(
            ApiResponse[m.UpdateBillingProfileResponse],
            self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["updateBillingProfile"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )


class AsyncBillingService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_billing_profile(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetBillingProfileResponse]:
        "Read the organization billing profile"
        return cast(
            ApiResponse[m.GetBillingProfileResponse],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getBillingProfile"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_current_usage(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetCurrentUsageResponse]:
        "Get month-to-date usage total"
        return cast(
            ApiResponse[m.GetCurrentUsageResponse],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getCurrentUsage"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_fiscal_invoice_xml(
        self, document_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download issued NFS-e XML"
        return cast(
            httpx.Response,
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getFiscalInvoiceXml"],
                "binary",
                {"document_id": document_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_invoice(
        self, invoice_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInvoiceResponse]:
        "Get an invoice with its line items"
        return cast(
            ApiResponse[m.GetInvoiceResponse],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getInvoice"],
                "json",
                {"invoice_id": invoice_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_invoice_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInvoiceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInvoiceResource]:
        return cast(
            ApiResponse[m.GetInvoiceResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_invoice(id, options=options),
                lambda match: self.list_invoices(
                    query=cast(
                        m.ListInvoicesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                False,
                None,
            ),
        )

    async def get_invoice_pdf(
        self, invoice_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download an invoice as a PDF statement"
        return cast(
            httpx.Response,
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["getInvoicePdf"],
                "binary",
                {"invoice_id": invoice_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_credits(
        self, *, query: m.ListCreditsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListCreditsResponse, m.ListCreditsItem]:
        "List credit grants"
        return cast(
            Page[m.ListCreditsResponse, m.ListCreditsItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listCredits"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_credits_all(
        self, *, query: m.ListCreditsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListCreditsItem]:
        return aiterate_pages(
            lambda marker: self.list_credits(
                query=cast(m.ListCreditsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_fiscal_invoices(
        self,
        *,
        query: m.ListFiscalInvoicesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListFiscalInvoicesResponse, m.ListFiscalInvoicesItem]:
        "List fiscal invoice issuance and delivery status"
        return cast(
            Page[m.ListFiscalInvoicesResponse, m.ListFiscalInvoicesItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listFiscalInvoices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_invoices(
        self, *, query: m.ListInvoicesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInvoicesResponse, m.ListInvoicesItem]:
        "List invoices"
        return cast(
            Page[m.ListInvoicesResponse, m.ListInvoicesItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listInvoices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_invoices_all(
        self, *, query: m.ListInvoicesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListInvoicesItem]:
        return aiterate_pages(
            lambda marker: self.list_invoices(
                query=cast(m.ListInvoicesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_payments(
        self, *, query: m.ListPaymentsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPaymentsResponse, m.ListPaymentsItem]:
        "List invoice payments"
        return cast(
            Page[m.ListPaymentsResponse, m.ListPaymentsItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listPayments"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_payments_all(
        self, *, query: m.ListPaymentsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListPaymentsItem]:
        return aiterate_pages(
            lambda marker: self.list_payments(
                query=cast(m.ListPaymentsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_prices(
        self, *, query: m.ListPricesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPricesResponse, m.ListPricesItem]:
        "List catalog prices"
        return cast(
            Page[m.ListPricesResponse, m.ListPricesItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listPrices"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_transactions(
        self, *, query: m.ListTransactionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTransactionsResponse, m.ListTransactionsItem]:
        "List ledger transactions"
        return cast(
            Page[m.ListTransactionsResponse, m.ListTransactionsItem],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["listTransactions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_transactions_all(
        self, *, query: m.ListTransactionsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListTransactionsItem]:
        return aiterate_pages(
            lambda marker: self.list_transactions(
                query=cast(m.ListTransactionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def update_billing_profile(
        self, body: m.UpdateBillingProfileBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateBillingProfileResponse]:
        "Save organization billing details"
        return cast(
            ApiResponse[m.UpdateBillingProfileResponse],
            await self._transport.request(
                "billing",
                "https://billing.basaltic.sh",
                _OPS["updateBillingProfile"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )
