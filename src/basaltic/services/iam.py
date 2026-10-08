"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import iam as m
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
    "assumeRole": Operation(
        id="assumeRole",
        method="POST",
        path="/v1/assume-role",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "assumeRoleWithWebIdentity": Operation(
        id="assumeRoleWithWebIdentity",
        method="POST",
        path="/v1/assume-role-with-web-identity",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachRolePolicy": Operation(
        id="attachRolePolicy",
        method="POST",
        path="/v1/roles/{role_id}/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachServiceAccountPolicy": Operation(
        id="attachServiceAccountPolicy",
        method="POST",
        path="/v1/service-accounts/{service_account_id}/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "authorizeOAuthClient": Operation(
        id="authorizeOAuthClient",
        method="POST",
        path="/v1/oauth/authorize",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createPersonalSSHKey": Operation(
        id="createPersonalSSHKey",
        method="POST",
        path="/v1/auth/ssh-keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createPolicy": Operation(
        id="createPolicy",
        method="POST",
        path="/v1/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRole": Operation(
        id="createRole",
        method="POST",
        path="/v1/roles",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createServiceAccount": Operation(
        id="createServiceAccount",
        method="POST",
        path="/v1/service-accounts",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createServiceAccountCredential": Operation(
        id="createServiceAccountCredential",
        method="POST",
        path="/v1/service-accounts/{service_account_id}/credentials",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createServiceAccountSSHKey": Operation(
        id="createServiceAccountSSHKey",
        method="POST",
        path="/v1/service-accounts/{service_account_id}/ssh-keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deletePersonalSSHKey": Operation(
        id="deletePersonalSSHKey",
        method="DELETE",
        path="/v1/auth/ssh-keys/{ssh_key_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deletePolicy": Operation(
        id="deletePolicy",
        method="DELETE",
        path="/v1/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRole": Operation(
        id="deleteRole",
        method="DELETE",
        path="/v1/roles/{role_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRoleInlinePolicy": Operation(
        id="deleteRoleInlinePolicy",
        method="DELETE",
        path="/v1/roles/{role_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteServiceAccount": Operation(
        id="deleteServiceAccount",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteServiceAccountCredential": Operation(
        id="deleteServiceAccountCredential",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}/credentials/{credential_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteServiceAccountInlinePolicy": Operation(
        id="deleteServiceAccountInlinePolicy",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteServiceAccountSSHKey": Operation(
        id="deleteServiceAccountSSHKey",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}/ssh-keys/{ssh_key_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachRolePolicy": Operation(
        id="detachRolePolicy",
        method="DELETE",
        path="/v1/roles/{role_id}/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachServiceAccountPolicy": Operation(
        id="detachServiceAccountPolicy",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getOAuthToken": Operation(
        id="getOAuthToken",
        method="POST",
        path="/v1/oauth/token",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "getPersonalLinuxIdentity": Operation(
        id="getPersonalLinuxIdentity",
        method="GET",
        path="/v1/auth/linux-identity",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getPolicy": Operation(
        id="getPolicy",
        method="GET",
        path="/v1/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRole": Operation(
        id="getRole",
        method="GET",
        path="/v1/roles/{role_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRoleInlinePolicy": Operation(
        id="getRoleInlinePolicy",
        method="GET",
        path="/v1/roles/{role_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRolePermissionBoundary": Operation(
        id="getRolePermissionBoundary",
        method="GET",
        path="/v1/roles/{role_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSTSSession": Operation(
        id="getSTSSession",
        method="GET",
        path="/v1/sts-sessions/{session_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getServiceAccount": Operation(
        id="getServiceAccount",
        method="GET",
        path="/v1/service-accounts/{service_account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getServiceAccountInlinePolicy": Operation(
        id="getServiceAccountInlinePolicy",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getServiceAccountLinuxIdentity": Operation(
        id="getServiceAccountLinuxIdentity",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/linux-identity",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getServiceAccountPermissionBoundary": Operation(
        id="getServiceAccountPermissionBoundary",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listPersonalSSHKeys": Operation(
        id="listPersonalSSHKeys",
        method="GET",
        path="/v1/auth/ssh-keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="ssh_keys",
    ),
    "listPolicies": Operation(
        id="listPolicies",
        method="GET",
        path="/v1/policies",
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
        itemsKey="policies",
    ),
    "listPolicyRoles": Operation(
        id="listPolicyRoles",
        method="GET",
        path="/v1/policies/{policy_id}/roles",
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
        itemsKey="roles",
    ),
    "listPolicyServiceAccounts": Operation(
        id="listPolicyServiceAccounts",
        method="GET",
        path="/v1/policies/{policy_id}/service-accounts",
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
        itemsKey="service_accounts",
    ),
    "listRegions": Operation(
        id="listRegions",
        method="GET",
        path="/v1/regions",
        authenticated=False,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="regions",
    ),
    "listRoleInlinePolicies": Operation(
        id="listRoleInlinePolicies",
        method="GET",
        path="/v1/roles/{role_id}/inline-policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="inline_policies",
    ),
    "listRolePolicies": Operation(
        id="listRolePolicies",
        method="GET",
        path="/v1/roles/{role_id}/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="policies",
    ),
    "listRoles": Operation(
        id="listRoles",
        method="GET",
        path="/v1/roles",
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
        itemsKey="roles",
    ),
    "listSTSSessions": Operation(
        id="listSTSSessions",
        method="GET",
        path="/v1/sts-sessions",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "role": {"style": "form", "explode": True},
            "principal": {"style": "form", "explode": True},
            "principal_type": {"style": "form", "explode": True},
            "active_only": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="sts_sessions",
    ),
    "listServiceAccountCredentials": Operation(
        id="listServiceAccountCredentials",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/credentials",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="credentials",
    ),
    "listServiceAccountInlinePolicies": Operation(
        id="listServiceAccountInlinePolicies",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/inline-policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="inline_policies",
    ),
    "listServiceAccountPolicies": Operation(
        id="listServiceAccountPolicies",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="policies",
    ),
    "listServiceAccountSSHKeys": Operation(
        id="listServiceAccountSSHKeys",
        method="GET",
        path="/v1/service-accounts/{service_account_id}/ssh-keys",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="ssh_keys",
    ),
    "listServiceAccounts": Operation(
        id="listServiceAccounts",
        method="GET",
        path="/v1/service-accounts",
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
        itemsKey="service_accounts",
    ),
    "putRoleInlinePolicy": Operation(
        id="putRoleInlinePolicy",
        method="PUT",
        path="/v1/roles/{role_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putServiceAccountInlinePolicy": Operation(
        id="putServiceAccountInlinePolicy",
        method="PUT",
        path="/v1/service-accounts/{service_account_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "removeRolePermissionBoundary": Operation(
        id="removeRolePermissionBoundary",
        method="DELETE",
        path="/v1/roles/{role_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "removeServiceAccountPermissionBoundary": Operation(
        id="removeServiceAccountPermissionBoundary",
        method="DELETE",
        path="/v1/service-accounts/{service_account_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "revokeOAuthToken": Operation(
        id="revokeOAuthToken",
        method="POST",
        path="/v1/oauth/revoke",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "revokeSTSSession": Operation(
        id="revokeSTSSession",
        method="DELETE",
        path="/v1/sts-sessions/{session_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "setRolePermissionBoundary": Operation(
        id="setRolePermissionBoundary",
        method="PUT",
        path="/v1/roles/{role_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "setServiceAccountPermissionBoundary": Operation(
        id="setServiceAccountPermissionBoundary",
        method="PUT",
        path="/v1/service-accounts/{service_account_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updatePolicy": Operation(
        id="updatePolicy",
        method="PATCH",
        path="/v1/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRole": Operation(
        id="updateRole",
        method="PATCH",
        path="/v1/roles/{role_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateServiceAccount": Operation(
        id="updateServiceAccount",
        method="PATCH",
        path="/v1/service-accounts/{service_account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class IamService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def assume_role(
        self, body: m.AssumeRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssumeRoleResponse]:
        "Assume role"
        return cast(
            ApiResponse[m.AssumeRoleResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["assumeRole"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def assume_role_with_web_identity(
        self, body: m.AssumeRoleWithWebIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssumeRoleWithWebIdentityResponse]:
        "Assume role with web identity"
        return cast(
            ApiResponse[m.AssumeRoleWithWebIdentityResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["assumeRoleWithWebIdentity"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def attach_role_policy(
        self, role_id: str, body: m.AttachRolePolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to role"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["attachRolePolicy"],
                "discard",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    def attach_service_account_policy(
        self,
        service_account_id: str,
        body: m.AttachServiceAccountPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Attach policy to service account"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["attachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    def authorize_oauth_client(
        self, body: m.AuthorizeOAuthClientBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AuthorizeOAuthClientResponse]:
        "Approve a CLI login and issue an authorization code"
        return cast(
            ApiResponse[m.AuthorizeOAuthClientResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["authorizeOAuthClient"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_personal_ssh_key(
        self, body: m.CreatePersonalSSHKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePersonalSSHKeyResponse]:
        "Add personal SSH key"
        return cast(
            ApiResponse[m.CreatePersonalSSHKeyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createPersonalSSHKey"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_policy(
        self, body: m.CreatePolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePolicyResponse]:
        "Create policy"
        return cast(
            ApiResponse[m.CreatePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_role(
        self, body: m.CreateRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRoleResponse]:
        "Create role"
        return cast(
            ApiResponse[m.CreateRoleResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createRole"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_service_account(
        self, body: m.CreateServiceAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateServiceAccountResponse]:
        "Create service account"
        return cast(
            ApiResponse[m.CreateServiceAccountResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccount"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_service_account_credential(
        self,
        service_account_id: str,
        body: m.CreateServiceAccountCredentialBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateServiceAccountCredentialResponse]:
        "Create credential"
        return cast(
            ApiResponse[m.CreateServiceAccountCredentialResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccountCredential"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    def create_service_account_ssh_key(
        self,
        service_account_id: str,
        body: m.CreateServiceAccountSSHKeyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateServiceAccountSSHKeyResponse]:
        "Add service-account SSH key"
        return cast(
            ApiResponse[m.CreateServiceAccountSSHKeyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccountSSHKey"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    def delete_personal_ssh_key(
        self, ssh_key_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke personal SSH key"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deletePersonalSSHKey"],
                "discard",
                {"ssh_key_id": ssh_key_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete policy"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deletePolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_role(self, role_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete role"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteRole"],
                "discard",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_role_inline_policy(
        self, role_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a role's inline policy by name"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteRoleInlinePolicy"],
                "discard",
                {"role_id": role_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def delete_service_account(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete service account"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccount"],
                "discard",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_service_account_credential(
        self, service_account_id: str, credential_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete credential"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountCredential"],
                "discard",
                {"service_account_id": service_account_id, "credential_id": credential_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_service_account_inline_policy(
        self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a service account's inline policy by name"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountInlinePolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def delete_service_account_ssh_key(
        self, service_account_id: str, ssh_key_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke service-account SSH key"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountSSHKey"],
                "discard",
                {"service_account_id": service_account_id, "ssh_key_id": ssh_key_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_role_policy(
        self, role_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from role"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["detachRolePolicy"],
                "discard",
                {"role_id": role_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_service_account_policy(
        self, service_account_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from service account"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["detachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_oauth_token(
        self, body: m.GetOAuthTokenBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetOAuthTokenResponse]:
        "Exchange an access key for a bearer token"
        return cast(
            ApiResponse[m.GetOAuthTokenResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getOAuthToken"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def get_personal_linux_identity(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPersonalLinuxIdentityResponse]:
        "Get personal Linux identity"
        return cast(
            ApiResponse[m.GetPersonalLinuxIdentityResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getPersonalLinuxIdentity"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPolicyResponse]:
        "Get policy"
        return cast(
            ApiResponse[m.GetPolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getPolicy"],
                "json",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_policy_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetPolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetPolicyResource]:
        return cast(
            ApiResponse[m.GetPolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_policy(id, options=options),
                lambda match: self.list_policies(
                    query=cast(
                        m.ListPoliciesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "policy",
            ),
        )

    def get_role(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRoleResponse]:
        "Get role"
        return cast(
            ApiResponse[m.GetRoleResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRole"],
                "json",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_role_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRoleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRoleResource]:
        return cast(
            ApiResponse[m.GetRoleResource],
            resolve_reference(
                reference,
                lambda id: self.get_role(id, options=options),
                lambda match: self.list_roles(
                    query=cast(m.ListRolesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "role",
            ),
        )

    def get_role_inline_policy(
        self, role_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRoleInlinePolicyResponse]:
        "Get a role's inline policy by name"
        return cast(
            ApiResponse[m.GetRoleInlinePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRoleInlinePolicy"],
                "json",
                {"role_id": role_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def get_role_inline_policy_by_reference(
        self,
        role_id: str,
        reference: str,
        *,
        scope: m.GetRoleInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRoleInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetRoleInlinePolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_role_inline_policy(role_id, id, options=options),
                lambda match: self.list_role_inline_policies(
                    role_id,
                    query=cast(m.ListRoleInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    def get_role_permission_boundary(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRolePermissionBoundaryResponse]:
        "Get a role's permission boundary"
        return cast(
            ApiResponse[m.GetRolePermissionBoundaryResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRolePermissionBoundary"],
                "json",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_sts_session(
        self, session_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSTSSessionResponse]:
        "Get STS session"
        return cast(
            ApiResponse[m.GetSTSSessionResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getSTSSession"],
                "json",
                {"session_id": session_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_sts_session_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSTSSessionScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSTSSessionResource]:
        return cast(
            ApiResponse[m.GetSTSSessionResource],
            resolve_reference(
                reference,
                lambda id: self.get_sts_session(id, options=options),
                lambda match: self.list_sts_sessions(
                    query=cast(
                        m.ListSTSSessionsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "sts_session",
            ),
        )

    def get_service_account(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountResponse]:
        "Get service account"
        return cast(
            ApiResponse[m.GetServiceAccountResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccount"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_service_account_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetServiceAccountScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetServiceAccountResource]:
        return cast(
            ApiResponse[m.GetServiceAccountResource],
            resolve_reference(
                reference,
                lambda id: self.get_service_account(id, options=options),
                lambda match: self.list_service_accounts(
                    query=cast(
                        m.ListServiceAccountsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "service_account",
            ),
        )

    def get_service_account_inline_policy(
        self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountInlinePolicyResponse]:
        "Get a service account's inline policy by name"
        return cast(
            ApiResponse[m.GetServiceAccountInlinePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountInlinePolicy"],
                "json",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def get_service_account_inline_policy_by_reference(
        self,
        service_account_id: str,
        reference: str,
        *,
        scope: m.GetServiceAccountInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetServiceAccountInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetServiceAccountInlinePolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_service_account_inline_policy(
                    service_account_id, id, options=options
                ),
                lambda match: self.list_service_account_inline_policies(
                    service_account_id,
                    query=cast(
                        m.ListServiceAccountInlinePoliciesQuery, {**reference_scope(scope), **match}
                    ),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    def get_service_account_linux_identity(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountLinuxIdentityResponse]:
        "Get serviceaccount Linux identity"
        return cast(
            ApiResponse[m.GetServiceAccountLinuxIdentityResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountLinuxIdentity"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_service_account_permission_boundary(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountPermissionBoundaryResponse]:
        "Get a service account's permission boundary"
        return cast(
            ApiResponse[m.GetServiceAccountPermissionBoundaryResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountPermissionBoundary"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_personal_ssh_keys(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListPersonalSSHKeysResponse, m.ListPersonalSSHKeysItem]:
        "List personal SSH keys"
        return cast(
            Page[m.ListPersonalSSHKeysResponse, m.ListPersonalSSHKeysItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPersonalSSHKeys"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def list_policies(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
        "List policies"
        return cast(
            Page[m.ListPoliciesResponse, m.ListPoliciesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicies"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_policies_all(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListPoliciesItem]:
        return iterate_pages(
            lambda marker: self.list_policies(
                query=cast(m.ListPoliciesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_policy_roles(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyRolesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem]:
        "List roles with policy"
        return cast(
            Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicyRoles"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_roles_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyRolesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListPolicyRolesItem]:
        return iterate_pages(
            lambda marker: self.list_policy_roles(
                policy_id,
                query=cast(m.ListPolicyRolesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_policy_service_accounts(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem]:
        "List service accounts with policy"
        return cast(
            Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicyServiceAccounts"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_service_accounts_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListPolicyServiceAccountsItem]:
        return iterate_pages(
            lambda marker: self.list_policy_service_accounts(
                policy_id,
                query=cast(m.ListPolicyServiceAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_regions(
        self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
        "List regions (legacy IAM)"
        return cast(
            Page[m.ListRegionsResponse, m.ListRegionsItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRegions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_role_inline_policies(
        self,
        role_id: str,
        *,
        query: m.ListRoleInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRoleInlinePoliciesResponse, m.ListRoleInlinePoliciesItem]:
        "List a role's inline policies"
        return cast(
            Page[m.ListRoleInlinePoliciesResponse, m.ListRoleInlinePoliciesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRoleInlinePolicies"],
                "page",
                {"role_id": role_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_role_policies(
        self,
        role_id: str,
        *,
        query: m.ListRolePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem]:
        "List role policies"
        return cast(
            Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRolePolicies"],
                "page",
                {"role_id": role_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_roles(
        self, *, query: m.ListRolesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRolesResponse, m.ListRolesItem]:
        "List roles"
        return cast(
            Page[m.ListRolesResponse, m.ListRolesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRoles"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_roles_all(
        self, *, query: m.ListRolesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListRolesItem]:
        return iterate_pages(
            lambda marker: self.list_roles(
                query=cast(m.ListRolesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_sts_sessions(
        self, *, query: m.ListSTSSessionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSTSSessionsResponse, m.ListSTSSessionsItem]:
        "List STS sessions"
        return cast(
            Page[m.ListSTSSessionsResponse, m.ListSTSSessionsItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listSTSSessions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_sts_sessions_all(
        self, *, query: m.ListSTSSessionsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSTSSessionsItem]:
        return iterate_pages(
            lambda marker: self.list_sts_sessions(
                query=cast(m.ListSTSSessionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_service_account_credentials(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountCredentialsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountCredentialsResponse, m.ListServiceAccountCredentialsItem]:
        "List credentials"
        return cast(
            Page[m.ListServiceAccountCredentialsResponse, m.ListServiceAccountCredentialsItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountCredentials"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_service_account_inline_policies(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountInlinePoliciesResponse, m.ListServiceAccountInlinePoliciesItem]:
        "List a service account's inline policies"
        return cast(
            Page[
                m.ListServiceAccountInlinePoliciesResponse, m.ListServiceAccountInlinePoliciesItem
            ],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountInlinePolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_service_account_policies(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem]:
        "List service account policies"
        return cast(
            Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountPolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_service_account_ssh_keys(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListServiceAccountSSHKeysResponse, m.ListServiceAccountSSHKeysItem]:
        "List service-account SSH keys"
        return cast(
            Page[m.ListServiceAccountSSHKeysResponse, m.ListServiceAccountSSHKeysItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountSSHKeys"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_service_accounts(
        self,
        *,
        query: m.ListServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountsResponse, m.ListServiceAccountsItem]:
        "List service accounts"
        return cast(
            Page[m.ListServiceAccountsResponse, m.ListServiceAccountsItem],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccounts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_service_accounts_all(
        self,
        *,
        query: m.ListServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListServiceAccountsItem]:
        return iterate_pages(
            lambda marker: self.list_service_accounts(
                query=cast(m.ListServiceAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def put_role_inline_policy(
        self,
        role_id: str,
        policy_name: str,
        body: m.PutRoleInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutRoleInlinePolicyResponse]:
        "Create or replace a role's inline policy"
        return cast(
            ApiResponse[m.PutRoleInlinePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["putRoleInlinePolicy"],
                "json",
                {"role_id": role_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    def put_service_account_inline_policy(
        self,
        service_account_id: str,
        policy_name: str,
        body: m.PutServiceAccountInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutServiceAccountInlinePolicyResponse]:
        "Create or replace a service account's inline policy"
        return cast(
            ApiResponse[m.PutServiceAccountInlinePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["putServiceAccountInlinePolicy"],
                "json",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    def remove_role_permission_boundary(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a role's permission boundary"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["removeRolePermissionBoundary"],
                "discard",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    def remove_service_account_permission_boundary(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a service account's permission boundary"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["removeServiceAccountPermissionBoundary"],
                "discard",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    def revoke_oauth_token(
        self, body: m.RevokeOAuthTokenBody, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke a bearer token"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["revokeOAuthToken"],
                "discard",
                {},
                body,
                None,
                options,
            ),
        )

    def revoke_sts_session(
        self,
        session_id: str,
        body: m.RevokeSTSSessionBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.RevokeSTSSessionResponse]:
        "Revoke STS session"
        return cast(
            ApiResponse[m.RevokeSTSSessionResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["revokeSTSSession"],
                "json",
                {"session_id": session_id},
                body,
                None,
                options,
            ),
        )

    def set_role_permission_boundary(
        self,
        role_id: str,
        body: m.SetRolePermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a role's permission boundary"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["setRolePermissionBoundary"],
                "discard",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    def set_service_account_permission_boundary(
        self,
        service_account_id: str,
        body: m.SetServiceAccountPermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a service account's permission boundary"
        return cast(
            None,
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["setServiceAccountPermissionBoundary"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    def update_policy(
        self, policy_id: str, body: m.UpdatePolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdatePolicyResponse]:
        "Update policy"
        return cast(
            ApiResponse[m.UpdatePolicyResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updatePolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )

    def update_role(
        self, role_id: str, body: m.UpdateRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateRoleResponse]:
        "Update role"
        return cast(
            ApiResponse[m.UpdateRoleResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updateRole"],
                "json",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    def update_service_account(
        self,
        service_account_id: str,
        body: m.UpdateServiceAccountBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateServiceAccountResponse]:
        "Update service account"
        return cast(
            ApiResponse[m.UpdateServiceAccountResponse],
            self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updateServiceAccount"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )


class AsyncIamService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def assume_role(
        self, body: m.AssumeRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssumeRoleResponse]:
        "Assume role"
        return cast(
            ApiResponse[m.AssumeRoleResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["assumeRole"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def assume_role_with_web_identity(
        self, body: m.AssumeRoleWithWebIdentityBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AssumeRoleWithWebIdentityResponse]:
        "Assume role with web identity"
        return cast(
            ApiResponse[m.AssumeRoleWithWebIdentityResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["assumeRoleWithWebIdentity"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def attach_role_policy(
        self, role_id: str, body: m.AttachRolePolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to role"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["attachRolePolicy"],
                "discard",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    async def attach_service_account_policy(
        self,
        service_account_id: str,
        body: m.AttachServiceAccountPolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Attach policy to service account"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["attachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    async def authorize_oauth_client(
        self, body: m.AuthorizeOAuthClientBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AuthorizeOAuthClientResponse]:
        "Approve a CLI login and issue an authorization code"
        return cast(
            ApiResponse[m.AuthorizeOAuthClientResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["authorizeOAuthClient"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_personal_ssh_key(
        self, body: m.CreatePersonalSSHKeyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePersonalSSHKeyResponse]:
        "Add personal SSH key"
        return cast(
            ApiResponse[m.CreatePersonalSSHKeyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createPersonalSSHKey"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_policy(
        self, body: m.CreatePolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePolicyResponse]:
        "Create policy"
        return cast(
            ApiResponse[m.CreatePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_role(
        self, body: m.CreateRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRoleResponse]:
        "Create role"
        return cast(
            ApiResponse[m.CreateRoleResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createRole"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_service_account(
        self, body: m.CreateServiceAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateServiceAccountResponse]:
        "Create service account"
        return cast(
            ApiResponse[m.CreateServiceAccountResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccount"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_service_account_credential(
        self,
        service_account_id: str,
        body: m.CreateServiceAccountCredentialBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateServiceAccountCredentialResponse]:
        "Create credential"
        return cast(
            ApiResponse[m.CreateServiceAccountCredentialResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccountCredential"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    async def create_service_account_ssh_key(
        self,
        service_account_id: str,
        body: m.CreateServiceAccountSSHKeyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateServiceAccountSSHKeyResponse]:
        "Add service-account SSH key"
        return cast(
            ApiResponse[m.CreateServiceAccountSSHKeyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["createServiceAccountSSHKey"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    async def delete_personal_ssh_key(
        self, ssh_key_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke personal SSH key"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deletePersonalSSHKey"],
                "discard",
                {"ssh_key_id": ssh_key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete policy"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deletePolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_role(self, role_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete role"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteRole"],
                "discard",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_role_inline_policy(
        self, role_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a role's inline policy by name"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteRoleInlinePolicy"],
                "discard",
                {"role_id": role_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_service_account(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete service account"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccount"],
                "discard",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_service_account_credential(
        self, service_account_id: str, credential_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete credential"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountCredential"],
                "discard",
                {"service_account_id": service_account_id, "credential_id": credential_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_service_account_inline_policy(
        self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a service account's inline policy by name"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountInlinePolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_service_account_ssh_key(
        self, service_account_id: str, ssh_key_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke service-account SSH key"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["deleteServiceAccountSSHKey"],
                "discard",
                {"service_account_id": service_account_id, "ssh_key_id": ssh_key_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_role_policy(
        self, role_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from role"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["detachRolePolicy"],
                "discard",
                {"role_id": role_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_service_account_policy(
        self, service_account_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from service account"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["detachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_oauth_token(
        self, body: m.GetOAuthTokenBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetOAuthTokenResponse]:
        "Exchange an access key for a bearer token"
        return cast(
            ApiResponse[m.GetOAuthTokenResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getOAuthToken"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def get_personal_linux_identity(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPersonalLinuxIdentityResponse]:
        "Get personal Linux identity"
        return cast(
            ApiResponse[m.GetPersonalLinuxIdentityResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getPersonalLinuxIdentity"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPolicyResponse]:
        "Get policy"
        return cast(
            ApiResponse[m.GetPolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getPolicy"],
                "json",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_policy_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetPolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetPolicyResource]:
        return cast(
            ApiResponse[m.GetPolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_policy(id, options=options),
                lambda match: self.list_policies(
                    query=cast(
                        m.ListPoliciesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "policy",
            ),
        )

    async def get_role(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRoleResponse]:
        "Get role"
        return cast(
            ApiResponse[m.GetRoleResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRole"],
                "json",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_role_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRoleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRoleResource]:
        return cast(
            ApiResponse[m.GetRoleResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_role(id, options=options),
                lambda match: self.list_roles(
                    query=cast(m.ListRolesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "role",
            ),
        )

    async def get_role_inline_policy(
        self, role_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRoleInlinePolicyResponse]:
        "Get a role's inline policy by name"
        return cast(
            ApiResponse[m.GetRoleInlinePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRoleInlinePolicy"],
                "json",
                {"role_id": role_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def get_role_inline_policy_by_reference(
        self,
        role_id: str,
        reference: str,
        *,
        scope: m.GetRoleInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRoleInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetRoleInlinePolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_role_inline_policy(role_id, id, options=options),
                lambda match: self.list_role_inline_policies(
                    role_id,
                    query=cast(m.ListRoleInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    async def get_role_permission_boundary(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRolePermissionBoundaryResponse]:
        "Get a role's permission boundary"
        return cast(
            ApiResponse[m.GetRolePermissionBoundaryResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getRolePermissionBoundary"],
                "json",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_sts_session(
        self, session_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSTSSessionResponse]:
        "Get STS session"
        return cast(
            ApiResponse[m.GetSTSSessionResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getSTSSession"],
                "json",
                {"session_id": session_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_sts_session_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSTSSessionScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSTSSessionResource]:
        return cast(
            ApiResponse[m.GetSTSSessionResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_sts_session(id, options=options),
                lambda match: self.list_sts_sessions(
                    query=cast(
                        m.ListSTSSessionsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "sts_session",
            ),
        )

    async def get_service_account(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountResponse]:
        "Get service account"
        return cast(
            ApiResponse[m.GetServiceAccountResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccount"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_service_account_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetServiceAccountScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetServiceAccountResource]:
        return cast(
            ApiResponse[m.GetServiceAccountResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_service_account(id, options=options),
                lambda match: self.list_service_accounts(
                    query=cast(
                        m.ListServiceAccountsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "service_account",
            ),
        )

    async def get_service_account_inline_policy(
        self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountInlinePolicyResponse]:
        "Get a service account's inline policy by name"
        return cast(
            ApiResponse[m.GetServiceAccountInlinePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountInlinePolicy"],
                "json",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def get_service_account_inline_policy_by_reference(
        self,
        service_account_id: str,
        reference: str,
        *,
        scope: m.GetServiceAccountInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetServiceAccountInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetServiceAccountInlinePolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_service_account_inline_policy(
                    service_account_id, id, options=options
                ),
                lambda match: self.list_service_account_inline_policies(
                    service_account_id,
                    query=cast(
                        m.ListServiceAccountInlinePoliciesQuery, {**reference_scope(scope), **match}
                    ),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    async def get_service_account_linux_identity(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountLinuxIdentityResponse]:
        "Get serviceaccount Linux identity"
        return cast(
            ApiResponse[m.GetServiceAccountLinuxIdentityResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountLinuxIdentity"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_service_account_permission_boundary(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetServiceAccountPermissionBoundaryResponse]:
        "Get a service account's permission boundary"
        return cast(
            ApiResponse[m.GetServiceAccountPermissionBoundaryResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["getServiceAccountPermissionBoundary"],
                "json",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_personal_ssh_keys(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListPersonalSSHKeysResponse, m.ListPersonalSSHKeysItem]:
        "List personal SSH keys"
        return cast(
            Page[m.ListPersonalSSHKeysResponse, m.ListPersonalSSHKeysItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPersonalSSHKeys"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def list_policies(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
        "List policies"
        return cast(
            Page[m.ListPoliciesResponse, m.ListPoliciesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicies"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_policies_all(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListPoliciesItem]:
        return aiterate_pages(
            lambda marker: self.list_policies(
                query=cast(m.ListPoliciesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_policy_roles(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyRolesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem]:
        "List roles with policy"
        return cast(
            Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicyRoles"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_roles_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyRolesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListPolicyRolesItem]:
        return aiterate_pages(
            lambda marker: self.list_policy_roles(
                policy_id,
                query=cast(m.ListPolicyRolesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_policy_service_accounts(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem]:
        "List service accounts with policy"
        return cast(
            Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listPolicyServiceAccounts"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_service_accounts_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListPolicyServiceAccountsItem]:
        return aiterate_pages(
            lambda marker: self.list_policy_service_accounts(
                policy_id,
                query=cast(m.ListPolicyServiceAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_regions(
        self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
        "List regions (legacy IAM)"
        return cast(
            Page[m.ListRegionsResponse, m.ListRegionsItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRegions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def list_role_inline_policies(
        self,
        role_id: str,
        *,
        query: m.ListRoleInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRoleInlinePoliciesResponse, m.ListRoleInlinePoliciesItem]:
        "List a role's inline policies"
        return cast(
            Page[m.ListRoleInlinePoliciesResponse, m.ListRoleInlinePoliciesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRoleInlinePolicies"],
                "page",
                {"role_id": role_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_role_policies(
        self,
        role_id: str,
        *,
        query: m.ListRolePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem]:
        "List role policies"
        return cast(
            Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRolePolicies"],
                "page",
                {"role_id": role_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_roles(
        self, *, query: m.ListRolesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRolesResponse, m.ListRolesItem]:
        "List roles"
        return cast(
            Page[m.ListRolesResponse, m.ListRolesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listRoles"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_roles_all(
        self, *, query: m.ListRolesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListRolesItem]:
        return aiterate_pages(
            lambda marker: self.list_roles(
                query=cast(m.ListRolesQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_sts_sessions(
        self, *, query: m.ListSTSSessionsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSTSSessionsResponse, m.ListSTSSessionsItem]:
        "List STS sessions"
        return cast(
            Page[m.ListSTSSessionsResponse, m.ListSTSSessionsItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listSTSSessions"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_sts_sessions_all(
        self, *, query: m.ListSTSSessionsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSTSSessionsItem]:
        return aiterate_pages(
            lambda marker: self.list_sts_sessions(
                query=cast(m.ListSTSSessionsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_service_account_credentials(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountCredentialsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountCredentialsResponse, m.ListServiceAccountCredentialsItem]:
        "List credentials"
        return cast(
            Page[m.ListServiceAccountCredentialsResponse, m.ListServiceAccountCredentialsItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountCredentials"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_service_account_inline_policies(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountInlinePoliciesResponse, m.ListServiceAccountInlinePoliciesItem]:
        "List a service account's inline policies"
        return cast(
            Page[
                m.ListServiceAccountInlinePoliciesResponse, m.ListServiceAccountInlinePoliciesItem
            ],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountInlinePolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_service_account_policies(
        self,
        service_account_id: str,
        *,
        query: m.ListServiceAccountPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem]:
        "List service account policies"
        return cast(
            Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountPolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_service_account_ssh_keys(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListServiceAccountSSHKeysResponse, m.ListServiceAccountSSHKeysItem]:
        "List service-account SSH keys"
        return cast(
            Page[m.ListServiceAccountSSHKeysResponse, m.ListServiceAccountSSHKeysItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccountSSHKeys"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_service_accounts(
        self,
        *,
        query: m.ListServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListServiceAccountsResponse, m.ListServiceAccountsItem]:
        "List service accounts"
        return cast(
            Page[m.ListServiceAccountsResponse, m.ListServiceAccountsItem],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["listServiceAccounts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_service_accounts_all(
        self,
        *,
        query: m.ListServiceAccountsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListServiceAccountsItem]:
        return aiterate_pages(
            lambda marker: self.list_service_accounts(
                query=cast(m.ListServiceAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def put_role_inline_policy(
        self,
        role_id: str,
        policy_name: str,
        body: m.PutRoleInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutRoleInlinePolicyResponse]:
        "Create or replace a role's inline policy"
        return cast(
            ApiResponse[m.PutRoleInlinePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["putRoleInlinePolicy"],
                "json",
                {"role_id": role_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    async def put_service_account_inline_policy(
        self,
        service_account_id: str,
        policy_name: str,
        body: m.PutServiceAccountInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutServiceAccountInlinePolicyResponse]:
        "Create or replace a service account's inline policy"
        return cast(
            ApiResponse[m.PutServiceAccountInlinePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["putServiceAccountInlinePolicy"],
                "json",
                {"service_account_id": service_account_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    async def remove_role_permission_boundary(
        self, role_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a role's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["removeRolePermissionBoundary"],
                "discard",
                {"role_id": role_id},
                UNSET,
                None,
                options,
            ),
        )

    async def remove_service_account_permission_boundary(
        self, service_account_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a service account's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["removeServiceAccountPermissionBoundary"],
                "discard",
                {"service_account_id": service_account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def revoke_oauth_token(
        self, body: m.RevokeOAuthTokenBody, *, options: RequestOptions | None = None
    ) -> None:
        "Revoke a bearer token"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["revokeOAuthToken"],
                "discard",
                {},
                body,
                None,
                options,
            ),
        )

    async def revoke_sts_session(
        self,
        session_id: str,
        body: m.RevokeSTSSessionBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.RevokeSTSSessionResponse]:
        "Revoke STS session"
        return cast(
            ApiResponse[m.RevokeSTSSessionResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["revokeSTSSession"],
                "json",
                {"session_id": session_id},
                body,
                None,
                options,
            ),
        )

    async def set_role_permission_boundary(
        self,
        role_id: str,
        body: m.SetRolePermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a role's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["setRolePermissionBoundary"],
                "discard",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    async def set_service_account_permission_boundary(
        self,
        service_account_id: str,
        body: m.SetServiceAccountPermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a service account's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["setServiceAccountPermissionBoundary"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    async def update_policy(
        self, policy_id: str, body: m.UpdatePolicyBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdatePolicyResponse]:
        "Update policy"
        return cast(
            ApiResponse[m.UpdatePolicyResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updatePolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )

    async def update_role(
        self, role_id: str, body: m.UpdateRoleBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateRoleResponse]:
        "Update role"
        return cast(
            ApiResponse[m.UpdateRoleResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updateRole"],
                "json",
                {"role_id": role_id},
                body,
                None,
                options,
            ),
        )

    async def update_service_account(
        self,
        service_account_id: str,
        body: m.UpdateServiceAccountBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateServiceAccountResponse]:
        "Update service account"
        return cast(
            ApiResponse[m.UpdateServiceAccountResponse],
            await self._transport.request(
                "iam",
                "https://iam.basaltic.sh",
                _OPS["updateServiceAccount"],
                "json",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )
