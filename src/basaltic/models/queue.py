"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

ChangeVisibilityRequestInput = TypedDict(
    "ChangeVisibilityRequestInput",
    {"receipt_handle": "Required[str]", "visibility_timeout_seconds": "Required[int]"},
    total=False,
)
ChangeMessageVisibilityBody: TypeAlias = "ChangeVisibilityRequestInput"
ChangeVisibilityBatchRequestInput = TypedDict(
    "ChangeVisibilityBatchRequestInput",
    {"entries": "Required[list[ChangeVisibilityBatchRequestInputEntriesItem]]"},
    total=False,
)
ChangeVisibilityBatchRequestInputEntriesItem = TypedDict(
    "ChangeVisibilityBatchRequestInputEntriesItem",
    {
        "id": "Required[str]",
        "receipt_handle": "Required[str]",
        "visibility_timeout_seconds": "Required[int]",
    },
    total=False,
)
ChangeMessageVisibilityBatchBody: TypeAlias = "ChangeVisibilityBatchRequestInput"
BatchResponse = TypedDict("BatchResponse", {"results": "Required[list[BatchResult]]"}, total=False)
BatchResult = TypedDict(
    "BatchResult",
    {
        "id": "Required[str]",
        "message_id": "NotRequired[str]",
        "duplicate": "NotRequired[bool]",
        "error": "NotRequired[str]",
        "message": "NotRequired[str]",
    },
    total=False,
)
ChangeMessageVisibilityBatchResponse: TypeAlias = "BatchResponse"
CreateQueueRequestInput = TypedDict(
    "CreateQueueRequestInput",
    {
        "name": "Required[str]",
        "visibility_timeout_seconds": "NotRequired[int]",
        "message_retention_seconds": "NotRequired[int]",
        "max_message_bytes": "NotRequired[int]",
        "delay_seconds": "NotRequired[int]",
        "receive_wait_time_seconds": "NotRequired[int]",
        "kms_data_key_reuse_period_seconds": "NotRequired[int]",
        "content_based_deduplication": "NotRequired[bool]",
        "kms_key": "NotRequired[str]",
        "redrive_policy": "NotRequired[RedrivePolicyInputInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
RedrivePolicyInputInput = TypedDict(
    "RedrivePolicyInputInput",
    {"dead_letter_queue": "Required[str]", "max_receive_count": "Required[int]"},
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateQueueBody: TypeAlias = "CreateQueueRequestInput"
QueueResponse = TypedDict("QueueResponse", {"queue": "Required[Queue]"}, total=False)
Queue = TypedDict(
    "Queue",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "kind": "Required[Literal['standard', 'fifo']]",
        "attributes": "Required[QueueAttributes]",
        "redrive_policy": "NotRequired[RedrivePolicy]",
        "content_based_deduplication": "NotRequired[bool]",
        "kms_key": "NotRequired[ResourceRef]",
        "tags": "NotRequired[Tags]",
        "depth": "NotRequired[QueueDepth]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
QueueAttributes = TypedDict(
    "QueueAttributes",
    {
        "visibility_timeout_seconds": "NotRequired[int]",
        "message_retention_seconds": "NotRequired[int]",
        "max_message_bytes": "NotRequired[int]",
        "delay_seconds": "NotRequired[int]",
        "receive_wait_time_seconds": "NotRequired[int]",
        "kms_data_key_reuse_period_seconds": "NotRequired[int]",
    },
    total=False,
)
RedrivePolicy = TypedDict(
    "RedrivePolicy",
    {"dead_letter_queue": "Required[ResourceRef]", "max_receive_count": "Required[int]"},
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
QueueDepth = TypedDict(
    "QueueDepth",
    {
        "approximate_available": "NotRequired[int]",
        "approximate_in_flight": "NotRequired[int]",
        "approximate_delayed": "NotRequired[int]",
        "counts_capped": "NotRequired[bool]",
    },
    total=False,
)
CreateQueueResponse: TypeAlias = "QueueResponse"
DeleteMessageParameters = TypedDict(
    "DeleteMessageParameters", {"receipt_handle": "Required[str]"}, total=False
)
DeleteMessageQuery: TypeAlias = "DeleteMessageParameters"
DeleteMessageBatchRequestInput = TypedDict(
    "DeleteMessageBatchRequestInput",
    {"entries": "Required[list[DeleteMessageBatchRequestInputEntriesItem]]"},
    total=False,
)
DeleteMessageBatchRequestInputEntriesItem = TypedDict(
    "DeleteMessageBatchRequestInputEntriesItem",
    {"id": "Required[str]", "receipt_handle": "Required[str]"},
    total=False,
)
DeleteMessageBatchBody: TypeAlias = "DeleteMessageBatchRequestInput"
DeleteMessageBatchResponse: TypeAlias = "BatchResponse"
DescribeQueueResponse: TypeAlias = "QueueResponse"
ListQueuesParameters = TypedDict(
    "ListQueuesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListQueuesQuery: TypeAlias = "ListQueuesParameters"
QueueListResponse = TypedDict(
    "QueueListResponse",
    {"queues": "Required[list[Queue]]", "meta": "NotRequired[PaginationMeta]"},
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
ListQueuesResponse: TypeAlias = "QueueListResponse"
ListQueuesItem: TypeAlias = "Queue"
PeekMessagesParameters = TypedDict(
    "PeekMessagesParameters",
    {
        "crn": "NotRequired[str]",
        "visibility": "NotRequired[Literal['available', 'in_flight', 'delayed']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
PeekMessagesQuery: TypeAlias = "PeekMessagesParameters"
PeekResponse = TypedDict(
    "PeekResponse",
    {"messages": "Required[list[Message]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
Message = TypedDict(
    "Message",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "queue_id": "Required[str]",
        "body": "NotRequired[str]",
        "attributes": "NotRequired[MessageAttributes]",
        "visibility": "Required[Literal['available', 'in_flight', 'delayed']]",
        "receive_count": "Required[int]",
        "body_bytes": "NotRequired[int]",
        "message_group_id": "NotRequired[str]",
        "enqueued_at": "Required[str]",
        "visible_at": "Required[str]",
        "expires_at": "Required[str]",
        "first_received_at": "NotRequired[str | None]",
    },
    total=False,
)
MessageAttributes: TypeAlias = "dict[str, MessageAttributesValue]"
MessageAttributesValue = TypedDict(
    "MessageAttributesValue",
    {"type": "Required[Literal['String', 'Number', 'Binary']]", "value": "Required[str]"},
    total=False,
)
PeekMessagesResponse: TypeAlias = "PeekResponse"
PurgeQueueResponse2 = TypedDict(
    "PurgeQueueResponse2", {"messages_deleted": "Required[int]"}, total=False
)
PurgeQueueResponse: TypeAlias = "PurgeQueueResponse2"
ReceiveRequestInput = TypedDict(
    "ReceiveRequestInput",
    {
        "max_messages": "NotRequired[int]",
        "visibility_timeout_seconds": "NotRequired[int]",
        "wait_time_seconds": "NotRequired[int]",
    },
    total=False,
)
ReceiveMessagesBody: TypeAlias = "ReceiveRequestInput"
ReceiveResponse = TypedDict(
    "ReceiveResponse", {"messages": "Required[list[ReceivedMessage]]"}, total=False
)
ReceivedMessage = TypedDict(
    "ReceivedMessage",
    {
        "id": "Required[str]",
        "receipt_handle": "Required[str]",
        "body": "Required[str]",
        "attributes": "NotRequired[MessageAttributes]",
        "receive_count": "Required[int]",
        "message_group_id": "NotRequired[str]",
        "enqueued_at": "Required[str]",
        "visible_at": "Required[str]",
    },
    total=False,
)
ReceiveMessagesResponse: TypeAlias = "ReceiveResponse"
SendMessageRequestInput = TypedDict(
    "SendMessageRequestInput",
    {
        "body": "Required[str]",
        "attributes": "NotRequired[MessageAttributesInput]",
        "delay_seconds": "NotRequired[int]",
        "message_group_id": "NotRequired[str]",
        "message_deduplication_id": "NotRequired[str]",
    },
    total=False,
)
MessageAttributesInput: TypeAlias = "dict[str, MessageAttributesInputValue]"
MessageAttributesInputValue = TypedDict(
    "MessageAttributesInputValue",
    {"type": "Required[Literal['String', 'Number', 'Binary']]", "value": "Required[str]"},
    total=False,
)
SendMessageBody: TypeAlias = "SendMessageRequestInput"
SendMessageResponse2 = TypedDict(
    "SendMessageResponse2", {"result": "Required[SendResult]"}, total=False
)
SendResult = TypedDict(
    "SendResult", {"message_id": "Required[str]", "duplicate": "NotRequired[bool]"}, total=False
)
SendMessageResponse: TypeAlias = "SendMessageResponse2"
SendMessageBatchRequestInput = TypedDict(
    "SendMessageBatchRequestInput",
    {"entries": "Required[list[SendMessageBatchRequestInputEntriesItem]]"},
    total=False,
)
SendMessageBatchRequestInputEntriesItem = TypedDict(
    "SendMessageBatchRequestInputEntriesItem",
    {
        "id": "Required[str]",
        "body": "Required[str]",
        "attributes": "NotRequired[MessageAttributesInput]",
        "delay_seconds": "NotRequired[int]",
        "message_group_id": "NotRequired[str]",
        "message_deduplication_id": "NotRequired[str]",
    },
    total=False,
)
SendMessageBatchBody: TypeAlias = "SendMessageBatchRequestInput"
SendMessageBatchResponse: TypeAlias = "BatchResponse"
UpdateQueueRequestInput = TypedDict(
    "UpdateQueueRequestInput",
    {
        "visibility_timeout_seconds": "NotRequired[int]",
        "message_retention_seconds": "NotRequired[int]",
        "max_message_bytes": "NotRequired[int]",
        "delay_seconds": "NotRequired[int]",
        "receive_wait_time_seconds": "NotRequired[int]",
        "kms_data_key_reuse_period_seconds": "NotRequired[int]",
        "redrive_policy": "NotRequired[UpdateQueueRequestInputRedrivePolicyObject | None]",
        "kms_key": "NotRequired[str | None]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateQueueRequestInputRedrivePolicyObject = TypedDict(
    "UpdateQueueRequestInputRedrivePolicyObject",
    {"dead_letter_queue": "Required[str]", "max_receive_count": "Required[int]"},
    total=False,
)
UpdateQueueBody: TypeAlias = "UpdateQueueRequestInput"
UpdateQueueResponse: TypeAlias = "QueueResponse"
