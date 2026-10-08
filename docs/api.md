# Python API reference

All methods are available on `Client` and `AsyncClient`.
Async methods are awaited. `*_all` helpers return (async) iterators.
Request bodies and query dictionaries retain API field names; method names use snake_case.
`ApiResponse.data` preserves JSON envelopes. Binary/HEAD calls return streaming `httpx.Response`.

## `audit.get_audit_log`

Get audit log entry

`GET /v1/audit-logs/{log_id}`

```python
def get_audit_log(self, log_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetAuditLogResponse]:
```

## `audit.list_audit_logs`

List audit logs

`GET /v1/audit-logs`

```python
def list_audit_logs(self, *, query: m.ListAuditLogsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListAuditLogsResponse, m.ListAuditLogsItem]:
```

## `billing.get_billing_profile`

Read the organization billing profile

`GET /v1/profile`

```python
def get_billing_profile(self, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBillingProfileResponse]:
```

## `billing.get_current_usage`

Get month-to-date usage total

`GET /v1/usage`

```python
def get_current_usage(self, *, options: RequestOptions | None = None) -> ApiResponse[m.GetCurrentUsageResponse]:
```

## `billing.get_fiscal_invoice_xml`

Download issued NFS-e XML

`GET /v1/fiscal-invoices/{document_id}/xml`

