"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import notifications as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    iterate_pages,
)

_OPS = {
    "createTopic": Operation(
        id="createTopic",
        method="POST",
        path="/v1/topics",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteTopic": Operation(
        id="deleteTopic",
        method="DELETE",
        path="/v1/topics/{topic_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteTopicPolicy": Operation(
        id="deleteTopicPolicy",
        method="DELETE",
        path="/v1/topics/{topic_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeMessage": Operation(
        id="describeMessage",
        method="GET",
        path="/v1/topics/{topic_id}/messages/{message_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeSubscription": Operation(
        id="describeSubscription",
        method="GET",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeTopic": Operation(
        id="describeTopic",
        method="GET",
        path="/v1/topics/{topic_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSubscriptionSigningSecret": Operation(
        id="getSubscriptionSigningSecret",
        method="GET",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}/signing-secret",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getTopicPolicy": Operation(
        id="getTopicPolicy",
        method="GET",
        path="/v1/topics/{topic_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listDeliveries": Operation(
        id="listDeliveries",
        method="GET",
        path="/v1/topics/{topic_id}/deliveries",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "message": {"style": "form", "explode": True},
            "subscription": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="deliveries",
    ),
    "listMessages": Operation(
        id="listMessages",
        method="GET",
        path="/v1/topics/{topic_id}/messages",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "fanout_state": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="messages",
    ),
    "listSubscriptions": Operation(
        id="listSubscriptions",
        method="GET",
        path="/v1/topics/{topic_id}/subscriptions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="subscriptions",
    ),
    "listTopics": Operation(
        id="listTopics",
        method="GET",
        path="/v1/topics",
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
        itemsKey="topics",
    ),
    "publish": Operation(
        id="publish",
        method="POST",
        path="/v1/topics/{topic_id}/publish",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "publishBatch": Operation(
        id="publishBatch",
        method="POST",
        path="/v1/topics/{topic_id}/publish-batch",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putTopicPolicy": Operation(
        id="putTopicPolicy",
        method="PUT",
        path="/v1/topics/{topic_id}/policy",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "resendConfirmation": Operation(
        id="resendConfirmation",
        method="POST",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}/resend-confirmation",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "rotateSubscriptionSigningSecret": Operation(
        id="rotateSubscriptionSigningSecret",
        method="POST",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}/signing-secret/rotate",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "subscribe": Operation(
        id="subscribe",
        method="POST",
        path="/v1/topics/{topic_id}/subscriptions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "unsubscribe": Operation(
        id="unsubscribe",
        method="DELETE",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "updateSubscription": Operation(
        id="updateSubscription",
        method="PATCH",
        path="/v1/topics/{topic_id}/subscriptions/{subscription_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateTopic": Operation(
        id="updateTopic",
        method="PATCH",
        path="/v1/topics/{topic_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class NotificationsService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create_topic(
        self, body: m.CreateTopicBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTopicResponse]:
        "Create a topic"
        return cast(
            ApiResponse[m.CreateTopicResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["createTopic"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_topic(self, topic_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a topic"
        return cast(
            None,
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["deleteTopic"],
                "discard",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_topic_policy(self, topic_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete the topic's resource policy"
        return cast(
            None,
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["deleteTopicPolicy"],
                "discard",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_message(
        self, topic_id: str, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeMessageResponse]:
        "Describe a published notification"
        return cast(
            ApiResponse[m.DescribeMessageResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeMessage"],
                "json",
                {"topic_id": topic_id, "message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_subscription(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSubscriptionResponse]:
        "Describe a subscription"
        return cast(
            ApiResponse[m.DescribeSubscriptionResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeSubscription"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_topic(
        self, topic_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeTopicResponse]:
        "Describe a topic"
        return cast(
            ApiResponse[m.DescribeTopicResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeTopic"],
                "json",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_subscription_signing_secret(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSubscriptionSigningSecretResponse]:
        "Read the webhook signing secret"
        return cast(
            ApiResponse[m.GetSubscriptionSigningSecretResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["getSubscriptionSigningSecret"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_topic_policy(
        self, topic_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTopicPolicyResponse]:
        "Read the topic's resource policy"
        return cast(
            ApiResponse[m.GetTopicPolicyResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["getTopicPolicy"],
                "json",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_deliveries(
        self,
        topic_id: str,
        *,
        query: m.ListDeliveriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListDeliveriesResponse, m.ListDeliveriesItem]:
        "List delivery records"
        return cast(
            Page[m.ListDeliveriesResponse, m.ListDeliveriesItem],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listDeliveries"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_deliveries_all(
        self,
        topic_id: str,
        *,
        query: m.ListDeliveriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListDeliveriesItem]:
        return iterate_pages(
            lambda marker: self.list_deliveries(
                topic_id,
                query=cast(m.ListDeliveriesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_messages(
        self,
        topic_id: str,
        *,
        query: m.ListMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListMessagesResponse, m.ListMessagesItem]:
        "List messages"
        return cast(
            Page[m.ListMessagesResponse, m.ListMessagesItem],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listMessages"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_messages_all(
        self,
        topic_id: str,
        *,
        query: m.ListMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListMessagesItem]:
        return iterate_pages(
            lambda marker: self.list_messages(
                topic_id,
                query=cast(m.ListMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_subscriptions(
        self,
        topic_id: str,
        *,
        query: m.ListSubscriptionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSubscriptionsResponse, m.ListSubscriptionsItem]:
        "List subscriptions"
        return cast(
            Page[m.ListSubscriptionsResponse, m.ListSubscriptionsItem],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listSubscriptions"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_subscriptions_all(
        self,
        topic_id: str,
        *,
        query: m.ListSubscriptionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListSubscriptionsItem]:
        return iterate_pages(
            lambda marker: self.list_subscriptions(
                topic_id,
                query=cast(m.ListSubscriptionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_topics(
        self, *, query: m.ListTopicsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTopicsResponse, m.ListTopicsItem]:
        "List topics"
        return cast(
            Page[m.ListTopicsResponse, m.ListTopicsItem],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listTopics"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_topics_all(
        self, *, query: m.ListTopicsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListTopicsItem]:
        return iterate_pages(
            lambda marker: self.list_topics(
                query=cast(m.ListTopicsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def publish(
        self, topic_id: str, body: m.PublishBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PublishResponse]:
        "Publish a notification"
        return cast(
            ApiResponse[m.PublishResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["publish"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    def publish_batch(
        self, topic_id: str, body: m.PublishBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PublishBatchResponse]:
        "Publish up to 10 notifications"
        return cast(
            ApiResponse[m.PublishBatchResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["publishBatch"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    def put_topic_policy(
        self, topic_id: str, body: m.PutTopicPolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutTopicPolicyResponse]:
        "Set the topic's resource policy"
        return cast(
            ApiResponse[m.PutTopicPolicyResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["putTopicPolicy"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    def resend_confirmation(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ResendConfirmationResponse]:
        "Re-send the confirmation handshake"
        return cast(
            ApiResponse[m.ResendConfirmationResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["resendConfirmation"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    def rotate_subscription_signing_secret(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RotateSubscriptionSigningSecretResponse]:
        "Rotate the webhook signing secret"
        return cast(
            ApiResponse[m.RotateSubscriptionSigningSecretResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["rotateSubscriptionSigningSecret"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    def subscribe(
        self, topic_id: str, body: m.SubscribeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SubscribeResponse]:
        "Subscribe an endpoint to a topic"
        return cast(
            ApiResponse[m.SubscribeResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["subscribe"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    def unsubscribe(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Unsubscribe"
        return cast(
            None,
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["unsubscribe"],
                "discard",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    def update_subscription(
        self,
        topic_id: str,
        subscription_id: str,
        body: m.UpdateSubscriptionBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSubscriptionResponse]:
        "Update mutable subscription settings"
        return cast(
            ApiResponse[m.UpdateSubscriptionResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["updateSubscription"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                body,
                None,
                options,
            ),
        )

    def update_topic(
        self, topic_id: str, body: m.UpdateTopicBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTopicResponse]:
        "Update mutable topic metadata"
        return cast(
            ApiResponse[m.UpdateTopicResponse],
            self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["updateTopic"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )


class AsyncNotificationsService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_topic(
        self, body: m.CreateTopicBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTopicResponse]:
        "Create a topic"
        return cast(
            ApiResponse[m.CreateTopicResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["createTopic"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_topic(self, topic_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a topic"
        return cast(
            None,
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["deleteTopic"],
                "discard",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_topic_policy(
        self, topic_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete the topic's resource policy"
        return cast(
            None,
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["deleteTopicPolicy"],
                "discard",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_message(
        self, topic_id: str, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeMessageResponse]:
        "Describe a published notification"
        return cast(
            ApiResponse[m.DescribeMessageResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeMessage"],
                "json",
                {"topic_id": topic_id, "message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_subscription(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSubscriptionResponse]:
        "Describe a subscription"
        return cast(
            ApiResponse[m.DescribeSubscriptionResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeSubscription"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_topic(
        self, topic_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeTopicResponse]:
        "Describe a topic"
        return cast(
            ApiResponse[m.DescribeTopicResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["describeTopic"],
                "json",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_subscription_signing_secret(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSubscriptionSigningSecretResponse]:
        "Read the webhook signing secret"
        return cast(
            ApiResponse[m.GetSubscriptionSigningSecretResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["getSubscriptionSigningSecret"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_topic_policy(
        self, topic_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTopicPolicyResponse]:
        "Read the topic's resource policy"
        return cast(
            ApiResponse[m.GetTopicPolicyResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["getTopicPolicy"],
                "json",
                {"topic_id": topic_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_deliveries(
        self,
        topic_id: str,
        *,
        query: m.ListDeliveriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListDeliveriesResponse, m.ListDeliveriesItem]:
        "List delivery records"
        return cast(
            Page[m.ListDeliveriesResponse, m.ListDeliveriesItem],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listDeliveries"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_deliveries_all(
        self,
        topic_id: str,
        *,
        query: m.ListDeliveriesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListDeliveriesItem]:
        return aiterate_pages(
            lambda marker: self.list_deliveries(
                topic_id,
                query=cast(m.ListDeliveriesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_messages(
        self,
        topic_id: str,
        *,
        query: m.ListMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListMessagesResponse, m.ListMessagesItem]:
        "List messages"
        return cast(
            Page[m.ListMessagesResponse, m.ListMessagesItem],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listMessages"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_messages_all(
        self,
        topic_id: str,
        *,
        query: m.ListMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListMessagesItem]:
        return aiterate_pages(
            lambda marker: self.list_messages(
                topic_id,
                query=cast(m.ListMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_subscriptions(
        self,
        topic_id: str,
        *,
        query: m.ListSubscriptionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSubscriptionsResponse, m.ListSubscriptionsItem]:
        "List subscriptions"
        return cast(
            Page[m.ListSubscriptionsResponse, m.ListSubscriptionsItem],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listSubscriptions"],
                "page",
                {"topic_id": topic_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_subscriptions_all(
        self,
        topic_id: str,
        *,
        query: m.ListSubscriptionsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListSubscriptionsItem]:
        return aiterate_pages(
            lambda marker: self.list_subscriptions(
                topic_id,
                query=cast(m.ListSubscriptionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_topics(
        self, *, query: m.ListTopicsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTopicsResponse, m.ListTopicsItem]:
        "List topics"
        return cast(
            Page[m.ListTopicsResponse, m.ListTopicsItem],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["listTopics"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_topics_all(
        self, *, query: m.ListTopicsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListTopicsItem]:
        return aiterate_pages(
            lambda marker: self.list_topics(
                query=cast(m.ListTopicsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def publish(
        self, topic_id: str, body: m.PublishBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PublishResponse]:
        "Publish a notification"
        return cast(
            ApiResponse[m.PublishResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["publish"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    async def publish_batch(
        self, topic_id: str, body: m.PublishBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PublishBatchResponse]:
        "Publish up to 10 notifications"
        return cast(
            ApiResponse[m.PublishBatchResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["publishBatch"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    async def put_topic_policy(
        self, topic_id: str, body: m.PutTopicPolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.PutTopicPolicyResponse]:
        "Set the topic's resource policy"
        return cast(
            ApiResponse[m.PutTopicPolicyResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["putTopicPolicy"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    async def resend_confirmation(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ResendConfirmationResponse]:
        "Re-send the confirmation handshake"
        return cast(
            ApiResponse[m.ResendConfirmationResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["resendConfirmation"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    async def rotate_subscription_signing_secret(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RotateSubscriptionSigningSecretResponse]:
        "Rotate the webhook signing secret"
        return cast(
            ApiResponse[m.RotateSubscriptionSigningSecretResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["rotateSubscriptionSigningSecret"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    async def subscribe(
        self, topic_id: str, body: m.SubscribeBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SubscribeResponse]:
        "Subscribe an endpoint to a topic"
        return cast(
            ApiResponse[m.SubscribeResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["subscribe"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )

    async def unsubscribe(
        self, topic_id: str, subscription_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Unsubscribe"
        return cast(
            None,
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["unsubscribe"],
                "discard",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                UNSET,
                None,
                options,
            ),
        )

    async def update_subscription(
        self,
        topic_id: str,
        subscription_id: str,
        body: m.UpdateSubscriptionBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSubscriptionResponse]:
        "Update mutable subscription settings"
        return cast(
            ApiResponse[m.UpdateSubscriptionResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["updateSubscription"],
                "json",
                {"topic_id": topic_id, "subscription_id": subscription_id},
                body,
                None,
                options,
            ),
        )

    async def update_topic(
        self, topic_id: str, body: m.UpdateTopicBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTopicResponse]:
        "Update mutable topic metadata"
        return cast(
            ApiResponse[m.UpdateTopicResponse],
            await self._transport.request(
                "notifications",
                "https://notifications.{region}.basaltic.sh",
                _OPS["updateTopic"],
                "json",
                {"topic_id": topic_id},
                body,
                None,
                options,
            ),
        )
