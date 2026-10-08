"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import workspace as m
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
    "addUser": Operation(
        id="addUser",
        method="POST",
        path="/v1/users",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "addUserToGroup": Operation(
        id="addUserToGroup",
        method="POST",
        path="/v1/users/{user_id}/groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "assignAccountRole": Operation(
        id="assignAccountRole",
        method="POST",
        path="/v1/accounts/{account_id}/role-assignments",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachGroupPolicy": Operation(
        id="attachGroupPolicy",
        method="POST",
        path="/v1/groups/{group_id}/policies",
        authenticated=True,
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
    "attachUserPolicy": Operation(
        id="attachUserPolicy",
        method="POST",
        path="/v1/users/{user_id}/policies",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "cancelInvitation": Operation(
        id="cancelInvitation",
        method="DELETE",
        path="/v1/invitations/{invitation_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "createAccount": Operation(
        id="createAccount",
        method="POST",
        path="/v1/accounts",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createGroup": Operation(
        id="createGroup",
        method="POST",
        path="/v1/groups",
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
    "deleteAccount": Operation(
        id="deleteAccount",
        method="DELETE",
        path="/v1/accounts/{account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteGroup": Operation(
        id="deleteGroup",
        method="DELETE",
        path="/v1/groups/{group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteGroupInlinePolicy": Operation(
        id="deleteGroupInlinePolicy",
        method="DELETE",
        path="/v1/groups/{group_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteOrganization": Operation(
        id="deleteOrganization",
        method="DELETE",
        path="/v1/organizations/{organization_id}",
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
    "deleteUserInlinePolicy": Operation(
        id="deleteUserInlinePolicy",
        method="DELETE",
        path="/v1/users/{user_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachGroupPolicy": Operation(
        id="detachGroupPolicy",
        method="DELETE",
        path="/v1/groups/{group_id}/policies/{policy_id}",
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
    "detachUserPolicy": Operation(
        id="detachUserPolicy",
        method="DELETE",
        path="/v1/users/{user_id}/policies/{policy_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getAccount": Operation(
        id="getAccount",
        method="GET",
        path="/v1/accounts/{account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getAccountResources": Operation(
        id="getAccountResources",
        method="GET",
        path="/v1/accounts/{account_id}/resources",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getGroup": Operation(
        id="getGroup",
        method="GET",
        path="/v1/groups/{group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getGroupInlinePolicy": Operation(
        id="getGroupInlinePolicy",
        method="GET",
        path="/v1/groups/{group_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInvitation": Operation(
        id="getInvitation",
        method="GET",
        path="/v1/invitations/{invitation_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getOrganization": Operation(
        id="getOrganization",
        method="GET",
        path="/v1/organizations/{organization_id}",
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
    "getUser": Operation(
        id="getUser",
        method="GET",
        path="/v1/users/{user_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getUserInlinePolicy": Operation(
        id="getUserInlinePolicy",
        method="GET",
        path="/v1/users/{user_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getUserPermissionBoundary": Operation(
        id="getUserPermissionBoundary",
        method="GET",
        path="/v1/users/{user_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listAccountRoleAssignments": Operation(
        id="listAccountRoleAssignments",
        method="GET",
        path="/v1/accounts/{account_id}/role-assignments",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="role_assignments",
    ),
    "listAccountRoles": Operation(
        id="listAccountRoles",
        method="GET",
        path="/v1/account-roles",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="account_roles",
    ),
    "listAccounts": Operation(
        id="listAccounts",
        method="GET",
        path="/v1/accounts",
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
        itemsKey="accounts",
    ),
    "listGroupInlinePolicies": Operation(
        id="listGroupInlinePolicies",
        method="GET",
        path="/v1/groups/{group_id}/inline-policies",
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
    "listGroupPolicies": Operation(
        id="listGroupPolicies",
        method="GET",
        path="/v1/groups/{group_id}/policies",
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
    "listGroupUsers": Operation(
        id="listGroupUsers",
        method="GET",
        path="/v1/groups/{group_id}/users",
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
        itemsKey="users",
    ),
    "listGroups": Operation(
        id="listGroups",
        method="GET",
        path="/v1/groups",
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
        itemsKey="groups",
    ),
    "listInvitations": Operation(
        id="listInvitations",
        method="GET",
        path="/v1/invitations",
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
        itemsKey="invitations",
    ),
    "listOrganizations": Operation(
        id="listOrganizations",
        method="GET",
        path="/v1/organizations",
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
        itemsKey="organizations",
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
    "listPolicyGroups": Operation(
        id="listPolicyGroups",
        method="GET",
        path="/v1/policies/{policy_id}/groups",
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
        itemsKey="groups",
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
    "listPolicyUsers": Operation(
        id="listPolicyUsers",
        method="GET",
        path="/v1/policies/{policy_id}/users",
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
        itemsKey="users",
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
    "listUserGroups": Operation(
        id="listUserGroups",
        method="GET",
        path="/v1/users/{user_id}/groups",
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
        itemsKey="groups",
    ),
    "listUserInlinePolicies": Operation(
        id="listUserInlinePolicies",
        method="GET",
        path="/v1/users/{user_id}/inline-policies",
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
    "listUserPolicies": Operation(
        id="listUserPolicies",
        method="GET",
        path="/v1/users/{user_id}/policies",
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
    "listUsers": Operation(
        id="listUsers",
        method="GET",
        path="/v1/users",
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
        itemsKey="users",
    ),
    "putGroupInlinePolicy": Operation(
        id="putGroupInlinePolicy",
        method="PUT",
        path="/v1/groups/{group_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "putUserInlinePolicy": Operation(
        id="putUserInlinePolicy",
        method="PUT",
        path="/v1/users/{user_id}/inline-policies/{policy_name}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "removeAccountRoleAssignment": Operation(
        id="removeAccountRoleAssignment",
        method="DELETE",
        path="/v1/accounts/{account_id}/role-assignments/{assignment_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "removeUser": Operation(
        id="removeUser",
        method="DELETE",
        path="/v1/users/{user_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "removeUserFromGroup": Operation(
        id="removeUserFromGroup",
        method="DELETE",
        path="/v1/users/{user_id}/groups/{group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "removeUserPermissionBoundary": Operation(
        id="removeUserPermissionBoundary",
        method="DELETE",
        path="/v1/users/{user_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "setUserPermissionBoundary": Operation(
        id="setUserPermissionBoundary",
        method="PUT",
        path="/v1/users/{user_id}/permission-boundary",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateAccount": Operation(
        id="updateAccount",
        method="PATCH",
        path="/v1/accounts/{account_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateGroup": Operation(
        id="updateGroup",
        method="PATCH",
        path="/v1/groups/{group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateOrganization": Operation(
        id="updateOrganization",
        method="PATCH",
        path="/v1/organizations/{organization_id}",
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
}


class WorkspaceService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def add_user(
        self, body: m.AddUserBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AddUserResponse]:
        "Add user to organization"
        return cast(
            ApiResponse[m.AddUserResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["addUser"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def add_user_to_group(
        self, user_id: str, body: m.AddUserToGroupBody, *, options: RequestOptions | None = None
    ) -> None:
        "Add user to group"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["addUserToGroup"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    def assign_account_role(
        self,
        account_id: str,
        body: m.AssignAccountRoleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AssignAccountRoleResponse]:
        "Assign account role"
        return cast(
            ApiResponse[m.AssignAccountRoleResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["assignAccountRole"],
                "json",
                {"account_id": account_id},
                body,
                None,
                options,
            ),
        )

    def attach_group_policy(
        self, group_id: str, body: m.AttachGroupPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to group"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachGroupPolicy"],
                "discard",
                {"group_id": group_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    def attach_user_policy(
        self, user_id: str, body: m.AttachUserPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to user"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachUserPolicy"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    def cancel_invitation(
        self, invitation_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Cancel invitation"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["cancelInvitation"],
                "discard",
                {"invitation_id": invitation_id},
                UNSET,
                None,
                options,
            ),
        )

    def create_account(
        self, body: m.CreateAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateAccountResponse]:
        "Create account"
        return cast(
            ApiResponse[m.CreateAccountResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createAccount"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_group(
        self, body: m.CreateGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateGroupResponse]:
        "Create group"
        return cast(
            ApiResponse[m.CreateGroupResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createGroup"],
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_account(self, account_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete account"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteAccount"],
                "discard",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_group(self, group_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete group"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteGroup"],
                "discard",
                {"group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_group_inline_policy(
        self, group_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a group's inline policy by name"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteGroupInlinePolicy"],
                "discard",
                {"group_id": group_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def delete_organization(
        self, organization_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete organization"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteOrganization"],
                "discard",
                {"organization_id": organization_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deletePolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_user_inline_policy(
        self, user_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a user's inline policy by name"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteUserInlinePolicy"],
                "discard",
                {"user_id": user_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def detach_group_policy(
        self, group_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from group"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachGroupPolicy"],
                "discard",
                {"group_id": group_id, "policy_id": policy_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_user_policy(
        self, user_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from user"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachUserPolicy"],
                "discard",
                {"user_id": user_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_account(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAccountResponse]:
        "Get account"
        return cast(
            ApiResponse[m.GetAccountResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getAccount"],
                "json",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_account_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAccountScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAccountResource]:
        return cast(
            ApiResponse[m.GetAccountResource],
            resolve_reference(
                reference,
                lambda id: self.get_account(id, options=options),
                lambda match: self.list_accounts(
                    query=cast(
                        m.ListAccountsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "account",
            ),
        )

    def get_account_resources(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAccountResourcesResponse]:
        "Check account resource presence"
        return cast(
            ApiResponse[m.GetAccountResourcesResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getAccountResources"],
                "json",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_group(
        self, group_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetGroupResponse]:
        "Get group"
        return cast(
            ApiResponse[m.GetGroupResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getGroup"],
                "json",
                {"group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetGroupResource]:
        return cast(
            ApiResponse[m.GetGroupResource],
            resolve_reference(
                reference,
                lambda id: self.get_group(id, options=options),
                lambda match: self.list_groups(
                    query=cast(m.ListGroupsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "group",
            ),
        )

    def get_group_inline_policy(
        self, group_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetGroupInlinePolicyResponse]:
        "Get a group's inline policy by name"
        return cast(
            ApiResponse[m.GetGroupInlinePolicyResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getGroupInlinePolicy"],
                "json",
                {"group_id": group_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def get_group_inline_policy_by_reference(
        self,
        group_id: str,
        reference: str,
        *,
        scope: m.GetGroupInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetGroupInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetGroupInlinePolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_group_inline_policy(group_id, id, options=options),
                lambda match: self.list_group_inline_policies(
                    group_id,
                    query=cast(m.ListGroupInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    def get_invitation(
        self, invitation_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInvitationResponse]:
        "Get invitation"
        return cast(
            ApiResponse[m.GetInvitationResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getInvitation"],
                "json",
                {"invitation_id": invitation_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_invitation_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInvitationScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInvitationResource]:
        return cast(
            ApiResponse[m.GetInvitationResource],
            resolve_reference(
                reference,
                lambda id: self.get_invitation(id, options=options),
                lambda match: self.list_invitations(
                    query=cast(
                        m.ListInvitationsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "invitation",
            ),
        )

    def get_organization(
        self, organization_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetOrganizationResponse]:
        "Get organization"
        return cast(
            ApiResponse[m.GetOrganizationResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getOrganization"],
                "json",
                {"organization_id": organization_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_organization_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetOrganizationScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetOrganizationResource]:
        return cast(
            ApiResponse[m.GetOrganizationResource],
            resolve_reference(
                reference,
                lambda id: self.get_organization(id, options=options),
                lambda match: self.list_organizations(
                    query=cast(
                        m.ListOrganizationsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "organization",
            ),
        )

    def get_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPolicyResponse]:
        "Get policy"
        return cast(
            ApiResponse[m.GetPolicyResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
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

    def get_user(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserResponse]:
        "Get user"
        return cast(
            ApiResponse[m.GetUserResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUser"],
                "json",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_user_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetUserScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetUserResource]:
        return cast(
            ApiResponse[m.GetUserResource],
            resolve_reference(
                reference,
                lambda id: self.get_user(id, options=options),
                lambda match: self.list_users(
                    query=cast(m.ListUsersQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "user",
            ),
        )

    def get_user_inline_policy(
        self, user_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserInlinePolicyResponse]:
        "Get a user's inline policy by name"
        return cast(
            ApiResponse[m.GetUserInlinePolicyResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUserInlinePolicy"],
                "json",
                {"user_id": user_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    def get_user_inline_policy_by_reference(
        self,
        user_id: str,
        reference: str,
        *,
        scope: m.GetUserInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetUserInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetUserInlinePolicyResource],
            resolve_reference(
                reference,
                lambda id: self.get_user_inline_policy(user_id, id, options=options),
                lambda match: self.list_user_inline_policies(
                    user_id,
                    query=cast(m.ListUserInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    def get_user_permission_boundary(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserPermissionBoundaryResponse]:
        "Get a user's permission boundary"
        return cast(
            ApiResponse[m.GetUserPermissionBoundaryResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUserPermissionBoundary"],
                "json",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_account_role_assignments(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListAccountRoleAssignmentsResponse, m.ListAccountRoleAssignmentsItem]:
        "List account role assignments"
        return cast(
            Page[m.ListAccountRoleAssignmentsResponse, m.ListAccountRoleAssignmentsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccountRoleAssignments"],
                "page",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_account_roles(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListAccountRolesResponse, m.ListAccountRolesItem]:
        "List assigned account roles"
        return cast(
            Page[m.ListAccountRolesResponse, m.ListAccountRolesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccountRoles"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def list_accounts(
        self, *, query: m.ListAccountsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAccountsResponse, m.ListAccountsItem]:
        "List accounts"
        return cast(
            Page[m.ListAccountsResponse, m.ListAccountsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccounts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_accounts_all(
        self, *, query: m.ListAccountsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListAccountsItem]:
        return iterate_pages(
            lambda marker: self.list_accounts(
                query=cast(m.ListAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_group_inline_policies(
        self,
        group_id: str,
        *,
        query: m.ListGroupInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupInlinePoliciesResponse, m.ListGroupInlinePoliciesItem]:
        "List a group's inline policies"
        return cast(
            Page[m.ListGroupInlinePoliciesResponse, m.ListGroupInlinePoliciesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupInlinePolicies"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_group_policies(
        self,
        group_id: str,
        *,
        query: m.ListGroupPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupPoliciesResponse, m.ListGroupPoliciesItem]:
        "List group policies"
        return cast(
            Page[m.ListGroupPoliciesResponse, m.ListGroupPoliciesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupPolicies"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_group_users(
        self,
        group_id: str,
        *,
        query: m.ListGroupUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupUsersResponse, m.ListGroupUsersItem]:
        "List group users"
        return cast(
            Page[m.ListGroupUsersResponse, m.ListGroupUsersItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupUsers"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_group_users_all(
        self,
        group_id: str,
        *,
        query: m.ListGroupUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListGroupUsersItem]:
        return iterate_pages(
            lambda marker: self.list_group_users(
                group_id,
                query=cast(m.ListGroupUsersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_groups(
        self, *, query: m.ListGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListGroupsResponse, m.ListGroupsItem]:
        "List groups"
        return cast(
            Page[m.ListGroupsResponse, m.ListGroupsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_groups_all(
        self, *, query: m.ListGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListGroupsItem]:
        return iterate_pages(
            lambda marker: self.list_groups(
                query=cast(m.ListGroupsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_invitations(
        self, *, query: m.ListInvitationsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInvitationsResponse, m.ListInvitationsItem]:
        "List invitations"
        return cast(
            Page[m.ListInvitationsResponse, m.ListInvitationsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listInvitations"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_invitations_all(
        self, *, query: m.ListInvitationsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListInvitationsItem]:
        return iterate_pages(
            lambda marker: self.list_invitations(
                query=cast(m.ListInvitationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_organizations(
        self,
        *,
        query: m.ListOrganizationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListOrganizationsResponse, m.ListOrganizationsItem]:
        "List organizations"
        return cast(
            Page[m.ListOrganizationsResponse, m.ListOrganizationsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listOrganizations"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_organizations_all(
        self,
        *,
        query: m.ListOrganizationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListOrganizationsItem]:
        return iterate_pages(
            lambda marker: self.list_organizations(
                query=cast(m.ListOrganizationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_policies(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
        "List policies"
        return cast(
            Page[m.ListPoliciesResponse, m.ListPoliciesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
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

    def list_policy_groups(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyGroupsResponse, m.ListPolicyGroupsItem]:
        "List groups with policy"
        return cast(
            Page[m.ListPolicyGroupsResponse, m.ListPolicyGroupsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listPolicyGroups"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_groups_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListPolicyGroupsItem]:
        return iterate_pages(
            lambda marker: self.list_policy_groups(
                policy_id,
                query=cast(m.ListPolicyGroupsQuery, {**(query or {}), "marker": marker}),
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
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

    def list_policy_users(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyUsersResponse, m.ListPolicyUsersItem]:
        "List users with policy"
        return cast(
            Page[m.ListPolicyUsersResponse, m.ListPolicyUsersItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listPolicyUsers"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_users_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListPolicyUsersItem]:
        return iterate_pages(
            lambda marker: self.list_policy_users(
                policy_id,
                query=cast(m.ListPolicyUsersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listRolePolicies"],
                "page",
                {"role_id": role_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listServiceAccountPolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_user_groups(
        self,
        user_id: str,
        *,
        query: m.ListUserGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserGroupsResponse, m.ListUserGroupsItem]:
        "List user groups"
        return cast(
            Page[m.ListUserGroupsResponse, m.ListUserGroupsItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserGroups"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_user_inline_policies(
        self,
        user_id: str,
        *,
        query: m.ListUserInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserInlinePoliciesResponse, m.ListUserInlinePoliciesItem]:
        "List a user's inline policies"
        return cast(
            Page[m.ListUserInlinePoliciesResponse, m.ListUserInlinePoliciesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserInlinePolicies"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_user_policies(
        self,
        user_id: str,
        *,
        query: m.ListUserPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserPoliciesResponse, m.ListUserPoliciesItem]:
        "List user policies"
        return cast(
            Page[m.ListUserPoliciesResponse, m.ListUserPoliciesItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserPolicies"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_users(
        self, *, query: m.ListUsersQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListUsersResponse, m.ListUsersItem]:
        "List users"
        return cast(
            Page[m.ListUsersResponse, m.ListUsersItem],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUsers"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_users_all(
        self, *, query: m.ListUsersQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListUsersItem]:
        return iterate_pages(
            lambda marker: self.list_users(
                query=cast(m.ListUsersQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def put_group_inline_policy(
        self,
        group_id: str,
        policy_name: str,
        body: m.PutGroupInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutGroupInlinePolicyResponse]:
        "Create or replace a group's inline policy"
        return cast(
            ApiResponse[m.PutGroupInlinePolicyResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["putGroupInlinePolicy"],
                "json",
                {"group_id": group_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    def put_user_inline_policy(
        self,
        user_id: str,
        policy_name: str,
        body: m.PutUserInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutUserInlinePolicyResponse]:
        "Create or replace a user's inline policy"
        return cast(
            ApiResponse[m.PutUserInlinePolicyResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["putUserInlinePolicy"],
                "json",
                {"user_id": user_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    def remove_account_role_assignment(
        self, account_id: str, assignment_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove account role assignment"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeAccountRoleAssignment"],
                "discard",
                {"account_id": account_id, "assignment_id": assignment_id},
                UNSET,
                None,
                options,
            ),
        )

    def remove_user(self, user_id: str, *, options: RequestOptions | None = None) -> None:
        "Remove user from organization"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUser"],
                "discard",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    def remove_user_from_group(
        self, user_id: str, group_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove user from group"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUserFromGroup"],
                "discard",
                {"user_id": user_id, "group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    def remove_user_permission_boundary(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a user's permission boundary"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUserPermissionBoundary"],
                "discard",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    def set_user_permission_boundary(
        self,
        user_id: str,
        body: m.SetUserPermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a user's permission boundary"
        return cast(
            None,
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["setUserPermissionBoundary"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    def update_account(
        self, account_id: str, body: m.UpdateAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateAccountResponse]:
        "Update account"
        return cast(
            ApiResponse[m.UpdateAccountResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateAccount"],
                "json",
                {"account_id": account_id},
                body,
                None,
                options,
            ),
        )

    def update_group(
        self, group_id: str, body: m.UpdateGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateGroupResponse]:
        "Update group"
        return cast(
            ApiResponse[m.UpdateGroupResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateGroup"],
                "json",
                {"group_id": group_id},
                body,
                None,
                options,
            ),
        )

    def update_organization(
        self,
        organization_id: str,
        body: m.UpdateOrganizationBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateOrganizationResponse]:
        "Update organization"
        return cast(
            ApiResponse[m.UpdateOrganizationResponse],
            self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateOrganization"],
                "json",
                {"organization_id": organization_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updatePolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )


class AsyncWorkspaceService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def add_user(
        self, body: m.AddUserBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AddUserResponse]:
        "Add user to organization"
        return cast(
            ApiResponse[m.AddUserResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["addUser"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def add_user_to_group(
        self, user_id: str, body: m.AddUserToGroupBody, *, options: RequestOptions | None = None
    ) -> None:
        "Add user to group"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["addUserToGroup"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    async def assign_account_role(
        self,
        account_id: str,
        body: m.AssignAccountRoleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AssignAccountRoleResponse]:
        "Assign account role"
        return cast(
            ApiResponse[m.AssignAccountRoleResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["assignAccountRole"],
                "json",
                {"account_id": account_id},
                body,
                None,
                options,
            ),
        )

    async def attach_group_policy(
        self, group_id: str, body: m.AttachGroupPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to group"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachGroupPolicy"],
                "discard",
                {"group_id": group_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id},
                body,
                None,
                options,
            ),
        )

    async def attach_user_policy(
        self, user_id: str, body: m.AttachUserPolicyBody, *, options: RequestOptions | None = None
    ) -> None:
        "Attach policy to user"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["attachUserPolicy"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    async def cancel_invitation(
        self, invitation_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Cancel invitation"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["cancelInvitation"],
                "discard",
                {"invitation_id": invitation_id},
                UNSET,
                None,
                options,
            ),
        )

    async def create_account(
        self, body: m.CreateAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateAccountResponse]:
        "Create account"
        return cast(
            ApiResponse[m.CreateAccountResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createAccount"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_group(
        self, body: m.CreateGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateGroupResponse]:
        "Create group"
        return cast(
            ApiResponse[m.CreateGroupResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createGroup"],
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["createPolicy"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_account(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete account"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteAccount"],
                "discard",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_group(self, group_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete group"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteGroup"],
                "discard",
                {"group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_group_inline_policy(
        self, group_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a group's inline policy by name"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteGroupInlinePolicy"],
                "discard",
                {"group_id": group_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_organization(
        self, organization_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete organization"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteOrganization"],
                "discard",
                {"organization_id": organization_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deletePolicy"],
                "discard",
                {"policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_user_inline_policy(
        self, user_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a user's inline policy by name"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["deleteUserInlinePolicy"],
                "discard",
                {"user_id": user_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_group_policy(
        self, group_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from group"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachGroupPolicy"],
                "discard",
                {"group_id": group_id, "policy_id": policy_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachServiceAccountPolicy"],
                "discard",
                {"service_account_id": service_account_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_user_policy(
        self, user_id: str, policy_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach policy from user"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["detachUserPolicy"],
                "discard",
                {"user_id": user_id, "policy_id": policy_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_account(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAccountResponse]:
        "Get account"
        return cast(
            ApiResponse[m.GetAccountResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getAccount"],
                "json",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_account_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAccountScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAccountResource]:
        return cast(
            ApiResponse[m.GetAccountResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_account(id, options=options),
                lambda match: self.list_accounts(
                    query=cast(
                        m.ListAccountsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "account",
            ),
        )

    async def get_account_resources(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAccountResourcesResponse]:
        "Check account resource presence"
        return cast(
            ApiResponse[m.GetAccountResourcesResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getAccountResources"],
                "json",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_group(
        self, group_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetGroupResponse]:
        "Get group"
        return cast(
            ApiResponse[m.GetGroupResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getGroup"],
                "json",
                {"group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetGroupResource]:
        return cast(
            ApiResponse[m.GetGroupResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_group(id, options=options),
                lambda match: self.list_groups(
                    query=cast(m.ListGroupsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "group",
            ),
        )

    async def get_group_inline_policy(
        self, group_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetGroupInlinePolicyResponse]:
        "Get a group's inline policy by name"
        return cast(
            ApiResponse[m.GetGroupInlinePolicyResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getGroupInlinePolicy"],
                "json",
                {"group_id": group_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def get_group_inline_policy_by_reference(
        self,
        group_id: str,
        reference: str,
        *,
        scope: m.GetGroupInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetGroupInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetGroupInlinePolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_group_inline_policy(group_id, id, options=options),
                lambda match: self.list_group_inline_policies(
                    group_id,
                    query=cast(m.ListGroupInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    async def get_invitation(
        self, invitation_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInvitationResponse]:
        "Get invitation"
        return cast(
            ApiResponse[m.GetInvitationResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getInvitation"],
                "json",
                {"invitation_id": invitation_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_invitation_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInvitationScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInvitationResource]:
        return cast(
            ApiResponse[m.GetInvitationResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_invitation(id, options=options),
                lambda match: self.list_invitations(
                    query=cast(
                        m.ListInvitationsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "invitation",
            ),
        )

    async def get_organization(
        self, organization_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetOrganizationResponse]:
        "Get organization"
        return cast(
            ApiResponse[m.GetOrganizationResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getOrganization"],
                "json",
                {"organization_id": organization_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_organization_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetOrganizationScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetOrganizationResource]:
        return cast(
            ApiResponse[m.GetOrganizationResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_organization(id, options=options),
                lambda match: self.list_organizations(
                    query=cast(
                        m.ListOrganizationsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "organization",
            ),
        )

    async def get_policy(
        self, policy_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetPolicyResponse]:
        "Get policy"
        return cast(
            ApiResponse[m.GetPolicyResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
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

    async def get_user(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserResponse]:
        "Get user"
        return cast(
            ApiResponse[m.GetUserResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUser"],
                "json",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_user_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetUserScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetUserResource]:
        return cast(
            ApiResponse[m.GetUserResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_user(id, options=options),
                lambda match: self.list_users(
                    query=cast(m.ListUsersQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "user",
            ),
        )

    async def get_user_inline_policy(
        self, user_id: str, policy_name: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserInlinePolicyResponse]:
        "Get a user's inline policy by name"
        return cast(
            ApiResponse[m.GetUserInlinePolicyResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUserInlinePolicy"],
                "json",
                {"user_id": user_id, "policy_name": policy_name},
                UNSET,
                None,
                options,
            ),
        )

    async def get_user_inline_policy_by_reference(
        self,
        user_id: str,
        reference: str,
        *,
        scope: m.GetUserInlinePolicyScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetUserInlinePolicyResource]:
        return cast(
            ApiResponse[m.GetUserInlinePolicyResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_user_inline_policy(user_id, id, options=options),
                lambda match: self.list_user_inline_policies(
                    user_id,
                    query=cast(m.ListUserInlinePoliciesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "inline_policy",
            ),
        )

    async def get_user_permission_boundary(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetUserPermissionBoundaryResponse]:
        "Get a user's permission boundary"
        return cast(
            ApiResponse[m.GetUserPermissionBoundaryResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["getUserPermissionBoundary"],
                "json",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_account_role_assignments(
        self, account_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListAccountRoleAssignmentsResponse, m.ListAccountRoleAssignmentsItem]:
        "List account role assignments"
        return cast(
            Page[m.ListAccountRoleAssignmentsResponse, m.ListAccountRoleAssignmentsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccountRoleAssignments"],
                "page",
                {"account_id": account_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_account_roles(
        self, *, options: RequestOptions | None = None
    ) -> Page[m.ListAccountRolesResponse, m.ListAccountRolesItem]:
        "List assigned account roles"
        return cast(
            Page[m.ListAccountRolesResponse, m.ListAccountRolesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccountRoles"],
                "page",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def list_accounts(
        self, *, query: m.ListAccountsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAccountsResponse, m.ListAccountsItem]:
        "List accounts"
        return cast(
            Page[m.ListAccountsResponse, m.ListAccountsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listAccounts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_accounts_all(
        self, *, query: m.ListAccountsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListAccountsItem]:
        return aiterate_pages(
            lambda marker: self.list_accounts(
                query=cast(m.ListAccountsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_group_inline_policies(
        self,
        group_id: str,
        *,
        query: m.ListGroupInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupInlinePoliciesResponse, m.ListGroupInlinePoliciesItem]:
        "List a group's inline policies"
        return cast(
            Page[m.ListGroupInlinePoliciesResponse, m.ListGroupInlinePoliciesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupInlinePolicies"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_group_policies(
        self,
        group_id: str,
        *,
        query: m.ListGroupPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupPoliciesResponse, m.ListGroupPoliciesItem]:
        "List group policies"
        return cast(
            Page[m.ListGroupPoliciesResponse, m.ListGroupPoliciesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupPolicies"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_group_users(
        self,
        group_id: str,
        *,
        query: m.ListGroupUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListGroupUsersResponse, m.ListGroupUsersItem]:
        "List group users"
        return cast(
            Page[m.ListGroupUsersResponse, m.ListGroupUsersItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroupUsers"],
                "page",
                {"group_id": group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_group_users_all(
        self,
        group_id: str,
        *,
        query: m.ListGroupUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListGroupUsersItem]:
        return aiterate_pages(
            lambda marker: self.list_group_users(
                group_id,
                query=cast(m.ListGroupUsersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_groups(
        self, *, query: m.ListGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListGroupsResponse, m.ListGroupsItem]:
        "List groups"
        return cast(
            Page[m.ListGroupsResponse, m.ListGroupsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_groups_all(
        self, *, query: m.ListGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListGroupsItem]:
        return aiterate_pages(
            lambda marker: self.list_groups(
                query=cast(m.ListGroupsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_invitations(
        self, *, query: m.ListInvitationsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInvitationsResponse, m.ListInvitationsItem]:
        "List invitations"
        return cast(
            Page[m.ListInvitationsResponse, m.ListInvitationsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listInvitations"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_invitations_all(
        self, *, query: m.ListInvitationsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListInvitationsItem]:
        return aiterate_pages(
            lambda marker: self.list_invitations(
                query=cast(m.ListInvitationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_organizations(
        self,
        *,
        query: m.ListOrganizationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListOrganizationsResponse, m.ListOrganizationsItem]:
        "List organizations"
        return cast(
            Page[m.ListOrganizationsResponse, m.ListOrganizationsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listOrganizations"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_organizations_all(
        self,
        *,
        query: m.ListOrganizationsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListOrganizationsItem]:
        return aiterate_pages(
            lambda marker: self.list_organizations(
                query=cast(m.ListOrganizationsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_policies(
        self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
        "List policies"
        return cast(
            Page[m.ListPoliciesResponse, m.ListPoliciesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
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

    async def list_policy_groups(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyGroupsResponse, m.ListPolicyGroupsItem]:
        "List groups with policy"
        return cast(
            Page[m.ListPolicyGroupsResponse, m.ListPolicyGroupsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listPolicyGroups"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_groups_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListPolicyGroupsItem]:
        return aiterate_pages(
            lambda marker: self.list_policy_groups(
                policy_id,
                query=cast(m.ListPolicyGroupsQuery, {**(query or {}), "marker": marker}),
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
                "workspace",
                "https://workspace.basaltic.sh",
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
                "workspace",
                "https://workspace.basaltic.sh",
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

    async def list_policy_users(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListPolicyUsersResponse, m.ListPolicyUsersItem]:
        "List users with policy"
        return cast(
            Page[m.ListPolicyUsersResponse, m.ListPolicyUsersItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listPolicyUsers"],
                "page",
                {"policy_id": policy_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_policy_users_all(
        self,
        policy_id: str,
        *,
        query: m.ListPolicyUsersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListPolicyUsersItem]:
        return aiterate_pages(
            lambda marker: self.list_policy_users(
                policy_id,
                query=cast(m.ListPolicyUsersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listRolePolicies"],
                "page",
                {"role_id": role_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listServiceAccountPolicies"],
                "page",
                {"service_account_id": service_account_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_user_groups(
        self,
        user_id: str,
        *,
        query: m.ListUserGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserGroupsResponse, m.ListUserGroupsItem]:
        "List user groups"
        return cast(
            Page[m.ListUserGroupsResponse, m.ListUserGroupsItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserGroups"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_user_inline_policies(
        self,
        user_id: str,
        *,
        query: m.ListUserInlinePoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserInlinePoliciesResponse, m.ListUserInlinePoliciesItem]:
        "List a user's inline policies"
        return cast(
            Page[m.ListUserInlinePoliciesResponse, m.ListUserInlinePoliciesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserInlinePolicies"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_user_policies(
        self,
        user_id: str,
        *,
        query: m.ListUserPoliciesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListUserPoliciesResponse, m.ListUserPoliciesItem]:
        "List user policies"
        return cast(
            Page[m.ListUserPoliciesResponse, m.ListUserPoliciesItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUserPolicies"],
                "page",
                {"user_id": user_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_users(
        self, *, query: m.ListUsersQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListUsersResponse, m.ListUsersItem]:
        "List users"
        return cast(
            Page[m.ListUsersResponse, m.ListUsersItem],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["listUsers"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_users_all(
        self, *, query: m.ListUsersQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListUsersItem]:
        return aiterate_pages(
            lambda marker: self.list_users(
                query=cast(m.ListUsersQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def put_group_inline_policy(
        self,
        group_id: str,
        policy_name: str,
        body: m.PutGroupInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutGroupInlinePolicyResponse]:
        "Create or replace a group's inline policy"
        return cast(
            ApiResponse[m.PutGroupInlinePolicyResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["putGroupInlinePolicy"],
                "json",
                {"group_id": group_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    async def put_user_inline_policy(
        self,
        user_id: str,
        policy_name: str,
        body: m.PutUserInlinePolicyBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.PutUserInlinePolicyResponse]:
        "Create or replace a user's inline policy"
        return cast(
            ApiResponse[m.PutUserInlinePolicyResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["putUserInlinePolicy"],
                "json",
                {"user_id": user_id, "policy_name": policy_name},
                body,
                None,
                options,
            ),
        )

    async def remove_account_role_assignment(
        self, account_id: str, assignment_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove account role assignment"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeAccountRoleAssignment"],
                "discard",
                {"account_id": account_id, "assignment_id": assignment_id},
                UNSET,
                None,
                options,
            ),
        )

    async def remove_user(self, user_id: str, *, options: RequestOptions | None = None) -> None:
        "Remove user from organization"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUser"],
                "discard",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    async def remove_user_from_group(
        self, user_id: str, group_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove user from group"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUserFromGroup"],
                "discard",
                {"user_id": user_id, "group_id": group_id},
                UNSET,
                None,
                options,
            ),
        )

    async def remove_user_permission_boundary(
        self, user_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Remove a user's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["removeUserPermissionBoundary"],
                "discard",
                {"user_id": user_id},
                UNSET,
                None,
                options,
            ),
        )

    async def set_user_permission_boundary(
        self,
        user_id: str,
        body: m.SetUserPermissionBoundaryBody,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Set a user's permission boundary"
        return cast(
            None,
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["setUserPermissionBoundary"],
                "discard",
                {"user_id": user_id},
                body,
                None,
                options,
            ),
        )

    async def update_account(
        self, account_id: str, body: m.UpdateAccountBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateAccountResponse]:
        "Update account"
        return cast(
            ApiResponse[m.UpdateAccountResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateAccount"],
                "json",
                {"account_id": account_id},
                body,
                None,
                options,
            ),
        )

    async def update_group(
        self, group_id: str, body: m.UpdateGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateGroupResponse]:
        "Update group"
        return cast(
            ApiResponse[m.UpdateGroupResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateGroup"],
                "json",
                {"group_id": group_id},
                body,
                None,
                options,
            ),
        )

    async def update_organization(
        self,
        organization_id: str,
        body: m.UpdateOrganizationBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateOrganizationResponse]:
        "Update organization"
        return cast(
            ApiResponse[m.UpdateOrganizationResponse],
            await self._transport.request(
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updateOrganization"],
                "json",
                {"organization_id": organization_id},
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
                "workspace",
                "https://workspace.basaltic.sh",
                _OPS["updatePolicy"],
                "json",
                {"policy_id": policy_id},
                body,
                None,
                options,
            ),
        )
