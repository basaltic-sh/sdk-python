"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import queue as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    iterate_pages,
)

_OPS = {
    "changeMessageVisibility": Operation(
        id="changeMessageVisibility",
        method="POST",
        path="/v1/queues/{queue_id}/messages/visibility",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "changeMessageVisibilityBatch": Operation(
        id="changeMessageVisibilityBatch",
        method="POST",
        path="/v1/queues/{queue_id}/messages/visibility-batch",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createQueue": Operation(
        id="createQueue",
        method="POST",
        path="/v1/queues",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteMessage": Operation(
        id="deleteMessage",
        method="DELETE",
        path="/v1/queues/{queue_id}/messages",
        authenticated=True,
        requiredQuery=["receipt_handle"],
        requiredHeaders=[],
        queryEncoding={"receipt_handle": {"style": "form", "explode": True}},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteMessageBatch": Operation(
        id="deleteMessageBatch",
        method="POST",
        path="/v1/queues/{queue_id}/messages/delete-batch",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteQueue": Operation(
        id="deleteQueue",
        method="DELETE",
        path="/v1/queues/{queue_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeQueue": Operation(
        id="describeQueue",
        method="GET",
        path="/v1/queues/{queue_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listQueues": Operation(
        id="listQueues",
        method="GET",
        path="/v1/queues",
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
        itemsKey="queues",
    ),
    "peekMessages": Operation(
        id="peekMessages",
        method="GET",
        path="/v1/queues/{queue_id}/messages",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "visibility": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "purgeQueue": Operation(
        id="purgeQueue",
        method="POST",
        path="/v1/queues/{queue_id}/purge",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "receiveMessages": Operation(
        id="receiveMessages",
        method="POST",
        path="/v1/queues/{queue_id}/messages/receive",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "sendMessage": Operation(
        id="sendMessage",
        method="POST",
        path="/v1/queues/{queue_id}/messages",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "sendMessageBatch": Operation(
        id="sendMessageBatch",
        method="POST",
        path="/v1/queues/{queue_id}/messages/batch",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateQueue": Operation(
        id="updateQueue",
        method="PATCH",
        path="/v1/queues/{queue_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class QueueService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def change_message_visibility(
        self,
        queue_id: str,
        body: m.ChangeMessageVisibilityBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Extend or shorten a lease"
        return cast(
            None,
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["changeMessageVisibility"],
                "discard",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def change_message_visibility_batch(
        self,
        queue_id: str,
        body: m.ChangeMessageVisibilityBatchBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ChangeMessageVisibilityBatchResponse]:
        "Extend or shorten up to ten leases"
        return cast(
            ApiResponse[m.ChangeMessageVisibilityBatchResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["changeMessageVisibilityBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def create_queue(
        self, body: m.CreateQueueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateQueueResponse]:
        "Create a queue"
        return cast(
            ApiResponse[m.CreateQueueResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["createQueue"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_message(
        self, queue_id: str, *, query: m.DeleteMessageQuery, options: RequestOptions | None = None
    ) -> None:
        "Delete a leased message"
        return cast(
            None,
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteMessage"],
                "discard",
                {"queue_id": queue_id},
                UNSET,
                query,
                options,
            ),
        )

    def delete_message_batch(
        self,
        queue_id: str,
        body: m.DeleteMessageBatchBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DeleteMessageBatchResponse]:
        "Delete up to ten leased messages"
        return cast(
            ApiResponse[m.DeleteMessageBatchResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteMessageBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def delete_queue(self, queue_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a queue"
        return cast(
            None,
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteQueue"],
                "discard",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_queue(
        self, queue_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeQueueResponse]:
        "Describe a queue"
        return cast(
            ApiResponse[m.DescribeQueueResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["describeQueue"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_queues(
        self, *, query: m.ListQueuesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListQueuesResponse, m.ListQueuesItem]:
        "List queues"
        return cast(
            Page[m.ListQueuesResponse, m.ListQueuesItem],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["listQueues"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_queues_all(
        self, *, query: m.ListQueuesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListQueuesItem]:
        return iterate_pages(
            lambda marker: self.list_queues(
                query=cast(m.ListQueuesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def peek_messages(
        self,
        queue_id: str,
        *,
        query: m.PeekMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PeekMessagesResponse]:
        "Peek at a queue's messages"
        return cast(
            ApiResponse[m.PeekMessagesResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["peekMessages"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                query,
                options,
            ),
        )

    def purge_queue(
        self, queue_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PurgeQueueResponse]:
        "Delete every message on a queue"
        return cast(
            ApiResponse[m.PurgeQueueResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["purgeQueue"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    def receive_messages(
        self,
        queue_id: str,
        body: m.ReceiveMessagesBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ReceiveMessagesResponse]:
        "Lease messages"
        return cast(
            ApiResponse[m.ReceiveMessagesResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["receiveMessages"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def send_message(
        self, queue_id: str, body: m.SendMessageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageResponse]:
        "Send a message"
        return cast(
            ApiResponse[m.SendMessageResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["sendMessage"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def send_message_batch(
        self, queue_id: str, body: m.SendMessageBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageBatchResponse]:
        "Send up to ten messages"
        return cast(
            ApiResponse[m.SendMessageBatchResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["sendMessageBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    def update_queue(
        self, queue_id: str, body: m.UpdateQueueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateQueueResponse]:
        "Update queue attributes"
        return cast(
            ApiResponse[m.UpdateQueueResponse],
            self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["updateQueue"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )


class AsyncQueueService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def change_message_visibility(
        self,
        queue_id: str,
        body: m.ChangeMessageVisibilityBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Extend or shorten a lease"
        return cast(
            None,
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["changeMessageVisibility"],
                "discard",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def change_message_visibility_batch(
        self,
        queue_id: str,
        body: m.ChangeMessageVisibilityBatchBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ChangeMessageVisibilityBatchResponse]:
        "Extend or shorten up to ten leases"
        return cast(
            ApiResponse[m.ChangeMessageVisibilityBatchResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["changeMessageVisibilityBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def create_queue(
        self, body: m.CreateQueueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateQueueResponse]:
        "Create a queue"
        return cast(
            ApiResponse[m.CreateQueueResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["createQueue"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_message(
        self, queue_id: str, *, query: m.DeleteMessageQuery, options: RequestOptions | None = None
    ) -> None:
        "Delete a leased message"
        return cast(
            None,
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteMessage"],
                "discard",
                {"queue_id": queue_id},
                UNSET,
                query,
                options,
            ),
        )

    async def delete_message_batch(
        self,
        queue_id: str,
        body: m.DeleteMessageBatchBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DeleteMessageBatchResponse]:
        "Delete up to ten leased messages"
        return cast(
            ApiResponse[m.DeleteMessageBatchResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteMessageBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def delete_queue(self, queue_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a queue"
        return cast(
            None,
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["deleteQueue"],
                "discard",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_queue(
        self, queue_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeQueueResponse]:
        "Describe a queue"
        return cast(
            ApiResponse[m.DescribeQueueResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["describeQueue"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_queues(
        self, *, query: m.ListQueuesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListQueuesResponse, m.ListQueuesItem]:
        "List queues"
        return cast(
            Page[m.ListQueuesResponse, m.ListQueuesItem],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["listQueues"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_queues_all(
        self, *, query: m.ListQueuesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListQueuesItem]:
        return aiterate_pages(
            lambda marker: self.list_queues(
                query=cast(m.ListQueuesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def peek_messages(
        self,
        queue_id: str,
        *,
        query: m.PeekMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PeekMessagesResponse]:
        "Peek at a queue's messages"
        return cast(
            ApiResponse[m.PeekMessagesResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["peekMessages"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                query,
                options,
            ),
        )

    async def purge_queue(
        self, queue_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PurgeQueueResponse]:
        "Delete every message on a queue"
        return cast(
            ApiResponse[m.PurgeQueueResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["purgeQueue"],
                "json",
                {"queue_id": queue_id},
                UNSET,
                None,
                options,
            ),
        )

    async def receive_messages(
        self,
        queue_id: str,
        body: m.ReceiveMessagesBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.ReceiveMessagesResponse]:
        "Lease messages"
        return cast(
            ApiResponse[m.ReceiveMessagesResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["receiveMessages"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def send_message(
        self, queue_id: str, body: m.SendMessageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageResponse]:
        "Send a message"
        return cast(
            ApiResponse[m.SendMessageResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["sendMessage"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def send_message_batch(
        self, queue_id: str, body: m.SendMessageBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageBatchResponse]:
        "Send up to ten messages"
        return cast(
            ApiResponse[m.SendMessageBatchResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["sendMessageBatch"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )

    async def update_queue(
        self, queue_id: str, body: m.UpdateQueueBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateQueueResponse]:
        "Update queue attributes"
        return cast(
            ApiResponse[m.UpdateQueueResponse],
            await self._transport.request(
                "queue",
                "https://queue.{region}.basaltic.sh",
                _OPS["updateQueue"],
                "json",
                {"queue_id": queue_id},
                body,
                None,
                options,
            ),
        )
