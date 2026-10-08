"""Generated service accessors; do not edit."""

from functools import cached_property

from ._client import AsyncClientBase, SyncClientBase
from .services.audit import AsyncAuditService, AuditService
from .services.billing import AsyncBillingService, BillingService
from .services.catalog import AsyncCatalogService, CatalogService
from .services.certificate import AsyncCertificateService, CertificateService
from .services.compute import AsyncComputeService, ComputeService
from .services.dns import AsyncDnsService, DnsService
from .services.iam import AsyncIamService, IamService
from .services.kms import AsyncKmsService, KmsService
from .services.loadbalancer import AsyncLoadbalancerService, LoadbalancerService
from .services.network import AsyncNetworkService, NetworkService
from .services.quota import AsyncQuotaService, QuotaService
from .services.secrets import AsyncSecretsService, SecretsService
from .services.storage import AsyncStorageService, StorageService
from .services.telemetry import AsyncTelemetryService, TelemetryService
from .services.workspace import AsyncWorkspaceService, WorkspaceService


class Client(SyncClientBase):
    @cached_property
    def audit(self) -> AuditService:
        return AuditService(self._transport)

    @cached_property
    def billing(self) -> BillingService:
        return BillingService(self._transport)

    @cached_property
    def catalog(self) -> CatalogService:
        return CatalogService(self._transport)

    @cached_property
    def certificate(self) -> CertificateService:
        return CertificateService(self._transport)

    @cached_property
    def compute(self) -> ComputeService:
        return ComputeService(self._transport)

    @cached_property
    def dns(self) -> DnsService:
        return DnsService(self._transport)

    @cached_property
    def iam(self) -> IamService:
        return IamService(self._transport)

    @cached_property
    def kms(self) -> KmsService:
        return KmsService(self._transport)

    @cached_property
    def loadbalancer(self) -> LoadbalancerService:
        return LoadbalancerService(self._transport)

    @cached_property
    def network(self) -> NetworkService:
        return NetworkService(self._transport)

    @cached_property
    def quota(self) -> QuotaService:
        return QuotaService(self._transport)

    @cached_property
    def secrets(self) -> SecretsService:
        return SecretsService(self._transport)

    @cached_property
    def storage(self) -> StorageService:
        return StorageService(self._transport)

    @cached_property
    def telemetry(self) -> TelemetryService:
        return TelemetryService(self._transport)

    @cached_property
    def workspace(self) -> WorkspaceService:
        return WorkspaceService(self._transport)


class AsyncClient(AsyncClientBase):
    @cached_property
    def audit(self) -> AsyncAuditService:
        return AsyncAuditService(self._transport)

    @cached_property
    def billing(self) -> AsyncBillingService:
        return AsyncBillingService(self._transport)

    @cached_property
    def catalog(self) -> AsyncCatalogService:
        return AsyncCatalogService(self._transport)

    @cached_property
    def certificate(self) -> AsyncCertificateService:
        return AsyncCertificateService(self._transport)

    @cached_property
    def compute(self) -> AsyncComputeService:
        return AsyncComputeService(self._transport)

    @cached_property
    def dns(self) -> AsyncDnsService:
        return AsyncDnsService(self._transport)

    @cached_property
    def iam(self) -> AsyncIamService:
        return AsyncIamService(self._transport)

    @cached_property
    def kms(self) -> AsyncKmsService:
        return AsyncKmsService(self._transport)

    @cached_property
    def loadbalancer(self) -> AsyncLoadbalancerService:
        return AsyncLoadbalancerService(self._transport)

    @cached_property
    def network(self) -> AsyncNetworkService:
        return AsyncNetworkService(self._transport)

    @cached_property
    def quota(self) -> AsyncQuotaService:
        return AsyncQuotaService(self._transport)

    @cached_property
    def secrets(self) -> AsyncSecretsService:
        return AsyncSecretsService(self._transport)

    @cached_property
    def storage(self) -> AsyncStorageService:
        return AsyncStorageService(self._transport)

    @cached_property
    def telemetry(self) -> AsyncTelemetryService:
        return AsyncTelemetryService(self._transport)

    @cached_property
    def workspace(self) -> AsyncWorkspaceService:
        return AsyncWorkspaceService(self._transport)
