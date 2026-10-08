"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AssumeRoleRequestInput = TypedDict(
    "AssumeRoleRequestInput",
    {
        "role": "Required[RoleReferenceInput]",
        "duration_seconds": "NotRequired[int]",
        "policy": "NotRequired[SessionPolicyDocumentInput]",
    },
    total=False,
)
RoleReferenceInput: TypeAlias = "str"
SessionPolicyDocumentInput = TypedDict(
    "SessionPolicyDocumentInput",
    {
        "version": "Required[Literal['2024-01-01']]",
        "statements": "Required[list[SessionPolicyStatementInput]]",
    },
    total=False,
)
SessionPolicyStatementInput = TypedDict(
    "SessionPolicyStatementInput",
    {
        "sid": "NotRequired[str]",
        "effect": "Required[Literal['allow', 'deny']]",
        "actions": "NotRequired[list[str]]",
        "not_actions": "NotRequired[list[str]]",
        "resources": "NotRequired[list[str]]",
        "not_resources": "NotRequired[list[str]]",
    },
    total=False,
)
AssumeRoleBody: TypeAlias = "AssumeRoleRequestInput"
AssumeRoleResponse2 = TypedDict(
    "AssumeRoleResponse2",
    {
        "access_token": "NotRequired[str]",
        "token_type": "NotRequired[str]",
        "expires_in": "NotRequired[int]",
        "access_key_id": "NotRequired[str]",
        "secret_access_key": "NotRequired[str]",
        "session_token": "NotRequired[str]",
        "expiration": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
        "role_id": "NotRequired[str]",
    },
    total=False,
)
AssumeRoleResponse: TypeAlias = "AssumeRoleResponse2"
AssumeRoleWithWebIdentityRequestInput = TypedDict(
    "AssumeRoleWithWebIdentityRequestInput",
    {
        "web_identity_token": "Required[str]",
        "role": "Required[RoleReferenceInput]",
        "account": "Required[AccountReferenceInput]",
        "session_name": "NotRequired[str]",
        "duration_seconds": "NotRequired[int]",
    },
    total=False,
)
AccountReferenceInput: TypeAlias = "str"
AssumeRoleWithWebIdentityBody: TypeAlias = "AssumeRoleWithWebIdentityRequestInput"
AssumeRoleWithWebIdentityResponse: TypeAlias = "AssumeRoleResponse2"
RolePolicyAttachRequestInput = TypedDict(
    "RolePolicyAttachRequestInput", {"policy": "Required[PolicyReferenceInput]"}, total=False
)
PolicyReferenceInput: TypeAlias = "str"
AttachRolePolicyBody: TypeAlias = "RolePolicyAttachRequestInput"
PolicyAttachRequestInput = TypedDict(
    "PolicyAttachRequestInput", {"policy": "Required[PolicyReferenceInput]"}, total=False
)
AttachServiceAccountPolicyBody: TypeAlias = "PolicyAttachRequestInput"
OAuthAuthorizeRequestInput = TypedDict(
    "OAuthAuthorizeRequestInput",
    {
        "client_id": "Required[str]",
        "redirect_uri": "Required[str]",
        "code_challenge": "Required[str]",
        "code_challenge_method": "Required[Literal['S256']]",
        "state": "NotRequired[str]",
        "organization": "Required[OrganizationReferenceInput]",
    },
    total=False,
)
OrganizationReferenceInput: TypeAlias = "str"
AuthorizeOAuthClientBody: TypeAlias = "OAuthAuthorizeRequestInput"
OAuthAuthorizeResponse = TypedDict(
    "OAuthAuthorizeResponse",
    {"code": "NotRequired[str]", "redirect_to": "NotRequired[str]", "expires_in": "Required[int]"},
    total=False,
)
AuthorizeOAuthClientResponse: TypeAlias = "OAuthAuthorizeResponse"
SSHKeyCreateRequestInput = TypedDict(
    "SSHKeyCreateRequestInput",
    {"name": "Required[str]", "public_key": "Required[str]", "expires_at": "NotRequired[str]"},
    total=False,
)
CreatePersonalSSHKeyBody: TypeAlias = "SSHKeyCreateRequestInput"
CreatePersonalSSHKeyResult = TypedDict(
    "CreatePersonalSSHKeyResult", {"ssh_key": "Required[SSHKey]"}, total=False
)
SSHKey = TypedDict(
    "SSHKey",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "public_key": "Required[str]",
        "fingerprint": "Required[str]",
        "algorithm": "Required[str]",
        "created_at": "Required[str]",
        "expires_at": "NotRequired[str]",
    },
    total=False,
)
CreatePersonalSSHKeyResponse: TypeAlias = "CreatePersonalSSHKeyResult"
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
TagsInput: TypeAlias = "dict[str, str]"
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
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
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
RoleCreateRequestInput = TypedDict(
    "RoleCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "trust_policy": "NotRequired[TrustPolicyInput]",
    },
    total=False,
)
TrustPolicyInput = TypedDict(
    "TrustPolicyInput",
    {
        "principals": "NotRequired[list[str]]",
        "conditions": "NotRequired[list[PolicyConditionInput]]",
    },
    total=False,
)
CreateRoleBody: TypeAlias = "RoleCreateRequestInput"
CreateRoleResult = TypedDict("CreateRoleResult", {"role": "NotRequired[Role]"}, total=False)
Role = TypedDict(
    "Role",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "trust_policy": "NotRequired[TrustPolicy]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
        "is_system": "NotRequired[bool]",
        "builtin_kind": "NotRequired[Literal['administrator', 'readonly']]",
    },
    total=False,
)
TrustPolicy = TypedDict(
    "TrustPolicy",
    {"principals": "NotRequired[list[str]]", "conditions": "NotRequired[list[PolicyCondition]]"},
    total=False,
)
CreateRoleResponse: TypeAlias = "CreateRoleResult"
ServiceAccountCreateRequestInput = TypedDict(
    "ServiceAccountCreateRequestInput",
    {"name": "Required[str]", "description": "NotRequired[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
CreateServiceAccountBody: TypeAlias = "ServiceAccountCreateRequestInput"
CreateServiceAccountResult = TypedDict(
    "CreateServiceAccountResult", {"service_account": "NotRequired[ServiceAccount]"}, total=False
)
ServiceAccount = TypedDict(
    "ServiceAccount",
    {
        "linux_identity": "NotRequired[LinuxIdentity]",
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[Tags]",
        "enabled": "NotRequired[bool]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
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
CreateServiceAccountResponse: TypeAlias = "CreateServiceAccountResult"
CredentialCreateRequestInput = TypedDict(
    "CredentialCreateRequestInput",
    {"name": "Required[str]", "expires_at": "NotRequired[str]"},
    total=False,
)
CreateServiceAccountCredentialBody: TypeAlias = "CredentialCreateRequestInput"
CredentialCreateResponse = TypedDict(
    "CredentialCreateResponse",
    {"credential": "NotRequired[Credential]", "secret_access_key": "NotRequired[str]"},
    total=False,
)
Credential = TypedDict(
    "Credential",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "access_key_id": "NotRequired[str]",
        "last_used_at": "NotRequired[str | None]",
        "expires_at": "NotRequired[str | None]",
        "created_at": "NotRequired[str]",
    },
    total=False,
)
CreateServiceAccountCredentialResponse: TypeAlias = "CredentialCreateResponse"
CreateServiceAccountSSHKeyBody: TypeAlias = "SSHKeyCreateRequestInput"
CreateServiceAccountSSHKeyResult = TypedDict(
    "CreateServiceAccountSSHKeyResult", {"ssh_key": "Required[SSHKey]"}, total=False
)
CreateServiceAccountSSHKeyResponse: TypeAlias = "CreateServiceAccountSSHKeyResult"
OAuthTokenRequestInput = TypedDict(
    "OAuthTokenRequestInput",
    {
        "grant_type": "Required[Literal['client_credentials', 'authorization_code', 'refresh_token']]",
        "client_id": "NotRequired[str]",
        "client_secret": "NotRequired[str]",
        "duration_seconds": "NotRequired[int]",
        "code": "NotRequired[str]",
        "code_verifier": "NotRequired[str]",
        "redirect_uri": "NotRequired[str]",
        "refresh_token": "NotRequired[str]",
    },
    total=False,
)
GetOAuthTokenBody: TypeAlias = "OAuthTokenRequestInput"
OAuthTokenResponse = TypedDict(
    "OAuthTokenResponse",
    {
        "access_token": "Required[str]",
        "token_type": "Required[Literal['Bearer']]",
        "expires_in": "Required[int]",
        "refresh_token": "NotRequired[str]",
    },
    total=False,
)
GetOAuthTokenResponse: TypeAlias = "OAuthTokenResponse"
GetPersonalLinuxIdentityResult = TypedDict(
    "GetPersonalLinuxIdentityResult", {"linux_identity": "Required[LinuxIdentity]"}, total=False
)
GetPersonalLinuxIdentityResponse: TypeAlias = "GetPersonalLinuxIdentityResult"
GetPolicyResult = TypedDict("GetPolicyResult", {"policy": "NotRequired[Policy]"}, total=False)
GetPolicyResponse: TypeAlias = "GetPolicyResult"
GetPolicyResource: TypeAlias = "Policy"
GetPolicyScope = TypedDict("GetPolicyScope", {"limit": "NotRequired[int]"}, total=False)
GetRoleResult = TypedDict("GetRoleResult", {"role": "NotRequired[Role]"}, total=False)
GetRoleResponse: TypeAlias = "GetRoleResult"
GetRoleResource: TypeAlias = "Role"
GetRoleScope = TypedDict("GetRoleScope", {"limit": "NotRequired[int]"}, total=False)
InlinePolicyResponse = TypedDict(
    "InlinePolicyResponse", {"inline_policy": "NotRequired[InlinePolicy]"}, total=False
)
InlinePolicy = TypedDict(
    "InlinePolicy",
    {
        "crn": "Required[str]",
        "id": "NotRequired[str]",
        "principal_id": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['service_account', 'role']]",
        "name": "NotRequired[str]",
        "document": "NotRequired[PolicyDocument]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
GetRoleInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
GetRoleInlinePolicyResource: TypeAlias = "InlinePolicy"
GetRoleInlinePolicyScope = TypedDict("GetRoleInlinePolicyScope", {}, total=False)
PermissionBoundaryResponse = TypedDict(
    "PermissionBoundaryResponse",
    {"permission_boundary": "NotRequired[PermissionBoundary]"},
    total=False,
)
PermissionBoundary = TypedDict(
    "PermissionBoundary",
    {
        "principal_id": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['service_account', 'role']]",
        "policy_id": "NotRequired[str]",
        "policy_name": "NotRequired[str]",
        "created_at": "NotRequired[str]",
    },
    total=False,
)
GetRolePermissionBoundaryResponse: TypeAlias = "PermissionBoundaryResponse"
STSSessionResponse = TypedDict(
    "STSSessionResponse", {"sts_session": "NotRequired[STSSession]"}, total=False
)
STSSession = TypedDict(
    "STSSession",
    {
        "id": "NotRequired[str]",
        "role_id": "NotRequired[str]",
        "principal_id": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user', 'service_account', 'assumed_role']]",
        "session_name": "NotRequired[str | None]",
        "created_at": "NotRequired[str]",
        "expires_at": "NotRequired[str]",
        "last_used_at": "NotRequired[str | None]",
        "revoked": "NotRequired[bool]",
        "revoked_at": "NotRequired[str | None]",
        "revoked_reason": "NotRequired[str | None]",
        "source_ip": "NotRequired[str | None]",
        "user_agent": "NotRequired[str | None]",
        "account_id": "NotRequired[str]",
        "account_handle": "NotRequired[str]",
        "source_account_id": "NotRequired[str | None]",
        "source_principal_type": "NotRequired[str | None]",
        "source_principal_crn": "NotRequired[str | None]",
        "parent_session_id": "NotRequired[str | None]",
        "grant_type": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
GetSTSSessionResponse: TypeAlias = "STSSessionResponse"
GetSTSSessionResource: TypeAlias = "STSSession"
GetSTSSessionScope = TypedDict(
    "GetSTSSessionScope",
    {
        "role": "NotRequired[str]",
        "principal": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user', 'service_account', 'role', 'assumed_role']]",
        "active_only": "NotRequired[bool]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
GetServiceAccountResult = TypedDict(
    "GetServiceAccountResult", {"service_account": "NotRequired[ServiceAccount]"}, total=False
)
GetServiceAccountResponse: TypeAlias = "GetServiceAccountResult"
GetServiceAccountResource: TypeAlias = "ServiceAccount"
GetServiceAccountScope = TypedDict(
    "GetServiceAccountScope", {"limit": "NotRequired[int]"}, total=False
)
GetServiceAccountInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
GetServiceAccountInlinePolicyResource: TypeAlias = "InlinePolicy"
GetServiceAccountInlinePolicyScope = TypedDict(
    "GetServiceAccountInlinePolicyScope", {}, total=False
)
GetServiceAccountLinuxIdentityResult = TypedDict(
    "GetServiceAccountLinuxIdentityResult",
    {"linux_identity": "Required[LinuxIdentity]"},
    total=False,
)
GetServiceAccountLinuxIdentityResponse: TypeAlias = "GetServiceAccountLinuxIdentityResult"
GetServiceAccountPermissionBoundaryResponse: TypeAlias = "PermissionBoundaryResponse"
ListPersonalSSHKeysResult = TypedDict(
    "ListPersonalSSHKeysResult", {"ssh_keys": "Required[list[SSHKey]]"}, total=False
)
ListPersonalSSHKeysResponse: TypeAlias = "ListPersonalSSHKeysResult"
ListPersonalSSHKeysItem: TypeAlias = "SSHKey"
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
ListPoliciesResponse: TypeAlias = "PolicyListResponse"
ListPoliciesItem: TypeAlias = "Policy"
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
    {"roles": "NotRequired[list[Role]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListPolicyRolesResponse: TypeAlias = "PolicyRolesListResponse"
ListPolicyRolesItem: TypeAlias = "Role"
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
        "service_accounts": "NotRequired[list[ServiceAccount]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
ListPolicyServiceAccountsResponse: TypeAlias = "PolicyServiceAccountsListResponse"
ListPolicyServiceAccountsItem: TypeAlias = "ServiceAccount"
ListRegionsParameters = TypedDict(
    "ListRegionsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListRegionsQuery: TypeAlias = "ListRegionsParameters"
ListRegionsResult = TypedDict(
    "ListRegionsResult",
    {"regions": "Required[list[Region]]", "default": "Required[str]"},
    total=False,
)
Region = TypedDict(
    "Region",
    {
        "crn": "Required[str]",
        "code": "Required[str]",
        "name": "Required[str]",
        "location": "Required[str]",
        "country_code": "Required[str]",
        "available": "Required[bool]",
        "coming_soon": "Required[bool]",
    },
    total=False,
)
ListRegionsResponse: TypeAlias = "ListRegionsResult"
ListRegionsItem: TypeAlias = "Region"
ListRoleInlinePoliciesParameters = TypedDict(
    "ListRoleInlinePoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListRoleInlinePoliciesQuery: TypeAlias = "ListRoleInlinePoliciesParameters"
InlinePolicyListResponse = TypedDict(
    "InlinePolicyListResponse", {"inline_policies": "NotRequired[list[InlinePolicy]]"}, total=False
)
ListRoleInlinePoliciesResponse: TypeAlias = "InlinePolicyListResponse"
ListRoleInlinePoliciesItem: TypeAlias = "InlinePolicy"
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
ListRolesParameters = TypedDict(
    "ListRolesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListRolesQuery: TypeAlias = "ListRolesParameters"
RoleListResponse = TypedDict(
    "RoleListResponse",
    {"roles": "NotRequired[list[Role]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListRolesResponse: TypeAlias = "RoleListResponse"
ListRolesItem: TypeAlias = "Role"
ListSTSSessionsParameters = TypedDict(
    "ListSTSSessionsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "role": "NotRequired[str]",
        "principal": "NotRequired[str]",
        "principal_type": "NotRequired[Literal['user', 'service_account', 'role', 'assumed_role']]",
        "active_only": "NotRequired[bool]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListSTSSessionsQuery: TypeAlias = "ListSTSSessionsParameters"
STSSessionListResponse = TypedDict(
    "STSSessionListResponse",
    {"sts_sessions": "NotRequired[list[STSSession]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListSTSSessionsResponse: TypeAlias = "STSSessionListResponse"
ListSTSSessionsItem: TypeAlias = "STSSession"
ListServiceAccountCredentialsParameters = TypedDict(
    "ListServiceAccountCredentialsParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListServiceAccountCredentialsQuery: TypeAlias = "ListServiceAccountCredentialsParameters"
CredentialListResponse = TypedDict(
    "CredentialListResponse", {"credentials": "NotRequired[list[Credential]]"}, total=False
)
ListServiceAccountCredentialsResponse: TypeAlias = "CredentialListResponse"
ListServiceAccountCredentialsItem: TypeAlias = "Credential"
ListServiceAccountInlinePoliciesParameters = TypedDict(
    "ListServiceAccountInlinePoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListServiceAccountInlinePoliciesQuery: TypeAlias = "ListServiceAccountInlinePoliciesParameters"
ListServiceAccountInlinePoliciesResponse: TypeAlias = "InlinePolicyListResponse"
ListServiceAccountInlinePoliciesItem: TypeAlias = "InlinePolicy"
ListServiceAccountPoliciesParameters = TypedDict(
    "ListServiceAccountPoliciesParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListServiceAccountPoliciesQuery: TypeAlias = "ListServiceAccountPoliciesParameters"
PrincipalPoliciesListResponse = TypedDict(
    "PrincipalPoliciesListResponse", {"policies": "NotRequired[list[Policy]]"}, total=False
)
ListServiceAccountPoliciesResponse: TypeAlias = "PrincipalPoliciesListResponse"
ListServiceAccountPoliciesItem: TypeAlias = "Policy"
ListServiceAccountSSHKeysResult = TypedDict(
    "ListServiceAccountSSHKeysResult", {"ssh_keys": "Required[list[SSHKey]]"}, total=False
)
ListServiceAccountSSHKeysResponse: TypeAlias = "ListServiceAccountSSHKeysResult"
ListServiceAccountSSHKeysItem: TypeAlias = "SSHKey"
ListServiceAccountsParameters = TypedDict(
    "ListServiceAccountsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListServiceAccountsQuery: TypeAlias = "ListServiceAccountsParameters"
ServiceAccountListResponse = TypedDict(
    "ServiceAccountListResponse",
    {
        "service_accounts": "NotRequired[list[ServiceAccount]]",
        "meta": "NotRequired[PaginationMeta]",
    },
    total=False,
)
ListServiceAccountsResponse: TypeAlias = "ServiceAccountListResponse"
ListServiceAccountsItem: TypeAlias = "ServiceAccount"
PutInlinePolicyRequestInput = TypedDict(
    "PutInlinePolicyRequestInput", {"document": "Required[PolicyDocumentInput]"}, total=False
)
PutRoleInlinePolicyBody: TypeAlias = "PutInlinePolicyRequestInput"
PutRoleInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
PutServiceAccountInlinePolicyBody: TypeAlias = "PutInlinePolicyRequestInput"
PutServiceAccountInlinePolicyResponse: TypeAlias = "InlinePolicyResponse"
OAuthRevokeRequestInput = TypedDict(
    "OAuthRevokeRequestInput",
    {"token": "Required[str]", "token_type_hint": "NotRequired[str]"},
    total=False,
)
RevokeOAuthTokenBody: TypeAlias = "OAuthRevokeRequestInput"
RevokeSTSSessionRequest = TypedDict(
    "RevokeSTSSessionRequest", {"reason": "NotRequired[str]"}, total=False
)
RevokeSTSSessionBody: TypeAlias = "RevokeSTSSessionRequest"
RevokeSTSSessionResponse: TypeAlias = "STSSessionResponse"
SetBoundaryRequestInput = TypedDict(
    "SetBoundaryRequestInput", {"policy": "Required[PolicyReferenceInput]"}, total=False
)
SetRolePermissionBoundaryBody: TypeAlias = "SetBoundaryRequestInput"
SetServiceAccountPermissionBoundaryBody: TypeAlias = "SetBoundaryRequestInput"
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
RoleUpdateRequestInput = TypedDict(
    "RoleUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "trust_policy": "NotRequired[TrustPolicyInput]",
    },
    total=False,
)
UpdateRoleBody: TypeAlias = "RoleUpdateRequestInput"
UpdateRoleResult = TypedDict("UpdateRoleResult", {"role": "NotRequired[Role]"}, total=False)
UpdateRoleResponse: TypeAlias = "UpdateRoleResult"
ServiceAccountUpdateRequestInput = TypedDict(
    "ServiceAccountUpdateRequestInput",
    {
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "enabled": "NotRequired[bool]",
    },
    total=False,
)
UpdateServiceAccountBody: TypeAlias = "ServiceAccountUpdateRequestInput"
UpdateServiceAccountResult = TypedDict(
    "UpdateServiceAccountResult", {"service_account": "NotRequired[ServiceAccount]"}, total=False
)
UpdateServiceAccountResponse: TypeAlias = "UpdateServiceAccountResult"
