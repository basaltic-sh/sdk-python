"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

CreateTopicRequestInput = TypedDict(
    "CreateTopicRequestInput",
    {
        "name": "Required[str]",
        "display_name": "NotRequired[str]",
        "delivery_policy": "NotRequired[DeliveryPolicyInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
DeliveryPolicyInput = TypedDict(
    "DeliveryPolicyInput",
    {
        "max_attempts": "NotRequired[int]",
        "min_delay_seconds": "NotRequired[int]",
        "max_delay_seconds": "NotRequired[int]",
        "timeout_seconds": "NotRequired[int]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateTopicBody: TypeAlias = "CreateTopicRequestInput"
TopicResponse = TypedDict("TopicResponse", {"topic": "Required[Topic]"}, total=False)
Topic = TypedDict(
    "Topic",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "display_name": "NotRequired[str]",
        "delivery_policy": "NotRequired[DeliveryPolicy]",
        "tags": "NotRequired[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
DeliveryPolicy = TypedDict(
    "DeliveryPolicy",
    {
        "max_attempts": "NotRequired[int]",
        "min_delay_seconds": "NotRequired[int]",
        "max_delay_seconds": "NotRequired[int]",
        "timeout_seconds": "NotRequired[int]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
CreateTopicResponse: TypeAlias = "TopicResponse"
MessageResponse = TypedDict("MessageResponse", {"message": "Required[Message]"}, total=False)
Message = TypedDict(
    "Message",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "subject": "NotRequired[str]",
        "message_structure": "NotRequired[Literal['', 'json']]",
        "attributes": "NotRequired[MessageAttributes]",
        "fanout_state": "Required[Literal['pending', 'complete']]",
        "delivery_count": "Required[int]",
        "published_at": "Required[str]",
        "fanned_out_at": "NotRequired[str | None]",
    },
    total=False,
)
MessageAttributes: TypeAlias = "dict[str, MessageAttributesValue]"
MessageAttributesValue = TypedDict(
    "MessageAttributesValue",
    {"type": "Required[Literal['String', 'Number']]", "value": "Required[str]"},
    total=False,
)
DescribeMessageResponse: TypeAlias = "MessageResponse"
SubscriptionResponse = TypedDict(
    "SubscriptionResponse", {"subscription": "Required[Subscription]"}, total=False
)
Subscription = TypedDict(
    "Subscription",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "protocol": "Required[Literal['email', 'https', 'http', 'queue']]",
        "endpoint": "Required[str]",
        "status": "Required[Literal['pending_confirmation', 'confirmed']]",
        "raw_message_delivery": "Required[bool]",
        "filter_policy": "NotRequired[FilterPolicy]",
        "delivery_policy": "NotRequired[DeliveryPolicy]",
        "redrive_policy": "NotRequired[RedrivePolicy]",
        "confirmation_expires_at": "NotRequired[str | None]",
        "confirmed_at": "NotRequired[str | None]",
        "tags": "NotRequired[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
FilterPolicy: TypeAlias = "dict[str, list[object]]"
RedrivePolicy = TypedDict(
    "RedrivePolicy", {"dead_letter_queue": "Required[ResourceRef]"}, total=False
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
DescribeSubscriptionResponse: TypeAlias = "SubscriptionResponse"
DescribeTopicResponse: TypeAlias = "TopicResponse"
SigningSecretResponse = TypedDict(
    "SigningSecretResponse",
    {"subscription": "Required[ResourceRef]", "signing_secret": "Required[str]"},
    total=False,
)
GetSubscriptionSigningSecretResponse: TypeAlias = "SigningSecretResponse"
TopicPolicyResponse = TypedDict(
    "TopicPolicyResponse", {"document": "Required[TopicPolicy]"}, total=False
)
TopicPolicy: TypeAlias = "dict[str, object]"
GetTopicPolicyResponse: TypeAlias = "TopicPolicyResponse"
ListDeliveriesParameters = TypedDict(
    "ListDeliveriesParameters",
    {
        "crn": "NotRequired[str]",
        "message": "NotRequired[str]",
        "subscription": "NotRequired[str]",
        "status": "NotRequired[Literal['pending', 'delivered', 'failed']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListDeliveriesQuery: TypeAlias = "ListDeliveriesParameters"
DeliveryListResponse = TypedDict(
    "DeliveryListResponse",
    {"deliveries": "Required[list[Delivery]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
Delivery = TypedDict(
    "Delivery",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "message": "Required[ResourceRef]",
        "subscription": "Required[ResourceRef]",
        "protocol": "Required[Literal['email', 'https', 'http', 'queue']]",
        "endpoint": "Required[str]",
        "status": "Required[Literal['pending', 'delivered', 'failed']]",
        "attempts": "Required[int]",
        "last_status_code": "NotRequired[int | None]",
        "last_error": "NotRequired[str]",
        "created_at": "Required[str]",
        "last_attempt_at": "NotRequired[str | None]",
        "completed_at": "NotRequired[str | None]",
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
ListDeliveriesResponse: TypeAlias = "DeliveryListResponse"
ListDeliveriesItem: TypeAlias = "Delivery"
ListMessagesParameters = TypedDict(
    "ListMessagesParameters",
    {
        "crn": "NotRequired[str]",
        "fanout_state": "NotRequired[Literal['pending', 'complete']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListMessagesQuery: TypeAlias = "ListMessagesParameters"
MessageListResponse = TypedDict(
    "MessageListResponse",
    {"messages": "Required[list[Message]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListMessagesResponse: TypeAlias = "MessageListResponse"
ListMessagesItem: TypeAlias = "Message"
ListSubscriptionsParameters = TypedDict(
    "ListSubscriptionsParameters",
    {
        "crn": "NotRequired[str]",
        "status": "NotRequired[Literal['pending_confirmation', 'confirmed']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListSubscriptionsQuery: TypeAlias = "ListSubscriptionsParameters"
SubscriptionListResponse = TypedDict(
    "SubscriptionListResponse",
    {"subscriptions": "Required[list[Subscription]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListSubscriptionsResponse: TypeAlias = "SubscriptionListResponse"
ListSubscriptionsItem: TypeAlias = "Subscription"
ListTopicsParameters = TypedDict(
    "ListTopicsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListTopicsQuery: TypeAlias = "ListTopicsParameters"
TopicListResponse = TypedDict(
    "TopicListResponse",
    {"topics": "Required[list[Topic]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListTopicsResponse: TypeAlias = "TopicListResponse"
ListTopicsItem: TypeAlias = "Topic"
PublishRequestInput = TypedDict(
    "PublishRequestInput",
    {
        "subject": "NotRequired[str]",
        "message": "Required[str]",
        "message_structure": "NotRequired[Literal['', 'json']]",
        "attributes": "NotRequired[MessageAttributesInput]",
    },
    total=False,
)
MessageAttributesInput: TypeAlias = "dict[str, MessageAttributesInputValue]"
MessageAttributesInputValue = TypedDict(
    "MessageAttributesInputValue",
    {"type": "Required[Literal['String', 'Number']]", "value": "Required[str]"},
    total=False,
)
PublishBody: TypeAlias = "PublishRequestInput"
PublishResponse2 = TypedDict("PublishResponse2", {"message_id": "Required[str]"}, total=False)
PublishResponse: TypeAlias = "PublishResponse2"
PublishBatchRequestInput = TypedDict(
    "PublishBatchRequestInput",
    {"entries": "Required[list[PublishBatchRequestInputEntriesItem]]"},
    total=False,
)
PublishBatchRequestInputEntriesItem = TypedDict(
    "PublishBatchRequestInputEntriesItem",
    {
        "id": "Required[str]",
        "subject": "NotRequired[str]",
        "message": "Required[str]",
        "message_structure": "NotRequired[Literal['', 'json']]",
        "attributes": "NotRequired[MessageAttributesInput]",
    },
    total=False,
)
PublishBatchBody: TypeAlias = "PublishBatchRequestInput"
PublishBatchResponse2 = TypedDict(
    "PublishBatchResponse2",
    {
        "successful": "NotRequired[list[PublishBatchResponse2SuccessfulItem]]",
        "failed": "NotRequired[list[PublishBatchResponse2FailedItem]]",
    },
    total=False,
)
PublishBatchResponse2SuccessfulItem = TypedDict(
    "PublishBatchResponse2SuccessfulItem",
    {"id": "Required[str]", "message_id": "Required[str]"},
    total=False,
)
PublishBatchResponse2FailedItem = TypedDict(
    "PublishBatchResponse2FailedItem",
    {"id": "Required[str]", "code": "Required[str]", "message": "Required[str]"},
    total=False,
)
PublishBatchResponse: TypeAlias = "PublishBatchResponse2"
PutTopicPolicyRequestInput = TypedDict(
    "PutTopicPolicyRequestInput", {"document": "Required[TopicPolicyInput]"}, total=False
)
TopicPolicyInput: TypeAlias = "dict[str, object]"
PutTopicPolicyBody: TypeAlias = "PutTopicPolicyRequestInput"
PutTopicPolicyResponse: TypeAlias = "TopicPolicyResponse"
ResendConfirmationResponse: TypeAlias = "SubscriptionResponse"
RotateSubscriptionSigningSecretResponse: TypeAlias = "SigningSecretResponse"
SubscribeRequestInput = TypedDict(
    "SubscribeRequestInput",
    {
        "protocol": "Required[Literal['email', 'https', 'http', 'queue']]",
        "endpoint": "Required[str]",
        "raw_message_delivery": "NotRequired[bool]",
        "filter_policy": "NotRequired[FilterPolicyInput]",
        "delivery_policy": "NotRequired[DeliveryPolicyInput]",
        "redrive_policy": "NotRequired[RedrivePolicyInputInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
FilterPolicyInput: TypeAlias = "dict[str, list[object]]"
RedrivePolicyInputInput = TypedDict(
    "RedrivePolicyInputInput", {"dead_letter_queue": "Required[str]"}, total=False
)
SubscribeBody: TypeAlias = "SubscribeRequestInput"
SubscribeResponse2 = TypedDict(
    "SubscribeResponse2",
    {"subscription": "Required[Subscription]", "signing_secret": "NotRequired[str]"},
    total=False,
)
SubscribeResponse: TypeAlias = "SubscribeResponse2"
UpdateSubscriptionRequestInput = TypedDict(
    "UpdateSubscriptionRequestInput",
    {
        "raw_message_delivery": "NotRequired[bool]",
        "filter_policy": "NotRequired[FilterPolicyInput]",
        "delivery_policy": "NotRequired[DeliveryPolicyInput]",
        "redrive_policy": "NotRequired[RedrivePolicyInputInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateSubscriptionBody: TypeAlias = "UpdateSubscriptionRequestInput"
UpdateSubscriptionResponse: TypeAlias = "SubscriptionResponse"
UpdateTopicRequestInput = TypedDict(
    "UpdateTopicRequestInput",
    {
        "display_name": "NotRequired[str]",
        "delivery_policy": "NotRequired[DeliveryPolicyInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateTopicBody: TypeAlias = "UpdateTopicRequestInput"
UpdateTopicResponse: TypeAlias = "TopicResponse"
