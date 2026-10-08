"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

KeyResponse = TypedDict("KeyResponse", {"key": "NotRequired[Key]"}, total=False)
Key = TypedDict(
    "Key",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "Required[Tags]",
        "key_spec": "Required[KeySpec]",
        "key_usage": "Required[KeyUsage]",
        "state": "Required[KeyState]",
        "system": "NotRequired[bool]",
        "deleted_at": "NotRequired[str | None]",
        "recovery_window_days": "NotRequired[int | None]",
        "scheduled_purge_at": "NotRequired[str | None]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
KeySpec: TypeAlias = "Literal['aes-256', 'rsa-2048', 'rsa-4096', 'ecdsa-p256']"
KeyUsage: TypeAlias = "Literal['encrypt_decrypt', 'sign_verify']"
KeyState: TypeAlias = "Literal['enabled', 'disabled', 'pending_deletion']"
CancelKeyDeletionResponse: TypeAlias = "KeyResponse"
CreateKeyRequestInput = TypedDict(
    "CreateKeyRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
        "key_spec": "Required[KeySpecInput]",
        "key_usage": "NotRequired[KeyUsageInput]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
KeySpecInput: TypeAlias = "Literal['aes-256', 'rsa-2048', 'rsa-4096', 'ecdsa-p256']"
KeyUsageInput: TypeAlias = "Literal['encrypt_decrypt', 'sign_verify']"
CreateKeyBody: TypeAlias = "CreateKeyRequestInput"
CreateKeyResponse: TypeAlias = "KeyResponse"
DecryptRequestInput = TypedDict(
    "DecryptRequestInput", {"ciphertext": "Required[str]", "aad": "NotRequired[str]"}, total=False
)
DecryptBody: TypeAlias = "DecryptRequestInput"
DecryptResponse2 = TypedDict("DecryptResponse2", {"plaintext": "NotRequired[str]"}, total=False)
DecryptResponse: TypeAlias = "DecryptResponse2"
DisableKeyResponse: TypeAlias = "KeyResponse"
EnableKeyResponse: TypeAlias = "KeyResponse"
EncryptRequestInput = TypedDict(
    "EncryptRequestInput", {"plaintext": "Required[str]", "aad": "NotRequired[str]"}, total=False
)
EncryptBody: TypeAlias = "EncryptRequestInput"
EncryptResponse2 = TypedDict(
    "EncryptResponse2",
    {"ciphertext": "NotRequired[str]", "key_crn": "NotRequired[str]"},
    total=False,
)
EncryptResponse: TypeAlias = "EncryptResponse2"
GenerateDataKeyRequestInput = TypedDict(
    "GenerateDataKeyRequestInput",
    {"number_of_bytes": "NotRequired[Literal[16, 32, 64]]"},
    total=False,
)
GenerateDataKeyBody: TypeAlias = "GenerateDataKeyRequestInput"
GenerateDataKeyResponse2 = TypedDict(
    "GenerateDataKeyResponse2",
    {"plaintext": "NotRequired[str]", "ciphertext": "NotRequired[str]"},
    total=False,
)
GenerateDataKeyResponse: TypeAlias = "GenerateDataKeyResponse2"
GetKeyResponse: TypeAlias = "KeyResponse"
GetKeyResource: TypeAlias = "Key"
GetKeyScope = TypedDict(
    "GetKeyScope", {"limit": "NotRequired[int]", "state": "NotRequired[KeyStateInput]"}, total=False
)
KeyStateInput: TypeAlias = "Literal['enabled', 'disabled', 'pending_deletion']"
ListKeysParameters = TypedDict(
    "ListKeysParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "state": "NotRequired[KeyStateInput]",
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
    },
    total=False,
)
ListKeysQuery: TypeAlias = "ListKeysParameters"
KeyListResponse = TypedDict(
    "KeyListResponse",
    {"keys": "NotRequired[list[Key]]", "meta": "NotRequired[PaginationMeta]"},
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
ListKeysResponse: TypeAlias = "KeyListResponse"
ListKeysItem: TypeAlias = "Key"
ScheduleKeyDeletionRequestInput = TypedDict(
    "ScheduleKeyDeletionRequestInput", {"recovery_window_days": "NotRequired[int]"}, total=False
)
ScheduleKeyDeletionBody: TypeAlias = "ScheduleKeyDeletionRequestInput"
ScheduleKeyDeletionResponse: TypeAlias = "KeyResponse"
SignRequestInput = TypedDict(
    "SignRequestInput",
    {"message": "Required[str]", "signing_algorithm": "NotRequired[SigningAlgorithmInput]"},
    total=False,
)
SigningAlgorithmInput: TypeAlias = (
    "Literal['RSASSA_PSS_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_256', 'ECDSA_SHA_256']"
)
SignBody: TypeAlias = "SignRequestInput"
SignResponse2 = TypedDict(
    "SignResponse2",
    {"signature": "NotRequired[str]", "signing_algorithm": "NotRequired[SigningAlgorithm]"},
    total=False,
)
SigningAlgorithm: TypeAlias = (
    "Literal['RSASSA_PSS_SHA_256', 'RSASSA_PKCS1_V1_5_SHA_256', 'ECDSA_SHA_256']"
)
SignResponse: TypeAlias = "SignResponse2"
UpdateKeyRequestInput = TypedDict(
    "UpdateKeyRequestInput",
    {"description": "NotRequired[str]", "tags": "NotRequired[TagsInput]"},
    total=False,
)
UpdateKeyBody: TypeAlias = "UpdateKeyRequestInput"
UpdateKeyResponse: TypeAlias = "KeyResponse"
VerifyRequestInput = TypedDict(
    "VerifyRequestInput",
    {
        "message": "Required[str]",
        "signature": "Required[str]",
        "signing_algorithm": "NotRequired[SigningAlgorithmInput]",
    },
    total=False,
)
VerifyBody: TypeAlias = "VerifyRequestInput"
VerifyResponse2 = TypedDict(
    "VerifyResponse2", {"signature_valid": "NotRequired[bool]"}, total=False
)
VerifyResponse: TypeAlias = "VerifyResponse2"
