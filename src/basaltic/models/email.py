"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

SuppressionOverrideRequestInput = TypedDict(
    "SuppressionOverrideRequestInput", {"address": "Required[str]"}, total=False
)
AddSuppressionOverrideBody: TypeAlias = "SuppressionOverrideRequestInput"
ConfigurationSetResponse = TypedDict(
    "ConfigurationSetResponse", {"configuration_set": "Required[ConfigurationSet]"}, total=False
)
ConfigurationSet = TypedDict(
    "ConfigurationSet",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "sending_enabled": "Required[bool]",
        "suppression_overrides": "Required[list[str]]",
        "ip_pool": "NotRequired[ResourceRef]",
        "tracking_open": "NotRequired[bool]",
        "tracking_click": "NotRequired[bool]",
        "tags": "NotRequired[Tags]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
AddSuppressionOverrideResponse: TypeAlias = "ConfigurationSetResponse"
IdentityResponse = TypedDict("IdentityResponse", {"identity": "Required[Identity]"}, total=False)
Identity = TypedDict(
    "Identity",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "type": "Required[Literal['domain']]",
        "status": "Required[Literal['pending', 'verified', 'failed', 'suspended']]",
        "dkim_selector": "Required[str]",
        "dkim_pending_selector": "NotRequired[str]",
        "dkim_selector_old": "NotRequired[str]",
        "dkim_old_expires_at": "NotRequired[str | None]",
        "mail_from_domain": "NotRequired[str]",
        "mail_from_status": "NotRequired[Literal['pending', 'verified', 'failed']]",
        "mail_from_verified_at": "NotRequired[str | None]",
        "bimi_logo_url": "NotRequired[str]",
        "bimi_vmc_url": "NotRequired[str]",
        "bimi_status": "NotRequired[Literal['pending', 'verified', 'failed']]",
        "bimi_verified_at": "NotRequired[str | None]",
        "verified_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "suspended_reason": "NotRequired[str]",
        "suspended_at": "NotRequired[str | None]",
        "tags": "NotRequired[Tags]",
        "dns_records": "NotRequired[list[DNSRecord]]",
    },
    total=False,
)
DNSRecord = TypedDict(
    "DNSRecord",
    {
        "purpose": "Required[Literal['ownership', 'dkim', 'dkim_cname', 'dkim_pending', 'dkim_pending_cname', 'dkim_rotated_out', 'spf', 'dmarc', 'return_path', 'mail_from_mx', 'mail_from_spf', 'bimi', 'receiving_mx']]",
        "type": "Required[Literal['TXT', 'CNAME', 'MX']]",
        "name": "Required[str]",
        "value": "Required[str]",
        "required": "Required[bool]",
        "group": "Required[Literal['sending', 'receiving']]",
        "alternative_group": "NotRequired[str]",
    },
    total=False,
)
BeginDKIMRotationResponse: TypeAlias = "IdentityResponse"
CancelDKIMRotationResponse: TypeAlias = "IdentityResponse"
CreateConfigurationSetRequestInput = TypedDict(
    "CreateConfigurationSetRequestInput",
    {
        "name": "Required[str]",
        "sending_enabled": "NotRequired[bool]",
        "tags": "NotRequired[TagsInput]",
        "ip_pool": "NotRequired[str | None]",
        "tracking_open": "NotRequired[bool]",
        "tracking_click": "NotRequired[bool]",
        "suppression_overrides": "NotRequired[list[str]]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateConfigurationSetBody: TypeAlias = "CreateConfigurationSetRequestInput"
CreateConfigurationSetResponse: TypeAlias = "ConfigurationSetResponse"
CreateIPPoolRequestInput = TypedDict(
    "CreateIPPoolRequestInput",
    {"name": "Required[str]", "description": "NotRequired[str]"},
    total=False,
)
CreateIPPoolBody: TypeAlias = "CreateIPPoolRequestInput"
IPPoolResponse = TypedDict("IPPoolResponse", {"ip_pool": "Required[IPPool]"}, total=False)
IPPool = TypedDict(
    "IPPool",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateIPPoolResponse: TypeAlias = "IPPoolResponse"
CreateIdentityRequestInput = TypedDict(
    "CreateIdentityRequestInput",
    {"name": "Required[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
CreateIdentityBody: TypeAlias = "CreateIdentityRequestInput"
CreateIdentityResponse: TypeAlias = "IdentityResponse"
CreateRecipientRuleRequestInput = TypedDict(
    "CreateRecipientRuleRequestInput",
    {
        "match_type": "Required[Literal['exact', 'prefix', 'all']]",
        "local_part": "NotRequired[str]",
        "topic": "Required[str]",
        "enabled": "NotRequired[bool]",
    },
    total=False,
)
CreateRecipientRuleBody: TypeAlias = "CreateRecipientRuleRequestInput"
RecipientRuleResponse = TypedDict(
    "RecipientRuleResponse", {"rule": "Required[RecipientRule]"}, total=False
)
RecipientRule = TypedDict(
    "RecipientRule",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "local_part": "Required[str]",
        "topic": "Required[ResourceRef]",
        "enabled": "Required[bool]",
        "match_type": "Required[Literal['exact', 'prefix', 'all']]",
    },
    total=False,
)
CreateRecipientRuleResponse: TypeAlias = "RecipientRuleResponse"
CreateSuppressionRequestInput = TypedDict(
    "CreateSuppressionRequestInput",
    {
        "address": "Required[str]",
        "description": "NotRequired[str]",
        "expires_at": "NotRequired[str]",
    },
    total=False,
)
CreateSuppressionBody: TypeAlias = "CreateSuppressionRequestInput"
SuppressionResponse = TypedDict(
    "SuppressionResponse", {"suppression": "Required[Suppression]"}, total=False
)
Suppression = TypedDict(
    "Suppression",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "address": "Required[str]",
        "reason": "Required[Literal['auto_bounce', 'auto_complaint', 'manual']]",
        "description": "NotRequired[str]",
        "source_message": "NotRequired[ResourceRef]",
        "expires_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateSuppressionResponse: TypeAlias = "SuppressionResponse"
CreateTemplateRequestInput = TypedDict(
    "CreateTemplateRequestInput",
    {
        "name": "Required[str]",
        "subject_template": "NotRequired[str]",
        "body_template": "Required[str]",
        "body_type": "NotRequired[Literal['text', 'html']]",
    },
    total=False,
)
CreateTemplateBody: TypeAlias = "CreateTemplateRequestInput"
TemplateResponse = TypedDict("TemplateResponse", {"template": "Required[Template]"}, total=False)
Template = TypedDict(
    "Template",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "subject_template": "Required[str]",
        "body_template": "Required[str]",
        "body_type": "Required[Literal['text', 'html']]",
        "variables": "Required[list[str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateTemplateResponse: TypeAlias = "TemplateResponse"
DescribeConfigurationSetResponse: TypeAlias = "ConfigurationSetResponse"
DedicatedIPResponse = TypedDict(
    "DedicatedIPResponse", {"dedicated_ip": "Required[DedicatedIP]"}, total=False
)
DedicatedIP = TypedDict(
    "DedicatedIP",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "address": "Required[str]",
        "warmup_status": "Required[Literal['new', 'warming', 'warm']]",
        "warmup_percentage": "Required[int]",
        "warmup_started_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "ip_pool": "Required[ResourceRef | None]",
    },
    total=False,
)
DescribeDedicatedIPResponse: TypeAlias = "DedicatedIPResponse"
DescribeIPPoolResponse: TypeAlias = "IPPoolResponse"
DescribeIdentityResponse: TypeAlias = "IdentityResponse"
ReceivedMessageResponse = TypedDict(
    "ReceivedMessageResponse", {"message": "Required[ReceivedMessage]"}, total=False
)
ReceivedMessage = TypedDict(
    "ReceivedMessage",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "recipient": "Required[str]",
        "from": "Required[str]",
        "subject": "Required[str]",
        "received_at": "Required[str]",
        "expires_at": "Required[str]",
        "published_at": "Required[str | None]",
        "content_available": "Required[bool]",
        "review_reason": "Required[Literal['', 'spam', 'sender_unverified', 'malware']]",
        "authenticated": "Required[bool]",
        "attachments": "Required[list[Attachment]]",
        "identity": "Required[ResourceRef | None]",
        "notification_status": "Required[Literal['pending', 'retrying', 'published']]",
        "notification_error": "Required[str | None]",
        "rfc_message_id": "NotRequired[str]",
    },
    total=False,
)
Attachment = TypedDict(
    "Attachment",
    {
        "name": "Required[str]",
        "content_type": "Required[str]",
        "size": "Required[int]",
        "bucket": "Required[ResourceRef | None]",
        "key": "Required[str]",
        "version_id": "NotRequired[str]",
        "sha256": "Required[str]",
        "id": "Required[str]",
    },
    total=False,
)
DescribeReceivedMessageResponse: TypeAlias = "ReceivedMessageResponse"
DescribeRecipientRuleResponse: TypeAlias = "RecipientRuleResponse"
MessageResponse = TypedDict("MessageResponse", {"message": "Required[Message]"}, total=False)
Message = TypedDict(
    "Message",
    {
        "expires_at": "Required[str]",
        "attachments": "Required[list[Attachment]]",
        "id": "Required[str]",
        "crn": "Required[str]",
        "identity": "Required[ResourceRef]",
        "from": "Required[str]",
        "to": "Required[list[str]]",
        "subject": "NotRequired[str]",
        "status": "Required[Literal['queued', 'sending', 'sent', 'failed', 'bounced', 'complained']]",
        "smtp_response": "NotRequired[str]",
        "error_message": "NotRequired[str]",
        "outbound_ip": "NotRequired[str]",
        "queued_at": "Required[str]",
        "sent_at": "NotRequired[str | None]",
        "failed_at": "NotRequired[str | None]",
    },
    total=False,
)
DescribeSentMessageResponse: TypeAlias = "MessageResponse"
DescribeSuppressionResponse: TypeAlias = "SuppressionResponse"
DescribeTemplateResponse: TypeAlias = "TemplateResponse"
FinalizeDKIMRotationResponse: TypeAlias = "IdentityResponse"
MessageContentResponse = TypedDict(
    "MessageContentResponse", {"content": "Required[MessageContent]"}, total=False
)
MessageContent = TypedDict(
    "MessageContent",
    {
        "from": "Required[str]",
        "to": "Required[list[str]]",
        "subject": "Required[str]",
        "text": "Required[str]",
        "html": "Required[str]",
        "rfc_message_id": "NotRequired[str]",
        "attachments": "Required[list[Attachment]]",
    },
    total=False,
)
GetReceivedMessageContentResponse: TypeAlias = "MessageContentResponse"
ReceivingConfigurationResponse = TypedDict(
    "ReceivingConfigurationResponse", {"receiving": "Required[ReceivingConfiguration]"}, total=False
)
ReceivingConfiguration = TypedDict(
    "ReceivingConfiguration",
    {"enabled": "Required[bool]", "attachments_bucket": "Required[ResourceRef | None]"},
    total=False,
)
GetReceivingConfigurationResponse: TypeAlias = "ReceivingConfigurationResponse"
GetSentMessageContentResponse: TypeAlias = "MessageContentResponse"
MessageEngagementResponse = TypedDict(
    "MessageEngagementResponse", {"engagement": "Required[MessageEngagement]"}, total=False
)
MessageEngagement = TypedDict(
    "MessageEngagement",
    {
        "generated_at": "Required[str]",
        "open_count": "Required[int]",
        "unique_opens": "Required[int]",
        "click_count": "Required[int]",
        "unique_clicks": "Required[int]",
        "first_open_at": "NotRequired[str | None]",
        "last_open_at": "NotRequired[str | None]",
        "first_click_at": "NotRequired[str | None]",
        "last_click_at": "NotRequired[str | None]",
    },
    total=False,
)
GetSentMessageEngagementResponse: TypeAlias = "MessageEngagementResponse"
ListConfigurationSetsParameters = TypedDict(
    "ListConfigurationSetsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListConfigurationSetsQuery: TypeAlias = "ListConfigurationSetsParameters"
ConfigurationSetListResponse = TypedDict(
    "ConfigurationSetListResponse",
    {"configuration_sets": "Required[list[ConfigurationSet]]", "meta": "Required[PaginationMeta]"},
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
ListConfigurationSetsResponse: TypeAlias = "ConfigurationSetListResponse"
ListConfigurationSetsItem: TypeAlias = "ConfigurationSet"
ListDMARCReportsParameters = TypedDict(
    "ListDMARCReportsParameters",
    {
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "from": "NotRequired[str]",
        "to": "NotRequired[str]",
    },
    total=False,
)
ListDMARCReportsQuery: TypeAlias = "ListDMARCReportsParameters"
DMARCReportListResponse = TypedDict(
    "DMARCReportListResponse",
    {"records": "Required[list[DMARCReportRecord]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
DMARCReportRecord = TypedDict(
    "DMARCReportRecord",
    {
        "reporter": "Required[str]",
        "report_id": "Required[str]",
        "period_start": "Required[str]",
        "period_end": "Required[str]",
        "received_at": "Required[str]",
        "source_ip": "Required[str]",
        "message_count": "Required[int]",
        "disposition": "Required[str]",
        "dkim_aligned": "Required[bool]",
        "spf_aligned": "Required[bool]",
        "dkim_domain": "Required[str]",
        "dkim_result": "Required[str]",
        "spf_domain": "Required[str]",
        "spf_result": "Required[str]",
        "header_from": "Required[str]",
    },
    total=False,
)
ListDMARCReportsResponse: TypeAlias = "DMARCReportListResponse"
ListDMARCReportsItem: TypeAlias = "DMARCReportRecord"
ListDedicatedIPsParameters = TypedDict(
    "ListDedicatedIPsParameters",
    {
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "ip_pool": "NotRequired[str]",
    },
    total=False,
)
ListDedicatedIPsQuery: TypeAlias = "ListDedicatedIPsParameters"
DedicatedIPListResponse = TypedDict(
    "DedicatedIPListResponse",
    {"dedicated_ips": "Required[list[DedicatedIP]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListDedicatedIPsResponse: TypeAlias = "DedicatedIPListResponse"
ListDedicatedIPsItem: TypeAlias = "DedicatedIP"
ListIPPoolsParameters = TypedDict(
    "ListIPPoolsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListIPPoolsQuery: TypeAlias = "ListIPPoolsParameters"
IPPoolListResponse = TypedDict(
    "IPPoolListResponse",
    {"ip_pools": "Required[list[IPPool]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListIPPoolsResponse: TypeAlias = "IPPoolListResponse"
ListIPPoolsItem: TypeAlias = "IPPool"
ListIdentitiesParameters = TypedDict(
    "ListIdentitiesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListIdentitiesQuery: TypeAlias = "ListIdentitiesParameters"
IdentityListResponse = TypedDict(
    "IdentityListResponse",
    {"identities": "Required[list[Identity]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListIdentitiesResponse: TypeAlias = "IdentityListResponse"
ListIdentitiesItem: TypeAlias = "Identity"
ListReceivedMessagesParameters = TypedDict(
    "ListReceivedMessagesParameters",
    {
        "identity": "NotRequired[str]",
        "recipient": "NotRequired[str]",
        "review_reason": "NotRequired[Literal['clear', 'spam', 'sender_unverified', 'malware']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListReceivedMessagesQuery: TypeAlias = "ListReceivedMessagesParameters"
ReceivedMessageListResponse = TypedDict(
    "ReceivedMessageListResponse",
    {"messages": "Required[list[ReceivedMessage]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListReceivedMessagesResponse: TypeAlias = "ReceivedMessageListResponse"
ListReceivedMessagesItem: TypeAlias = "ReceivedMessage"
ListRecipientRulesParameters = TypedDict(
    "ListRecipientRulesParameters",
    {"marker": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
ListRecipientRulesQuery: TypeAlias = "ListRecipientRulesParameters"
RecipientRuleListResponse = TypedDict(
    "RecipientRuleListResponse",
    {"rules": "Required[list[RecipientRule]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListRecipientRulesResponse: TypeAlias = "RecipientRuleListResponse"
ListRecipientRulesItem: TypeAlias = "RecipientRule"
ListRejectionsParameters = TypedDict(
    "ListRejectionsParameters",
    {
        "crn": "NotRequired[str]",
        "before": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "identity": "NotRequired[str]",
        "reason": "NotRequired[Literal['ALL_RECIPIENTS_SUPPRESSED', 'IDENTITY_SUSPENDED', 'IDENTITY_NOT_VERIFIED', 'FROM_DOMAIN_MISMATCH', 'RATE_LIMIT']]",
    },
    total=False,
)
ListRejectionsQuery: TypeAlias = "ListRejectionsParameters"
RejectionListResponse = TypedDict(
    "RejectionListResponse",
    {"rejections": "Required[list[Rejection]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
Rejection = TypedDict(
    "Rejection",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "identity": "NotRequired[ResourceRef]",
        "from": "NotRequired[str]",
        "to": "Required[list[str]]",
        "reason": "Required[Literal['ALL_RECIPIENTS_SUPPRESSED', 'IDENTITY_SUSPENDED', 'IDENTITY_NOT_VERIFIED', 'FROM_DOMAIN_MISMATCH', 'RATE_LIMIT']]",
        "detail": "NotRequired[str]",
        "rejected_at": "Required[str]",
    },
    total=False,
)
ListRejectionsResponse: TypeAlias = "RejectionListResponse"
ListRejectionsItem: TypeAlias = "Rejection"
ListSentMessagesParameters = TypedDict(
    "ListSentMessagesParameters",
    {
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "identity": "NotRequired[str]",
        "status": "NotRequired[str]",
        "recipient": "NotRequired[str]",
    },
    total=False,
)
ListSentMessagesQuery: TypeAlias = "ListSentMessagesParameters"
MessageListResponse = TypedDict(
    "MessageListResponse",
    {"messages": "Required[list[Message]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListSentMessagesResponse: TypeAlias = "MessageListResponse"
ListSentMessagesItem: TypeAlias = "Message"
ListSuppressionsParameters = TypedDict(
    "ListSuppressionsParameters",
    {
        "crn": "NotRequired[str]",
        "reason": "NotRequired[Literal['auto_bounce', 'auto_complaint', 'manual']]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListSuppressionsQuery: TypeAlias = "ListSuppressionsParameters"
SuppressionListResponse = TypedDict(
    "SuppressionListResponse",
    {"suppressions": "Required[list[Suppression]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListSuppressionsResponse: TypeAlias = "SuppressionListResponse"
ListSuppressionsItem: TypeAlias = "Suppression"
ListTemplatesParameters = TypedDict(
    "ListTemplatesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListTemplatesQuery: TypeAlias = "ListTemplatesParameters"
TemplateListResponse = TypedDict(
    "TemplateListResponse",
    {"templates": "Required[list[Template]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListTemplatesResponse: TypeAlias = "TemplateListResponse"
ListTemplatesItem: TypeAlias = "Template"
RemoveSuppressionOverrideResponse: TypeAlias = "ConfigurationSetResponse"
RequestDedicatedIPRequestInput = TypedDict(
    "RequestDedicatedIPRequestInput", {"ip_pool": "NotRequired[str]"}, total=False
)
RequestDedicatedIPBody: TypeAlias = "RequestDedicatedIPRequestInput"
RequestDedicatedIPResponse: TypeAlias = "DedicatedIPResponse"
SendMessageRequestInput = TypedDict(
    "SendMessageRequestInput",
    {
        "attachments_bucket": "NotRequired[str]",
        "attachments": "NotRequired[list[AttachmentInputInput]]",
        "identity": "Required[str]",
        "from": "Required[str]",
        "to": "Required[list[str]]",
        "subject": "NotRequired[str]",
        "configuration_set": "NotRequired[str]",
        "content": "Required[SendContentInput]",
    },
    total=False,
)
AttachmentInputInput = TypedDict(
    "AttachmentInputInput",
    {
        "bucket": "Required[str]",
        "key": "Required[str]",
        "version_id": "NotRequired[str]",
        "name": "Required[str]",
        "content_type": "NotRequired[str]",
    },
    total=False,
)
SendContentInput: TypeAlias = (
    "SendContentInputVariant1 | SendContentInputVariant2 | SendContentInputVariant3"
)
SendContentInputVariant1 = TypedDict(
    "SendContentInputVariant1",
    {
        "text": "NotRequired[str]",
        "html": "NotRequired[str]",
        "raw": "NotRequired[str]",
        "template": "NotRequired[str]",
        "template_data": "NotRequired[dict[str, str]]",
    },
    total=False,
)
SendContentInputVariant2 = TypedDict(
    "SendContentInputVariant2",
    {
        "text": "NotRequired[str]",
        "html": "NotRequired[str]",
        "raw": "Required[str]",
        "template": "NotRequired[str]",
        "template_data": "NotRequired[dict[str, str]]",
    },
    total=False,
)
SendContentInputVariant3 = TypedDict(
    "SendContentInputVariant3",
    {
        "text": "NotRequired[str]",
        "html": "NotRequired[str]",
        "raw": "NotRequired[str]",
        "template": "Required[str]",
        "template_data": "NotRequired[dict[str, str]]",
    },
    total=False,
)
SendMessageBody: TypeAlias = "SendMessageRequestInput"
SendMessageResponse: TypeAlias = "MessageResponse"
BatchSendRequestInput = TypedDict(
    "BatchSendRequestInput", {"messages": "Required[list[SendMessageRequestInput]]"}, total=False
)
SendMessageBatchBody: TypeAlias = "BatchSendRequestInput"
BatchSendResponse = TypedDict(
    "BatchSendResponse", {"results": "Required[list[BatchSendResult]]"}, total=False
)
BatchSendResult = TypedDict(
    "BatchSendResult",
    {
        "index": "Required[int]",
        "status": "Required[Literal['queued', 'rejected']]",
        "message": "NotRequired[ResourceRef]",
        "error": "NotRequired[Error]",
    },
    total=False,
)
Error = TypedDict(
    "Error",
    {
        "code": "Required[str]",
        "message": "Required[str]",
        "params": "NotRequired[dict[str, object]]",
        "request_id": "Required[str]",
    },
    total=False,
)
SendMessageBatchResponse: TypeAlias = "BatchSendResponse"
SetBIMIRequestInput = TypedDict(
    "SetBIMIRequestInput",
    {"logo_url": "NotRequired[str | None]", "vmc_url": "NotRequired[str | None]"},
    total=False,
)
SetBIMIBody: TypeAlias = "SetBIMIRequestInput"
SetBIMIResponse: TypeAlias = "IdentityResponse"
SetMailFromDomainRequestInput = TypedDict(
    "SetMailFromDomainRequestInput", {"domain": "NotRequired[str | None]"}, total=False
)
SetMailFromDomainBody: TypeAlias = "SetMailFromDomainRequestInput"
SetMailFromDomainResponse: TypeAlias = "IdentityResponse"
UpdateConfigurationSetRequestInput = TypedDict(
    "UpdateConfigurationSetRequestInput",
    {
        "sending_enabled": "NotRequired[bool]",
        "suppression_overrides": "NotRequired[list[str]]",
        "ip_pool": "NotRequired[str | None]",
        "tracking_open": "NotRequired[bool]",
        "tracking_click": "NotRequired[bool]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateConfigurationSetBody: TypeAlias = "UpdateConfigurationSetRequestInput"
UpdateConfigurationSetResponse: TypeAlias = "ConfigurationSetResponse"
UpdateDedicatedIPRequestInput = TypedDict(
    "UpdateDedicatedIPRequestInput",
    {
        "warmup_status": "NotRequired[Literal['new', 'warming', 'warm']]",
        "ip_pool": "NotRequired[str | None]",
    },
    total=False,
)
UpdateDedicatedIPBody: TypeAlias = "UpdateDedicatedIPRequestInput"
UpdateDedicatedIPResponse: TypeAlias = "DedicatedIPResponse"
UpdateIPPoolRequestInput = TypedDict(
    "UpdateIPPoolRequestInput", {"description": "NotRequired[str]"}, total=False
)
UpdateIPPoolBody: TypeAlias = "UpdateIPPoolRequestInput"
UpdateIPPoolResponse: TypeAlias = "IPPoolResponse"
UpdateIdentityRequestInput = TypedDict(
    "UpdateIdentityRequestInput", {"tags": "NotRequired[TagsInput]"}, total=False
)
UpdateIdentityBody: TypeAlias = "UpdateIdentityRequestInput"
UpdateIdentityResponse: TypeAlias = "IdentityResponse"
UpdateReceivingConfigurationRequestInput = TypedDict(
    "UpdateReceivingConfigurationRequestInput",
    {"enabled": "NotRequired[bool]", "attachments_bucket": "NotRequired[str | None]"},
    total=False,
)
UpdateReceivingConfigurationBody: TypeAlias = "UpdateReceivingConfigurationRequestInput"
UpdateRecipientRuleRequestInput = TypedDict(
    "UpdateRecipientRuleRequestInput",
    {
        "match_type": "NotRequired[Literal['exact', 'prefix', 'all']]",
        "local_part": "NotRequired[str]",
        "topic": "NotRequired[str]",
        "enabled": "NotRequired[bool]",
    },
    total=False,
)
UpdateRecipientRuleBody: TypeAlias = "UpdateRecipientRuleRequestInput"
UpdateRecipientRuleResponse: TypeAlias = "RecipientRuleResponse"
UpdateSuppressionRequestInput = TypedDict(
    "UpdateSuppressionRequestInput",
    {"description": "NotRequired[str]", "expires_at": "NotRequired[str | None]"},
    total=False,
)
UpdateSuppressionBody: TypeAlias = "UpdateSuppressionRequestInput"
UpdateSuppressionResponse: TypeAlias = "SuppressionResponse"
UpdateTemplateRequestInput = TypedDict(
    "UpdateTemplateRequestInput",
    {
        "subject_template": "NotRequired[str]",
        "body_template": "NotRequired[str]",
        "body_type": "NotRequired[Literal['text', 'html']]",
    },
    total=False,
)
UpdateTemplateBody: TypeAlias = "UpdateTemplateRequestInput"
UpdateTemplateResponse: TypeAlias = "TemplateResponse"
VerifyBIMIResponse: TypeAlias = "IdentityResponse"
VerifyIdentityResponse: TypeAlias = "IdentityResponse"
VerifyMailFromDomainResponse: TypeAlias = "IdentityResponse"