```python
def get_fiscal_invoice_xml(self, document_id: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `billing.get_invoice`

Get an invoice with its line items

`GET /v1/invoices/{invoice_id}`

```python
def get_invoice(self, invoice_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInvoiceResponse]:
```

## `billing.get_invoice_pdf`

Download an invoice as a PDF statement

`GET /v1/invoices/{invoice_id}/pdf`

```python
def get_invoice_pdf(self, invoice_id: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `billing.list_credits`

List credit grants

`GET /v1/credits`

```python
def list_credits(self, *, query: m.ListCreditsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListCreditsResponse, m.ListCreditsItem]:
```

## `billing.list_fiscal_invoices`

List fiscal invoice issuance and delivery status

`GET /v1/fiscal-invoices`

```python
def list_fiscal_invoices(self, *, query: m.ListFiscalInvoicesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListFiscalInvoicesResponse, m.ListFiscalInvoicesItem]:
```

## `billing.list_invoices`

List invoices

`GET /v1/invoices`

```python
def list_invoices(self, *, query: m.ListInvoicesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInvoicesResponse, m.ListInvoicesItem]:
```

## `billing.list_payments`

List invoice payments

`GET /v1/payments`

```python
def list_payments(self, *, query: m.ListPaymentsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPaymentsResponse, m.ListPaymentsItem]:
```

## `billing.list_prices`

List catalog prices

`GET /v1/prices`

```python
def list_prices(self, *, query: m.ListPricesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPricesResponse, m.ListPricesItem]:
```

## `billing.list_transactions`

List ledger transactions

`GET /v1/transactions`

```python
def list_transactions(self, *, query: m.ListTransactionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListTransactionsResponse, m.ListTransactionsItem]:
```

## `billing.update_billing_profile`

Save organization billing details

`PUT /v1/profile`

```python
def update_billing_profile(self, body: m.UpdateBillingProfileBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateBillingProfileResponse]:
```

## `catalog.get_region`

Get a region

`GET /v1/regions/{code}`

```python
def get_region(self, code: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRegionResponse]:
```

## `catalog.list_regions`

List regions

`GET /v1/regions`

```python
def list_regions(self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
```

## `certificate.create_certificate`

Create certificate

`POST /v1/certificates`

```python
def create_certificate(self, body: m.CreateCertificateBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateCertificateResponse]:
```

## `certificate.delete_certificate`

Delete certificate

`DELETE /v1/certificates/{certificate_id}`

```python
def delete_certificate(self, certificate_id: str, *, options: RequestOptions | None = None) -> None:
```

## `certificate.get_certificate`

Get certificate

`GET /v1/certificates/{certificate_id}`

```python
def get_certificate(self, certificate_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetCertificateResponse]:
```

## `certificate.get_certificate_material`

Fetch certificate material (leaf, chain, private key)

`GET /v1/certificates/{certificate_id}/material`

```python
def get_certificate_material(self, certificate_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetCertificateMaterialResponse]:
```

## `certificate.list_certificates`

List certificates

`GET /v1/certificates`

```python
def list_certificates(self, *, query: m.ListCertificatesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListCertificatesResponse, m.ListCertificatesItem]:
```

## `certificate.revoke_certificate`

Revoke certificate

`POST /v1/certificates/{certificate_id}/revoke`

```python
def revoke_certificate(self, certificate_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.RevokeCertificateResponse]:
```

## `compute.attach_instance_nic`

Attach an existing NIC to an instance

`POST /v1/instances/{instance_id}/nics`

```python
def attach_instance_nic(self, instance_id: str, body: m.AttachInstanceNICBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachInstanceNICResponse]:
```

## `compute.attach_instance_pool_floating_ip`

Give the pool a shared public address

`POST /v1/instance-pools/{pool_id}/floating-ips`

```python
def attach_instance_pool_floating_ip(self, pool_id: str, body: m.AttachInstancePoolFloatingIpBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachInstancePoolFloatingIpResponse]:
```

## `compute.attach_instance_volume`

Attach a data volume to an instance

`POST /v1/instances/{instance_id}/volumes`

```python
def attach_instance_volume(self, instance_id: str, body: m.AttachInstanceVolumeBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachInstanceVolumeResponse]:
```

## `compute.create_image`

Import an image from an object URL

`POST /v1/images`

```python
def create_image(self, body: m.CreateImageBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateImageResponse]:
```

## `compute.create_instance`

Create instance

`POST /v1/instances`

```python
def create_instance(self, body: m.CreateInstanceBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInstanceResponse]:
```

## `compute.create_instance_pool`

Create an instance pool

`POST /v1/instance-pools`

```python
def create_instance_pool(self, body: m.CreateInstancePoolBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInstancePoolResponse]:
```

## `compute.create_serial_console_ticket`

Mint a ticket for the serial console

`POST /v1/instances/{instance_id}/console/ticket`

```python
def create_serial_console_ticket(self, instance_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSerialConsoleTicketResponse]:
```

## `compute.delete_image`

Delete an unused image

`DELETE /v1/images/{image_id}`

```python
def delete_image(self, image_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.DeleteImageResponse]:
```

## `compute.delete_instance`

Delete instance

`DELETE /v1/instances/{instance_id}`

```python
def delete_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.delete_instance_pool`

Delete an instance pool

`DELETE /v1/instance-pools/{pool_id}`

```python
def delete_instance_pool(self, pool_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.detach_instance_nic`

Detach a NIC from a running instance

`DELETE /v1/instances/{instance_id}/nics/{interface_id}`

```python
def detach_instance_nic(self, instance_id: str, interface_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.detach_instance_pool_floating_ip`

Take a shared address off the pool

`DELETE /v1/instance-pools/{pool_id}/floating-ips/{floating_ip_id}`

```python
def detach_instance_pool_floating_ip(self, pool_id: str, floating_ip_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.detach_instance_volume`

Detach a data volume from an instance

`DELETE /v1/instances/{instance_id}/volumes/{volume_id}`

```python
def detach_instance_volume(self, instance_id: str, volume_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.get_console_output`

Get the instance's serial console output

`GET /v1/instances/{instance_id}/console/output`

```python
def get_console_output(self, instance_id: str, *, query: m.GetConsoleOutputQuery | None = None, options: RequestOptions | None = None) -> ApiResponse[m.GetConsoleOutputResponse]:
```

## `compute.get_console_screenshot`

Capture the instance's display

`GET /v1/instances/{instance_id}/console/screenshot`

```python
def get_console_screenshot(self, instance_id: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `compute.get_flavor`

Get flavor

`GET /v1/flavors/{flavor_id}`

```python
def get_flavor(self, flavor_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetFlavorResponse]:
```

## `compute.get_image`

Get an image

`GET /v1/images/{image_id}`

```python
def get_image(self, image_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetImageResponse]:
```

## `compute.get_instance`

Get instance

`GET /v1/instances/{instance_id}`

```python
def get_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInstanceResponse]:
```

## `compute.get_instance_pool`

Get an instance pool

`GET /v1/instance-pools/{pool_id}`

```python
def get_instance_pool(self, pool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInstancePoolResponse]:
```

## `compute.list_flavors`

List flavors

`GET /v1/flavors`

```python
def list_flavors(self, *, query: m.ListFlavorsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListFlavorsResponse, m.ListFlavorsItem]:
```

## `compute.list_image_catalog`

List the launch image catalog

`GET /v1/image-catalog`

```python
def list_image_catalog(self, *, query: m.ListImageCatalogQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListImageCatalogResponse, m.ListImageCatalogItem]:
```

## `compute.list_images`

List images

`GET /v1/images`

```python
def list_images(self, *, query: m.ListImagesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListImagesResponse, m.ListImagesItem]:
```

## `compute.list_instance_ni_cs`

List the instance's network interfaces

`GET /v1/instances/{instance_id}/nics`

```python
def list_instance_ni_cs(self, instance_id: str, *, query: m.ListInstanceNICsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInstanceNICsResponse, m.ListInstanceNICsItem]:
```

## `compute.list_instance_pool_floating_ips`

List the pool's shared public addresses

`GET /v1/instance-pools/{pool_id}/floating-ips`

```python
def list_instance_pool_floating_ips(self, pool_id: str, *, query: m.ListInstancePoolFloatingIpsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInstancePoolFloatingIpsResponse, m.ListInstancePoolFloatingIpsItem]:
```

## `compute.list_instance_pools`

List instance pools

`GET /v1/instance-pools`

```python
def list_instance_pools(self, *, query: m.ListInstancePoolsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInstancePoolsResponse, m.ListInstancePoolsItem]:
```

## `compute.list_instance_volumes`

List the instance's attached volumes

`GET /v1/instances/{instance_id}/volumes`

```python
def list_instance_volumes(self, instance_id: str, *, query: m.ListInstanceVolumesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInstanceVolumesResponse, m.ListInstanceVolumesItem]:
```

## `compute.list_instances`

List instances

`GET /v1/instances`

```python
def list_instances(self, *, query: m.ListInstancesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInstancesResponse, m.ListInstancesItem]:
```

## `compute.list_pool_instances`

List a pool's instances

`GET /v1/instance-pools/{pool_id}/instances`

```python
def list_pool_instances(self, pool_id: str, *, query: m.ListPoolInstancesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPoolInstancesResponse, m.ListPoolInstancesItem]:
```

## `compute.reboot_instance`

Reboot instance

`POST /v1/instances/{instance_id}/reboot`

```python
def reboot_instance(self, instance_id: str, body: m.RebootInstanceBody | Unset = UNSET, *, options: RequestOptions | None = None) -> None:
```

## `compute.refresh_instance_pool`

Roll every member onto the pool's current launch template

`POST /v1/instance-pools/{pool_id}/refresh`

```python
def refresh_instance_pool(self, pool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.RefreshInstancePoolResponse]:
```

## `compute.reinstall_instance`

Reinstall instance

`POST /v1/instances/{instance_id}/reinstall`

```python
def reinstall_instance(self, instance_id: str, body: m.ReinstallInstanceBody | Unset = UNSET, *, options: RequestOptions | None = None) -> None:
```

## `compute.resize_instance`

Resize instance

`POST /v1/instances/{instance_id}/resize`

```python
def resize_instance(self, instance_id: str, body: m.ResizeInstanceBody, *, options: RequestOptions | None = None) -> None:
```

## `compute.start_instance`

Start instance

`POST /v1/instances/{instance_id}/start`

```python
def start_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.start_serial_console`

Open an interactive serial console

`GET /v1/instances/{instance_id}/console/serial`

```python
def start_serial_console(self, instance_id: str, *, query: m.StartSerialConsoleQuery | None = None, options: RequestOptions | None = None) -> WebSocketConnection:
```

## `compute.stop_instance`

Stop instance

`POST /v1/instances/{instance_id}/stop`

```python
def stop_instance(self, instance_id: str, *, options: RequestOptions | None = None) -> None:
```

## `compute.update_image`

Update an image's metadata

`PATCH /v1/images/{image_id}`

```python
def update_image(self, image_id: str, body: m.UpdateImageBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateImageResponse]:
```

## `compute.update_instance`

Update instance

`PATCH /v1/instances/{instance_id}`

```python
def update_instance(self, instance_id: str, body: m.UpdateInstanceBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateInstanceResponse]:
```

## `compute.update_instance_pool`

Update an instance pool's description, size, tags or launch template

`PATCH /v1/instance-pools/{pool_id}`

```python
def update_instance_pool(self, pool_id: str, body: m.UpdateInstancePoolBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateInstancePoolResponse]:
```

## `compute.update_instance_volume_attachment`

Update a volume attachment's settings

`PATCH /v1/instances/{instance_id}/volumes/{volume_id}`

```python
def update_instance_volume_attachment(self, instance_id: str, volume_id: str, body: m.UpdateInstanceVolumeAttachmentBody, *, options: RequestOptions | None = None) -> None:
```

## `dns.associate_zone_vpc`

Associate a VPC with a private zone

`POST /v1/zones/{zone_id}/vpc-associations`

```python
def associate_zone_vpc(self, zone_id: str, body: m.AssociateZoneVPCBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AssociateZoneVPCResponse]:
```

## `dns.create_record`

Create record

`POST /v1/zones/{zone_id}/records`

```python
def create_record(self, zone_id: str, body: m.CreateRecordBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateRecordResponse]:
```

## `dns.create_zone`

Create zone

`POST /v1/zones`

```python
def create_zone(self, body: m.CreateZoneBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateZoneResponse]:
```

## `dns.delete_record`

Delete record

`DELETE /v1/zones/{zone_id}/records/{record_id}`

```python
def delete_record(self, zone_id: str, record_id: str, *, options: RequestOptions | None = None) -> None:
```

## `dns.delete_zone`

Delete zone

`DELETE /v1/zones/{zone_id}`

```python
def delete_zone(self, zone_id: str, *, options: RequestOptions | None = None) -> None:
```

## `dns.delete_zone_record_import`

Discard the record-import outcome

`DELETE /v1/zones/{zone_id}/record-import`

```python
def delete_zone_record_import(self, zone_id: str, *, options: RequestOptions | None = None) -> None:
```

## `dns.dissociate_zone_vpc`

Dissociate a VPC from a private zone

`DELETE /v1/zones/{zone_id}/vpc-associations/{vpc_id}`

```python
def dissociate_zone_vpc(self, zone_id: str, vpc_id: str, *, options: RequestOptions | None = None) -> None:
```

## `dns.export_zone_file`

Export the zone as a zone file

`GET /v1/zones/{zone_id}/export`

```python
def export_zone_file(self, zone_id: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `dns.get_record`

Get record

`GET /v1/zones/{zone_id}/records/{record_id}`

```python
def get_record(self, zone_id: str, record_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRecordResponse]:
```

## `dns.get_zone`

Get zone

`GET /v1/zones/{zone_id}`

```python
def get_zone(self, zone_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetZoneResponse]:
```

## `dns.get_zone_record_import`

Get the record-import outcome

`GET /v1/zones/{zone_id}/record-import`

```python
def get_zone_record_import(self, zone_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetZoneRecordImportResponse]:
```

## `dns.import_zone_file`

Import a zone file

`POST /v1/zones/{zone_id}/import`

```python
def import_zone_file(self, zone_id: str, body: m.ImportZoneFileBody, *, options: RequestOptions | None = None) -> ApiResponse[m.ImportZoneFileResponse]:
```

## `dns.list_records`

List records

`GET /v1/zones/{zone_id}/records`

```python
def list_records(self, zone_id: str, *, query: m.ListRecordsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRecordsResponse, m.ListRecordsItem]:
```

## `dns.list_zone_vpc_associations`

List VPC associations

`GET /v1/zones/{zone_id}/vpc-associations`

```python
def list_zone_vpc_associations(self, zone_id: str, *, query: m.ListZoneVPCAssociationsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListZoneVPCAssociationsResponse, m.ListZoneVPCAssociationsItem]:
```

## `dns.list_zones`

List zones

`GET /v1/zones`

```python
def list_zones(self, *, query: m.ListZonesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListZonesResponse, m.ListZonesItem]:
```

## `dns.update_record`

Update record

`PATCH /v1/zones/{zone_id}/records/{record_id}`

```python
def update_record(self, zone_id: str, record_id: str, body: m.UpdateRecordBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateRecordResponse]:
```

## `dns.update_zone`

Update zone

`PATCH /v1/zones/{zone_id}`

```python
def update_zone(self, zone_id: str, body: m.UpdateZoneBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateZoneResponse]:
```

## `dns.verify_zone_ownership`

Verify zone ownership

`POST /v1/zones/{zone_id}/verify-ownership`

```python
def verify_zone_ownership(self, zone_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.VerifyZoneOwnershipResponse]:
```

## `iam.assume_role`

Assume role

`POST /v1/assume-role`

```python
def assume_role(self, body: m.AssumeRoleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AssumeRoleResponse]:
```

## `iam.assume_role_with_web_identity`

Assume role with web identity

`POST /v1/assume-role-with-web-identity`

```python
def assume_role_with_web_identity(self, body: m.AssumeRoleWithWebIdentityBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AssumeRoleWithWebIdentityResponse]:
```

## `iam.attach_role_policy`

Attach policy to role

`POST /v1/roles/{role_id}/policies`

```python
def attach_role_policy(self, role_id: str, body: m.AttachRolePolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `iam.attach_service_account_policy`

Attach policy to service account

`POST /v1/service-accounts/{service_account_id}/policies`

```python
def attach_service_account_policy(self, service_account_id: str, body: m.AttachServiceAccountPolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `iam.authorize_oauth_client`

Approve a CLI login and issue an authorization code

`POST /v1/oauth/authorize`

```python
def authorize_oauth_client(self, body: m.AuthorizeOAuthClientBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AuthorizeOAuthClientResponse]:
```

## `iam.create_personal_ssh_key`

Add personal SSH key

`POST /v1/auth/ssh-keys`

```python
def create_personal_ssh_key(self, body: m.CreatePersonalSSHKeyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreatePersonalSSHKeyResponse]:
```

## `iam.create_policy`

Create policy

`POST /v1/policies`

```python
def create_policy(self, body: m.CreatePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreatePolicyResponse]:
```

## `iam.create_role`

Create role

`POST /v1/roles`

```python
def create_role(self, body: m.CreateRoleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateRoleResponse]:
```

## `iam.create_service_account`

Create service account

`POST /v1/service-accounts`

```python
def create_service_account(self, body: m.CreateServiceAccountBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateServiceAccountResponse]:
```

## `iam.create_service_account_credential`

Create credential

`POST /v1/service-accounts/{service_account_id}/credentials`

```python
def create_service_account_credential(self, service_account_id: str, body: m.CreateServiceAccountCredentialBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateServiceAccountCredentialResponse]:
```

## `iam.create_service_account_ssh_key`

Add service-account SSH key

`POST /v1/service-accounts/{service_account_id}/ssh-keys`

```python
def create_service_account_ssh_key(self, service_account_id: str, body: m.CreateServiceAccountSSHKeyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateServiceAccountSSHKeyResponse]:
```

## `iam.delete_personal_ssh_key`

Revoke personal SSH key

`DELETE /v1/auth/ssh-keys/{ssh_key_id}`

```python
def delete_personal_ssh_key(self, ssh_key_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_policy`

Delete policy

`DELETE /v1/policies/{policy_id}`

```python
def delete_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_role`

Delete role

`DELETE /v1/roles/{role_id}`

```python
def delete_role(self, role_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_role_inline_policy`

Delete a role's inline policy by name

`DELETE /v1/roles/{role_id}/inline-policies/{policy_name}`

```python
def delete_role_inline_policy(self, role_id: str, policy_name: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_service_account`

Delete service account

`DELETE /v1/service-accounts/{service_account_id}`

```python
def delete_service_account(self, service_account_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_service_account_credential`

Delete credential

`DELETE /v1/service-accounts/{service_account_id}/credentials/{credential_id}`

```python
def delete_service_account_credential(self, service_account_id: str, credential_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_service_account_inline_policy`

Delete a service account's inline policy by name

`DELETE /v1/service-accounts/{service_account_id}/inline-policies/{policy_name}`

```python
def delete_service_account_inline_policy(self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.delete_service_account_ssh_key`

Revoke service-account SSH key

`DELETE /v1/service-accounts/{service_account_id}/ssh-keys/{ssh_key_id}`

```python
def delete_service_account_ssh_key(self, service_account_id: str, ssh_key_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.detach_role_policy`

Detach policy from role

`DELETE /v1/roles/{role_id}/policies/{policy_id}`

```python
def detach_role_policy(self, role_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.detach_service_account_policy`

Detach policy from service account

`DELETE /v1/service-accounts/{service_account_id}/policies/{policy_id}`

```python
def detach_service_account_policy(self, service_account_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.get_oauth_token`

Exchange an access key for a bearer token

`POST /v1/oauth/token`

```python
def get_oauth_token(self, body: m.GetOAuthTokenBody, *, options: RequestOptions | None = None) -> ApiResponse[m.GetOAuthTokenResponse]:
```

## `iam.get_personal_linux_identity`

Get personal Linux identity

`GET /v1/auth/linux-identity`

```python
def get_personal_linux_identity(self, *, options: RequestOptions | None = None) -> ApiResponse[m.GetPersonalLinuxIdentityResponse]:
```

## `iam.get_policy`

Get policy

`GET /v1/policies/{policy_id}`

```python
def get_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetPolicyResponse]:
```

## `iam.get_role`

Get role

`GET /v1/roles/{role_id}`

```python
def get_role(self, role_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRoleResponse]:
```

## `iam.get_role_inline_policy`

Get a role's inline policy by name

`GET /v1/roles/{role_id}/inline-policies/{policy_name}`

```python
def get_role_inline_policy(self, role_id: str, policy_name: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRoleInlinePolicyResponse]:
```

## `iam.get_role_permission_boundary`

Get a role's permission boundary

`GET /v1/roles/{role_id}/permission-boundary`

```python
def get_role_permission_boundary(self, role_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRolePermissionBoundaryResponse]:
```

## `iam.get_sts_session`

Get STS session

`GET /v1/sts-sessions/{session_id}`

```python
def get_sts_session(self, session_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSTSSessionResponse]:
```

## `iam.get_service_account`

Get service account

`GET /v1/service-accounts/{service_account_id}`

```python
def get_service_account(self, service_account_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetServiceAccountResponse]:
```

## `iam.get_service_account_inline_policy`

Get a service account's inline policy by name

`GET /v1/service-accounts/{service_account_id}/inline-policies/{policy_name}`

```python
def get_service_account_inline_policy(self, service_account_id: str, policy_name: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetServiceAccountInlinePolicyResponse]:
```

## `iam.get_service_account_linux_identity`

Get serviceaccount Linux identity

`GET /v1/service-accounts/{service_account_id}/linux-identity`

```python
def get_service_account_linux_identity(self, service_account_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetServiceAccountLinuxIdentityResponse]:
```

## `iam.get_service_account_permission_boundary`

Get a service account's permission boundary

`GET /v1/service-accounts/{service_account_id}/permission-boundary`

```python
def get_service_account_permission_boundary(self, service_account_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetServiceAccountPermissionBoundaryResponse]:
```

## `iam.list_personal_ssh_keys`

List personal SSH keys

`GET /v1/auth/ssh-keys`

```python
def list_personal_ssh_keys(self, *, options: RequestOptions | None = None) -> Page[m.ListPersonalSSHKeysResponse, m.ListPersonalSSHKeysItem]:
```

## `iam.list_policies`

List policies

`GET /v1/policies`

```python
def list_policies(self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
```

## `iam.list_policy_roles`

List roles with policy

`GET /v1/policies/{policy_id}/roles`

```python
def list_policy_roles(self, policy_id: str, *, query: m.ListPolicyRolesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem]:
```

## `iam.list_policy_service_accounts`

List service accounts with policy

`GET /v1/policies/{policy_id}/service-accounts`

```python
def list_policy_service_accounts(self, policy_id: str, *, query: m.ListPolicyServiceAccountsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem]:
```

## `iam.list_regions`

List regions (legacy IAM)

`GET /v1/regions`

```python
def list_regions(self, *, query: m.ListRegionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRegionsResponse, m.ListRegionsItem]:
```

## `iam.list_role_inline_policies`

List a role's inline policies

`GET /v1/roles/{role_id}/inline-policies`

```python
def list_role_inline_policies(self, role_id: str, *, query: m.ListRoleInlinePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRoleInlinePoliciesResponse, m.ListRoleInlinePoliciesItem]:
```

## `iam.list_role_policies`

List role policies

`GET /v1/roles/{role_id}/policies`

```python
def list_role_policies(self, role_id: str, *, query: m.ListRolePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem]:
```

## `iam.list_roles`

List roles

`GET /v1/roles`

```python
def list_roles(self, *, query: m.ListRolesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRolesResponse, m.ListRolesItem]:
```

## `iam.list_sts_sessions`

List STS sessions

`GET /v1/sts-sessions`

```python
def list_sts_sessions(self, *, query: m.ListSTSSessionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSTSSessionsResponse, m.ListSTSSessionsItem]:
```

## `iam.list_service_account_credentials`

List credentials

`GET /v1/service-accounts/{service_account_id}/credentials`

```python
def list_service_account_credentials(self, service_account_id: str, *, query: m.ListServiceAccountCredentialsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListServiceAccountCredentialsResponse, m.ListServiceAccountCredentialsItem]:
```

## `iam.list_service_account_inline_policies`

List a service account's inline policies

`GET /v1/service-accounts/{service_account_id}/inline-policies`

```python
def list_service_account_inline_policies(self, service_account_id: str, *, query: m.ListServiceAccountInlinePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListServiceAccountInlinePoliciesResponse, m.ListServiceAccountInlinePoliciesItem]:
```

## `iam.list_service_account_policies`

List service account policies

`GET /v1/service-accounts/{service_account_id}/policies`

```python
def list_service_account_policies(self, service_account_id: str, *, query: m.ListServiceAccountPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem]:
```

## `iam.list_service_account_ssh_keys`

List service-account SSH keys

`GET /v1/service-accounts/{service_account_id}/ssh-keys`

```python
def list_service_account_ssh_keys(self, service_account_id: str, *, options: RequestOptions | None = None) -> Page[m.ListServiceAccountSSHKeysResponse, m.ListServiceAccountSSHKeysItem]:
```

## `iam.list_service_accounts`

List service accounts

`GET /v1/service-accounts`

```python
def list_service_accounts(self, *, query: m.ListServiceAccountsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListServiceAccountsResponse, m.ListServiceAccountsItem]:
```

## `iam.put_role_inline_policy`

Create or replace a role's inline policy

`PUT /v1/roles/{role_id}/inline-policies/{policy_name}`

```python
def put_role_inline_policy(self, role_id: str, policy_name: str, body: m.PutRoleInlinePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutRoleInlinePolicyResponse]:
```

## `iam.put_service_account_inline_policy`

Create or replace a service account's inline policy

`PUT /v1/service-accounts/{service_account_id}/inline-policies/{policy_name}`

```python
def put_service_account_inline_policy(self, service_account_id: str, policy_name: str, body: m.PutServiceAccountInlinePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutServiceAccountInlinePolicyResponse]:
```

## `iam.remove_role_permission_boundary`

Remove a role's permission boundary

`DELETE /v1/roles/{role_id}/permission-boundary`

```python
def remove_role_permission_boundary(self, role_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.remove_service_account_permission_boundary`

Remove a service account's permission boundary

`DELETE /v1/service-accounts/{service_account_id}/permission-boundary`

```python
def remove_service_account_permission_boundary(self, service_account_id: str, *, options: RequestOptions | None = None) -> None:
```

## `iam.revoke_oauth_token`

Revoke a bearer token

`POST /v1/oauth/revoke`

```python
def revoke_oauth_token(self, body: m.RevokeOAuthTokenBody, *, options: RequestOptions | None = None) -> None:
```

## `iam.revoke_sts_session`

Revoke STS session

`DELETE /v1/sts-sessions/{session_id}`

```python
def revoke_sts_session(self, session_id: str, body: m.RevokeSTSSessionBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.RevokeSTSSessionResponse]:
```

## `iam.set_role_permission_boundary`

Set a role's permission boundary

`PUT /v1/roles/{role_id}/permission-boundary`

```python
def set_role_permission_boundary(self, role_id: str, body: m.SetRolePermissionBoundaryBody, *, options: RequestOptions | None = None) -> None:
```

## `iam.set_service_account_permission_boundary`

Set a service account's permission boundary

`PUT /v1/service-accounts/{service_account_id}/permission-boundary`

```python
def set_service_account_permission_boundary(self, service_account_id: str, body: m.SetServiceAccountPermissionBoundaryBody, *, options: RequestOptions | None = None) -> None:
```

## `iam.update_policy`

Update policy

`PATCH /v1/policies/{policy_id}`

```python
def update_policy(self, policy_id: str, body: m.UpdatePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdatePolicyResponse]:
```

## `iam.update_role`

Update role

`PATCH /v1/roles/{role_id}`

```python
def update_role(self, role_id: str, body: m.UpdateRoleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateRoleResponse]:
```

## `iam.update_service_account`

Update service account

`PATCH /v1/service-accounts/{service_account_id}`

```python
def update_service_account(self, service_account_id: str, body: m.UpdateServiceAccountBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateServiceAccountResponse]:
```

## `kms.cancel_key_deletion`

Cancel a scheduled deletion

`POST /v1/keys/{key_id}/cancel-deletion`

```python
def cancel_key_deletion(self, key_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.CancelKeyDeletionResponse]:
```

## `kms.create_key`

Create a KMS key

`POST /v1/keys`

```python
def create_key(self, body: m.CreateKeyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateKeyResponse]:
```

## `kms.decrypt`

Decrypt a ciphertext

`POST /v1/keys/{key_id}/decrypt`

```python
def decrypt(self, key_id: str, body: m.DecryptBody, *, options: RequestOptions | None = None) -> ApiResponse[m.DecryptResponse]:
```

## `kms.disable_key`

Disable a key

`POST /v1/keys/{key_id}/disable`

```python
def disable_key(self, key_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.DisableKeyResponse]:
```

## `kms.enable_key`

Enable a disabled key

`POST /v1/keys/{key_id}/enable`

```python
def enable_key(self, key_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.EnableKeyResponse]:
```

## `kms.encrypt`

Encrypt a payload

`POST /v1/keys/{key_id}/encrypt`

```python
def encrypt(self, key_id: str, body: m.EncryptBody, *, options: RequestOptions | None = None) -> ApiResponse[m.EncryptResponse]:
```

## `kms.generate_data_key`

Generate a fresh data key

`POST /v1/keys/{key_id}/generate-data-key`

```python
def generate_data_key(self, key_id: str, body: m.GenerateDataKeyBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.GenerateDataKeyResponse]:
```

## `kms.get_key`

Get a KMS key

`GET /v1/keys/{key_id}`

```python
def get_key(self, key_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetKeyResponse]:
```

## `kms.list_keys`

List KMS keys

`GET /v1/keys`

```python
def list_keys(self, *, query: m.ListKeysQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListKeysResponse, m.ListKeysItem]:
```

## `kms.schedule_key_deletion`

Schedule key for deletion

`POST /v1/keys/{key_id}/schedule-deletion`

```python
def schedule_key_deletion(self, key_id: str, body: m.ScheduleKeyDeletionBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.ScheduleKeyDeletionResponse]:
```

## `kms.sign`

Sign a message

`POST /v1/keys/{key_id}/sign`

```python
def sign(self, key_id: str, body: m.SignBody, *, options: RequestOptions | None = None) -> ApiResponse[m.SignResponse]:
```

## `kms.update_key`

Update key metadata

`PATCH /v1/keys/{key_id}`

```python
def update_key(self, key_id: str, body: m.UpdateKeyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateKeyResponse]:
```

## `kms.verify`

Verify a signature

`POST /v1/keys/{key_id}/verify`

```python
def verify(self, key_id: str, body: m.VerifyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.VerifyResponse]:
```

## `loadbalancer.attach_listener_certificate`

Attach an additional certificate to an HTTPS listener

`POST /v1/load-balancers/{id}/listeners/{listener_id}/certificates`

```python
def attach_listener_certificate(self, id: str, listener_id: str, body: m.AttachListenerCertificateBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachListenerCertificateResponse]:
```

## `loadbalancer.attach_target`

Attach a target to this group

`POST /v1/target-groups/{id}/targets`

```python
def attach_target(self, id: str, body: m.AttachTargetBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachTargetResponse]:
```

## `loadbalancer.create_listener`

Create a listener on this load balancer

`POST /v1/load-balancers/{id}/listeners`

```python
def create_listener(self, id: str, body: m.CreateListenerBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateListenerResponse]:
```

## `loadbalancer.create_load_balancer`

Create a load balancer

`POST /v1/load-balancers`

```python
def create_load_balancer(self, body: m.CreateLoadBalancerBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateLoadBalancerResponse]:
```

## `loadbalancer.create_rule`

Create a routing rule on this listener (HTTP/HTTPS only)

`POST /v1/load-balancers/{id}/listeners/{listener_id}/rules`

```python
def create_rule(self, id: str, listener_id: str, body: m.CreateRuleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateRuleResponse]:
```

## `loadbalancer.create_target_group`

Create a target group

`POST /v1/target-groups`

```python
def create_target_group(self, body: m.CreateTargetGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateTargetGroupResponse]:
```

## `loadbalancer.delete_listener`

Delete a listener

`DELETE /v1/load-balancers/{id}/listeners/{listener_id}`

```python
def delete_listener(self, id: str, listener_id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.delete_load_balancer`

Delete a load balancer

`DELETE /v1/load-balancers/{id}`

```python
def delete_load_balancer(self, id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.delete_rule_in_listener`

Delete a routing rule

`DELETE /v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}`

```python
def delete_rule_in_listener(self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.delete_target_group`

Delete a target group

`DELETE /v1/target-groups/{id}`

```python
def delete_target_group(self, id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.detach_listener_certificate`

Detach a certificate from an HTTPS listener

`DELETE /v1/load-balancers/{id}/listeners/{listener_id}/certificates/{certificate_id}`

```python
def detach_listener_certificate(self, id: str, listener_id: str, certificate_id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.detach_target`

Detach a target

`DELETE /v1/target-groups/{id}/targets/{target_id}`

```python
def detach_target(self, id: str, target_id: str, *, options: RequestOptions | None = None) -> None:
```

## `loadbalancer.get_listener`

Get a listener

`GET /v1/load-balancers/{id}/listeners/{listener_id}`

```python
def get_listener(self, id: str, listener_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetListenerResponse]:
```

## `loadbalancer.get_load_balancer`

Get a load balancer

`GET /v1/load-balancers/{id}`

```python
def get_load_balancer(self, id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetLoadBalancerResponse]:
```

## `loadbalancer.get_rule`

Get a routing rule

`GET /v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}`

```python
def get_rule(self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRuleResponse]:
```

## `loadbalancer.get_target`

Get a target

`GET /v1/target-groups/{id}/targets/{target_id}`

```python
def get_target(self, id: str, target_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetTargetResponse]:
```

## `loadbalancer.get_target_group`

Get a target group

`GET /v1/target-groups/{id}`

```python
def get_target_group(self, id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetTargetGroupResponse]:
```

## `loadbalancer.list_listeners`

List this load balancer's listeners

`GET /v1/load-balancers/{id}/listeners`

```python
def list_listeners(self, id: str, *, query: m.ListListenersQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListListenersResponse, m.ListListenersItem]:
```

## `loadbalancer.list_load_balancer_replicas`

List the LB's instance replicas with live health

`GET /v1/load-balancers/{id}/replicas`

```python
def list_load_balancer_replicas(self, id: str, *, query: m.ListLoadBalancerReplicasQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListLoadBalancerReplicasResponse, m.ListLoadBalancerReplicasItem]:
```

## `loadbalancer.list_load_balancers`

List load balancers

`GET /v1/load-balancers`

```python
def list_load_balancers(self, *, query: m.ListLoadBalancersQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListLoadBalancersResponse, m.ListLoadBalancersItem]:
```

## `loadbalancer.list_rules`

List this listener's rules

`GET /v1/load-balancers/{id}/listeners/{listener_id}/rules`

```python
def list_rules(self, id: str, listener_id: str, *, query: m.ListRulesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRulesResponse, m.ListRulesItem]:
```

## `loadbalancer.list_target_groups`

List target groups

`GET /v1/target-groups`

```python
def list_target_groups(self, *, query: m.ListTargetGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListTargetGroupsResponse, m.ListTargetGroupsItem]:
```

## `loadbalancer.list_targets`

List targets in this group

`GET /v1/target-groups/{id}/targets`

```python
def list_targets(self, id: str, *, query: m.ListTargetsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListTargetsResponse, m.ListTargetsItem]:
```

## `loadbalancer.update_listener`

Patch a listener (rotate cert, change default target group)

`PATCH /v1/load-balancers/{id}/listeners/{listener_id}`

```python
def update_listener(self, id: str, listener_id: str, body: m.UpdateListenerBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateListenerResponse]:
```

## `loadbalancer.update_load_balancer`

Scale or resize a load balancer

`PATCH /v1/load-balancers/{id}`

```python
def update_load_balancer(self, id: str, body: m.UpdateLoadBalancerBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateLoadBalancerResponse]:
```

## `loadbalancer.update_rule`

Update a routing rule (full replace)

`PATCH /v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}`

```python
def update_rule(self, id: str, listener_id: str, rule_id: str, body: m.UpdateRuleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateRuleResponse]:
```

## `loadbalancer.update_target_group`

Update target group health checks, framing, or stickiness

`PATCH /v1/target-groups/{id}`

```python
def update_target_group(self, id: str, body: m.UpdateTargetGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateTargetGroupResponse]:
```

## `network.attach_floating_ip`

Attach a floating IP to an interface

`POST /v1/floating-ips/{floating_ip_id}/attach`

```python
def attach_floating_ip(self, floating_ip_id: str, body: m.AttachFloatingIpBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachFloatingIpResponse]:
```

## `network.attach_internet_gateway`

Attach internet gateway to a VPC

`POST /v1/internet-gateways/{internet_gateway_id}/attach`

```python
def attach_internet_gateway(self, internet_gateway_id: str, body: m.AttachInternetGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AttachInternetGatewayResponse]:
```

## `network.create_egress_only_gateway`

Create egress-only gateway

`POST /v1/egress-only-gateways`

```python
def create_egress_only_gateway(self, body: m.CreateEgressOnlyGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateEgressOnlyGatewayResponse]:
```

## `network.create_floating_ip`

Allocate floating IP

`POST /v1/floating-ips`

```python
def create_floating_ip(self, body: m.CreateFloatingIpBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateFloatingIpResponse]:
```

## `network.create_interface`

Create interface

`POST /v1/interfaces`

```python
def create_interface(self, body: m.CreateInterfaceBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInterfaceResponse]:
```

## `network.create_interface_address`

Create interface address

`POST /v1/interfaces/{interface_id}/addresses`

```python
def create_interface_address(self, interface_id: str, body: m.CreateInterfaceAddressBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInterfaceAddressResponse]:
```

## `network.create_interface_prefix`

Create interface prefix

`POST /v1/interfaces/{interface_id}/prefixes`

```python
def create_interface_prefix(self, interface_id: str, body: m.CreateInterfacePrefixBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInterfacePrefixResponse]:
```

## `network.create_internet_gateway`

Create internet gateway

`POST /v1/internet-gateways`

```python
def create_internet_gateway(self, body: m.CreateInternetGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateInternetGatewayResponse]:
```

## `network.create_nat_gateway`

Create NAT gateway

`POST /v1/nat-gateways`

```python
def create_nat_gateway(self, body: m.CreateNATGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateNATGatewayResponse]:
```

## `network.create_prefix_pool`

Create prefix pool

`POST /v1/vpcs/{vpc_id}/prefix-pools`

```python
def create_prefix_pool(self, vpc_id: str, body: m.CreatePrefixPoolBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreatePrefixPoolResponse]:
```

## `network.create_route`

Create route

`POST /v1/route-tables/{route_table_id}/routes`

```python
def create_route(self, route_table_id: str, body: m.CreateRouteBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateRouteResponse]:
```

## `network.create_route_table`

Create route table

`POST /v1/route-tables`

```python
def create_route_table(self, body: m.CreateRouteTableBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateRouteTableResponse]:
```

## `network.create_security_group`

Create security group

`POST /v1/security-groups`

```python
def create_security_group(self, body: m.CreateSecurityGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSecurityGroupResponse]:
```

## `network.create_security_group_rule`

Create security group rule

`POST /v1/security-groups/{security_group_id}/rules`

```python
def create_security_group_rule(self, security_group_id: str, body: m.CreateSecurityGroupRuleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSecurityGroupRuleResponse]:
```

## `network.create_subnet`

Create subnet

`POST /v1/subnets`

```python
def create_subnet(self, body: m.CreateSubnetBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSubnetResponse]:
```

## `network.create_vpc`

Create VPC

`POST /v1/vpcs`

```python
def create_vpc(self, body: m.CreateVpcBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateVpcResponse]:
```

## `network.delete_egress_only_gateway`

Delete egress-only gateway

`DELETE /v1/egress-only-gateways/{egress_only_gateway_id}`

```python
def delete_egress_only_gateway(self, egress_only_gateway_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_floating_ip`

Release floating IP

`DELETE /v1/floating-ips/{floating_ip_id}`

```python
def delete_floating_ip(self, floating_ip_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_interface`

Delete interface

`DELETE /v1/interfaces/{interface_id}`

```python
def delete_interface(self, interface_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_interface_address`

Delete interface address

`DELETE /v1/interfaces/{interface_id}/addresses/{address_id}`

```python
def delete_interface_address(self, interface_id: str, address_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_interface_prefix`

Delete interface prefix

`DELETE /v1/interfaces/{interface_id}/prefixes/{prefix_id}`

```python
def delete_interface_prefix(self, interface_id: str, prefix_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_internet_gateway`

Delete internet gateway

`DELETE /v1/internet-gateways/{internet_gateway_id}`

```python
def delete_internet_gateway(self, internet_gateway_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_nat_gateway`

Delete NAT gateway

`DELETE /v1/nat-gateways/{nat_gateway_id}`

```python
def delete_nat_gateway(self, nat_gateway_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_prefix_pool`

Delete prefix pool

`DELETE /v1/vpcs/{vpc_id}/prefix-pools/{pool_id}`

```python
def delete_prefix_pool(self, vpc_id: str, pool_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_route`

Delete route

`DELETE /v1/route-tables/{route_table_id}/routes/{route_id}`

```python
def delete_route(self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_route_table`

Delete route table

`DELETE /v1/route-tables/{route_table_id}`

```python
def delete_route_table(self, route_table_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_security_group`

Delete security group

`DELETE /v1/security-groups/{security_group_id}`

```python
def delete_security_group(self, security_group_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_security_group_rule`

Delete security group rule

`DELETE /v1/security-groups/{security_group_id}/rules/{rule_id}`

```python
def delete_security_group_rule(self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_subnet`

Delete subnet

`DELETE /v1/subnets/{subnet_id}`

```python
def delete_subnet(self, subnet_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.delete_vpc`

Delete VPC

`DELETE /v1/vpcs/{vpc_id}`

```python
def delete_vpc(self, vpc_id: str, *, options: RequestOptions | None = None) -> None:
```

## `network.detach_floating_ip`

Detach a floating IP

`POST /v1/floating-ips/{floating_ip_id}/detach`

```python
def detach_floating_ip(self, floating_ip_id: str, body: m.DetachFloatingIpBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.DetachFloatingIpResponse]:
```

## `network.detach_internet_gateway`

Detach internet gateway from its VPC

`POST /v1/internet-gateways/{internet_gateway_id}/detach`

```python
def detach_internet_gateway(self, internet_gateway_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.DetachInternetGatewayResponse]:
```

## `network.get_egress_only_gateway`

Get egress-only gateway

`GET /v1/egress-only-gateways/{egress_only_gateway_id}`

```python
def get_egress_only_gateway(self, egress_only_gateway_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetEgressOnlyGatewayResponse]:
```

## `network.get_floating_ip`

Get floating IP

`GET /v1/floating-ips/{floating_ip_id}`

```python
def get_floating_ip(self, floating_ip_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetFloatingIpResponse]:
```

## `network.get_interface`

Get interface

`GET /v1/interfaces/{interface_id}`

```python
def get_interface(self, interface_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInterfaceResponse]:
```

## `network.get_interface_address`

Get interface address

`GET /v1/interfaces/{interface_id}/addresses/{address_id}`

```python
def get_interface_address(self, interface_id: str, address_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInterfaceAddressResponse]:
```

## `network.get_internet_gateway`

Get internet gateway

`GET /v1/internet-gateways/{internet_gateway_id}`

```python
def get_internet_gateway(self, internet_gateway_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInternetGatewayResponse]:
```

## `network.get_nat_gateway`

Get NAT gateway

`GET /v1/nat-gateways/{nat_gateway_id}`

```python
def get_nat_gateway(self, nat_gateway_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetNATGatewayResponse]:
```

## `network.get_route`

Get route

`GET /v1/route-tables/{route_table_id}/routes/{route_id}`

```python
def get_route(self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRouteResponse]:
```

## `network.get_route_table`

Get route table

`GET /v1/route-tables/{route_table_id}`

```python
def get_route_table(self, route_table_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRouteTableResponse]:
```

## `network.get_security_group`

Get security group

`GET /v1/security-groups/{security_group_id}`

```python
def get_security_group(self, security_group_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSecurityGroupResponse]:
```

## `network.get_security_group_rule`

Get security group rule

`GET /v1/security-groups/{security_group_id}/rules/{rule_id}`

```python
def get_security_group_rule(self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSecurityGroupRuleResponse]:
```

## `network.get_subnet`

Get subnet

`GET /v1/subnets/{subnet_id}`

```python
def get_subnet(self, subnet_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSubnetResponse]:
```

## `network.get_vpc`

Get VPC

`GET /v1/vpcs/{vpc_id}`

```python
def get_vpc(self, vpc_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetVpcResponse]:
```

## `network.list_egress_only_gateway_routes`

List egress-only gateway routes

`GET /v1/egress-only-gateways/{egress_only_gateway_id}/routes`

```python
def list_egress_only_gateway_routes(self, egress_only_gateway_id: str, *, query: m.ListEgressOnlyGatewayRoutesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListEgressOnlyGatewayRoutesResponse, m.ListEgressOnlyGatewayRoutesItem]:
```

## `network.list_egress_only_gateways`

List egress-only gateways

`GET /v1/egress-only-gateways`

```python
def list_egress_only_gateways(self, *, query: m.ListEgressOnlyGatewaysQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListEgressOnlyGatewaysResponse, m.ListEgressOnlyGatewaysItem]:
```

## `network.list_floating_ips`

List floating IPs

`GET /v1/floating-ips`

```python
def list_floating_ips(self, *, query: m.ListFloatingIpsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListFloatingIpsResponse, m.ListFloatingIpsItem]:
```

## `network.list_interface_addresses`

List interface addresses

`GET /v1/interfaces/{interface_id}/addresses`

```python
def list_interface_addresses(self, interface_id: str, *, options: RequestOptions | None = None) -> Page[m.ListInterfaceAddressesResponse, m.ListInterfaceAddressesItem]:
```

## `network.list_interface_prefixes`

List interface prefixes

`GET /v1/interfaces/{interface_id}/prefixes`

```python
def list_interface_prefixes(self, interface_id: str, *, options: RequestOptions | None = None) -> Page[m.ListInterfacePrefixesResponse, m.ListInterfacePrefixesItem]:
```

## `network.list_interface_security_groups`

List interface security-group membership

`GET /v1/interfaces/{interface_id}/security-groups`

```python
def list_interface_security_groups(self, interface_id: str, *, query: m.ListInterfaceSecurityGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInterfaceSecurityGroupsResponse, m.ListInterfaceSecurityGroupsItem]:
```

## `network.list_interfaces`

List interfaces

`GET /v1/interfaces`

```python
def list_interfaces(self, *, query: m.ListInterfacesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInterfacesResponse, m.ListInterfacesItem]:
```

## `network.list_internet_gateway_routes`

List internet gateway routes

`GET /v1/internet-gateways/{internet_gateway_id}/routes`

```python
def list_internet_gateway_routes(self, internet_gateway_id: str, *, query: m.ListInternetGatewayRoutesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInternetGatewayRoutesResponse, m.ListInternetGatewayRoutesItem]:
```

## `network.list_internet_gateways`

List internet gateways

`GET /v1/internet-gateways`

```python
def list_internet_gateways(self, *, query: m.ListInternetGatewaysQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInternetGatewaysResponse, m.ListInternetGatewaysItem]:
```

## `network.list_nat_gateway_routes`

List NAT gateway routes

`GET /v1/nat-gateways/{nat_gateway_id}/routes`

```python
def list_nat_gateway_routes(self, nat_gateway_id: str, *, query: m.ListNATGatewayRoutesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListNATGatewayRoutesResponse, m.ListNATGatewayRoutesItem]:
```

## `network.list_nat_gateways`

List NAT gateways

`GET /v1/nat-gateways`

```python
def list_nat_gateways(self, *, query: m.ListNATGatewaysQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListNATGatewaysResponse, m.ListNATGatewaysItem]:
```

## `network.list_prefix_pools`

List prefix pools

`GET /v1/vpcs/{vpc_id}/prefix-pools`

```python
def list_prefix_pools(self, vpc_id: str, *, options: RequestOptions | None = None) -> Page[m.ListPrefixPoolsResponse, m.ListPrefixPoolsItem]:
```

## `network.list_route_tables`

List route tables

`GET /v1/route-tables`

```python
def list_route_tables(self, *, query: m.ListRouteTablesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRouteTablesResponse, m.ListRouteTablesItem]:
```

## `network.list_routes`

List routes

`GET /v1/route-tables/{route_table_id}/routes`

```python
def list_routes(self, route_table_id: str, *, query: m.ListRoutesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRoutesResponse, m.ListRoutesItem]:
```

## `network.list_security_group_rules`

List security group rules

`GET /v1/security-groups/{security_group_id}/rules`

```python
def list_security_group_rules(self, security_group_id: str, *, query: m.ListSecurityGroupRulesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSecurityGroupRulesResponse, m.ListSecurityGroupRulesItem]:
```

## `network.list_security_groups`

List security groups

`GET /v1/security-groups`

```python
def list_security_groups(self, *, query: m.ListSecurityGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSecurityGroupsResponse, m.ListSecurityGroupsItem]:
```

## `network.list_subnets`

List subnets

`GET /v1/subnets`

```python
def list_subnets(self, *, query: m.ListSubnetsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSubnetsResponse, m.ListSubnetsItem]:
```

## `network.list_vpcs`

List VPCs

`GET /v1/vpcs`

```python
def list_vpcs(self, *, query: m.ListVpcsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListVpcsResponse, m.ListVpcsItem]:
```

## `network.set_interface_security_groups`

Set interface security-group membership

`PUT /v1/interfaces/{interface_id}/security-groups`

```python
def set_interface_security_groups(self, interface_id: str, body: m.SetInterfaceSecurityGroupsBody, *, options: RequestOptions | None = None) -> ApiResponse[m.SetInterfaceSecurityGroupsResponse]:
```

## `network.update_egress_only_gateway`

Update egress-only gateway

`PATCH /v1/egress-only-gateways/{egress_only_gateway_id}`

```python
def update_egress_only_gateway(self, egress_only_gateway_id: str, body: m.UpdateEgressOnlyGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateEgressOnlyGatewayResponse]:
```

## `network.update_floating_ip`

Update floating IP

`PATCH /v1/floating-ips/{floating_ip_id}`

```python
def update_floating_ip(self, floating_ip_id: str, body: m.UpdateFloatingIpBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateFloatingIpResponse]:
```

## `network.update_interface`

Update interface

`PATCH /v1/interfaces/{interface_id}`

```python
def update_interface(self, interface_id: str, body: m.UpdateInterfaceBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateInterfaceResponse]:
```

## `network.update_internet_gateway`

Update internet gateway

`PATCH /v1/internet-gateways/{internet_gateway_id}`

```python
def update_internet_gateway(self, internet_gateway_id: str, body: m.UpdateInternetGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateInternetGatewayResponse]:
```

## `network.update_nat_gateway`

Update NAT gateway

`PATCH /v1/nat-gateways/{nat_gateway_id}`

```python
def update_nat_gateway(self, nat_gateway_id: str, body: m.UpdateNATGatewayBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateNATGatewayResponse]:
```

## `network.update_route`

Update route

`PATCH /v1/route-tables/{route_table_id}/routes/{route_id}`

```python
def update_route(self, route_table_id: str, route_id: str, body: m.UpdateRouteBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateRouteResponse]:
```

## `network.update_route_table`

Update route table

`PATCH /v1/route-tables/{route_table_id}`

```python
def update_route_table(self, route_table_id: str, body: m.UpdateRouteTableBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateRouteTableResponse]:
```

## `network.update_security_group`

Update security group

`PATCH /v1/security-groups/{security_group_id}`

```python
def update_security_group(self, security_group_id: str, body: m.UpdateSecurityGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateSecurityGroupResponse]:
```

## `network.update_subnet`

Update subnet

`PATCH /v1/subnets/{subnet_id}`

```python
def update_subnet(self, subnet_id: str, body: m.UpdateSubnetBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateSubnetResponse]:
```

## `network.update_vpc`

Update VPC

`PATCH /v1/vpcs/{vpc_id}`

```python
def update_vpc(self, vpc_id: str, body: m.UpdateVpcBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateVpcResponse]:
```

## `quota.list_quotas`

List quotas

`GET /v1/quotas`

```python
def list_quotas(self, *, query: m.ListQuotasQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListQuotasResponse, m.ListQuotasItem]:
```

## `secrets.create_secret`

Create a new secret with an initial value

`POST /v1/secrets`

```python
def create_secret(self, body: m.CreateSecretBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSecretResponse]:
```

## `secrets.delete_secret`

Schedule deletion (soft delete with recovery window)

`DELETE /v1/secrets/{secret_id}`

```python
def delete_secret(self, secret_id: str, body: m.DeleteSecretBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.DeleteSecretResponse]:
```

## `secrets.describe_secret`

Describe a secret (no value)

`GET /v1/secrets/{secret_id}`

```python
def describe_secret(self, secret_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.DescribeSecretResponse]:
```

## `secrets.get_secret_value`

Read the current value (or a specific version)

`GET /v1/secrets/{secret_id}/value`

```python
def get_secret_value(self, secret_id: str, *, query: m.GetSecretValueQuery | None = None, options: RequestOptions | None = None) -> ApiResponse[m.GetSecretValueResponse]:
```

## `secrets.list_secrets`

List secrets

`GET /v1/secrets`

```python
def list_secrets(self, *, query: m.ListSecretsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSecretsResponse, m.ListSecretsItem]:
```

## `secrets.list_versions`

List versions

`GET /v1/secrets/{secret_id}/versions`

```python
def list_versions(self, secret_id: str, *, query: m.ListVersionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListVersionsResponse, m.ListVersionsItem]:
```

## `secrets.put_secret_value`

Store a new version (becomes current)

`POST /v1/secrets/{secret_id}/value`

```python
def put_secret_value(self, secret_id: str, body: m.PutSecretValueBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutSecretValueResponse]:
```

## `secrets.restore_secret`

Restore a secret from the recovery window

`POST /v1/secrets/{secret_id}/restore`

```python
def restore_secret(self, secret_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.RestoreSecretResponse]:
```

## `secrets.update_secret`

Update mutable metadata

`PATCH /v1/secrets/{secret_id}`

```python
def update_secret(self, secret_id: str, body: m.UpdateSecretBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateSecretResponse]:
```

## `storage.abort_multipart_upload`

Abort a multipart upload

`DELETE /v1/buckets/{bucket}/multipart-uploads/{upload_id}`

```python
def abort_multipart_upload(self, bucket: str, upload_id: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.complete_multipart_upload`

Complete a multipart upload

`POST /v1/buckets/{bucket}/multipart-uploads/{upload_id}/complete`

```python
def complete_multipart_upload(self, bucket: str, upload_id: str, body: m.CompleteMultipartUploadBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CompleteMultipartUploadResponse]:
```

## `storage.create_bucket`

Create bucket

`POST /v1/buckets`

```python
def create_bucket(self, body: m.CreateBucketBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateBucketResponse]:
```

## `storage.create_snapshot`

Create snapshot

`POST /v1/snapshots`

```python
def create_snapshot(self, body: m.CreateSnapshotBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSnapshotResponse]:
```

## `storage.create_snapshot_policy`

Create snapshot policy

`POST /v1/snapshot-policies`

```python
def create_snapshot_policy(self, body: m.CreateSnapshotPolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateSnapshotPolicyResponse]:
```

## `storage.create_volume`

Create volume

`POST /v1/volumes`

```python
def create_volume(self, body: m.CreateVolumeBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateVolumeResponse]:
```

## `storage.delete_bucket`

Delete bucket

`DELETE /v1/buckets/{bucket}`

```python
def delete_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.DeleteBucketResponse]:
```

## `storage.delete_bucket_cors`

Delete bucket CORS configuration

`DELETE /v1/buckets/{bucket}/cors`

```python
def delete_bucket_cors(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_bucket_encryption`

Delete bucket encryption configuration

`DELETE /v1/buckets/{bucket}/encryption`

```python
def delete_bucket_encryption(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_bucket_lifecycle`

Delete bucket lifecycle configuration

`DELETE /v1/buckets/{bucket}/lifecycle`

```python
def delete_bucket_lifecycle(self, bucket: str, *, options: RequestOptions) -> None:
```

## `storage.delete_bucket_object_lock`

Delete bucket object-lock configuration

`DELETE /v1/buckets/{bucket}/object-lock`

```python
def delete_bucket_object_lock(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_bucket_policy`

Delete bucket policy

`DELETE /v1/buckets/{bucket}/policy`

```python
def delete_bucket_policy(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_bucket_tagging`

Delete bucket tag set

`DELETE /v1/buckets/{bucket}/tagging`

```python
def delete_bucket_tagging(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_object`

Delete object

`DELETE /v1/buckets/{bucket}/objects/{key}`

```python
def delete_object(self, bucket: str, key: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_snapshot`

Delete snapshot

`DELETE /v1/snapshots/{snapshot_id}`

```python
def delete_snapshot(self, snapshot_id: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_snapshot_policy`

Delete snapshot policy

`DELETE /v1/snapshot-policies/{policy_id}`

```python
def delete_snapshot_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.delete_volume`

Delete volume

`DELETE /v1/volumes/{volume_id}`

```python
def delete_volume(self, volume_id: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.extend_volume`

Extend volume

`POST /v1/volumes/{volume_id}/extend`

```python
def extend_volume(self, volume_id: str, body: m.ExtendVolumeBody, *, options: RequestOptions | None = None) -> ApiResponse[m.ExtendVolumeResponse]:
```

## `storage.get_bucket_cors`

Get bucket CORS configuration

`GET /v1/buckets/{bucket}/cors`

```python
def get_bucket_cors(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketCORSResponse]:
```

## `storage.get_bucket_encryption`

Get bucket encryption configuration

`GET /v1/buckets/{bucket}/encryption`

```python
def get_bucket_encryption(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketEncryptionResponse]:
```

## `storage.get_bucket_lifecycle`

Get bucket lifecycle configuration

`GET /v1/buckets/{bucket}/lifecycle`

```python
def get_bucket_lifecycle(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketLifecycleResponse]:
```

## `storage.get_bucket_object_lock`

Get bucket object-lock configuration

`GET /v1/buckets/{bucket}/object-lock`

```python
def get_bucket_object_lock(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketObjectLockResponse]:
```

## `storage.get_bucket_policy`

Get bucket policy

`GET /v1/buckets/{bucket}/policy`

```python
def get_bucket_policy(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketPolicyResponse]:
```

## `storage.get_bucket_tagging`

Get bucket tag set

`GET /v1/buckets/{bucket}/tagging`

```python
def get_bucket_tagging(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketTaggingResponse]:
```

## `storage.get_bucket_versioning`

Get bucket versioning state

`GET /v1/buckets/{bucket}/versioning`

```python
def get_bucket_versioning(self, bucket: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetBucketVersioningResponse]:
```

## `storage.get_object`

Download object

`GET /v1/buckets/{bucket}/objects/{key}`

```python
def get_object(self, bucket: str, key: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `storage.get_snapshot`

Get snapshot

`GET /v1/snapshots/{snapshot_id}`

```python
def get_snapshot(self, snapshot_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSnapshotResponse]:
```

## `storage.get_snapshot_policy`

Get snapshot policy

`GET /v1/snapshot-policies/{policy_id}`

```python
def get_snapshot_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetSnapshotPolicyResponse]:
```

## `storage.get_volume`

Get volume

`GET /v1/volumes/{volume_id}`

```python
def get_volume(self, volume_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetVolumeResponse]:
```

## `storage.head_bucket`

Head bucket

`HEAD /v1/buckets/{bucket}`

```python
def head_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `storage.head_object`

Head object

`HEAD /v1/buckets/{bucket}/objects/{key}`

```python
def head_object(self, bucket: str, key: str, *, options: RequestOptions | None = None) -> httpx.Response:
```

## `storage.initiate_multipart_upload`

Initiate a multipart upload

`POST /v1/buckets/{bucket}/multipart-uploads`

```python
def initiate_multipart_upload(self, bucket: str, body: m.InitiateMultipartUploadBody, *, options: RequestOptions | None = None) -> ApiResponse[m.InitiateMultipartUploadResponse]:
```

## `storage.list_buckets`

List buckets

`GET /v1/buckets`

```python
def list_buckets(self, *, query: m.ListBucketsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListBucketsResponse, m.ListBucketsItem]:
```

## `storage.list_multipart_uploads`

List in-flight multipart uploads

`GET /v1/buckets/{bucket}/multipart-uploads`

```python
def list_multipart_uploads(self, bucket: str, *, query: m.ListMultipartUploadsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListMultipartUploadsResponse, m.ListMultipartUploadsItem]:
```

## `storage.list_object_versions`

List object versions

`GET /v1/buckets/{bucket}/object-versions`

```python
def list_object_versions(self, bucket: str, *, query: m.ListObjectVersionsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListObjectVersionsResponse, m.ListObjectVersionsItem]:
```

## `storage.list_objects`

List objects

`GET /v1/buckets/{bucket}/objects`

```python
def list_objects(self, bucket: str, *, query: m.ListObjectsQuery | None = None, options: RequestOptions | None = None) -> ApiResponse[m.ListObjectsResponse]:
```

## `storage.list_parts`

List uploaded parts

`GET /v1/buckets/{bucket}/multipart-uploads/{upload_id}/parts`

```python
def list_parts(self, bucket: str, upload_id: str, *, options: RequestOptions | None = None) -> Page[m.ListPartsResponse, m.ListPartsItem]:
```

## `storage.list_snapshot_policies`

List snapshot policies

`GET /v1/snapshot-policies`

```python
def list_snapshot_policies(self, *, query: m.ListSnapshotPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSnapshotPoliciesResponse, m.ListSnapshotPoliciesItem]:
```

## `storage.list_snapshots`

List snapshots

`GET /v1/snapshots`

```python
def list_snapshots(self, *, query: m.ListSnapshotsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListSnapshotsResponse, m.ListSnapshotsItem]:
```

## `storage.list_volume_types`

List volume types

`GET /v1/volume-types`

```python
def list_volume_types(self, *, query: m.ListVolumeTypesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListVolumeTypesResponse, m.ListVolumeTypesItem]:
```

## `storage.list_volumes`

List volumes

`GET /v1/volumes`

```python
def list_volumes(self, *, query: m.ListVolumesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListVolumesResponse, m.ListVolumesItem]:
```

## `storage.put_bucket_cors`

Put bucket CORS configuration

`PUT /v1/buckets/{bucket}/cors`

```python
def put_bucket_cors(self, bucket: str, body: m.PutBucketCORSBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_deletion_protection`

Set bucket deletion protection

`PUT /v1/buckets/{bucket}/deletion-protection`

```python
def put_bucket_deletion_protection(self, bucket: str, body: m.PutBucketDeletionProtectionBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_encryption`

Put bucket encryption configuration

`PUT /v1/buckets/{bucket}/encryption`

```python
def put_bucket_encryption(self, bucket: str, body: m.PutBucketEncryptionBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_lifecycle`

Put bucket lifecycle configuration

`PUT /v1/buckets/{bucket}/lifecycle`

```python
def put_bucket_lifecycle(self, bucket: str, body: m.PutBucketLifecycleBody, *, options: RequestOptions) -> None:
```

## `storage.put_bucket_object_lock`

Put bucket object-lock configuration

`PUT /v1/buckets/{bucket}/object-lock`

```python
def put_bucket_object_lock(self, bucket: str, body: m.PutBucketObjectLockBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_policy`

Put bucket policy

`PUT /v1/buckets/{bucket}/policy`

```python
def put_bucket_policy(self, bucket: str, body: m.PutBucketPolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_tagging`

Put bucket tag set

`PUT /v1/buckets/{bucket}/tagging`

```python
def put_bucket_tagging(self, bucket: str, body: m.PutBucketTaggingBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_bucket_versioning`

Set bucket versioning state

`PUT /v1/buckets/{bucket}/versioning`

```python
def put_bucket_versioning(self, bucket: str, body: m.PutBucketVersioningBody, *, options: RequestOptions | None = None) -> None:
```

## `storage.put_object`

Upload object

`PUT /v1/buckets/{bucket}/objects/{key}`

```python
def put_object(self, bucket: str, key: str, body: BinaryBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutObjectResponse]:
```

## `storage.restore_bucket`

Restore a bucket pending deletion

`POST /v1/buckets/{bucket}/restore`

```python
def restore_bucket(self, bucket: str, *, options: RequestOptions | None = None) -> None:
```

## `storage.update_snapshot`

Update snapshot metadata

`PATCH /v1/snapshots/{snapshot_id}`

```python
def update_snapshot(self, snapshot_id: str, body: m.UpdateSnapshotBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateSnapshotResponse]:
```

## `storage.update_snapshot_policy`

Update snapshot policy

`PATCH /v1/snapshot-policies/{policy_id}`

```python
def update_snapshot_policy(self, policy_id: str, body: m.UpdateSnapshotPolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateSnapshotPolicyResponse]:
```

## `storage.update_volume`

Update volume metadata

`PATCH /v1/volumes/{volume_id}`

```python
def update_volume(self, volume_id: str, body: m.UpdateVolumeBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateVolumeResponse]:
```

## `storage.update_volume_performance`

Update provisioned performance

`POST /v1/volumes/{volume_id}/performance`

```python
def update_volume_performance(self, volume_id: str, body: m.UpdateVolumePerformanceBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateVolumePerformanceResponse]:
```

## `storage.upload_part`

Upload a part

`PUT /v1/buckets/{bucket}/multipart-uploads/{upload_id}/parts/{part_number}`

```python
def upload_part(self, bucket: str, upload_id: str, part_number: str, body: BinaryBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UploadPartResponse]:
```

## `telemetry.create_log_group`

Create a log group

`POST /v1/log-groups`

```python
def create_log_group(self, body: m.CreateLogGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateLogGroupResponse]:
```

## `telemetry.delete_log_group`

Delete a log group

`DELETE /v1/log-groups/{id}`

```python
def delete_log_group(self, id: str, *, options: RequestOptions | None = None) -> None:
```

## `telemetry.delete_trace_settings`

Delete trace settings

`DELETE /v1/trace-settings`

```python
def delete_trace_settings(self, *, options: RequestOptions | None = None) -> None:
```

## `telemetry.get_log`

Get a single log record by id

`GET /v1/logs/{log_id}`

```python
def get_log(self, log_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetLogResponse]:
```

## `telemetry.get_log_group`

Get a log group by id

`GET /v1/log-groups/{id}`

```python
def get_log_group(self, id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetLogGroupResponse]:
```

## `telemetry.get_retained_telemetry_presence`

Check retained telemetry presence

`GET /v1/trace-settings/retained-data`

```python
def get_retained_telemetry_presence(self, *, options: RequestOptions | None = None) -> ApiResponse[m.GetRetainedTelemetryPresenceResponse]:
```

## `telemetry.get_trace`

Get all spans for a trace

`GET /v1/traces/{trace_id}`

```python
def get_trace(self, trace_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetTraceResponse]:
```

## `telemetry.get_trace_settings`

Get the caller account's trace settings

`GET /v1/trace-settings`

```python
def get_trace_settings(self, *, options: RequestOptions | None = None) -> ApiResponse[m.GetTraceSettingsResponse]:
```

## `telemetry.ingest_logs`

Ingest a batch of log records

`POST /v1/logs`

```python
def ingest_logs(self, body: m.IngestLogsBody, *, options: RequestOptions | None = None) -> ApiResponse[m.IngestLogsResponse]:
```

## `telemetry.ingest_spans`

Ingest a batch of trace spans

`POST /v1/spans`

```python
def ingest_spans(self, body: m.IngestSpansBody, *, options: RequestOptions | None = None) -> ApiResponse[m.IngestSpansResponse]:
```

## `telemetry.list_log_groups`

List log groups (or look up one by name)

`GET /v1/log-groups`

```python
def list_log_groups(self, *, query: m.ListLogGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListLogGroupsResponse, m.ListLogGroupsItem]:
```

## `telemetry.list_metric_names`

List the distinct metric names emitted in a time window

`GET /v1/metrics/names`

```python
def list_metric_names(self, *, query: m.ListMetricNamesQuery, options: RequestOptions | None = None) -> Page[m.ListMetricNamesResponse, m.ListMetricNamesItem]:
```

## `telemetry.list_metric_names_post`

List the distinct metric names emitted in a time window (form body)

`POST /v1/metrics/names`

```python
def list_metric_names_post(self, body: m.ListMetricNamesPostBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.ListMetricNamesPostResponse]:
```

## `telemetry.list_metric_series`

List distinct label sets for a metric

`GET /v1/metrics/series`

```python
def list_metric_series(self, *, query: m.ListMetricSeriesQuery, options: RequestOptions | None = None) -> ApiResponse[m.ListMetricSeriesResponse]:
```

## `telemetry.list_metric_series_post`

List distinct label sets for a metric (form body)

`POST /v1/metrics/series`

```python
def list_metric_series_post(self, body: m.ListMetricSeriesPostBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.ListMetricSeriesPostResponse]:
```

## `telemetry.put_trace_settings`

Update the caller account's trace settings

`PUT /v1/trace-settings`

```python
def put_trace_settings(self, body: m.PutTraceSettingsBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutTraceSettingsResponse]:
```

## `telemetry.query_metrics_instant`

Instant structured metric query

`GET /v1/metrics/query`

```python
def query_metrics_instant(self, *, query: m.QueryMetricsInstantQuery, options: RequestOptions | None = None) -> ApiResponse[m.QueryMetricsInstantResponse]:
```

## `telemetry.query_metrics_instant_post`

Instant structured metric query (form body)

`POST /v1/metrics/query`

```python
def query_metrics_instant_post(self, body: m.QueryMetricsInstantPostBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.QueryMetricsInstantPostResponse]:
```

## `telemetry.query_metrics_range`

Range structured metric query

`GET /v1/metrics/query_range`

```python
def query_metrics_range(self, *, query: m.QueryMetricsRangeQuery, options: RequestOptions | None = None) -> ApiResponse[m.QueryMetricsRangeResponse]:
```

## `telemetry.query_metrics_range_post`

Range structured metric query (form body)

`POST /v1/metrics/query_range`

```python
def query_metrics_range_post(self, body: m.QueryMetricsRangePostBody | Unset = UNSET, *, options: RequestOptions | None = None) -> ApiResponse[m.QueryMetricsRangePostResponse]:
```

## `telemetry.search_logs`

Search log records

`GET /v1/logs`

```python
def search_logs(self, *, query: m.SearchLogsQuery, options: RequestOptions | None = None) -> ApiResponse[m.SearchLogsResponse]:
```

## `telemetry.search_traces`

List traces

`GET /v1/traces`

```python
def search_traces(self, *, query: m.SearchTracesQuery, options: RequestOptions | None = None) -> ApiResponse[m.SearchTracesResponse]:
```

## `telemetry.update_log_group`

Update a log group

`PATCH /v1/log-groups/{id}`

```python
def update_log_group(self, id: str, body: m.UpdateLogGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateLogGroupResponse]:
```

## `telemetry.write_metrics`

Prometheus remote_write ingest

`POST /v1/metrics/write`

```python
def write_metrics(self, body: BinaryBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.add_user`

Add user to organization

`POST /v1/users`

```python
def add_user(self, body: m.AddUserBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AddUserResponse]:
```

## `workspace.add_user_to_group`

Add user to group

`POST /v1/users/{user_id}/groups`

```python
def add_user_to_group(self, user_id: str, body: m.AddUserToGroupBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.assign_account_role`

Assign account role

`POST /v1/accounts/{account_id}/role-assignments`

```python
def assign_account_role(self, account_id: str, body: m.AssignAccountRoleBody, *, options: RequestOptions | None = None) -> ApiResponse[m.AssignAccountRoleResponse]:
```

## `workspace.attach_group_policy`

Attach policy to group

`POST /v1/groups/{group_id}/policies`

```python
def attach_group_policy(self, group_id: str, body: m.AttachGroupPolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.attach_role_policy`

Attach policy to role

`POST /v1/roles/{role_id}/policies`

```python
def attach_role_policy(self, role_id: str, body: m.AttachRolePolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.attach_service_account_policy`

Attach policy to service account

`POST /v1/service-accounts/{service_account_id}/policies`

```python
def attach_service_account_policy(self, service_account_id: str, body: m.AttachServiceAccountPolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.attach_user_policy`

Attach policy to user

`POST /v1/users/{user_id}/policies`

```python
def attach_user_policy(self, user_id: str, body: m.AttachUserPolicyBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.cancel_invitation`

Cancel invitation

`DELETE /v1/invitations/{invitation_id}`

```python
def cancel_invitation(self, invitation_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.create_account`

Create account

`POST /v1/accounts`

```python
def create_account(self, body: m.CreateAccountBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateAccountResponse]:
```

## `workspace.create_group`

Create group

`POST /v1/groups`

```python
def create_group(self, body: m.CreateGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreateGroupResponse]:
```

## `workspace.create_policy`

Create policy

`POST /v1/policies`

```python
def create_policy(self, body: m.CreatePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.CreatePolicyResponse]:
```

## `workspace.delete_account`

Delete account

`DELETE /v1/accounts/{account_id}`

```python
def delete_account(self, account_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.delete_group`

Delete group

`DELETE /v1/groups/{group_id}`

```python
def delete_group(self, group_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.delete_group_inline_policy`

Delete a group's inline policy by name

`DELETE /v1/groups/{group_id}/inline-policies/{policy_name}`

```python
def delete_group_inline_policy(self, group_id: str, policy_name: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.delete_organization`

Delete organization

`DELETE /v1/organizations/{organization_id}`

```python
def delete_organization(self, organization_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.delete_policy`

Delete policy

`DELETE /v1/policies/{policy_id}`

```python
def delete_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.delete_user_inline_policy`

Delete a user's inline policy by name

`DELETE /v1/users/{user_id}/inline-policies/{policy_name}`

```python
def delete_user_inline_policy(self, user_id: str, policy_name: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.detach_group_policy`

Detach policy from group

`DELETE /v1/groups/{group_id}/policies/{policy_id}`

```python
def detach_group_policy(self, group_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.detach_role_policy`

Detach policy from role

`DELETE /v1/roles/{role_id}/policies/{policy_id}`

```python
def detach_role_policy(self, role_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.detach_service_account_policy`

Detach policy from service account

`DELETE /v1/service-accounts/{service_account_id}/policies/{policy_id}`

```python
def detach_service_account_policy(self, service_account_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.detach_user_policy`

Detach policy from user

`DELETE /v1/users/{user_id}/policies/{policy_id}`

```python
def detach_user_policy(self, user_id: str, policy_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.get_account`

Get account

`GET /v1/accounts/{account_id}`

```python
def get_account(self, account_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetAccountResponse]:
```

## `workspace.get_account_resources`

Check account resource presence

`GET /v1/accounts/{account_id}/resources`

```python
def get_account_resources(self, account_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetAccountResourcesResponse]:
```

## `workspace.get_group`

Get group

`GET /v1/groups/{group_id}`

```python
def get_group(self, group_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetGroupResponse]:
```

## `workspace.get_group_inline_policy`

Get a group's inline policy by name

`GET /v1/groups/{group_id}/inline-policies/{policy_name}`

```python
def get_group_inline_policy(self, group_id: str, policy_name: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetGroupInlinePolicyResponse]:
```

## `workspace.get_invitation`

Get invitation

`GET /v1/invitations/{invitation_id}`

```python
def get_invitation(self, invitation_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetInvitationResponse]:
```

## `workspace.get_organization`

Get organization

`GET /v1/organizations/{organization_id}`

```python
def get_organization(self, organization_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetOrganizationResponse]:
```

## `workspace.get_policy`

Get policy

`GET /v1/policies/{policy_id}`

```python
def get_policy(self, policy_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetPolicyResponse]:
```

## `workspace.get_user`

Get user

`GET /v1/users/{user_id}`

```python
def get_user(self, user_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetUserResponse]:
```

## `workspace.get_user_inline_policy`

Get a user's inline policy by name

`GET /v1/users/{user_id}/inline-policies/{policy_name}`

```python
def get_user_inline_policy(self, user_id: str, policy_name: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetUserInlinePolicyResponse]:
```

## `workspace.get_user_permission_boundary`

Get a user's permission boundary

`GET /v1/users/{user_id}/permission-boundary`

```python
def get_user_permission_boundary(self, user_id: str, *, options: RequestOptions | None = None) -> ApiResponse[m.GetUserPermissionBoundaryResponse]:
```

## `workspace.list_account_role_assignments`

List account role assignments

`GET /v1/accounts/{account_id}/role-assignments`

```python
def list_account_role_assignments(self, account_id: str, *, options: RequestOptions | None = None) -> Page[m.ListAccountRoleAssignmentsResponse, m.ListAccountRoleAssignmentsItem]:
```

## `workspace.list_account_roles`

List assigned account roles

`GET /v1/account-roles`

```python
def list_account_roles(self, *, options: RequestOptions | None = None) -> Page[m.ListAccountRolesResponse, m.ListAccountRolesItem]:
```

## `workspace.list_accounts`

List accounts

`GET /v1/accounts`

```python
def list_accounts(self, *, query: m.ListAccountsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListAccountsResponse, m.ListAccountsItem]:
```

## `workspace.list_group_inline_policies`

List a group's inline policies

`GET /v1/groups/{group_id}/inline-policies`

```python
def list_group_inline_policies(self, group_id: str, *, query: m.ListGroupInlinePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListGroupInlinePoliciesResponse, m.ListGroupInlinePoliciesItem]:
```

## `workspace.list_group_policies`

List group policies

`GET /v1/groups/{group_id}/policies`

```python
def list_group_policies(self, group_id: str, *, query: m.ListGroupPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListGroupPoliciesResponse, m.ListGroupPoliciesItem]:
```

## `workspace.list_group_users`

List group users

`GET /v1/groups/{group_id}/users`

```python
def list_group_users(self, group_id: str, *, query: m.ListGroupUsersQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListGroupUsersResponse, m.ListGroupUsersItem]:
```

## `workspace.list_groups`

List groups

`GET /v1/groups`

```python
def list_groups(self, *, query: m.ListGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListGroupsResponse, m.ListGroupsItem]:
```

## `workspace.list_invitations`

List invitations

`GET /v1/invitations`

```python
def list_invitations(self, *, query: m.ListInvitationsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListInvitationsResponse, m.ListInvitationsItem]:
```

## `workspace.list_organizations`

List organizations

`GET /v1/organizations`

```python
def list_organizations(self, *, query: m.ListOrganizationsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListOrganizationsResponse, m.ListOrganizationsItem]:
```

## `workspace.list_policies`

List policies

`GET /v1/policies`

```python
def list_policies(self, *, query: m.ListPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPoliciesResponse, m.ListPoliciesItem]:
```

## `workspace.list_policy_groups`

List groups with policy

`GET /v1/policies/{policy_id}/groups`

```python
def list_policy_groups(self, policy_id: str, *, query: m.ListPolicyGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyGroupsResponse, m.ListPolicyGroupsItem]:
```

## `workspace.list_policy_roles`

List roles with policy

`GET /v1/policies/{policy_id}/roles`

```python
def list_policy_roles(self, policy_id: str, *, query: m.ListPolicyRolesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyRolesResponse, m.ListPolicyRolesItem]:
```

## `workspace.list_policy_service_accounts`

List service accounts with policy

`GET /v1/policies/{policy_id}/service-accounts`

```python
def list_policy_service_accounts(self, policy_id: str, *, query: m.ListPolicyServiceAccountsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyServiceAccountsResponse, m.ListPolicyServiceAccountsItem]:
```

## `workspace.list_policy_users`

List users with policy

`GET /v1/policies/{policy_id}/users`

```python
def list_policy_users(self, policy_id: str, *, query: m.ListPolicyUsersQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListPolicyUsersResponse, m.ListPolicyUsersItem]:
```

## `workspace.list_role_policies`

List role policies

`GET /v1/roles/{role_id}/policies`

```python
def list_role_policies(self, role_id: str, *, query: m.ListRolePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListRolePoliciesResponse, m.ListRolePoliciesItem]:
```

## `workspace.list_service_account_policies`

List service account policies

`GET /v1/service-accounts/{service_account_id}/policies`

```python
def list_service_account_policies(self, service_account_id: str, *, query: m.ListServiceAccountPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListServiceAccountPoliciesResponse, m.ListServiceAccountPoliciesItem]:
```

## `workspace.list_user_groups`

List user groups

`GET /v1/users/{user_id}/groups`

```python
def list_user_groups(self, user_id: str, *, query: m.ListUserGroupsQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListUserGroupsResponse, m.ListUserGroupsItem]:
```

## `workspace.list_user_inline_policies`

List a user's inline policies

`GET /v1/users/{user_id}/inline-policies`

```python
def list_user_inline_policies(self, user_id: str, *, query: m.ListUserInlinePoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListUserInlinePoliciesResponse, m.ListUserInlinePoliciesItem]:
```

## `workspace.list_user_policies`

List user policies

`GET /v1/users/{user_id}/policies`

```python
def list_user_policies(self, user_id: str, *, query: m.ListUserPoliciesQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListUserPoliciesResponse, m.ListUserPoliciesItem]:
```

## `workspace.list_users`

List users

`GET /v1/users`

```python
def list_users(self, *, query: m.ListUsersQuery | None = None, options: RequestOptions | None = None) -> Page[m.ListUsersResponse, m.ListUsersItem]:
```

## `workspace.put_group_inline_policy`

Create or replace a group's inline policy

`PUT /v1/groups/{group_id}/inline-policies/{policy_name}`

```python
def put_group_inline_policy(self, group_id: str, policy_name: str, body: m.PutGroupInlinePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutGroupInlinePolicyResponse]:
```

## `workspace.put_user_inline_policy`

Create or replace a user's inline policy

`PUT /v1/users/{user_id}/inline-policies/{policy_name}`

```python
def put_user_inline_policy(self, user_id: str, policy_name: str, body: m.PutUserInlinePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.PutUserInlinePolicyResponse]:
```

## `workspace.remove_account_role_assignment`

Remove account role assignment

`DELETE /v1/accounts/{account_id}/role-assignments/{assignment_id}`

```python
def remove_account_role_assignment(self, account_id: str, assignment_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.remove_user`

Remove user from organization

`DELETE /v1/users/{user_id}`

```python
def remove_user(self, user_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.remove_user_from_group`

Remove user from group

`DELETE /v1/users/{user_id}/groups/{group_id}`

```python
def remove_user_from_group(self, user_id: str, group_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.remove_user_permission_boundary`

Remove a user's permission boundary

`DELETE /v1/users/{user_id}/permission-boundary`

```python
def remove_user_permission_boundary(self, user_id: str, *, options: RequestOptions | None = None) -> None:
```

## `workspace.set_user_permission_boundary`

Set a user's permission boundary

`PUT /v1/users/{user_id}/permission-boundary`

```python
def set_user_permission_boundary(self, user_id: str, body: m.SetUserPermissionBoundaryBody, *, options: RequestOptions | None = None) -> None:
```

## `workspace.update_account`

Update account

`PATCH /v1/accounts/{account_id}`

```python
def update_account(self, account_id: str, body: m.UpdateAccountBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateAccountResponse]:
```

## `workspace.update_group`

Update group

`PATCH /v1/groups/{group_id}`

```python
def update_group(self, group_id: str, body: m.UpdateGroupBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateGroupResponse]:
```

## `workspace.update_organization`

Update organization

`PATCH /v1/organizations/{organization_id}`

```python
def update_organization(self, organization_id: str, body: m.UpdateOrganizationBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdateOrganizationResponse]:
```

## `workspace.update_policy`

Update policy

`PATCH /v1/policies/{policy_id}`

```python
def update_policy(self, policy_id: str, body: m.UpdatePolicyBody, *, options: RequestOptions | None = None) -> ApiResponse[m.UpdatePolicyResponse]:
```
