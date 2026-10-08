"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

UserAddRequestInput = TypedDict(
    "UserAddRequestInput",
    {
        "email": "Required[str]",
        "tags": "NotRequired[TagsInput]",
        "groups": "NotRequired[list[GroupReferenceInput]]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
GroupReferenceInput: TypeAlias = "str"
AddUserBody: TypeAlias = "UserAddRequestInput"
UserAddResponse = TypedDict(
    "UserAddResponse",
    {"invitation": "Required[Invitation]", "status": "Required[Literal['invited']]"},
    total=False,
)
Invitation = TypedDict(
    "Invitation",
    {
        "id": "NotRequired[str]",
        "email": "NotRequired[str]",
        "groups": "NotRequired[list[GroupSummary]]",
        "invited_by": "NotRequired[InvitationInvitedBy]",
        "status": "NotRequired[Literal['pending', 'accepted', 'expired', 'cancelled']]",
        "expires_at": "NotRequired[str]",
        "created_at": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
GroupSummary = TypedDict(
    "GroupSummary", {"id": "NotRequired[str]", "name": "NotRequired[str]"}, total=False
)
InvitationInvitedBy = TypedDict(
    "InvitationInvitedBy",
    {
        "id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "email": "NotRequired[str]",
        "type": "NotRequired[Literal['user', 'service_account', 'assumed_role']]",
        "crn": "NotRequired[str]",
        "account_id": "NotRequired[str]",
    },
    total=False,
)
AddUserResponse: TypeAlias = "UserAddResponse"
UserGroupAddRequestInput = TypedDict(
    "UserGroupAddRequestInput", {"group": "Required[GroupReferenceInput]"}, total=False
)
AddUserToGroupBody: TypeAlias = "UserGroupAddRequestInput"
AccountRoleAssignmentCreateRequestInput = TypedDict(
    "AccountRoleAssignmentCreateRequestInput",
    {
        "principal_type": "Required[Literal['user', 'group']]",
        "principal_id": "Required[str]",
        "role_id": "Required[str]",
    },
    total=False,
)
AssignAccountRoleBody: TypeAlias = "AccountRoleAssignmentCreateRequestInput"
AccountRoleAssignmentResponse = TypedDict(
    "AccountRoleAssignmentResponse",
    {"role_assignment": "NotRequired[AccountRoleAssignment]"},
    total=False,
)
AccountRoleAssignment = TypedDict(
    "AccountRoleAssignment",
    {
        "crn": "NotRequired[str]",
        "id": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "role_id": "NotRequired[str]",
        "role_name": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user', 'group']]",
        "principal_id": "NotRequired[str]",
        "created_at": "NotRequired[str]",
    },
    total=False,
)
AssignAccountRoleResponse: TypeAlias = "AccountRoleAssignmentResponse"
PolicyAttachRequestInput = TypedDict(
    "PolicyAttachRequestInput", {"policy": "Required[PolicyReferenceInput]"}, total=False
)
PolicyReferenceInput: TypeAlias = "str"
AttachGroupPolicyBody: TypeAlias = "PolicyAttachRequestInput"
OrganizationPolicyAttachRequestInput = TypedDict(
    "OrganizationPolicyAttachRequestInput", {"policy_id": "Required[str]"}, total=False
)
AttachRolePolicyBody: TypeAlias = "OrganizationPolicyAttachRequestInput"
AttachServiceAccountPolicyBody: TypeAlias = "OrganizationPolicyAttachRequestInput"
AttachUserPolicyBody: TypeAlias = "PolicyAttachRequestInput"
CreateAccountRequestInput = TypedDict(
    "CreateAccountRequestInput",
    {"name": "Required[str]", "handle": "Required[str]", "description": "NotRequired[str]"},
    total=False,
)
CreateAccountBody: TypeAlias = "CreateAccountRequestInput"
AccountResponse = TypedDict("AccountResponse", {"account": "NotRequired[Account]"}, total=False)
Account = TypedDict(
    "Account",
    {
        "id": "NotRequired[str]",
        "organization_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "handle": "NotRequired[str]",
        "description": "NotRequired[str]",
        "status": "NotRequired[Literal['active', 'suspended', 'deleted']]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "bootstrap_role_id": "NotRequired[str]",
        "bootstrap_role_crn": "NotRequired[str]",
    },
    total=False,
)
CreateAccountResponse: TypeAlias = "AccountResponse"
GroupCreateRequestInput = TypedDict(
    "GroupCreateRequestInput",
    {"name": "Required[str]", "description": "NotRequired[str]"},
    total=False,
)
CreateGroupBody: TypeAlias = "GroupCreateRequestInput"
CreateGroupResult = TypedDict("CreateGroupResult", {"group": "NotRequired[Group]"}, total=False)
Group = TypedDict(
    "Group",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
CreateGroupResponse: TypeAlias = "CreateGroupResult"
PolicyCreateRequestInput = TypedDict(
    "PolicyCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "document": "Required[PolicyDocumentInput]",
    },
    total=False,
)
PolicyDocumentInput = TypedDict(
    "PolicyDocumentInput",
    {
        "version": "Required[Literal['2024-01-01']]",
        "statements": "Required[list[PolicyStatementInput]]",
    },
    total=False,
)
PolicyStatementInput = TypedDict(
    "PolicyStatementInput",
    {
        "sid": "NotRequired[str]",
        "effect": "Required[Literal['allow', 'deny']]",
        "actions": "NotRequired[list[str]]",
        "not_actions": "NotRequired[list[str]]",
        "resources": "NotRequired[list[str]]",
        "not_resources": "NotRequired[list[str]]",
        "conditions": "NotRequired[list[PolicyConditionInput]]",
    },
    total=False,
)
PolicyConditionInput = TypedDict(
    "PolicyConditionInput",
    {
        "operator": "Required[Literal['equals', 'not_equals', 'starts_with', 'ends_with', 'contains', 'in', 'not_in', 'greater_than', 'less_than', 'greater_than_or_equals', 'less_than_or_equals', 'exists', 'not_exists', 'ip_address', 'not_ip_address']]",
        "key": "Required[str]",
        "values": "Required[list[str]]",
        "set_operator": "NotRequired[Literal['for_all_values', 'for_any_value']]",
    },
    total=False,
)
CreatePolicyBody: TypeAlias = "PolicyCreateRequestInput"
CreatePolicyResult = TypedDict("CreatePolicyResult", {"policy": "NotRequired[Policy]"}, total=False)
Policy = TypedDict(
    "Policy",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "is_system": "NotRequired[bool]",
        "document": "NotRequired[PolicyDocument]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
PolicyDocument = TypedDict(
    "PolicyDocument",
    {"version": "Required[Literal['2024-01-01']]", "statements": "Required[list[PolicyStatement]]"},
    total=False,
)
PolicyStatement = TypedDict(
    "PolicyStatement",
    {
        "sid": "NotRequired[str]",
        "effect": "Required[Literal['allow', 'deny']]",
        "actions": "NotRequired[list[str]]",
        "not_actions": "NotRequired[list[str]]",
        "resources": "NotRequired[list[str]]",
        "not_resources": "NotRequired[list[str]]",
        "conditions": "NotRequired[list[PolicyCondition]]",
    },
    total=False,
)
PolicyCondition = TypedDict(
    "PolicyCondition",
    {
        "operator": "Required[Literal['equals', 'not_equals', 'starts_with', 'ends_with', 'contains', 'in', 'not_in', 'greater_than', 'less_than', 'greater_than_or_equals', 'less_than_or_equals', 'exists', 'not_exists', 'ip_address', 'not_ip_address']]",
        "key": "Required[str]",
        "values": "Required[list[str]]",
        "set_operator": "NotRequired[Literal['for_all_values', 'for_any_value']]",
    },
    total=False,
)
CreatePolicyResponse: TypeAlias = "CreatePolicyResult"
GetAccountResponse: TypeAlias = "AccountResponse"
GetAccountResource: TypeAlias = "Account"
GetAccountScope = TypedDict("GetAccountScope", {"limit": "NotRequired[int]"}, total=False)
GetAccountResourcesResult = TypedDict(
    "GetAccountResourcesResult", {"has_resources": "Required[bool]"}, total=False
)
GetAccountResourcesResponse: TypeAlias = "GetAccountResourcesResult"
GetGroupResult = TypedDict("GetGroupResult", {"group": "NotRequired[Group]"}, total=False)
GetGroupResponse: TypeAlias = "GetGroupResult"
GetGroupResource: TypeAlias = "Group"
GetGroupScope = TypedDict("GetGroupScope", {"limit": "NotRequired[int]"}, total=False)
InlinePolicyResponse = TypedDict(
    "InlinePolicyResponse", {"inline_policy": "NotRequired[InlinePolicy]"}, total=False
)
InlinePolicy = TypedDict(
    "InlinePolicy",
    {
        "crn": "Required[str]",
        "id": "NotRequired[str]",
        "principal_id": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user', 'group']]",
        "name": "NotRequired[str]",
        "document": "NotRequired[PolicyDocument]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
GetGroupInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
GetGroupInlinePolicyResource: TypeAlias = "InlinePolicy"
GetGroupInlinePolicyScope = TypedDict("GetGroupInlinePolicyScope", {}, total=False)
GetInvitationResult = TypedDict(
    "GetInvitationResult", {"invitation": "NotRequired[Invitation]"}, total=False
)
GetInvitationResponse: TypeAlias = "GetInvitationResult"
GetInvitationResource: TypeAlias = "Invitation"
GetInvitationScope = TypedDict("GetInvitationScope", {"limit": "NotRequired[int]"}, total=False)
OrganizationResponse = TypedDict(
    "OrganizationResponse", {"organization": "NotRequired[Organization]"}, total=False
)
Organization = TypedDict(
    "Organization",
    {
        "language": "NotRequired[Literal['en', 'pt-BR', 'es']]",
        "time_zone": "NotRequired[str]",
        "id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "owner_id": "NotRequired[str]",
        "status": "NotRequired[Literal['pending', 'active', 'suspended', 'terminated']]",
        "suspension_reason": "NotRequired[Literal['billing', 'manual']]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
GetOrganizationResponse: TypeAlias = "OrganizationResponse"
GetOrganizationResource: TypeAlias = "Organization"
GetOrganizationScope = TypedDict("GetOrganizationScope", {"limit": "NotRequired[int]"}, total=False)
GetPolicyResult = TypedDict("GetPolicyResult", {"policy": "NotRequired[Policy]"}, total=False)
GetPolicyResponse: TypeAlias = "GetPolicyResult"
GetPolicyResource: TypeAlias = "Policy"
GetPolicyScope = TypedDict("GetPolicyScope", {"limit": "NotRequired[int]"}, total=False)
GetUserResult = TypedDict("GetUserResult", {"user": "NotRequired[User]"}, total=False)
User = TypedDict(
    "User",
    {
        "username": "NotRequired[str]",
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "email": "NotRequired[str]",
        "name": "NotRequired[str]",
        "linux_identity": "NotRequired[LinuxIdentity]",
        "added_at": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
    },
    total=False,
)
LinuxIdentity = TypedDict(
    "LinuxIdentity",
    {
        "home_directory": "Required[str]",
        "username": "Required[str]",
        "uid": "Required[int]",
        "gid": "Required[int]",
    },
    total=False,
)
GetUserResponse: TypeAlias = "GetUserResult"
GetUserResource: TypeAlias = "User"
GetUserScope = TypedDict("GetUserScope", {"limit": "NotRequired[int]"}, total=False)
GetUserInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
GetUserInlinePolicyResource: TypeAlias = "InlinePolicy"
GetUserInlinePolicyScope = TypedDict("GetUserInlinePolicyScope", {}, total=False)
PermissionBoundaryResponse = TypedDict(
    "PermissionBoundaryResponse",
    {"permission_boundary": "NotRequired[PermissionBoundary]"},
    total=False,
)
PermissionBoundary = TypedDict(
    "PermissionBoundary",
    {
        "principal_id": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user']]",
        "policy_id": "NotRequired[str]",
        "policy_name": "NotRequired[str]",
        "created_at": "NotRequired[str]",
    },
    total=False,
)
GetUserPermissionBoundaryResponse: TypeAlias = "PermissionBoundaryResponse"
AccountRoleAssignmentListResponse = TypedDict(
    "AccountRoleAssignmentListResponse",
    {"role_assignments": "NotRequired[list[AccountRoleAssignment]]"},
    total=False,
)
ListAccountRoleAssignmentsResponse: TypeAlias = "AccountRoleAssignmentListResponse"
ListAccountRoleAssignmentsItem: TypeAlias = "AccountRoleAssignment"
AccountRoleListResponse = TypedDict(
    "AccountRoleListResponse", {"account_roles": "NotRequired[list[AccountRole]]"}, total=False
)
AccountRole = TypedDict(
    "AccountRole",
    {
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
        "account_name": "NotRequired[str]",
        "role_id": "NotRequired[str]",
        "role_name": "NotRequired[str]",
        "role_crn": "NotRequired[str]",
    },
    total=False,
)
ListAccountRolesResponse: TypeAlias = "AccountRoleListResponse"
ListAccountRolesItem: TypeAlias = "AccountRole"
ListAccountsParameters = TypedDict(
    "ListAccountsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListAccountsQuery: TypeAlias = "ListAccountsParameters"
AccountListResponse = TypedDict(
    "AccountListResponse",
    {"accounts": "NotRequired[list[Account]]", "meta": "NotRequired[PaginationMeta]"},
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
ListAccountsResponse: TypeAlias = "AccountListResponse"
ListAccountsItem: TypeAlias = "Account"
ListGroupInlinePoliciesParameters = TypedDict(
    "ListGroupInlinePoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListGroupInlinePoliciesQuery: TypeAlias = "ListGroupInlinePoliciesParameters"
InlinePolicyListResponse = TypedDict(
    "InlinePolicyListResponse", {"inline_policies": "NotRequired[list[InlinePolicy]]"}, total=False
)
ListGroupInlinePoliciesResponse: TypeAlias = "InlinePolicyListResponse"
ListGroupInlinePoliciesItem: TypeAlias = "InlinePolicy"
ListGroupPoliciesParameters = TypedDict(
    "ListGroupPoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListGroupPoliciesQuery: TypeAlias = "ListGroupPoliciesParameters"
PrincipalPoliciesListResponse = TypedDict(
    "PrincipalPoliciesListResponse", {"policies": "NotRequired[list[Policy]]"}, total=False
)
ListGroupPoliciesResponse: TypeAlias = "PrincipalPoliciesListResponse"
ListGroupPoliciesItem: TypeAlias = "Policy"
ListGroupUsersParameters = TypedDict(
    "ListGroupUsersParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListGroupUsersQuery: TypeAlias = "ListGroupUsersParameters"
GroupUsersListResponse = TypedDict(
    "GroupUsersListResponse",
    {"users": "NotRequired[list[GroupUser]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
GroupUser = TypedDict(
    "GroupUser",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "email": "NotRequired[str]",
        "name": "NotRequired[str]",
        "added_at": "NotRequired[str]",
    },
    total=False,
)
ListGroupUsersResponse: TypeAlias = "GroupUsersListResponse"
ListGroupUsersItem: TypeAlias = "GroupUser"
ListGroupsParameters = TypedDict(
    "ListGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListGroupsQuery: TypeAlias = "ListGroupsParameters"
GroupListResponse = TypedDict(
    "GroupListResponse",
    {"groups": "NotRequired[list[Group]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListGroupsResponse: TypeAlias = "GroupListResponse"
ListGroupsItem: TypeAlias = "Group"
ListInvitationsParameters = TypedDict(
    "ListInvitationsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInvitationsQuery: TypeAlias = "ListInvitationsParameters"
InvitationListResponse = TypedDict(
    "InvitationListResponse",
    {"invitations": "NotRequired[list[Invitation]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListInvitationsResponse: TypeAlias = "InvitationListResponse"
ListInvitationsItem: TypeAlias = "Invitation"
ListOrganizationsParameters = TypedDict(
    "ListOrganizationsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListOrganizationsQuery: TypeAlias = "ListOrganizationsParameters"
OrganizationListResponse = TypedDict(
    "OrganizationListResponse",
    {
        "organizations": "NotRequired[list[OrganizationWithMembership]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
OrganizationWithMembership = TypedDict(
    "OrganizationWithMembership",
    {
        "language": "NotRequired[Literal['en', 'pt-BR', 'es']]",
        "time_zone": "NotRequired[str]",
        "id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "owner_id": "NotRequired[str]",
        "status": "NotRequired[Literal['pending', 'active', 'suspended', 'terminated']]",
        "suspension_reason": "NotRequired[Literal['billing', 'manual']]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
ListOrganizationsResponse: TypeAlias = "OrganizationListResponse"
ListOrganizationsItem: TypeAlias = "OrganizationWithMembership"
ListPoliciesParameters = TypedDict(
    "ListPoliciesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListPoliciesQuery: TypeAlias = "ListPoliciesParameters"
PolicyListResponse = TypedDict(
    "PolicyListResponse",
    {"policies": "NotRequired[list[Policy]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListPoliciesResponse: TypeAlias = "PolicyListResponse"
ListPoliciesItem: TypeAlias = "Policy"
ListPolicyGroupsParameters = TypedDict(
    "ListPolicyGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListPolicyGroupsQuery: TypeAlias = "ListPolicyGroupsParameters"
PolicyGroupsListResponse = TypedDict(
    "PolicyGroupsListResponse",
    {"groups": "NotRequired[list[Group]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListPolicyGroupsResponse: TypeAlias = "PolicyGroupsListResponse"
ListPolicyGroupsItem: TypeAlias = "Group"
ListPolicyRolesParameters = TypedDict(
    "ListPolicyRolesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListPolicyRolesQuery: TypeAlias = "ListPolicyRolesParameters"
PolicyRolesListResponse = TypedDict(
    "PolicyRolesListResponse",
    {
        "roles": "NotRequired[list[AccountPrincipalReference]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
AccountPrincipalReference = TypedDict(
    "AccountPrincipalReference",
    {
        "id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
    },
    total=False,
)
ListPolicyRolesResponse: TypeAlias = "PolicyRolesListResponse"
ListPolicyRolesItem: TypeAlias = "AccountPrincipalReference"
ListPolicyServiceAccountsParameters = TypedDict(
    "ListPolicyServiceAccountsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListPolicyServiceAccountsQuery: TypeAlias = "ListPolicyServiceAccountsParameters"
PolicyServiceAccountsListResponse = TypedDict(
    "PolicyServiceAccountsListResponse",
    {
        "service_accounts": "NotRequired[list[AccountPrincipalReference]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
ListPolicyServiceAccountsResponse: TypeAlias = "PolicyServiceAccountsListResponse"
ListPolicyServiceAccountsItem: TypeAlias = "AccountPrincipalReference"
ListPolicyUsersParameters = TypedDict(
    "ListPolicyUsersParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListPolicyUsersQuery: TypeAlias = "ListPolicyUsersParameters"
PolicyUsersListResponse = TypedDict(
    "PolicyUsersListResponse",
    {"users": "NotRequired[list[User]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListPolicyUsersResponse: TypeAlias = "PolicyUsersListResponse"
ListPolicyUsersItem: TypeAlias = "User"
ListRolePoliciesParameters = TypedDict(
    "ListRolePoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListRolePoliciesQuery: TypeAlias = "ListRolePoliciesParameters"
RolePoliciesListResponse = TypedDict(
    "RolePoliciesListResponse", {"policies": "NotRequired[list[Policy]]"}, total=False
)
ListRolePoliciesResponse: TypeAlias = "RolePoliciesListResponse"
ListRolePoliciesItem: TypeAlias = "Policy"
ListServiceAccountPoliciesParameters = TypedDict(
    "ListServiceAccountPoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListServiceAccountPoliciesQuery: TypeAlias = "ListServiceAccountPoliciesParameters"
ListServiceAccountPoliciesResponse: TypeAlias = "PrincipalPoliciesListResponse"
ListServiceAccountPoliciesItem: TypeAlias = "Policy"
ListUserGroupsParameters = TypedDict(
    "ListUserGroupsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListUserGroupsQuery: TypeAlias = "ListUserGroupsParameters"
ListUserGroupsResponse: TypeAlias = "GroupListResponse"
ListUserGroupsItem: TypeAlias = "Group"
ListUserInlinePoliciesParameters = TypedDict(
    "ListUserInlinePoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListUserInlinePoliciesQuery: TypeAlias = "ListUserInlinePoliciesParameters"
ListUserInlinePoliciesResponse: TypeAlias = "InlinePolicyListResponse"
ListUserInlinePoliciesItem: TypeAlias = "InlinePolicy"
ListUserPoliciesParameters = TypedDict(
    "ListUserPoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListUserPoliciesQuery: TypeAlias = "ListUserPoliciesParameters"
ListUserPoliciesResponse: TypeAlias = "PrincipalPoliciesListResponse"
ListUserPoliciesItem: TypeAlias = "Policy"
ListUsersParameters = TypedDict(
    "ListUsersParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListUsersQuery: TypeAlias = "ListUsersParameters"
UserListResponse = TypedDict(
    "UserListResponse",
    {"users": "NotRequired[list[User]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListUsersResponse: TypeAlias = "UserListResponse"
ListUsersItem: TypeAlias = "User"
PutInlinePolicyRequestInput = TypedDict(
    "PutInlinePolicyRequestInput", {"document": "Required[PolicyDocumentInput]"}, total=False
)
PutGroupInlinePolicyBody: TypeAlias = "PutInlinePolicyRequestInput"
PutGroupInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
PutUserInlinePolicyBody: TypeAlias = "PutInlinePolicyRequestInput"
PutUserInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
SetBoundaryRequestInput = TypedDict(
    "SetBoundaryRequestInput", {"policy": "Required[PolicyReferenceInput]"}, total=False
)
SetUserPermissionBoundaryBody: TypeAlias = "SetBoundaryRequestInput"
UpdateAccountRequestInput = TypedDict(
    "UpdateAccountRequestInput",
    {"name": "NotRequired[str]", "description": "NotRequired[str]"},
    total=False,
)
UpdateAccountBody: TypeAlias = "UpdateAccountRequestInput"
UpdateAccountResponse: TypeAlias = "AccountResponse"
GroupUpdateRequestInput = TypedDict(
    "GroupUpdateRequestInput", {"description": "NotRequired[str]"}, total=False
)
UpdateGroupBody: TypeAlias = "GroupUpdateRequestInput"
UpdateGroupResult = TypedDict("UpdateGroupResult", {"group": "NotRequired[Group]"}, total=False)
UpdateGroupResponse: TypeAlias = "UpdateGroupResult"
OrganizationUpdateRequestInput = TypedDict(
    "OrganizationUpdateRequestInput",
    {
        "language": "NotRequired[Literal['en', 'pt-BR', 'es']]",
        "time_zone": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "captcha_token": "Required[str]",
    },
    total=False,
)
UpdateOrganizationBody: TypeAlias = "OrganizationUpdateRequestInput"
UpdateOrganizationResponse: TypeAlias = "OrganizationResponse"
PolicyUpdateRequestInput = TypedDict(
    "PolicyUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "document": "NotRequired[PolicyDocumentInput]",
    },
    total=False,
)
UpdatePolicyBody: TypeAlias = "PolicyUpdateRequestInput"
UpdatePolicyResult = TypedDict("UpdatePolicyResult", {"policy": "NotRequired[Policy]"}, total=False)
UpdatePolicyResponse: TypeAlias = "UpdatePolicyResult"
