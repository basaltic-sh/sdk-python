"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

BillingProfile = TypedDict(
    "BillingProfile",
    {
        "customer_type": "NotRequired[Literal['', 'individual', 'company']]",
        "company_name": "NotRequired[str]",
        "country": "NotRequired[str]",
        "tax_id": "NotRequired[str]",
        "foreign_tax_id": "NotRequired[str]",
        "no_tax_id_reason": "NotRequired[str]",
        "email": "NotRequired[str]",
        "phone": "NotRequired[str]",
        "street_name": "NotRequired[str]",
        "street_number": "NotRequired[str]",
        "complement": "NotRequired[str]",
        "neighborhood": "NotRequired[str]",
        "city": "NotRequired[str]",
        "municipality_code": "NotRequired[str]",
        "state": "NotRequired[str]",
        "postal_code": "NotRequired[str]",
        "ready": "NotRequired[bool]",
        "missing_fields": "NotRequired[list[str]]",
    },
    total=False,
)
GetBillingProfileResponse: TypeAlias = "BillingProfile"
CurrentUsage = TypedDict(
    "CurrentUsage",
    {
        "amount": "Required[str]",
        "period_start": "Required[str]",
        "items": "Required[list[UsageLine]]",
    },
    total=False,
)
UsageLine = TypedDict(
    "UsageLine",
    {
        "sku": "Required[str]",
        "description": "Required[str]",
        "quantity": "Required[str]",
        "unit": "Required[str]",
        "amount": "Required[str]",
    },
    total=False,
)
GetCurrentUsageResponse: TypeAlias = "CurrentUsage"
Invoice = TypedDict(
    "Invoice",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "invoice_number": "Required[str]",
        "period_start": "Required[str]",
        "period_end": "Required[str]",
        "subtotal": "Required[str]",
        "credits_applied": "Required[str]",
        "total": "Required[str]",
        "currency": "Required[str]",
        "refunded_amount": "Required[str]",
        "disputed_amount": "Required[str]",
        "status": "Required[Literal['open', 'paid', 'past_due', 'uncollectible', 'void']]",
        "issued_at": "NotRequired[str | None]",
        "due_at": "NotRequired[str | None]",
        "paid_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
        "pdf_url": "NotRequired[str]",
        "items": "NotRequired[list[InvoiceItem]]",
    },
    total=False,
)
InvoiceItem = TypedDict(
    "InvoiceItem",
    {
        "kind": "Required[Literal['usage', 'credit']]",
        "sku": "NotRequired[str | None]",
        "description": "Required[str]",
        "quantity": "Required[str]",
        "unit": "NotRequired[str | None]",
        "unit_price": "Required[str]",
        "amount": "Required[str]",
    },
    total=False,
)
GetInvoiceResponse: TypeAlias = "Invoice"
GetInvoiceResource: TypeAlias = "GetInvoiceResponse"
GetInvoiceScope = TypedDict("GetInvoiceScope", {"limit": "NotRequired[int]"}, total=False)
ListCreditsParameters = TypedDict(
    "ListCreditsParameters",
    {"crn": "NotRequired[str]", "marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListCreditsQuery: TypeAlias = "ListCreditsParameters"
CreditListResponse = TypedDict(
    "CreditListResponse",
    {"credits": "Required[list[Credit]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
Credit = TypedDict(
    "Credit",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "source": "Required[Literal['promo', 'coupon', 'adjustment', 'migration']]",
        "description": "Required[str]",
        "amount": "Required[str]",
        "remaining": "Required[str]",
        "expires_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
    },
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
ListCreditsResponse: TypeAlias = "CreditListResponse"
ListCreditsItem: TypeAlias = "Credit"
ListFiscalInvoicesParameters = TypedDict(
    "ListFiscalInvoicesParameters", {"invoice": "NotRequired[str]"}, total=False
)
ListFiscalInvoicesQuery: TypeAlias = "ListFiscalInvoicesParameters"
ListFiscalInvoicesResult = TypedDict(
    "ListFiscalInvoicesResult", {"fiscal_documents": "Required[list[FiscalInvoice]]"}, total=False
)
FiscalInvoice = TypedDict(
    "FiscalInvoice",
    {
        "id": "Required[str]",
        "organization_id": "Required[str]",
        "payment_id": "Required[str]",
        "invoice_id": "NotRequired[str | None]",
        "amount": "Required[str]",
        "status": "Required[Literal['queued', 'waiting_details', 'retrying', 'rejected', 'issued', 'review_required']]",
        "email_status": "Required[Literal['pending', 'queued']]",
        "last_error": "NotRequired[str]",
        "attempts": "Required[int]",
        "number": "NotRequired[str]",
        "verification_code": "NotRequired[str]",
        "url": "NotRequired[str]",
        "issued_at": "NotRequired[str]",
        "requires_review": "Required[bool]",
        "created_at": "Required[str]",
    },
    total=False,
)
ListFiscalInvoicesResponse: TypeAlias = "ListFiscalInvoicesResult"
ListFiscalInvoicesItem: TypeAlias = "FiscalInvoice"
ListInvoicesParameters = TypedDict(
    "ListInvoicesParameters",
    {"crn": "NotRequired[str]", "marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListInvoicesQuery: TypeAlias = "ListInvoicesParameters"
InvoiceListResponse = TypedDict(
    "InvoiceListResponse",
    {"invoices": "Required[list[Invoice]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInvoicesResponse: TypeAlias = "InvoiceListResponse"
ListInvoicesItem: TypeAlias = "Invoice"
ListPaymentsParameters = TypedDict(
    "ListPaymentsParameters",
    {"crn": "NotRequired[str]", "marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListPaymentsQuery: TypeAlias = "ListPaymentsParameters"
PaymentListResponse = TypedDict(
    "PaymentListResponse",
    {"payments": "Required[list[Payment]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
Payment = TypedDict(
    "Payment",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "invoice": "Required[Invoice | Literal[None] | None]",
        "amount": "Required[str]",
        "refunded_amount": "Required[str]",
        "disputed_amount": "Required[str]",
        "retained_amount": "Required[str]",
        "status": "Required[Literal['pending', 'processing', 'succeeded', 'failed', 'refunded']]",
        "attempt": "Required[int]",
        "completed_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
    },
    total=False,
)
ListPaymentsResponse: TypeAlias = "PaymentListResponse"
ListPaymentsItem: TypeAlias = "Payment"
ListPricesParameters = TypedDict(
    "ListPricesParameters",
    {
        "service": "NotRequired[str]",
        "resource_type": "NotRequired[str]",
        "sku": "NotRequired[str]",
        "family": "NotRequired[str]",
        "at": "NotRequired[str]",
    },
    total=False,
)
ListPricesQuery: TypeAlias = "ListPricesParameters"
PriceListResponse = TypedDict(
    "PriceListResponse", {"prices": "Required[list[Price]]", "as_of": "Required[str]"}, total=False
)
Price = TypedDict(
    "Price",
    {
        "sku": "Required[str]",
        "service": "Required[str]",
        "resource_type": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str | None]",
        "unit": "Required[str]",
        "unit_price": "Required[str]",
        "currency": "Required[str]",
        "metadata": "Required[dict[str, object]]",
    },
    total=False,
)
ListPricesResponse: TypeAlias = "PriceListResponse"
ListPricesItem: TypeAlias = "Price"
ListTransactionsParameters = TypedDict(
    "ListTransactionsParameters",
    {"crn": "NotRequired[str]", "marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListTransactionsQuery: TypeAlias = "ListTransactionsParameters"
TransactionListResponse = TypedDict(
    "TransactionListResponse",
    {"transactions": "Required[list[Transaction]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
Transaction = TypedDict(
    "Transaction",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "type": "Required[Literal['payment', 'refund', 'refund_reversal', 'dispute', 'dispute_reversal', 'adjustment', 'credit_grant', 'credit_applied']]",
        "amount": "Required[str]",
        "description": "NotRequired[str | None]",
        "reference": "NotRequired[str | None]",
        "created_at": "Required[str]",
    },
    total=False,
)
ListTransactionsResponse: TypeAlias = "TransactionListResponse"
ListTransactionsItem: TypeAlias = "Transaction"
BillingProfileInput = TypedDict(
    "BillingProfileInput",
    {
        "customer_type": "NotRequired[Literal['', 'individual', 'company']]",
        "company_name": "NotRequired[str]",
        "country": "NotRequired[str]",
        "tax_id": "NotRequired[str]",
        "foreign_tax_id": "NotRequired[str]",
        "no_tax_id_reason": "NotRequired[str]",
        "email": "NotRequired[str]",
        "phone": "NotRequired[str]",
        "street_name": "NotRequired[str]",
        "street_number": "NotRequired[str]",
        "complement": "NotRequired[str]",
        "neighborhood": "NotRequired[str]",
        "city": "NotRequired[str]",
        "municipality_code": "NotRequired[str]",
        "state": "NotRequired[str]",
        "postal_code": "NotRequired[str]",
    },
    total=False,
)
UpdateBillingProfileBody: TypeAlias = "BillingProfileInput"
UpdateBillingProfileResponse: TypeAlias = "BillingProfile"
