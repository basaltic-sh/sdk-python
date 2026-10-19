"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

import httpx

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import email as m
from ..response import (
    ApiResponse,
    Page,
    aiterate_pages,
    iterate_pages,
)

_OPS = {
    "addSuppressionOverride": Operation(
        id="addSuppressionOverride",
        method="POST",
        path="/v1/configuration-sets/{configuration_set_id}/suppression-overrides",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "beginDKIMRotation": Operation(
        id="beginDKIMRotation",
        method="POST",
        path="/v1/identities/{identity_id}/dkim/rotate",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "cancelDKIMRotation": Operation(
        id="cancelDKIMRotation",
        method="DELETE",
        path="/v1/identities/{identity_id}/dkim/rotate",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "createConfigurationSet": Operation(
        id="createConfigurationSet",
        method="POST",
        path="/v1/configuration-sets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createIPPool": Operation(
        id="createIPPool",
        method="POST",
        path="/v1/ip-pools",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createIdentity": Operation(
        id="createIdentity",
        method="POST",
        path="/v1/identities",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRecipientRule": Operation(
        id="createRecipientRule",
        method="POST",
        path="/v1/identities/{identity_id}/recipient-rules",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSuppression": Operation(
        id="createSuppression",
        method="POST",
        path="/v1/suppressions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createTemplate": Operation(
        id="createTemplate",
        method="POST",
        path="/v1/templates",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteConfigurationSet": Operation(
        id="deleteConfigurationSet",
        method="DELETE",
        path="/v1/configuration-sets/{configuration_set_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteIPPool": Operation(
        id="deleteIPPool",
        method="DELETE",
        path="/v1/ip-pools/{ip_pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteIdentity": Operation(
        id="deleteIdentity",
        method="DELETE",
        path="/v1/identities/{identity_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRecipientRule": Operation(
        id="deleteRecipientRule",
        method="DELETE",
        path="/v1/identities/{identity_id}/recipient-rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSuppression": Operation(
        id="deleteSuppression",
        method="DELETE",
        path="/v1/suppressions/{suppression_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteTemplate": Operation(
        id="deleteTemplate",
        method="DELETE",
        path="/v1/templates/{template_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeConfigurationSet": Operation(
        id="describeConfigurationSet",
        method="GET",
        path="/v1/configuration-sets/{configuration_set_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeDedicatedIP": Operation(
        id="describeDedicatedIP",
        method="GET",
        path="/v1/dedicated-ips/{dedicated_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeIPPool": Operation(
        id="describeIPPool",
        method="GET",
        path="/v1/ip-pools/{ip_pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeIdentity": Operation(
        id="describeIdentity",
        method="GET",
        path="/v1/identities/{identity_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeReceivedMessage": Operation(
        id="describeReceivedMessage",
        method="GET",
        path="/v1/received-messages/{message_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeRecipientRule": Operation(
        id="describeRecipientRule",
        method="GET",
        path="/v1/identities/{identity_id}/recipient-rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeSentMessage": Operation(
        id="describeSentMessage",
        method="GET",
        path="/v1/sent-messages/{message_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeSuppression": Operation(
        id="describeSuppression",
        method="GET",
        path="/v1/suppressions/{suppression_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "describeTemplate": Operation(
        id="describeTemplate",
        method="GET",
        path="/v1/templates/{template_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "downloadReceivedAttachment": Operation(
        id="downloadReceivedAttachment",
        method="GET",
        path="/v1/received-messages/{message_id}/attachments/{attachment_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "downloadReceivedMessage": Operation(
        id="downloadReceivedMessage",
        method="GET",
        path="/v1/received-messages/{message_id}/raw",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "downloadSentAttachment": Operation(
        id="downloadSentAttachment",
        method="GET",
        path="/v1/sent-messages/{message_id}/attachments/{attachment_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "downloadSentMessage": Operation(
        id="downloadSentMessage",
        method="GET",
        path="/v1/sent-messages/{message_id}/raw",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="*/*",
    ),
    "finalizeDKIMRotation": Operation(
        id="finalizeDKIMRotation",
        method="POST",
        path="/v1/identities/{identity_id}/dkim/rotate/finalize",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getReceivedMessageContent": Operation(
        id="getReceivedMessageContent",
        method="GET",
        path="/v1/received-messages/{message_id}/content",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getReceivingConfiguration": Operation(
        id="getReceivingConfiguration",
        method="GET",
        path="/v1/identities/{identity_id}/receiving",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSentMessageContent": Operation(
        id="getSentMessageContent",
        method="GET",
        path="/v1/sent-messages/{message_id}/content",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSentMessageEngagement": Operation(
        id="getSentMessageEngagement",
        method="GET",
        path="/v1/sent-messages/{message_id}/engagement",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listConfigurationSets": Operation(
        id="listConfigurationSets",
        method="GET",
        path="/v1/configuration-sets",
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
        itemsKey="configuration_sets",
    ),
    "listDMARCReports": Operation(
        id="listDMARCReports",
        method="GET",
        path="/v1/identities/{identity_id}/dmarc-reports",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "from": {"style": "form", "explode": True},
            "to": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="records",
    ),
    "listDedicatedIPs": Operation(
        id="listDedicatedIPs",
        method="GET",
        path="/v1/dedicated-ips",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "ip_pool": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="dedicated_ips",
    ),
    "listIPPools": Operation(
        id="listIPPools",
        method="GET",
        path="/v1/ip-pools",
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
        itemsKey="ip_pools",
    ),
    "listIdentities": Operation(
        id="listIdentities",
        method="GET",
        path="/v1/identities",
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
        itemsKey="identities",
    ),
    "listReceivedMessages": Operation(
        id="listReceivedMessages",
        method="GET",
        path="/v1/received-messages",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "identity": {"style": "form", "explode": True},
            "recipient": {"style": "form", "explode": True},
            "review_reason": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="messages",
    ),
    "listRecipientRules": Operation(
        id="listRecipientRules",
        method="GET",
        path="/v1/identities/{identity_id}/recipient-rules",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="rules",
    ),
    "listRejections": Operation(
        id="listRejections",
        method="GET",
        path="/v1/rejections",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "before": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "identity": {"style": "form", "explode": True},
            "reason": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="rejections",
    ),
    "listSentMessages": Operation(
        id="listSentMessages",
        method="GET",
        path="/v1/sent-messages",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "identity": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "recipient": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="messages",
    ),
    "listSuppressions": Operation(
        id="listSuppressions",
        method="GET",
        path="/v1/suppressions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "crn": {"style": "form", "explode": True},
            "reason": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="suppressions",
    ),
    "listTemplates": Operation(
        id="listTemplates",
        method="GET",
        path="/v1/templates",
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
        itemsKey="templates",
    ),
    "releaseDedicatedIP": Operation(
        id="releaseDedicatedIP",
        method="DELETE",
        path="/v1/dedicated-ips/{dedicated_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "removeSuppressionOverride": Operation(
        id="removeSuppressionOverride",
        method="DELETE",
        path="/v1/configuration-sets/{configuration_set_id}/suppression-overrides/{address}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "requestDedicatedIP": Operation(
        id="requestDedicatedIP",
        method="POST",
        path="/v1/dedicated-ips",
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
        path="/v1/sent-messages",
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
        path="/v1/sent-messages/batch",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "setBIMI": Operation(
        id="setBIMI",
        method="PATCH",
        path="/v1/identities/{identity_id}/bimi",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "setMailFromDomain": Operation(
        id="setMailFromDomain",
        method="PATCH",
        path="/v1/identities/{identity_id}/mail-from-domain",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateConfigurationSet": Operation(
        id="updateConfigurationSet",
        method="PATCH",
        path="/v1/configuration-sets/{configuration_set_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateDedicatedIP": Operation(
        id="updateDedicatedIP",
        method="PATCH",
        path="/v1/dedicated-ips/{dedicated_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateIPPool": Operation(
        id="updateIPPool",
        method="PATCH",
        path="/v1/ip-pools/{ip_pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateIdentity": Operation(
        id="updateIdentity",
        method="PATCH",
        path="/v1/identities/{identity_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateReceivingConfiguration": Operation(
        id="updateReceivingConfiguration",
        method="PATCH",
        path="/v1/identities/{identity_id}/receiving",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRecipientRule": Operation(
        id="updateRecipientRule",
        method="PATCH",
        path="/v1/identities/{identity_id}/recipient-rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateSuppression": Operation(
        id="updateSuppression",
        method="PATCH",
        path="/v1/suppressions/{suppression_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateTemplate": Operation(
        id="updateTemplate",
        method="PATCH",
        path="/v1/templates/{template_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "verifyBIMI": Operation(
        id="verifyBIMI",
        method="POST",
        path="/v1/identities/{identity_id}/bimi/verify",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "verifyIdentity": Operation(
        id="verifyIdentity",
        method="POST",
        path="/v1/identities/{identity_id}/verify",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "verifyMailFromDomain": Operation(
        id="verifyMailFromDomain",
        method="POST",
        path="/v1/identities/{identity_id}/mail-from-domain/verify",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
}


class EmailService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def add_suppression_override(
        self,
        configuration_set_id: str,
        body: m.AddSuppressionOverrideBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AddSuppressionOverrideResponse]:
        "Add a suppression override address"
        return cast(
            ApiResponse[m.AddSuppressionOverrideResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["addSuppressionOverride"],
                "json",
                {"configuration_set_id": configuration_set_id},
                body,
                None,
                options,
            ),
        )

    def begin_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.BeginDKIMRotationResponse]:
        "Begin DKIM key rotation"
        return cast(
            ApiResponse[m.BeginDKIMRotationResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["beginDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def cancel_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CancelDKIMRotationResponse]:
        "Cancel in-progress DKIM rotation"
        return cast(
            ApiResponse[m.CancelDKIMRotationResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["cancelDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def create_configuration_set(
        self, body: m.CreateConfigurationSetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateConfigurationSetResponse]:
        "Create a configuration set"
        return cast(
            ApiResponse[m.CreateConfigurationSetResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createConfigurationSet"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_ip_pool(
        self, body: m.CreateIPPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateIPPoolResponse]:
        "Create an IP pool"
        return cast(
            ApiResponse[m.CreateIPPoolResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createIPPool"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_identity(
        self, body: m.CreateIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateIdentityResponse]:
        "Create a sender identity"
        return cast(
            ApiResponse[m.CreateIdentityResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createIdentity"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_recipient_rule(
        self,
        identity_id: str,
        body: m.CreateRecipientRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateRecipientRuleResponse]:
        "Create recipient rule"
        return cast(
            ApiResponse[m.CreateRecipientRuleResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createRecipientRule"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    def create_suppression(
        self, body: m.CreateSuppressionBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSuppressionResponse]:
        "Add a suppression entry"
        return cast(
            ApiResponse[m.CreateSuppressionResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createSuppression"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_template(
        self, body: m.CreateTemplateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTemplateResponse]:
        "Create a template"
        return cast(
            ApiResponse[m.CreateTemplateResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createTemplate"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_configuration_set(
        self, configuration_set_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a configuration set"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteConfigurationSet"],
                "discard",
                {"configuration_set_id": configuration_set_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_ip_pool(self, ip_pool_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete an IP pool"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteIPPool"],
                "discard",
                {"ip_pool_id": ip_pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_identity(self, identity_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete an identity"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteIdentity"],
                "discard",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_recipient_rule(
        self, identity_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete recipient rule"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteRecipientRule"],
                "discard",
                {"identity_id": identity_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_suppression(
        self, suppression_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete suppression"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteSuppression"],
                "discard",
                {"suppression_id": suppression_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_template(self, template_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a template"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteTemplate"],
                "discard",
                {"template_id": template_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_configuration_set(
        self, configuration_set_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeConfigurationSetResponse]:
        "Describe a configuration set"
        return cast(
            ApiResponse[m.DescribeConfigurationSetResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeConfigurationSet"],
                "json",
                {"configuration_set_id": configuration_set_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_dedicated_ip(
        self, dedicated_ip_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeDedicatedIPResponse]:
        "Describe a dedicated IP"
        return cast(
            ApiResponse[m.DescribeDedicatedIPResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeDedicatedIP"],
                "json",
                {"dedicated_ip_id": dedicated_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_ip_pool(
        self, ip_pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeIPPoolResponse]:
        "Describe an IP pool"
        return cast(
            ApiResponse[m.DescribeIPPoolResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeIPPool"],
                "json",
                {"ip_pool_id": ip_pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_identity(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeIdentityResponse]:
        "Describe an identity"
        return cast(
            ApiResponse[m.DescribeIdentityResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeIdentity"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_received_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeReceivedMessageResponse]:
        "Get received message metadata"
        return cast(
            ApiResponse[m.DescribeReceivedMessageResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeReceivedMessage"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_recipient_rule(
        self, identity_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeRecipientRuleResponse]:
        "Get recipient rule"
        return cast(
            ApiResponse[m.DescribeRecipientRuleResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeRecipientRule"],
                "json",
                {"identity_id": identity_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_sent_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSentMessageResponse]:
        "Describe a sent message"
        return cast(
            ApiResponse[m.DescribeSentMessageResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeSentMessage"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_suppression(
        self, suppression_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSuppressionResponse]:
        "Get suppression"
        return cast(
            ApiResponse[m.DescribeSuppressionResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeSuppression"],
                "json",
                {"suppression_id": suppression_id},
                UNSET,
                None,
                options,
            ),
        )

    def describe_template(
        self, template_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeTemplateResponse]:
        "Describe a template"
        return cast(
            ApiResponse[m.DescribeTemplateResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeTemplate"],
                "json",
                {"template_id": template_id},
                UNSET,
                None,
                options,
            ),
        )

    def download_received_attachment(
        self, message_id: str, attachment_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download received attachment"
        return cast(
            httpx.Response,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadReceivedAttachment"],
                "binary",
                {"message_id": message_id, "attachment_id": attachment_id},
                UNSET,
                None,
                options,
            ),
        )

    def download_received_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download received message"
        return cast(
            httpx.Response,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadReceivedMessage"],
                "binary",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def download_sent_attachment(
        self, message_id: str, attachment_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download sent attachment"
        return cast(
            httpx.Response,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadSentAttachment"],
                "binary",
                {"message_id": message_id, "attachment_id": attachment_id},
                UNSET,
                None,
                options,
            ),
        )

    def download_sent_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download sent message"
        return cast(
            httpx.Response,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadSentMessage"],
                "binary",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def finalize_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.FinalizeDKIMRotationResponse]:
        "Finalize DKIM key rotation"
        return cast(
            ApiResponse[m.FinalizeDKIMRotationResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["finalizeDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_received_message_content(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetReceivedMessageContentResponse]:
        "Get received message content"
        return cast(
            ApiResponse[m.GetReceivedMessageContentResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getReceivedMessageContent"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_receiving_configuration(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetReceivingConfigurationResponse]:
        "Get receiving configuration"
        return cast(
            ApiResponse[m.GetReceivingConfigurationResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getReceivingConfiguration"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_sent_message_content(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSentMessageContentResponse]:
        "Get sent message content"
        return cast(
            ApiResponse[m.GetSentMessageContentResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getSentMessageContent"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_sent_message_engagement(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSentMessageEngagementResponse]:
        "Sent message engagement"
        return cast(
            ApiResponse[m.GetSentMessageEngagementResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getSentMessageEngagement"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_configuration_sets(
        self,
        *,
        query: m.ListConfigurationSetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListConfigurationSetsResponse, m.ListConfigurationSetsItem]:
        "List configuration sets"
        return cast(
            Page[m.ListConfigurationSetsResponse, m.ListConfigurationSetsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listConfigurationSets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_configuration_sets_all(
        self,
        *,
        query: m.ListConfigurationSetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListConfigurationSetsItem]:
        return iterate_pages(
            lambda marker: self.list_configuration_sets(
                query=cast(m.ListConfigurationSetsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_dmarc_reports(
        self,
        identity_id: str,
        *,
        query: m.ListDMARCReportsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListDMARCReportsResponse, m.ListDMARCReportsItem]:
        "List DMARC report records"
        return cast(
            Page[m.ListDMARCReportsResponse, m.ListDMARCReportsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listDMARCReports"],
                "page",
                {"identity_id": identity_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_dmarc_reports_all(
        self,
        identity_id: str,
        *,
        query: m.ListDMARCReportsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListDMARCReportsItem]:
        return iterate_pages(
            lambda marker: self.list_dmarc_reports(
                identity_id,
                query=cast(m.ListDMARCReportsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_dedicated_i_ps(
        self, *, query: m.ListDedicatedIPsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListDedicatedIPsResponse, m.ListDedicatedIPsItem]:
        "List dedicated IPs"
        return cast(
            Page[m.ListDedicatedIPsResponse, m.ListDedicatedIPsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listDedicatedIPs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_dedicated_i_ps_all(
        self, *, query: m.ListDedicatedIPsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListDedicatedIPsItem]:
        return iterate_pages(
            lambda marker: self.list_dedicated_i_ps(
                query=cast(m.ListDedicatedIPsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_ip_pools(
        self, *, query: m.ListIPPoolsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListIPPoolsResponse, m.ListIPPoolsItem]:
        "List IP pools"
        return cast(
            Page[m.ListIPPoolsResponse, m.ListIPPoolsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listIPPools"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_ip_pools_all(
        self, *, query: m.ListIPPoolsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListIPPoolsItem]:
        return iterate_pages(
            lambda marker: self.list_ip_pools(
                query=cast(m.ListIPPoolsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_identities(
        self, *, query: m.ListIdentitiesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListIdentitiesResponse, m.ListIdentitiesItem]:
        "List sender identities"
        return cast(
            Page[m.ListIdentitiesResponse, m.ListIdentitiesItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listIdentities"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_identities_all(
        self, *, query: m.ListIdentitiesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListIdentitiesItem]:
        return iterate_pages(
            lambda marker: self.list_identities(
                query=cast(m.ListIdentitiesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_received_messages(
        self,
        *,
        query: m.ListReceivedMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListReceivedMessagesResponse, m.ListReceivedMessagesItem]:
        "List received messages"
        return cast(
            Page[m.ListReceivedMessagesResponse, m.ListReceivedMessagesItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listReceivedMessages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_received_messages_all(
        self,
        *,
        query: m.ListReceivedMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListReceivedMessagesItem]:
        return iterate_pages(
            lambda marker: self.list_received_messages(
                query=cast(m.ListReceivedMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_recipient_rules(
        self,
        identity_id: str,
        *,
        query: m.ListRecipientRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRecipientRulesResponse, m.ListRecipientRulesItem]:
        "List recipient rules"
        return cast(
            Page[m.ListRecipientRulesResponse, m.ListRecipientRulesItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listRecipientRules"],
                "page",
                {"identity_id": identity_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_recipient_rules_all(
        self,
        identity_id: str,
        *,
        query: m.ListRecipientRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListRecipientRulesItem]:
        return iterate_pages(
            lambda marker: self.list_recipient_rules(
                identity_id,
                query=cast(m.ListRecipientRulesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_rejections(
        self, *, query: m.ListRejectionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRejectionsResponse, m.ListRejectionsItem]:
        "List API-side send rejections"
        return cast(
            Page[m.ListRejectionsResponse, m.ListRejectionsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listRejections"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_sent_messages(
        self, *, query: m.ListSentMessagesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSentMessagesResponse, m.ListSentMessagesItem]:
        "List sent messages"
        return cast(
            Page[m.ListSentMessagesResponse, m.ListSentMessagesItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listSentMessages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_sent_messages_all(
        self, *, query: m.ListSentMessagesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSentMessagesItem]:
        return iterate_pages(
            lambda marker: self.list_sent_messages(
                query=cast(m.ListSentMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_suppressions(
        self, *, query: m.ListSuppressionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSuppressionsResponse, m.ListSuppressionsItem]:
        "List suppression entries"
        return cast(
            Page[m.ListSuppressionsResponse, m.ListSuppressionsItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listSuppressions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_suppressions_all(
        self, *, query: m.ListSuppressionsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSuppressionsItem]:
        return iterate_pages(
            lambda marker: self.list_suppressions(
                query=cast(m.ListSuppressionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_templates(
        self, *, query: m.ListTemplatesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTemplatesResponse, m.ListTemplatesItem]:
        "List templates"
        return cast(
            Page[m.ListTemplatesResponse, m.ListTemplatesItem],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listTemplates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_templates_all(
        self, *, query: m.ListTemplatesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListTemplatesItem]:
        return iterate_pages(
            lambda marker: self.list_templates(
                query=cast(m.ListTemplatesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def release_dedicated_ip(
        self, dedicated_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Release a dedicated IP"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["releaseDedicatedIP"],
                "discard",
                {"dedicated_ip_id": dedicated_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    def remove_suppression_override(
        self, configuration_set_id: str, address: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RemoveSuppressionOverrideResponse]:
        "Remove a suppression override address"
        return cast(
            ApiResponse[m.RemoveSuppressionOverrideResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["removeSuppressionOverride"],
                "json",
                {"configuration_set_id": configuration_set_id, "address": address},
                UNSET,
                None,
                options,
            ),
        )

    def request_dedicated_ip(
        self,
        body: m.RequestDedicatedIPBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.RequestDedicatedIPResponse]:
        "Request a dedicated IP"
        return cast(
            ApiResponse[m.RequestDedicatedIPResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["requestDedicatedIP"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def send_message(
        self, body: m.SendMessageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageResponse]:
        "Send a message"
        return cast(
            ApiResponse[m.SendMessageResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["sendMessage"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def send_message_batch(
        self, body: m.SendMessageBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageBatchResponse]:
        "Send message batch"
        return cast(
            ApiResponse[m.SendMessageBatchResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["sendMessageBatch"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def set_bimi(
        self, identity_id: str, body: m.SetBIMIBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SetBIMIResponse]:
        "Set BIMI logo / VMC URLs"
        return cast(
            ApiResponse[m.SetBIMIResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["setBIMI"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    def set_mail_from_domain(
        self,
        identity_id: str,
        body: m.SetMailFromDomainBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetMailFromDomainResponse]:
        "Set custom MAIL FROM domain"
        return cast(
            ApiResponse[m.SetMailFromDomainResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["setMailFromDomain"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    def update_configuration_set(
        self,
        configuration_set_id: str,
        body: m.UpdateConfigurationSetBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateConfigurationSetResponse]:
        "Update a configuration set"
        return cast(
            ApiResponse[m.UpdateConfigurationSetResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateConfigurationSet"],
                "json",
                {"configuration_set_id": configuration_set_id},
                body,
                None,
                options,
            ),
        )

    def update_dedicated_ip(
        self,
        dedicated_ip_id: str,
        body: m.UpdateDedicatedIPBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateDedicatedIPResponse]:
        "Update a dedicated IP"
        return cast(
            ApiResponse[m.UpdateDedicatedIPResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateDedicatedIP"],
                "json",
                {"dedicated_ip_id": dedicated_ip_id},
                body,
                None,
                options,
            ),
        )

    def update_ip_pool(
        self, ip_pool_id: str, body: m.UpdateIPPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateIPPoolResponse]:
        "Update an IP pool"
        return cast(
            ApiResponse[m.UpdateIPPoolResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateIPPool"],
                "json",
                {"ip_pool_id": ip_pool_id},
                body,
                None,
                options,
            ),
        )

    def update_identity(
        self, identity_id: str, body: m.UpdateIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateIdentityResponse]:
        "Update identity"
        return cast(
            ApiResponse[m.UpdateIdentityResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateIdentity"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    def update_receiving_configuration(
        self,
        identity_id: str,
        body: m.UpdateReceivingConfigurationBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Update receiving configuration"
        return cast(
            None,
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateReceivingConfiguration"],
                "discard",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    def update_recipient_rule(
        self,
        identity_id: str,
        rule_id: str,
        body: m.UpdateRecipientRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRecipientRuleResponse]:
        "Update recipient rule"
        return cast(
            ApiResponse[m.UpdateRecipientRuleResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateRecipientRule"],
                "json",
                {"identity_id": identity_id, "rule_id": rule_id},
                body,
                None,
                options,
            ),
        )

    def update_suppression(
        self,
        suppression_id: str,
        body: m.UpdateSuppressionBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSuppressionResponse]:
        "Update suppression"
        return cast(
            ApiResponse[m.UpdateSuppressionResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateSuppression"],
                "json",
                {"suppression_id": suppression_id},
                body,
                None,
                options,
            ),
        )

    def update_template(
        self, template_id: str, body: m.UpdateTemplateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTemplateResponse]:
        "Update a template"
        return cast(
            ApiResponse[m.UpdateTemplateResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateTemplate"],
                "json",
                {"template_id": template_id},
                body,
                None,
                options,
            ),
        )

    def verify_bimi(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyBIMIResponse]:
        "Verify BIMI logo (+ optional VMC)"
        return cast(
            ApiResponse[m.VerifyBIMIResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyBIMI"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def verify_identity(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyIdentityResponse]:
        "Trigger DNS verification"
        return cast(
            ApiResponse[m.VerifyIdentityResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyIdentity"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    def verify_mail_from_domain(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyMailFromDomainResponse]:
        "Verify custom MAIL FROM domain MX"
        return cast(
            ApiResponse[m.VerifyMailFromDomainResponse],
            self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyMailFromDomain"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )


class AsyncEmailService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def add_suppression_override(
        self,
        configuration_set_id: str,
        body: m.AddSuppressionOverrideBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AddSuppressionOverrideResponse]:
        "Add a suppression override address"
        return cast(
            ApiResponse[m.AddSuppressionOverrideResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["addSuppressionOverride"],
                "json",
                {"configuration_set_id": configuration_set_id},
                body,
                None,
                options,
            ),
        )

    async def begin_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.BeginDKIMRotationResponse]:
        "Begin DKIM key rotation"
        return cast(
            ApiResponse[m.BeginDKIMRotationResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["beginDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def cancel_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CancelDKIMRotationResponse]:
        "Cancel in-progress DKIM rotation"
        return cast(
            ApiResponse[m.CancelDKIMRotationResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["cancelDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def create_configuration_set(
        self, body: m.CreateConfigurationSetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateConfigurationSetResponse]:
        "Create a configuration set"
        return cast(
            ApiResponse[m.CreateConfigurationSetResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createConfigurationSet"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_ip_pool(
        self, body: m.CreateIPPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateIPPoolResponse]:
        "Create an IP pool"
        return cast(
            ApiResponse[m.CreateIPPoolResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createIPPool"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_identity(
        self, body: m.CreateIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateIdentityResponse]:
        "Create a sender identity"
        return cast(
            ApiResponse[m.CreateIdentityResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createIdentity"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_recipient_rule(
        self,
        identity_id: str,
        body: m.CreateRecipientRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateRecipientRuleResponse]:
        "Create recipient rule"
        return cast(
            ApiResponse[m.CreateRecipientRuleResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createRecipientRule"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    async def create_suppression(
        self, body: m.CreateSuppressionBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSuppressionResponse]:
        "Add a suppression entry"
        return cast(
            ApiResponse[m.CreateSuppressionResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createSuppression"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_template(
        self, body: m.CreateTemplateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTemplateResponse]:
        "Create a template"
        return cast(
            ApiResponse[m.CreateTemplateResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["createTemplate"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_configuration_set(
        self, configuration_set_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a configuration set"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteConfigurationSet"],
                "discard",
                {"configuration_set_id": configuration_set_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_ip_pool(
        self, ip_pool_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete an IP pool"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteIPPool"],
                "discard",
                {"ip_pool_id": ip_pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_identity(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete an identity"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteIdentity"],
                "discard",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_recipient_rule(
        self, identity_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete recipient rule"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteRecipientRule"],
                "discard",
                {"identity_id": identity_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_suppression(
        self, suppression_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete suppression"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteSuppression"],
                "discard",
                {"suppression_id": suppression_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_template(
        self, template_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a template"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["deleteTemplate"],
                "discard",
                {"template_id": template_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_configuration_set(
        self, configuration_set_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeConfigurationSetResponse]:
        "Describe a configuration set"
        return cast(
            ApiResponse[m.DescribeConfigurationSetResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeConfigurationSet"],
                "json",
                {"configuration_set_id": configuration_set_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_dedicated_ip(
        self, dedicated_ip_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeDedicatedIPResponse]:
        "Describe a dedicated IP"
        return cast(
            ApiResponse[m.DescribeDedicatedIPResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeDedicatedIP"],
                "json",
                {"dedicated_ip_id": dedicated_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_ip_pool(
        self, ip_pool_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeIPPoolResponse]:
        "Describe an IP pool"
        return cast(
            ApiResponse[m.DescribeIPPoolResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeIPPool"],
                "json",
                {"ip_pool_id": ip_pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_identity(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeIdentityResponse]:
        "Describe an identity"
        return cast(
            ApiResponse[m.DescribeIdentityResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeIdentity"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_received_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeReceivedMessageResponse]:
        "Get received message metadata"
        return cast(
            ApiResponse[m.DescribeReceivedMessageResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeReceivedMessage"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_recipient_rule(
        self, identity_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeRecipientRuleResponse]:
        "Get recipient rule"
        return cast(
            ApiResponse[m.DescribeRecipientRuleResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeRecipientRule"],
                "json",
                {"identity_id": identity_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_sent_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSentMessageResponse]:
        "Describe a sent message"
        return cast(
            ApiResponse[m.DescribeSentMessageResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeSentMessage"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_suppression(
        self, suppression_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeSuppressionResponse]:
        "Get suppression"
        return cast(
            ApiResponse[m.DescribeSuppressionResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeSuppression"],
                "json",
                {"suppression_id": suppression_id},
                UNSET,
                None,
                options,
            ),
        )

    async def describe_template(
        self, template_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DescribeTemplateResponse]:
        "Describe a template"
        return cast(
            ApiResponse[m.DescribeTemplateResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["describeTemplate"],
                "json",
                {"template_id": template_id},
                UNSET,
                None,
                options,
            ),
        )

    async def download_received_attachment(
        self, message_id: str, attachment_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download received attachment"
        return cast(
            httpx.Response,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadReceivedAttachment"],
                "binary",
                {"message_id": message_id, "attachment_id": attachment_id},
                UNSET,
                None,
                options,
            ),
        )

    async def download_received_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download received message"
        return cast(
            httpx.Response,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadReceivedMessage"],
                "binary",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def download_sent_attachment(
        self, message_id: str, attachment_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download sent attachment"
        return cast(
            httpx.Response,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadSentAttachment"],
                "binary",
                {"message_id": message_id, "attachment_id": attachment_id},
                UNSET,
                None,
                options,
            ),
        )

    async def download_sent_message(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> httpx.Response:
        "Download sent message"
        return cast(
            httpx.Response,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["downloadSentMessage"],
                "binary",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def finalize_dkim_rotation(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.FinalizeDKIMRotationResponse]:
        "Finalize DKIM key rotation"
        return cast(
            ApiResponse[m.FinalizeDKIMRotationResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["finalizeDKIMRotation"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_received_message_content(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetReceivedMessageContentResponse]:
        "Get received message content"
        return cast(
            ApiResponse[m.GetReceivedMessageContentResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getReceivedMessageContent"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_receiving_configuration(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetReceivingConfigurationResponse]:
        "Get receiving configuration"
        return cast(
            ApiResponse[m.GetReceivingConfigurationResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getReceivingConfiguration"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_sent_message_content(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSentMessageContentResponse]:
        "Get sent message content"
        return cast(
            ApiResponse[m.GetSentMessageContentResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getSentMessageContent"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_sent_message_engagement(
        self, message_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSentMessageEngagementResponse]:
        "Sent message engagement"
        return cast(
            ApiResponse[m.GetSentMessageEngagementResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["getSentMessageEngagement"],
                "json",
                {"message_id": message_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_configuration_sets(
        self,
        *,
        query: m.ListConfigurationSetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListConfigurationSetsResponse, m.ListConfigurationSetsItem]:
        "List configuration sets"
        return cast(
            Page[m.ListConfigurationSetsResponse, m.ListConfigurationSetsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listConfigurationSets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_configuration_sets_all(
        self,
        *,
        query: m.ListConfigurationSetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListConfigurationSetsItem]:
        return aiterate_pages(
            lambda marker: self.list_configuration_sets(
                query=cast(m.ListConfigurationSetsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_dmarc_reports(
        self,
        identity_id: str,
        *,
        query: m.ListDMARCReportsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListDMARCReportsResponse, m.ListDMARCReportsItem]:
        "List DMARC report records"
        return cast(
            Page[m.ListDMARCReportsResponse, m.ListDMARCReportsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listDMARCReports"],
                "page",
                {"identity_id": identity_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_dmarc_reports_all(
        self,
        identity_id: str,
        *,
        query: m.ListDMARCReportsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListDMARCReportsItem]:
        return aiterate_pages(
            lambda marker: self.list_dmarc_reports(
                identity_id,
                query=cast(m.ListDMARCReportsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_dedicated_i_ps(
        self, *, query: m.ListDedicatedIPsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListDedicatedIPsResponse, m.ListDedicatedIPsItem]:
        "List dedicated IPs"
        return cast(
            Page[m.ListDedicatedIPsResponse, m.ListDedicatedIPsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listDedicatedIPs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_dedicated_i_ps_all(
        self, *, query: m.ListDedicatedIPsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListDedicatedIPsItem]:
        return aiterate_pages(
            lambda marker: self.list_dedicated_i_ps(
                query=cast(m.ListDedicatedIPsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_ip_pools(
        self, *, query: m.ListIPPoolsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListIPPoolsResponse, m.ListIPPoolsItem]:
        "List IP pools"
        return cast(
            Page[m.ListIPPoolsResponse, m.ListIPPoolsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listIPPools"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_ip_pools_all(
        self, *, query: m.ListIPPoolsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListIPPoolsItem]:
        return aiterate_pages(
            lambda marker: self.list_ip_pools(
                query=cast(m.ListIPPoolsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_identities(
        self, *, query: m.ListIdentitiesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListIdentitiesResponse, m.ListIdentitiesItem]:
        "List sender identities"
        return cast(
            Page[m.ListIdentitiesResponse, m.ListIdentitiesItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listIdentities"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_identities_all(
        self, *, query: m.ListIdentitiesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListIdentitiesItem]:
        return aiterate_pages(
            lambda marker: self.list_identities(
                query=cast(m.ListIdentitiesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_received_messages(
        self,
        *,
        query: m.ListReceivedMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListReceivedMessagesResponse, m.ListReceivedMessagesItem]:
        "List received messages"
        return cast(
            Page[m.ListReceivedMessagesResponse, m.ListReceivedMessagesItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listReceivedMessages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_received_messages_all(
        self,
        *,
        query: m.ListReceivedMessagesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListReceivedMessagesItem]:
        return aiterate_pages(
            lambda marker: self.list_received_messages(
                query=cast(m.ListReceivedMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_recipient_rules(
        self,
        identity_id: str,
        *,
        query: m.ListRecipientRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRecipientRulesResponse, m.ListRecipientRulesItem]:
        "List recipient rules"
        return cast(
            Page[m.ListRecipientRulesResponse, m.ListRecipientRulesItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listRecipientRules"],
                "page",
                {"identity_id": identity_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_recipient_rules_all(
        self,
        identity_id: str,
        *,
        query: m.ListRecipientRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListRecipientRulesItem]:
        return aiterate_pages(
            lambda marker: self.list_recipient_rules(
                identity_id,
                query=cast(m.ListRecipientRulesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_rejections(
        self, *, query: m.ListRejectionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRejectionsResponse, m.ListRejectionsItem]:
        "List API-side send rejections"
        return cast(
            Page[m.ListRejectionsResponse, m.ListRejectionsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listRejections"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_sent_messages(
        self, *, query: m.ListSentMessagesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSentMessagesResponse, m.ListSentMessagesItem]:
        "List sent messages"
        return cast(
            Page[m.ListSentMessagesResponse, m.ListSentMessagesItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listSentMessages"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_sent_messages_all(
        self, *, query: m.ListSentMessagesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSentMessagesItem]:
        return aiterate_pages(
            lambda marker: self.list_sent_messages(
                query=cast(m.ListSentMessagesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_suppressions(
        self, *, query: m.ListSuppressionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSuppressionsResponse, m.ListSuppressionsItem]:
        "List suppression entries"
        return cast(
            Page[m.ListSuppressionsResponse, m.ListSuppressionsItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listSuppressions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_suppressions_all(
        self, *, query: m.ListSuppressionsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSuppressionsItem]:
        return aiterate_pages(
            lambda marker: self.list_suppressions(
                query=cast(m.ListSuppressionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_templates(
        self, *, query: m.ListTemplatesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTemplatesResponse, m.ListTemplatesItem]:
        "List templates"
        return cast(
            Page[m.ListTemplatesResponse, m.ListTemplatesItem],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["listTemplates"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_templates_all(
        self, *, query: m.ListTemplatesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListTemplatesItem]:
        return aiterate_pages(
            lambda marker: self.list_templates(
                query=cast(m.ListTemplatesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def release_dedicated_ip(
        self, dedicated_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Release a dedicated IP"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["releaseDedicatedIP"],
                "discard",
                {"dedicated_ip_id": dedicated_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    async def remove_suppression_override(
        self, configuration_set_id: str, address: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.RemoveSuppressionOverrideResponse]:
        "Remove a suppression override address"
        return cast(
            ApiResponse[m.RemoveSuppressionOverrideResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["removeSuppressionOverride"],
                "json",
                {"configuration_set_id": configuration_set_id, "address": address},
                UNSET,
                None,
                options,
            ),
        )

    async def request_dedicated_ip(
        self,
        body: m.RequestDedicatedIPBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.RequestDedicatedIPResponse]:
        "Request a dedicated IP"
        return cast(
            ApiResponse[m.RequestDedicatedIPResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["requestDedicatedIP"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def send_message(
        self, body: m.SendMessageBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageResponse]:
        "Send a message"
        return cast(
            ApiResponse[m.SendMessageResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["sendMessage"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def send_message_batch(
        self, body: m.SendMessageBatchBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SendMessageBatchResponse]:
        "Send message batch"
        return cast(
            ApiResponse[m.SendMessageBatchResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["sendMessageBatch"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def set_bimi(
        self, identity_id: str, body: m.SetBIMIBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.SetBIMIResponse]:
        "Set BIMI logo / VMC URLs"
        return cast(
            ApiResponse[m.SetBIMIResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["setBIMI"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    async def set_mail_from_domain(
        self,
        identity_id: str,
        body: m.SetMailFromDomainBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetMailFromDomainResponse]:
        "Set custom MAIL FROM domain"
        return cast(
            ApiResponse[m.SetMailFromDomainResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["setMailFromDomain"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    async def update_configuration_set(
        self,
        configuration_set_id: str,
        body: m.UpdateConfigurationSetBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateConfigurationSetResponse]:
        "Update a configuration set"
        return cast(
            ApiResponse[m.UpdateConfigurationSetResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateConfigurationSet"],
                "json",
                {"configuration_set_id": configuration_set_id},
                body,
                None,
                options,
            ),
        )

    async def update_dedicated_ip(
        self,
        dedicated_ip_id: str,
        body: m.UpdateDedicatedIPBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateDedicatedIPResponse]:
        "Update a dedicated IP"
        return cast(
            ApiResponse[m.UpdateDedicatedIPResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateDedicatedIP"],
                "json",
                {"dedicated_ip_id": dedicated_ip_id},
                body,
                None,
                options,
            ),
        )

    async def update_ip_pool(
        self, ip_pool_id: str, body: m.UpdateIPPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateIPPoolResponse]:
        "Update an IP pool"
        return cast(
            ApiResponse[m.UpdateIPPoolResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateIPPool"],
                "json",
                {"ip_pool_id": ip_pool_id},
                body,
                None,
                options,
            ),
        )

    async def update_identity(
        self, identity_id: str, body: m.UpdateIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateIdentityResponse]:
        "Update identity"
        return cast(
            ApiResponse[m.UpdateIdentityResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateIdentity"],
                "json",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    async def update_receiving_configuration(
        self,
        identity_id: str,
        body: m.UpdateReceivingConfigurationBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Update receiving configuration"
        return cast(
            None,
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateReceivingConfiguration"],
                "discard",
                {"identity_id": identity_id},
                body,
                None,
                options,
            ),
        )

    async def update_recipient_rule(
        self,
        identity_id: str,
        rule_id: str,
        body: m.UpdateRecipientRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRecipientRuleResponse]:
        "Update recipient rule"
        return cast(
            ApiResponse[m.UpdateRecipientRuleResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateRecipientRule"],
                "json",
                {"identity_id": identity_id, "rule_id": rule_id},
                body,
                None,
                options,
            ),
        )

    async def update_suppression(
        self,
        suppression_id: str,
        body: m.UpdateSuppressionBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSuppressionResponse]:
        "Update suppression"
        return cast(
            ApiResponse[m.UpdateSuppressionResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateSuppression"],
                "json",
                {"suppression_id": suppression_id},
                body,
                None,
                options,
            ),
        )

    async def update_template(
        self, template_id: str, body: m.UpdateTemplateBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTemplateResponse]:
        "Update a template"
        return cast(
            ApiResponse[m.UpdateTemplateResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["updateTemplate"],
                "json",
                {"template_id": template_id},
                body,
                None,
                options,
            ),
        )

    async def verify_bimi(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyBIMIResponse]:
        "Verify BIMI logo (+ optional VMC)"
        return cast(
            ApiResponse[m.VerifyBIMIResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyBIMI"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def verify_identity(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyIdentityResponse]:
        "Trigger DNS verification"
        return cast(
            ApiResponse[m.VerifyIdentityResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyIdentity"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )

    async def verify_mail_from_domain(
        self, identity_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.VerifyMailFromDomainResponse]:
        "Verify custom MAIL FROM domain MX"
        return cast(
            ApiResponse[m.VerifyMailFromDomainResponse],
            await self._transport.request(
                "email",
                "https://email.{region}.basaltic.sh",
                _OPS["verifyMailFromDomain"],
                "json",
                {"identity_id": identity_id},
                UNSET,
                None,
                options,
            ),
        )
