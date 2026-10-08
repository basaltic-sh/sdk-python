"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

CertificateIssueRequestInput = TypedDict(
    "CertificateIssueRequestInput",
    {
        "name": "Required[str]",
        "domains": "Required[list[str]]",
        "key_algorithm": "NotRequired[CertificateKeyAlgorithmInput]",
        "source": "NotRequired[CertificateSourceInput]",
        "certificate_pem": "NotRequired[str]",
        "chain_pem": "NotRequired[str]",
        "private_key_pem": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
CertificateKeyAlgorithmInput: TypeAlias = (
    "Literal['ecdsa-p256', 'ecdsa-p384', 'rsa-2048', 'rsa-4096']"
)
CertificateSourceInput: TypeAlias = "Literal['acme', 'uploaded']"
TagsInput: TypeAlias = "dict[str, str]"
CreateCertificateBody: TypeAlias = "CertificateIssueRequestInput"
CertificateResponse = TypedDict(
    "CertificateResponse", {"certificate": "NotRequired[Certificate]"}, total=False
)
Certificate = TypedDict(
    "Certificate",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
        "domains": "NotRequired[list[str]]",
        "status": "NotRequired[CertificateStatus]",
        "source": "NotRequired[CertificateSource]",
        "key_algorithm": "NotRequired[CertificateKeyAlgorithm]",
        "challenges": "NotRequired[list[CertificateChallenge]]",
        "certificate_pem": "NotRequired[str]",
        "chain_pem": "NotRequired[str]",
        "fingerprint": "NotRequired[str]",
        "issued_at": "NotRequired[str]",
        "expires_at": "NotRequired[str]",
        "faults": "Required[list[Fault]]",
        "tags": "NotRequired[Tags]",
    },
    total=False,
)
CertificateStatus: TypeAlias = (
    "Literal['pending_dns', 'pending', 'active', 'error', 'expired', 'revoked']"
)
CertificateSource: TypeAlias = "Literal['acme', 'uploaded']"
CertificateKeyAlgorithm: TypeAlias = "Literal['ecdsa-p256', 'ecdsa-p384', 'rsa-2048', 'rsa-4096']"
CertificateChallenge = TypedDict(
    "CertificateChallenge",
    {
        "domain": "NotRequired[str]",
        "cname_record_name": "NotRequired[str]",
        "expected_cname": "NotRequired[str]",
        "our_dns": "NotRequired[bool]",
        "verified": "NotRequired[bool]",
        "verified_at": "NotRequired[str]",
        "faults": "Required[list[Fault]]",
    },
    total=False,
)
Fault = TypedDict(
    "Fault",
    {
        "code": "Required[str]",
        "severity": "Required[Literal['error', 'warning']]",
        "message": "Required[str]",
        "details": "Required[dict[str, object] | None]",
        "first_at": "Required[str]",
        "last_at": "Required[str]",
        "occurrences": "Required[int]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
CreateCertificateResponse: TypeAlias = "CertificateResponse"
GetCertificateResponse: TypeAlias = "CertificateResponse"
GetCertificateResource: TypeAlias = "Certificate"
GetCertificateScope = TypedDict("GetCertificateScope", {"limit": "NotRequired[int]"}, total=False)
MaterialResponse = TypedDict("MaterialResponse", {"material": "NotRequired[Material]"}, total=False)
Material = TypedDict(
    "Material",
    {
        "certificate_pem": "NotRequired[str]",
        "chain_pem": "NotRequired[str]",
        "private_key_pem": "NotRequired[str]",
        "fingerprint": "NotRequired[str]",
    },
    total=False,
)
GetCertificateMaterialResponse: TypeAlias = "MaterialResponse"
ListCertificatesParameters = TypedDict(
    "ListCertificatesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListCertificatesQuery: TypeAlias = "ListCertificatesParameters"
CertificateListResponse = TypedDict(
    "CertificateListResponse",
    {"certificates": "NotRequired[list[Certificate]]", "meta": "NotRequired[PaginationMeta]"},
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
ListCertificatesResponse: TypeAlias = "CertificateListResponse"
ListCertificatesItem: TypeAlias = "Certificate"
RevokeCertificateResponse: TypeAlias = "CertificateResponse"
