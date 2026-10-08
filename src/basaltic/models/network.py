"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachFloatingIpRequest = TypedDict(
    "AttachFloatingIpRequest",
    {"interface": "Required[str]", "address_id": "Required[str]"},
    total=False,
)
AttachFloatingIpBody: TypeAlias = "AttachFloatingIpRequest"
AttachFloatingIpResult = TypedDict(
    "AttachFloatingIpResult", {"floating_ip": "NotRequired[FloatingIp]"}, total=False
)
FloatingIp = TypedDict(
    "FloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "description": "NotRequired[str]",
        "family": "Required[IpFamily]",
        "attached_to": "Required[str | None]",
        "members": "Required[list[FloatingIpMember]]",
        "tags": "Required[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheck]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "address": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "subnet_id": "NotRequired[str | None]",
        "vpc_id": "NotRequired[str]",
    },
    total=False,
)
IpFamily: TypeAlias = "Literal['ipv4', 'ipv6']"
FloatingIpMember = TypedDict(
    "FloatingIpMember",
    {
        "interface": "Required[FloatingIpMemberInterfaceObject | None]",
        "health": "Required[Literal['unknown', 'healthy', 'unhealthy']]",
        "reason": "Required[Literal['unprobed', 'booting', 'probe_failed', 'passing']]",
        "created_at": "Required[str]",
        "address_id": "NotRequired[str | None]",
    },
    total=False,
)
FloatingIpMemberInterfaceObject = TypedDict(
    "FloatingIpMemberInterfaceObject",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "instance": "Required[FloatingIpMemberInterfaceObjectInstanceObject | None]",
    },
    total=False,
)
FloatingIpMemberInterfaceObjectInstanceObject = TypedDict(
    "FloatingIpMemberInterfaceObjectInstanceObject",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
)
FloatingIpHealthCheck = TypedDict(
    "FloatingIpHealthCheck",
    {
        "protocol": "Required[Literal['tcp', 'http', 'https']]",
        "path": "NotRequired[str]",
        "port": "Required[int]",
        "interval_sec": "Required[int]",
        "timeout_sec": "Required[int]",
        "healthy_threshold": "Required[int]",
        "unhealthy_threshold": "Required[int]",
        "matcher": "NotRequired[str]",
    },
    total=False,
)
AttachFloatingIpResponse: TypeAlias = "AttachFloatingIpResult"
InternetGatewayAttachRequestInput = TypedDict(
    "InternetGatewayAttachRequestInput", {"vpc": "Required[str]"}, total=False
)
AttachInternetGatewayBody: TypeAlias = "InternetGatewayAttachRequestInput"
InternetGatewayResponse = TypedDict(
    "InternetGatewayResponse", {"internet_gateway": "NotRequired[InternetGateway]"}, total=False
)
InternetGateway = TypedDict(
    "InternetGateway",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "attached_vpc_id": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
AttachInternetGatewayResponse: TypeAlias = "InternetGatewayResponse"
EgressOnlyGatewayCreateRequestInput = TypedDict(
    "EgressOnlyGatewayCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "vpc": "Required[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateEgressOnlyGatewayBody: TypeAlias = "EgressOnlyGatewayCreateRequestInput"
EgressOnlyGatewayResponse = TypedDict(
    "EgressOnlyGatewayResponse",
    {"egress_only_gateway": "NotRequired[EgressOnlyGateway]"},
    total=False,
)
EgressOnlyGateway = TypedDict(
    "EgressOnlyGateway",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "vpc": "Required[Vpc]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
Vpc = TypedDict(
    "Vpc",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "cidr_ipv6": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateEgressOnlyGatewayResponse: TypeAlias = "EgressOnlyGatewayResponse"
FloatingIpCreateRequestInput = TypedDict(
    "FloatingIpCreateRequestInput",
    {
        "description": "NotRequired[str]",
        "family": "NotRequired[IpFamilyInput]",
        "tags": "NotRequired[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheckInput]",
        "visibility": "NotRequired[Literal['public', 'private']]",
        "subnet": "NotRequired[str]",
    },
    total=False,
)
IpFamilyInput: TypeAlias = "Literal['ipv4', 'ipv6']"
FloatingIpHealthCheckInput = TypedDict(
    "FloatingIpHealthCheckInput",
    {
        "protocol": "Required[Literal['tcp', 'http', 'https']]",
        "path": "NotRequired[str]",
        "port": "Required[int]",
        "interval_sec": "Required[int]",
        "timeout_sec": "Required[int]",
        "healthy_threshold": "Required[int]",
        "unhealthy_threshold": "Required[int]",
        "matcher": "NotRequired[str]",
    },
    total=False,
)
CreateFloatingIpBody: TypeAlias = "FloatingIpCreateRequestInput"
FloatingIpResponse = TypedDict(
    "FloatingIpResponse", {"floating_ip": "NotRequired[FloatingIp]"}, total=False
)
CreateFloatingIpResponse: TypeAlias = "FloatingIpResponse"
InterfaceCreateRequestInput = TypedDict(
    "InterfaceCreateRequestInput",
    {
        "subnet": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "mac": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
        "addresses": "NotRequired[list[AddressRequestInput]]",
    },
    total=False,
)
AddressRequestInput = TypedDict(
    "AddressRequestInput",
    {"family": "Required[Literal['ipv4', 'ipv6']]", "address": "NotRequired[str]"},
    total=False,
)
CreateInterfaceBody: TypeAlias = "InterfaceCreateRequestInput"
InterfaceResponse = TypedDict(
    "InterfaceResponse", {"interface": "NotRequired[Interface]"}, total=False
)
Interface = TypedDict(
    "Interface",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "subnet": "Required[Subnet]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "mac": "Required[str]",
        "attached_to": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "addresses": "Required[list[InterfaceAddress]]",
        "routed_prefixes": "Required[list[RoutedPrefix]]",
    },
    total=False,
)
Subnet = TypedDict(
    "Subnet",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "vpc": "Required[Vpc]",
        "route_table": "Required[RouteTableSummary]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "gateway_ipv4": "Required[str]",
        "cidr_ipv6": "NotRequired[str | None]",
        "gateway_ipv6": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
RouteTableSummary: TypeAlias = "RouteTableSummaryObject | None"
RouteTableSummaryObject = TypedDict(
    "RouteTableSummaryObject",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
)
InterfaceAddress = TypedDict(
    "InterfaceAddress",
    {
        "id": "Required[str]",
        "family": "Required[Literal['ipv4', 'ipv6']]",
        "address": "Required[str]",
        "prefix": "Required[str]",
        "primary": "Required[bool]",
        "floating_ips": "Required[list[AddressFloatingIp]]",
    },
    total=False,
)
AddressFloatingIp = TypedDict(
    "AddressFloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "address": "Required[str]",
    },
    total=False,
)
RoutedPrefix = TypedDict(
    "RoutedPrefix",
    {
        "id": "Required[str]",
        "pool_id": "Required[str]",
        "family": "Required[Literal['ipv4']]",
        "prefix": "Required[str]",
    },
    total=False,
)
CreateInterfaceResponse: TypeAlias = "InterfaceResponse"
CreateInterfaceAddressBody: TypeAlias = "AddressRequestInput"
CreateInterfaceAddressResult = TypedDict(
    "CreateInterfaceAddressResult", {"address": "NotRequired[InterfaceAddress]"}, total=False
)
CreateInterfaceAddressResponse: TypeAlias = "CreateInterfaceAddressResult"
CreateInterfacePrefixRequest = TypedDict(
    "CreateInterfacePrefixRequest", {"pool_id": "Required[str]"}, total=False
)
CreateInterfacePrefixBody: TypeAlias = "CreateInterfacePrefixRequest"
CreateInterfacePrefixResult = TypedDict(
    "CreateInterfacePrefixResult",
    {"routed_prefixes": "NotRequired[list[RoutedPrefix]]"},
    total=False,
)
CreateInterfacePrefixResponse: TypeAlias = "CreateInterfacePrefixResult"
InternetGatewayCreateRequestInput = TypedDict(
    "InternetGatewayCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateInternetGatewayBody: TypeAlias = "InternetGatewayCreateRequestInput"
CreateInternetGatewayResponse: TypeAlias = "InternetGatewayResponse"
NATGatewayCreateRequestInput = TypedDict(
    "NATGatewayCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "subnet": "Required[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateNATGatewayBody: TypeAlias = "NATGatewayCreateRequestInput"
NATGatewayResponse = TypedDict(
    "NATGatewayResponse", {"nat_gateway": "NotRequired[NATGateway]"}, total=False
)
NATGateway = TypedDict(
    "NATGateway",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "subnet": "Required[Subnet]",
        "public_ipv4": "Required[str]",
        "public_ipv6": "NotRequired[str]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateNATGatewayResponse: TypeAlias = "NATGatewayResponse"
CreatePrefixPoolRequest = TypedDict(
    "CreatePrefixPoolRequest", {"cidr_ipv4": "Required[str]"}, total=False
)
CreatePrefixPoolBody: TypeAlias = "CreatePrefixPoolRequest"
CreatePrefixPoolResult = TypedDict(
    "CreatePrefixPoolResult", {"prefix_pools": "NotRequired[list[PrefixPool]]"}, total=False
)
PrefixPool = TypedDict(
    "PrefixPool", {"id": "Required[str]", "cidr_ipv4": "Required[str]"}, total=False
)
CreatePrefixPoolResponse: TypeAlias = "CreatePrefixPoolResult"
RouteCreateRequestInput = TypedDict(
    "RouteCreateRequestInput",
    {
        "description": "NotRequired[str]",
        "destination_cidr": "Required[str]",
        "next_hop_ip": "NotRequired[str | None]",
        "target_internet_gateway": "NotRequired[str]",
        "target_nat_gateway": "NotRequired[str]",
        "target_egress_only_gateway": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateRouteBody: TypeAlias = "RouteCreateRequestInput"
RouteResponse = TypedDict("RouteResponse", {"route": "NotRequired[Route]"}, total=False)
Route = TypedDict(
    "Route",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "route_table_id": "Required[str]",
        "description": "NotRequired[str]",
        "destination_cidr": "Required[str]",
        "target_type": "Required[RouteTargetType]",
        "next_hop_ip": "NotRequired[str | None]",
        "target_internet_gateway_id": "NotRequired[str | None]",
        "target_nat_gateway_id": "NotRequired[str | None]",
        "target_egress_only_gateway_id": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
RouteTargetType: TypeAlias = (
    "Literal['ip', 'internet_gateway', 'nat_gateway', 'egress_only_gateway']"
)
CreateRouteResponse: TypeAlias = "RouteResponse"
RouteTableCreateRequestInput = TypedDict(
    "RouteTableCreateRequestInput",
    {
        "vpc": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateRouteTableBody: TypeAlias = "RouteTableCreateRequestInput"
RouteTableResponse = TypedDict(
    "RouteTableResponse", {"route_table": "NotRequired[RouteTable]"}, total=False
)
RouteTable = TypedDict(
    "RouteTable",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "vpc": "Required[Vpc]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "is_main": "Required[bool]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateRouteTableResponse: TypeAlias = "RouteTableResponse"
SecurityGroupCreateRequestInput = TypedDict(
    "SecurityGroupCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateSecurityGroupBody: TypeAlias = "SecurityGroupCreateRequestInput"
SecurityGroupResponse = TypedDict(
    "SecurityGroupResponse", {"security_group": "NotRequired[SecurityGroup]"}, total=False
)
SecurityGroup = TypedDict(
    "SecurityGroup",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateSecurityGroupResponse: TypeAlias = "SecurityGroupResponse"
SecurityGroupRuleCreateRequestInput = TypedDict(
    "SecurityGroupRuleCreateRequestInput",
    {
        "description": "NotRequired[str]",
        "direction": "Required[SecurityGroupRuleDirectionInput]",
        "ethertype": "NotRequired[SecurityGroupRuleEthertypeInput]",
        "protocol": "Required[SecurityGroupRuleProtocolInput]",
        "port_min": "NotRequired[int | None]",
        "port_max": "NotRequired[int | None]",
        "remote_cidr": "NotRequired[str | None]",
        "source_security_group": "NotRequired[str]",
    },
    total=False,
)
SecurityGroupRuleDirectionInput: TypeAlias = "Literal['ingress', 'egress']"
SecurityGroupRuleEthertypeInput: TypeAlias = "Literal['ipv4', 'ipv6']"
SecurityGroupRuleProtocolInput: TypeAlias = "Literal['tcp', 'udp', 'icmp', 'all']"
CreateSecurityGroupRuleBody: TypeAlias = "SecurityGroupRuleCreateRequestInput"
SecurityGroupRuleResponse = TypedDict(
    "SecurityGroupRuleResponse", {"rule": "NotRequired[SecurityGroupRule]"}, total=False
)
SecurityGroupRule = TypedDict(
    "SecurityGroupRule",
    {
        "id": "Required[str]",
        "security_group_id": "Required[str]",
        "description": "NotRequired[str]",
        "direction": "Required[SecurityGroupRuleDirection]",
        "ethertype": "Required[SecurityGroupRuleEthertype]",
        "protocol": "Required[SecurityGroupRuleProtocol]",
        "port_min": "NotRequired[int | None]",
        "port_max": "NotRequired[int | None]",
        "remote_cidr": "NotRequired[str | None]",
        "source_security_group_id": "NotRequired[str | None]",
        "created_at": "Required[str]",
    },
    total=False,
)
SecurityGroupRuleDirection: TypeAlias = "Literal['ingress', 'egress']"
SecurityGroupRuleEthertype: TypeAlias = "Literal['ipv4', 'ipv6']"
SecurityGroupRuleProtocol: TypeAlias = "Literal['tcp', 'udp', 'icmp', 'all']"
CreateSecurityGroupRuleResponse: TypeAlias = "SecurityGroupRuleResponse"
SubnetCreateRequestInput = TypedDict(
    "SubnetCreateRequestInput",
    {
        "vpc": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "gateway_ipv4": "NotRequired[str | None]",
        "route_table": "NotRequired[str]",
        "allocate_cidr_ipv6": "NotRequired[bool]",
        "cidr_ipv6": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateSubnetBody: TypeAlias = "SubnetCreateRequestInput"
SubnetResponse = TypedDict("SubnetResponse", {"subnet": "NotRequired[Subnet]"}, total=False)
CreateSubnetResponse: TypeAlias = "SubnetResponse"
VpcCreateRequestInput = TypedDict(
    "VpcCreateRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "cidr_ipv4": "Required[str]",
        "allocate_cidr_ipv6": "NotRequired[bool]",
        "tags": "NotRequired[dict[str, str]]",
        "cidr_ipv6": "NotRequired[str]",
    },
    total=False,
)
CreateVpcBody: TypeAlias = "VpcCreateRequestInput"
VpcResponse = TypedDict("VpcResponse", {"vpc": "NotRequired[Vpc]"}, total=False)
CreateVpcResponse: TypeAlias = "VpcResponse"
DetachFloatingIpRequest = TypedDict(
    "DetachFloatingIpRequest", {"interface": "NotRequired[str]"}, total=False
)
DetachFloatingIpBody: TypeAlias = "DetachFloatingIpRequest"
DetachFloatingIpResult = TypedDict(
    "DetachFloatingIpResult", {"floating_ip": "NotRequired[FloatingIp]"}, total=False
)
DetachFloatingIpResponse: TypeAlias = "DetachFloatingIpResult"
DetachInternetGatewayResponse: TypeAlias = "InternetGatewayResponse"
GetEgressOnlyGatewayResponse: TypeAlias = "EgressOnlyGatewayResponse"
GetEgressOnlyGatewayResource: TypeAlias = "EgressOnlyGateway"
GetEgressOnlyGatewayScope = TypedDict(
    "GetEgressOnlyGatewayScope", {"limit": "NotRequired[int]"}, total=False
)
GetFloatingIpResponse: TypeAlias = "FloatingIpResponse"
GetFloatingIpResource: TypeAlias = "FloatingIp"
GetFloatingIpScope = TypedDict(
    "GetFloatingIpScope",
    {"attached_to": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
GetInterfaceResponse: TypeAlias = "InterfaceResponse"
GetInterfaceResource: TypeAlias = "Interface"
GetInterfaceScope = TypedDict(
    "GetInterfaceScope",
    {"subnet": "NotRequired[str]", "vpc": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
GetInterfaceAddressResult = TypedDict(
    "GetInterfaceAddressResult", {"address": "NotRequired[InterfaceAddress]"}, total=False
)
GetInterfaceAddressResponse: TypeAlias = "GetInterfaceAddressResult"
GetInternetGatewayResponse: TypeAlias = "InternetGatewayResponse"
GetInternetGatewayResource: TypeAlias = "InternetGateway"
GetInternetGatewayScope = TypedDict(
    "GetInternetGatewayScope", {"limit": "NotRequired[int]"}, total=False
)
GetNATGatewayResponse: TypeAlias = "NATGatewayResponse"
GetNATGatewayResource: TypeAlias = "NATGateway"
GetNATGatewayScope = TypedDict(
    "GetNATGatewayScope",
    {"subnet": "NotRequired[str]", "vpc": "NotRequired[str]", "limit": "NotRequired[int]"},
    total=False,
)
GetRouteResponse: TypeAlias = "RouteResponse"
GetRouteResource: TypeAlias = "Route"
GetRouteScope = TypedDict("GetRouteScope", {"limit": "NotRequired[int]"}, total=False)
GetRouteTableResponse: TypeAlias = "RouteTableResponse"
GetRouteTableResource: TypeAlias = "RouteTable"
GetRouteTableScope = TypedDict(
    "GetRouteTableScope", {"vpc": "NotRequired[str]", "limit": "NotRequired[int]"}, total=False
)
GetSecurityGroupResponse: TypeAlias = "SecurityGroupResponse"
GetSecurityGroupResource: TypeAlias = "SecurityGroup"
GetSecurityGroupScope = TypedDict(
    "GetSecurityGroupScope", {"limit": "NotRequired[int]"}, total=False
)
GetSecurityGroupRuleResponse: TypeAlias = "SecurityGroupRuleResponse"
GetSecurityGroupRuleResource: TypeAlias = "SecurityGroupRule"
GetSecurityGroupRuleScope = TypedDict(
    "GetSecurityGroupRuleScope", {"limit": "NotRequired[int]"}, total=False
)
GetSubnetResponse: TypeAlias = "SubnetResponse"
GetSubnetResource: TypeAlias = "Subnet"
GetSubnetScope = TypedDict(
    "GetSubnetScope", {"vpc": "NotRequired[str]", "limit": "NotRequired[int]"}, total=False
)
GetVpcResponse: TypeAlias = "VpcResponse"
GetVpcResource: TypeAlias = "Vpc"
GetVpcScope = TypedDict("GetVpcScope", {"limit": "NotRequired[int]"}, total=False)
ListEgressOnlyGatewayRoutesParameters = TypedDict(
    "ListEgressOnlyGatewayRoutesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListEgressOnlyGatewayRoutesQuery: TypeAlias = "ListEgressOnlyGatewayRoutesParameters"
GatewayRouteListResponse = TypedDict(
    "GatewayRouteListResponse",
    {"routes": "Required[list[GatewayRoute]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
GatewayRoute = TypedDict(
    "GatewayRoute",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "route_table_id": "Required[str]",
        "description": "NotRequired[str]",
        "destination_cidr": "Required[str]",
        "target_type": "Required[RouteTargetType]",
        "next_hop_ip": "NotRequired[str | None]",
        "target_internet_gateway_id": "NotRequired[str | None]",
        "target_nat_gateway_id": "NotRequired[str | None]",
        "target_egress_only_gateway_id": "NotRequired[str | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "route_table": "Required[RouteTableSummary]",
    },
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
ListEgressOnlyGatewayRoutesResponse: TypeAlias = "GatewayRouteListResponse"
ListEgressOnlyGatewayRoutesItem: TypeAlias = "GatewayRoute"
ListEgressOnlyGatewaysParameters = TypedDict(
    "ListEgressOnlyGatewaysParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListEgressOnlyGatewaysQuery: TypeAlias = "ListEgressOnlyGatewaysParameters"
EgressOnlyGatewayListResponse = TypedDict(
    "EgressOnlyGatewayListResponse",
    {
        "egress_only_gateways": "Required[list[EgressOnlyGateway]]",
        "meta": "Required[PaginationMeta]",
    },
    total=False,
)
ListEgressOnlyGatewaysResponse: TypeAlias = "EgressOnlyGatewayListResponse"
ListEgressOnlyGatewaysItem: TypeAlias = "EgressOnlyGateway"
ListFloatingIpsParameters = TypedDict(
    "ListFloatingIpsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "attached_to": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListFloatingIpsQuery: TypeAlias = "ListFloatingIpsParameters"
FloatingIpListResponse = TypedDict(
    "FloatingIpListResponse",
    {"floating_ips": "Required[list[FloatingIp]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListFloatingIpsResponse: TypeAlias = "FloatingIpListResponse"
ListFloatingIpsItem: TypeAlias = "FloatingIp"
ListInterfaceAddressesResult = TypedDict(
    "ListInterfaceAddressesResult",
    {"addresses": "NotRequired[list[InterfaceAddress]]"},
    total=False,
)
ListInterfaceAddressesResponse: TypeAlias = "ListInterfaceAddressesResult"
ListInterfaceAddressesItem: TypeAlias = "InterfaceAddress"
ListInterfacePrefixesResult = TypedDict(
    "ListInterfacePrefixesResult",
    {"routed_prefixes": "NotRequired[list[RoutedPrefix]]"},
    total=False,
)
ListInterfacePrefixesResponse: TypeAlias = "ListInterfacePrefixesResult"
ListInterfacePrefixesItem: TypeAlias = "RoutedPrefix"
ListInterfaceSecurityGroupsParameters = TypedDict(
    "ListInterfaceSecurityGroupsParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListInterfaceSecurityGroupsQuery: TypeAlias = "ListInterfaceSecurityGroupsParameters"
InterfaceSecurityGroupsResponse = TypedDict(
    "InterfaceSecurityGroupsResponse", {"security_group_ids": "Required[list[str]]"}, total=False
)
ListInterfaceSecurityGroupsResponse: TypeAlias = "InterfaceSecurityGroupsResponse"
ListInterfaceSecurityGroupsItem: TypeAlias = "str"
ListInterfacesParameters = TypedDict(
    "ListInterfacesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "subnet": "NotRequired[str]",
        "vpc": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInterfacesQuery: TypeAlias = "ListInterfacesParameters"
InterfaceListResponse = TypedDict(
    "InterfaceListResponse",
    {"interfaces": "Required[list[Interface]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInterfacesResponse: TypeAlias = "InterfaceListResponse"
ListInterfacesItem: TypeAlias = "Interface"
ListInternetGatewayRoutesParameters = TypedDict(
    "ListInternetGatewayRoutesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInternetGatewayRoutesQuery: TypeAlias = "ListInternetGatewayRoutesParameters"
ListInternetGatewayRoutesResponse: TypeAlias = "GatewayRouteListResponse"
ListInternetGatewayRoutesItem: TypeAlias = "GatewayRoute"
ListInternetGatewaysParameters = TypedDict(
    "ListInternetGatewaysParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListInternetGatewaysQuery: TypeAlias = "ListInternetGatewaysParameters"
InternetGatewayListResponse = TypedDict(
    "InternetGatewayListResponse",
    {"internet_gateways": "Required[list[InternetGateway]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInternetGatewaysResponse: TypeAlias = "InternetGatewayListResponse"
ListInternetGatewaysItem: TypeAlias = "InternetGateway"
ListNATGatewayRoutesParameters = TypedDict(
    "ListNATGatewayRoutesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListNATGatewayRoutesQuery: TypeAlias = "ListNATGatewayRoutesParameters"
ListNATGatewayRoutesResponse: TypeAlias = "GatewayRouteListResponse"
ListNATGatewayRoutesItem: TypeAlias = "GatewayRoute"
ListNATGatewaysParameters = TypedDict(
    "ListNATGatewaysParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "subnet": "NotRequired[str]",
        "vpc": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListNATGatewaysQuery: TypeAlias = "ListNATGatewaysParameters"
NATGatewayListResponse = TypedDict(
    "NATGatewayListResponse",
    {"nat_gateways": "Required[list[NATGateway]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListNATGatewaysResponse: TypeAlias = "NATGatewayListResponse"
ListNATGatewaysItem: TypeAlias = "NATGateway"
ListPrefixPoolsResult = TypedDict(
    "ListPrefixPoolsResult", {"prefix_pools": "NotRequired[list[PrefixPool]]"}, total=False
)
ListPrefixPoolsResponse: TypeAlias = "ListPrefixPoolsResult"
ListPrefixPoolsItem: TypeAlias = "PrefixPool"
ListRouteTablesParameters = TypedDict(
    "ListRouteTablesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "vpc": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListRouteTablesQuery: TypeAlias = "ListRouteTablesParameters"
RouteTableListResponse = TypedDict(
    "RouteTableListResponse",
    {"route_tables": "Required[list[RouteTable]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListRouteTablesResponse: TypeAlias = "RouteTableListResponse"
ListRouteTablesItem: TypeAlias = "RouteTable"
ListRoutesParameters = TypedDict(
    "ListRoutesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListRoutesQuery: TypeAlias = "ListRoutesParameters"
RouteListResponse = TypedDict(
    "RouteListResponse",
    {"routes": "Required[list[Route]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListRoutesResponse: TypeAlias = "RouteListResponse"
ListRoutesItem: TypeAlias = "Route"
ListSecurityGroupRulesParameters = TypedDict(
    "ListSecurityGroupRulesParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListSecurityGroupRulesQuery: TypeAlias = "ListSecurityGroupRulesParameters"
SecurityGroupRuleListResponse = TypedDict(
    "SecurityGroupRuleListResponse",
    {"rules": "Required[list[SecurityGroupRule]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListSecurityGroupRulesResponse: TypeAlias = "SecurityGroupRuleListResponse"
ListSecurityGroupRulesItem: TypeAlias = "SecurityGroupRule"
ListSecurityGroupsParameters = TypedDict(
    "ListSecurityGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListSecurityGroupsQuery: TypeAlias = "ListSecurityGroupsParameters"
SecurityGroupListResponse = TypedDict(
    "SecurityGroupListResponse",
    {"security_groups": "Required[list[SecurityGroup]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListSecurityGroupsResponse: TypeAlias = "SecurityGroupListResponse"
ListSecurityGroupsItem: TypeAlias = "SecurityGroup"
ListSubnetsParameters = TypedDict(
    "ListSubnetsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "vpc": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListSubnetsQuery: TypeAlias = "ListSubnetsParameters"
SubnetListResponse = TypedDict(
    "SubnetListResponse",
    {"subnets": "Required[list[Subnet]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListSubnetsResponse: TypeAlias = "SubnetListResponse"
ListSubnetsItem: TypeAlias = "Subnet"
ListVpcsParameters = TypedDict(
    "ListVpcsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListVpcsQuery: TypeAlias = "ListVpcsParameters"
VpcListResponse = TypedDict(
    "VpcListResponse",
    {"vpcs": "Required[list[Vpc]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListVpcsResponse: TypeAlias = "VpcListResponse"
ListVpcsItem: TypeAlias = "Vpc"
InterfaceSecurityGroupsRequestInput = TypedDict(
    "InterfaceSecurityGroupsRequestInput", {"security_groups": "Required[list[str]]"}, total=False
)
SetInterfaceSecurityGroupsBody: TypeAlias = "InterfaceSecurityGroupsRequestInput"
SetInterfaceSecurityGroupsResponse: TypeAlias = "InterfaceSecurityGroupsResponse"
EgressOnlyGatewayUpdateRequestInput = TypedDict(
    "EgressOnlyGatewayUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateEgressOnlyGatewayBody: TypeAlias = "EgressOnlyGatewayUpdateRequestInput"
UpdateEgressOnlyGatewayResponse: TypeAlias = "EgressOnlyGatewayResponse"
FloatingIpUpdateRequestInput = TypedDict(
    "FloatingIpUpdateRequestInput",
    {
        "description": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheckInput | None]",
    },
    total=False,
)
UpdateFloatingIpBody: TypeAlias = "FloatingIpUpdateRequestInput"
UpdateFloatingIpResponse: TypeAlias = "FloatingIpResponse"
InterfaceUpdateRequestInput = TypedDict(
    "InterfaceUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateInterfaceBody: TypeAlias = "InterfaceUpdateRequestInput"
UpdateInterfaceResponse: TypeAlias = "InterfaceResponse"
InternetGatewayUpdateRequestInput = TypedDict(
    "InternetGatewayUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateInternetGatewayBody: TypeAlias = "InternetGatewayUpdateRequestInput"
UpdateInternetGatewayResponse: TypeAlias = "InternetGatewayResponse"
NATGatewayUpdateRequestInput = TypedDict(
    "NATGatewayUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateNATGatewayBody: TypeAlias = "NATGatewayUpdateRequestInput"
UpdateNATGatewayResponse: TypeAlias = "NATGatewayResponse"
RouteUpdateRequestInput = TypedDict(
    "RouteUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateRouteBody: TypeAlias = "RouteUpdateRequestInput"
UpdateRouteResponse: TypeAlias = "RouteResponse"
RouteTableUpdateRequestInput = TypedDict(
    "RouteTableUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateRouteTableBody: TypeAlias = "RouteTableUpdateRequestInput"
UpdateRouteTableResponse: TypeAlias = "RouteTableResponse"
SecurityGroupUpdateRequestInput = TypedDict(
    "SecurityGroupUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateSecurityGroupBody: TypeAlias = "SecurityGroupUpdateRequestInput"
UpdateSecurityGroupResponse: TypeAlias = "SecurityGroupResponse"
SubnetUpdateRequestInput = TypedDict(
    "SubnetUpdateRequestInput",
    {
        "description": "NotRequired[str | None]",
        "route_table": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
        "allocate_cidr_ipv6": "NotRequired[bool]",
        "cidr_ipv6": "NotRequired[str | None]",
        "copy_ipv4_security_rules": "NotRequired[bool]",
        "ipv6_routing": "NotRequired[Literal['match_ipv4', 'unchanged', 'internet_gateway', 'nat_gateway', 'egress_only_gateway']]",
    },
    total=False,
)
UpdateSubnetBody: TypeAlias = "SubnetUpdateRequestInput"
UpdateSubnetResponse: TypeAlias = "SubnetResponse"
VpcUpdateRequestInput = TypedDict(
    "VpcUpdateRequestInput",
    {
        "description": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
        "allocate_cidr_ipv6": "NotRequired[bool]",
        "cidr_ipv6": "NotRequired[str]",
    },
    total=False,
)
UpdateVpcBody: TypeAlias = "VpcUpdateRequestInput"
UpdateVpcResponse: TypeAlias = "VpcResponse"
