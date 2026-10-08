"""Generated typed API methods; do not edit."""

from __future__ import annotations

from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import quota as m
from ..response import (
    Page,
)

_OPS = {
    "listQuotas": Operation(
        id="listQuotas",
        method="GET",
        path="/v1/quotas",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={"region": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="quotas",
    ),
}


class QuotaService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list_quotas(
        self, *, query: m.ListQuotasQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListQuotasResponse, m.ListQuotasItem]:
        "List quotas"
        return cast(
            Page[m.ListQuotasResponse, m.ListQuotasItem],
            self._transport.request(
                "quota",
                "https://quota.basaltic.sh",
                _OPS["listQuotas"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )


class AsyncQuotaService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list_quotas(
        self, *, query: m.ListQuotasQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListQuotasResponse, m.ListQuotasItem]:
        "List quotas"
        return cast(
            Page[m.ListQuotasResponse, m.ListQuotasItem],
            await self._transport.request(
                "quota",
                "https://quota.basaltic.sh",
                _OPS["listQuotas"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )
