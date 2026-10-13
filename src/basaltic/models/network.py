"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachFloatingIpRequest = TypedDict(
    "AttachFloatingIpRequest",
    {"interface": "Required[str]", "address_id": "Required[str]"},
    total=False,
)
AttachFloatingIpBody: TypeAlias = "AttachFloatingIpRequest"
FloatingIpInterfaceResponse = TypedDict(
    "FloatingIpInterfaceResponse", {"interface": "Required[FloatingIpInterface]"}, total=False
)
FloatingIpInterface = TypedDict(
    "FloatingIpInterface",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "subnet": "Required[ResourceRef]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "mac": "Required[str]",
        "attached_to": "Required[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "health": "Required[Literal['unknown', 'healthy', 'unhealthy']]",
        "reason": "Required[Literal['unprobed', 'booting', 'probe_failed', 'passing']]",
        "address_id": "NotRequired[str]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
AttachFloatingIpResponse: TypeAlias = "FloatingIpInterfaceResponse"
InterfaceSecurityGroupRequestInput = TypedDict(
    "InterfaceSecurityGroupRequestInput", {"security_group": "Required[str]"}, total=False
)
AttachInterfaceSecurityGroupBody: TypeAlias = "InterfaceSecurityGroupRequestInput"
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
AttachInterfaceSecurityGroupResponse: TypeAlias = "SecurityGroupResponse"
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
        "vpc": "Required[ResourceRef]",
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
    "FloatingIpResponse", {"floating_ip": "Required[FloatingIp]"}, total=False
)
FloatingIp = TypedDict(
    "FloatingIp",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "description": "NotRequired[str]",
        "family": "Required[IpFamily]",
        "attached_to": "Required[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "health_check": "NotRequired[FloatingIpHealthCheck]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "address": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "subnet": "Required[ResourceRef | Literal[None] | None]",
        "vpc": "Required[ResourceRef | Literal[None] | None]",
    },
    total=False,
)
IpFamily: TypeAlias = "Literal['ipv4', 'ipv6']"
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
    "InterfaceResponse", {"interface": "Required[Interface]"}, total=False
)
Interface = TypedDict(
    "Interface",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "subnet": "Required[ResourceRef]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "mac": "Required[str]",
        "attached_to": "Required[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateInterfaceResponse: TypeAlias = "InterfaceResponse"
CreateInterfaceAddressBody: TypeAlias = "AddressRequestInput"
CreateInterfaceAddressResult = TypedDict(
    "CreateInterfaceAddressResult", {"address": "NotRequired[InterfaceAddress]"}, total=False
)
InterfaceAddress = TypedDict(
    "InterfaceAddress",
    {
        "id": "Required[str]",
        "family": "Required[Literal['ipv4', 'ipv6']]",
        "address": "Required[str]",
        "prefix": "Required[str]",
        "primary": "Required[bool]",
        "floating_ips": "Required[list[FloatingIPRef]]",
    },
    total=False,
)
FloatingIPRef = TypedDict(
    "FloatingIPRef",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "visibility": "Required[Literal['public', 'private']]",
        "address": "Required[str]",
    },
    total=False,
)
CreateInterfaceAddressResponse: TypeAlias = "CreateInterfaceAddressResult"
CreateInterfacePrefixRequest = TypedDict(
    "CreateInterfacePrefixRequest", {"pool": "Required[str]"}, total=False
)
CreateInterfacePrefixBody: TypeAlias = "CreateInterfacePrefixRequest"
CreateInterfacePrefixResult = TypedDict(
    "CreateInterfacePrefixResult", {"prefix": "Required[RoutedPrefix]"}, total=False
)
RoutedPrefix = TypedDict(
    "RoutedPrefix",
    {
        "id": "Required[str]",
        "pool": "Required[ResourceRef]",
        "family": "Required[Literal['ipv4']]",
        "prefix": "Required[str]",
    },
    total=False,
)
CreateInterfacePrefixResponse: TypeAlias = "CreateInterfacePrefixResult"
InternetGatewayCreateRequestInput = TypedDict(
    "InternetGatewayCreateRequestInput",
    {
        "vpc": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateInternetGatewayBody: TypeAlias = "InternetGatewayCreateRequestInput"
InternetGatewayResponse = TypedDict(
    "InternetGatewayResponse", {"internet_gateway": "Required[InternetGateway]"}, total=False
)
InternetGateway = TypedDict(
    "InternetGateway",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "attached_vpc": "NotRequired[ResourceRef | Literal[None] | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
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
        "subnet": "Required[ResourceRef]",
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
    "CreatePrefixPoolResult", {"prefix_pool": "Required[PrefixPool]"}, total=False
)
PrefixPool = TypedDict(
    "PrefixPool",
    {"crn": "Required[str]", "id": "Required[str]", "cidr_ipv4": "Required[str]"},
    total=False,
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
        "description": "NotRequired[str]",
        "destination_cidr": "Required[str]",
        "target_type": "Required[RouteTargetType]",
        "next_hop_ip": "NotRequired[str | None]",
        "target_internet_gateway": "NotRequired[ResourceRef]",
        "target_nat_gateway": "NotRequired[ResourceRef]",
        "target_egress_only_gateway": "NotRequired[ResourceRef]",
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
        "vpc": "Required[ResourceRef]",
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
        "description": "NotRequired[str]",
        "direction": "Required[SecurityGroupRuleDirection]",
        "ethertype": "Required[SecurityGroupRuleEthertype]",
        "protocol": "Required[SecurityGroupRuleProtocol]",
        "port_min": "NotRequired[int | None]",
        "port_max": "NotRequired[int | None]",
        "remote_cidr": "NotRequired[str | None]",
        "source_security_group": "NotRequired[ResourceRef]",
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
SubnetResponse = TypedDict("SubnetResponse", {"subnet": "Required[Subnet]"}, total=False)
Subnet = TypedDict(
    "Subnet",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "vpc": "Required[ResourceRef]",
        "route_table": "Required[ResourceRef | Literal[None] | None]",
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
VpcResponse = TypedDict("VpcResponse", {"vpc": "Required[Vpc]"}, total=False)
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
CreateVpcResponse: TypeAlias = "VpcResponse"
SubnetIPv6RequestInput: TypeAlias = (
    "SubnetIPv6RequestInputVariant1 | SubnetIPv6RequestInputVariant2"
)
SubnetIPv6RequestInputVariant1 = TypedDict(
    "SubnetIPv6RequestInputVariant1",
    {
        "allocate_cidr_ipv6": "Required[bool]",
        "cidr_ipv6": "NotRequired[str]",
        "copy_ipv4_security_rules": "NotRequired[bool]",
        "ipv6_routing": "NotRequired[Literal['match_ipv4', 'unchanged', 'internet_gateway', 'nat_gateway', 'egress_only_gateway']]",
    },
    total=False,
)
SubnetIPv6RequestInputVariant2 = TypedDict(
    "SubnetIPv6RequestInputVariant2",
    {
        "allocate_cidr_ipv6": "NotRequired[bool]",
        "cidr_ipv6": "Required[str]",
        "copy_ipv4_security_rules": "NotRequired[bool]",
        "ipv6_routing": "NotRequired[Literal['match_ipv4', 'unchanged', 'internet_gateway', 'nat_gateway', 'egress_only_gateway']]",
    },
    total=False,
)
EnableSubnetIPv6Body: TypeAlias = "SubnetIPv6RequestInput"
EnableSubnetIPv6Response: TypeAlias = "SubnetResponse"
VpcIPv6RequestInput: TypeAlias = "VpcIPv6RequestInputVariant1 | VpcIPv6RequestInputVariant2"
VpcIPv6RequestInputVariant1 = TypedDict(
    "VpcIPv6RequestInputVariant1",
    {"allocate_cidr_ipv6": "Required[bool]", "cidr_ipv6": "NotRequired[str]"},
    total=False,
)
VpcIPv6RequestInputVariant2 = TypedDict(
    "VpcIPv6RequestInputVariant2",
    {"allocate_cidr_ipv6": "NotRequired[bool]", "cidr_ipv6": "Required[str]"},
    total=False,
)
EnableVPCIPv6Body: TypeAlias = "VpcIPv6RequestInput"
EnableVPCIPv6Response: TypeAlias = "VpcResponse"
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
        "description": "NotRequired[str]",
        "destination_cidr": "Required[str]",
        "target_type": "Required[RouteTargetType]",
        "next_hop_ip": "NotRequired[str | None]",
        "target_internet_gateway": "NotRequired[ResourceRef]",
        "target_nat_gateway": "NotRequired[ResourceRef]",
        "target_egress_only_gateway": "NotRequired[ResourceRef]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "route_table": "Required[ResourceRef]",
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
ListFloatingIpInterfacesParameters = TypedDict(
    "ListFloatingIpInterfacesParameters",
    {
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "name": "NotRequired[str]",
    },
    total=False,
)
ListFloatingIpInterfacesQuery: TypeAlias = "ListFloatingIpInterfacesParameters"
FloatingIpInterfaceListResponse = TypedDict(
    "FloatingIpInterfaceListResponse",
    {"interfaces": "Required[list[FloatingIpInterface]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListFloatingIpInterfacesResponse: TypeAlias = "FloatingIpInterfaceListResponse"
ListFloatingIpInterfacesItem: TypeAlias = "FloatingIpInterface"
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
    {"prefixes": "Required[list[RoutedPrefix]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInterfacePrefixesResponse: TypeAlias = "ListInterfacePrefixesResult"
ListInterfacePrefixesItem: TypeAlias = "RoutedPrefix"
ListInterfaceSecurityGroupsParameters = TypedDict(
    "ListInterfaceSecurityGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "marker": "NotRequired[str]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListInterfaceSecurityGroupsQuery: TypeAlias = "ListInterfaceSecurityGroupsParameters"
SecurityGroupListResponse = TypedDict(
    "SecurityGroupListResponse",
    {"security_groups": "Required[list[SecurityGroup]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListInterfaceSecurityGroupsResponse: TypeAlias = "SecurityGroupListResponse"
ListInterfaceSecurityGroupsItem: TypeAlias = "SecurityGroup"
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
    "ListPrefixPoolsResult",
    {"prefix_pools": "Required[list[PrefixPool]]", "meta": "Required[PaginationMeta]"},
    total=False,
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
        "health_check": "NotRequired[FloatingIpHealthCheckInput | Literal[None] | None]",
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
    },
    total=False,
)
UpdateSubnetBody: TypeAlias = "SubnetUpdateRequestInput"
UpdateSubnetResponse: TypeAlias = "SubnetResponse"
VpcUpdateRequestInput = TypedDict(
    "VpcUpdateRequestInput",
    {"description": "NotRequired[str | None]", "tags": "NotRequired[dict[str, str]]"},
    total=False,
)
UpdateVpcBody: TypeAlias = "VpcUpdateRequestInput"
UpdateVpcResponse: TypeAlias = "VpcResponse"
