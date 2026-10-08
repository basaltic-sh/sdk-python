"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation, Unset
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import network as m
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
    "attachFloatingIp": Operation(
        id="attachFloatingIp",
        method="POST",
        path="/v1/floating-ips/{floating_ip_id}/attach",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachInternetGateway": Operation(
        id="attachInternetGateway",
        method="POST",
        path="/v1/internet-gateways/{internet_gateway_id}/attach",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createEgressOnlyGateway": Operation(
        id="createEgressOnlyGateway",
        method="POST",
        path="/v1/egress-only-gateways",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createFloatingIp": Operation(
        id="createFloatingIp",
        method="POST",
        path="/v1/floating-ips",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "createInterface": Operation(
        id="createInterface",
        method="POST",
        path="/v1/interfaces",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createInterfaceAddress": Operation(
        id="createInterfaceAddress",
        method="POST",
        path="/v1/interfaces/{interface_id}/addresses",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createInterfacePrefix": Operation(
        id="createInterfacePrefix",
        method="POST",
        path="/v1/interfaces/{interface_id}/prefixes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createInternetGateway": Operation(
        id="createInternetGateway",
        method="POST",
        path="/v1/internet-gateways",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createNATGateway": Operation(
        id="createNATGateway",
        method="POST",
        path="/v1/nat-gateways",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createPrefixPool": Operation(
        id="createPrefixPool",
        method="POST",
        path="/v1/vpcs/{vpc_id}/prefix-pools",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRoute": Operation(
        id="createRoute",
        method="POST",
        path="/v1/route-tables/{route_table_id}/routes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRouteTable": Operation(
        id="createRouteTable",
        method="POST",
        path="/v1/route-tables",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSecurityGroup": Operation(
        id="createSecurityGroup",
        method="POST",
        path="/v1/security-groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSecurityGroupRule": Operation(
        id="createSecurityGroupRule",
        method="POST",
        path="/v1/security-groups/{security_group_id}/rules",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createSubnet": Operation(
        id="createSubnet",
        method="POST",
        path="/v1/subnets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createVpc": Operation(
        id="createVpc",
        method="POST",
        path="/v1/vpcs",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteEgressOnlyGateway": Operation(
        id="deleteEgressOnlyGateway",
        method="DELETE",
        path="/v1/egress-only-gateways/{egress_only_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteFloatingIp": Operation(
        id="deleteFloatingIp",
        method="DELETE",
        path="/v1/floating-ips/{floating_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInterface": Operation(
        id="deleteInterface",
        method="DELETE",
        path="/v1/interfaces/{interface_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInterfaceAddress": Operation(
        id="deleteInterfaceAddress",
        method="DELETE",
        path="/v1/interfaces/{interface_id}/addresses/{address_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInterfacePrefix": Operation(
        id="deleteInterfacePrefix",
        method="DELETE",
        path="/v1/interfaces/{interface_id}/prefixes/{prefix_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteInternetGateway": Operation(
        id="deleteInternetGateway",
        method="DELETE",
        path="/v1/internet-gateways/{internet_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteNATGateway": Operation(
        id="deleteNATGateway",
        method="DELETE",
        path="/v1/nat-gateways/{nat_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deletePrefixPool": Operation(
        id="deletePrefixPool",
        method="DELETE",
        path="/v1/vpcs/{vpc_id}/prefix-pools/{pool_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRoute": Operation(
        id="deleteRoute",
        method="DELETE",
        path="/v1/route-tables/{route_table_id}/routes/{route_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRouteTable": Operation(
        id="deleteRouteTable",
        method="DELETE",
        path="/v1/route-tables/{route_table_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSecurityGroup": Operation(
        id="deleteSecurityGroup",
        method="DELETE",
        path="/v1/security-groups/{security_group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSecurityGroupRule": Operation(
        id="deleteSecurityGroupRule",
        method="DELETE",
        path="/v1/security-groups/{security_group_id}/rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteSubnet": Operation(
        id="deleteSubnet",
        method="DELETE",
        path="/v1/subnets/{subnet_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteVpc": Operation(
        id="deleteVpc",
        method="DELETE",
        path="/v1/vpcs/{vpc_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachFloatingIp": Operation(
        id="detachFloatingIp",
        method="POST",
        path="/v1/floating-ips/{floating_ip_id}/detach",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    ),
    "detachInternetGateway": Operation(
        id="detachInternetGateway",
        method="POST",
        path="/v1/internet-gateways/{internet_gateway_id}/detach",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getEgressOnlyGateway": Operation(
        id="getEgressOnlyGateway",
        method="GET",
        path="/v1/egress-only-gateways/{egress_only_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getFloatingIp": Operation(
        id="getFloatingIp",
        method="GET",
        path="/v1/floating-ips/{floating_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInterface": Operation(
        id="getInterface",
        method="GET",
        path="/v1/interfaces/{interface_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInterfaceAddress": Operation(
        id="getInterfaceAddress",
        method="GET",
        path="/v1/interfaces/{interface_id}/addresses/{address_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getInternetGateway": Operation(
        id="getInternetGateway",
        method="GET",
        path="/v1/internet-gateways/{internet_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getNATGateway": Operation(
        id="getNATGateway",
        method="GET",
        path="/v1/nat-gateways/{nat_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRoute": Operation(
        id="getRoute",
        method="GET",
        path="/v1/route-tables/{route_table_id}/routes/{route_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRouteTable": Operation(
        id="getRouteTable",
        method="GET",
        path="/v1/route-tables/{route_table_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSecurityGroup": Operation(
        id="getSecurityGroup",
        method="GET",
        path="/v1/security-groups/{security_group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSecurityGroupRule": Operation(
        id="getSecurityGroupRule",
        method="GET",
        path="/v1/security-groups/{security_group_id}/rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getSubnet": Operation(
        id="getSubnet",
        method="GET",
        path="/v1/subnets/{subnet_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getVpc": Operation(
        id="getVpc",
        method="GET",
        path="/v1/vpcs/{vpc_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listEgressOnlyGatewayRoutes": Operation(
        id="listEgressOnlyGatewayRoutes",
        method="GET",
        path="/v1/egress-only-gateways/{egress_only_gateway_id}/routes",
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
        itemsKey="routes",
    ),
    "listEgressOnlyGateways": Operation(
        id="listEgressOnlyGateways",
        method="GET",
        path="/v1/egress-only-gateways",
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
        itemsKey="egress_only_gateways",
    ),
    "listFloatingIps": Operation(
        id="listFloatingIps",
        method="GET",
        path="/v1/floating-ips",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "attached_to": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="floating_ips",
    ),
    "listInterfaceAddresses": Operation(
        id="listInterfaceAddresses",
        method="GET",
        path="/v1/interfaces/{interface_id}/addresses",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="addresses",
    ),
    "listInterfacePrefixes": Operation(
        id="listInterfacePrefixes",
        method="GET",
        path="/v1/interfaces/{interface_id}/prefixes",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="routed_prefixes",
    ),
    "listInterfaceSecurityGroups": Operation(
        id="listInterfaceSecurityGroups",
        method="GET",
        path="/v1/interfaces/{interface_id}/security-groups",
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
        itemsKey="security_group_ids",
    ),
    "listInterfaces": Operation(
        id="listInterfaces",
        method="GET",
        path="/v1/interfaces",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "subnet": {"style": "form", "explode": True},
            "vpc": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="interfaces",
    ),
    "listInternetGatewayRoutes": Operation(
        id="listInternetGatewayRoutes",
        method="GET",
        path="/v1/internet-gateways/{internet_gateway_id}/routes",
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
        itemsKey="routes",
    ),
    "listInternetGateways": Operation(
        id="listInternetGateways",
        method="GET",
        path="/v1/internet-gateways",
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
        itemsKey="internet_gateways",
    ),
    "listNATGatewayRoutes": Operation(
        id="listNATGatewayRoutes",
        method="GET",
        path="/v1/nat-gateways/{nat_gateway_id}/routes",
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
        itemsKey="routes",
    ),
    "listNATGateways": Operation(
        id="listNATGateways",
        method="GET",
        path="/v1/nat-gateways",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "subnet": {"style": "form", "explode": True},
            "vpc": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="nat_gateways",
    ),
    "listPrefixPools": Operation(
        id="listPrefixPools",
        method="GET",
        path="/v1/vpcs/{vpc_id}/prefix-pools",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="prefix_pools",
    ),
    "listRouteTables": Operation(
        id="listRouteTables",
        method="GET",
        path="/v1/route-tables",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "vpc": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="route_tables",
    ),
    "listRoutes": Operation(
        id="listRoutes",
        method="GET",
        path="/v1/route-tables/{route_table_id}/routes",
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
        itemsKey="routes",
    ),
    "listSecurityGroupRules": Operation(
        id="listSecurityGroupRules",
        method="GET",
        path="/v1/security-groups/{security_group_id}/rules",
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
        itemsKey="rules",
    ),
    "listSecurityGroups": Operation(
        id="listSecurityGroups",
        method="GET",
        path="/v1/security-groups",
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
        itemsKey="security_groups",
    ),
    "listSubnets": Operation(
        id="listSubnets",
        method="GET",
        path="/v1/subnets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "vpc": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="subnets",
    ),
    "listVpcs": Operation(
        id="listVpcs",
        method="GET",
        path="/v1/vpcs",
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
        itemsKey="vpcs",
    ),
    "setInterfaceSecurityGroups": Operation(
        id="setInterfaceSecurityGroups",
        method="PUT",
        path="/v1/interfaces/{interface_id}/security-groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateEgressOnlyGateway": Operation(
        id="updateEgressOnlyGateway",
        method="PATCH",
        path="/v1/egress-only-gateways/{egress_only_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateFloatingIp": Operation(
        id="updateFloatingIp",
        method="PATCH",
        path="/v1/floating-ips/{floating_ip_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateInterface": Operation(
        id="updateInterface",
        method="PATCH",
        path="/v1/interfaces/{interface_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateInternetGateway": Operation(
        id="updateInternetGateway",
        method="PATCH",
        path="/v1/internet-gateways/{internet_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateNATGateway": Operation(
        id="updateNATGateway",
        method="PATCH",
        path="/v1/nat-gateways/{nat_gateway_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRoute": Operation(
        id="updateRoute",
        method="PATCH",
        path="/v1/route-tables/{route_table_id}/routes/{route_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRouteTable": Operation(
        id="updateRouteTable",
        method="PATCH",
        path="/v1/route-tables/{route_table_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateSecurityGroup": Operation(
        id="updateSecurityGroup",
        method="PATCH",
        path="/v1/security-groups/{security_group_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateSubnet": Operation(
        id="updateSubnet",
        method="PATCH",
        path="/v1/subnets/{subnet_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateVpc": Operation(
        id="updateVpc",
        method="PATCH",
        path="/v1/vpcs/{vpc_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class NetworkService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach_floating_ip(
        self,
        floating_ip_id: str,
        body: m.AttachFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachFloatingIpResponse]:
        "Attach a floating IP to an interface"
        return cast(
            ApiResponse[m.AttachFloatingIpResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["attachFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    def attach_internet_gateway(
        self,
        internet_gateway_id: str,
        body: m.AttachInternetGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInternetGatewayResponse]:
        "Attach internet gateway to a VPC"
        return cast(
            ApiResponse[m.AttachInternetGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["attachInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                body,
                None,
                options,
            ),
        )

    def create_egress_only_gateway(
        self, body: m.CreateEgressOnlyGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateEgressOnlyGatewayResponse]:
        "Create egress-only gateway"
        return cast(
            ApiResponse[m.CreateEgressOnlyGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createEgressOnlyGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_floating_ip(
        self, body: m.CreateFloatingIpBody | Unset = UNSET, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateFloatingIpResponse]:
        "Allocate floating IP"
        return cast(
            ApiResponse[m.CreateFloatingIpResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createFloatingIp"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_interface(
        self, body: m.CreateInterfaceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInterfaceResponse]:
        "Create interface"
        return cast(
            ApiResponse[m.CreateInterfaceResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterface"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_interface_address(
        self,
        interface_id: str,
        body: m.CreateInterfaceAddressBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateInterfaceAddressResponse]:
        "Create interface address"
        return cast(
            ApiResponse[m.CreateInterfaceAddressResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterfaceAddress"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    def create_interface_prefix(
        self,
        interface_id: str,
        body: m.CreateInterfacePrefixBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateInterfacePrefixResponse]:
        "Create interface prefix"
        return cast(
            ApiResponse[m.CreateInterfacePrefixResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterfacePrefix"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    def create_internet_gateway(
        self, body: m.CreateInternetGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInternetGatewayResponse]:
        "Create internet gateway"
        return cast(
            ApiResponse[m.CreateInternetGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInternetGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_nat_gateway(
        self, body: m.CreateNATGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateNATGatewayResponse]:
        "Create NAT gateway"
        return cast(
            ApiResponse[m.CreateNATGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createNATGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_prefix_pool(
        self, vpc_id: str, body: m.CreatePrefixPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePrefixPoolResponse]:
        "Create prefix pool"
        return cast(
            ApiResponse[m.CreatePrefixPoolResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createPrefixPool"],
                "json",
                {"vpc_id": vpc_id},
                body,
                None,
                options,
            ),
        )

    def create_route(
        self, route_table_id: str, body: m.CreateRouteBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRouteResponse]:
        "Create route"
        return cast(
            ApiResponse[m.CreateRouteResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createRoute"],
                "json",
                {"route_table_id": route_table_id},
                body,
                None,
                options,
            ),
        )

    def create_route_table(
        self, body: m.CreateRouteTableBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRouteTableResponse]:
        "Create route table"
        return cast(
            ApiResponse[m.CreateRouteTableResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createRouteTable"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_security_group(
        self, body: m.CreateSecurityGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSecurityGroupResponse]:
        "Create security group"
        return cast(
            ApiResponse[m.CreateSecurityGroupResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSecurityGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_security_group_rule(
        self,
        security_group_id: str,
        body: m.CreateSecurityGroupRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateSecurityGroupRuleResponse]:
        "Create security group rule"
        return cast(
            ApiResponse[m.CreateSecurityGroupRuleResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSecurityGroupRule"],
                "json",
                {"security_group_id": security_group_id},
                body,
                None,
                options,
            ),
        )

    def create_subnet(
        self, body: m.CreateSubnetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSubnetResponse]:
        "Create subnet"
        return cast(
            ApiResponse[m.CreateSubnetResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSubnet"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_vpc(
        self, body: m.CreateVpcBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateVpcResponse]:
        "Create VPC"
        return cast(
            ApiResponse[m.CreateVpcResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createVpc"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_egress_only_gateway(
        self, egress_only_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete egress-only gateway"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteEgressOnlyGateway"],
                "discard",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_floating_ip(
        self, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Release floating IP"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteFloatingIp"],
                "discard",
                {"floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_interface(self, interface_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete interface"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterface"],
                "discard",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_interface_address(
        self, interface_id: str, address_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete interface address"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterfaceAddress"],
                "discard",
                {"interface_id": interface_id, "address_id": address_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_interface_prefix(
        self, interface_id: str, prefix_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete interface prefix"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterfacePrefix"],
                "discard",
                {"interface_id": interface_id, "prefix_id": prefix_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete internet gateway"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInternetGateway"],
                "discard",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_nat_gateway(
        self, nat_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete NAT gateway"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteNATGateway"],
                "discard",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_prefix_pool(
        self, vpc_id: str, pool_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete prefix pool"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deletePrefixPool"],
                "discard",
                {"vpc_id": vpc_id, "pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_route(
        self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete route"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteRoute"],
                "discard",
                {"route_table_id": route_table_id, "route_id": route_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_route_table(
        self, route_table_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete route table"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteRouteTable"],
                "discard",
                {"route_table_id": route_table_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_security_group(
        self, security_group_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete security group"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSecurityGroup"],
                "discard",
                {"security_group_id": security_group_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_security_group_rule(
        self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete security group rule"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSecurityGroupRule"],
                "discard",
                {"security_group_id": security_group_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_subnet(self, subnet_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete subnet"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSubnet"],
                "discard",
                {"subnet_id": subnet_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_vpc(self, vpc_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete VPC"
        return cast(
            None,
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteVpc"],
                "discard",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_floating_ip(
        self,
        floating_ip_id: str,
        body: m.DetachFloatingIpBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DetachFloatingIpResponse]:
        "Detach a floating IP"
        return cast(
            ApiResponse[m.DetachFloatingIpResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["detachFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    def detach_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DetachInternetGatewayResponse]:
        "Detach internet gateway from its VPC"
        return cast(
            ApiResponse[m.DetachInternetGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["detachInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_egress_only_gateway(
        self, egress_only_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetEgressOnlyGatewayResponse]:
        "Get egress-only gateway"
        return cast(
            ApiResponse[m.GetEgressOnlyGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getEgressOnlyGateway"],
                "json",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_egress_only_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetEgressOnlyGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetEgressOnlyGatewayResource]:
        return cast(
            ApiResponse[m.GetEgressOnlyGatewayResource],
            resolve_reference(
                reference,
                lambda id: self.get_egress_only_gateway(id, options=options),
                lambda match: self.list_egress_only_gateways(
                    query=cast(
                        m.ListEgressOnlyGatewaysQuery,
                        {**reference_scope(scope), **match, "limit": 2},
                    ),
                    options=options,
                ),
                True,
                "egress_only_gateway",
            ),
        )

    def get_floating_ip(
        self, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetFloatingIpResponse]:
        "Get floating IP"
        return cast(
            ApiResponse[m.GetFloatingIpResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_floating_ip_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetFloatingIpScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetFloatingIpResource]:
        return cast(
            ApiResponse[m.GetFloatingIpResource],
            resolve_reference(
                reference,
                lambda id: self.get_floating_ip(id, options=options),
                lambda match: self.list_floating_ips(
                    query=cast(
                        m.ListFloatingIpsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "floating_ip",
            ),
        )

    def get_interface(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInterfaceResponse]:
        "Get interface"
        return cast(
            ApiResponse[m.GetInterfaceResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInterface"],
                "json",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_interface_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInterfaceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInterfaceResource]:
        return cast(
            ApiResponse[m.GetInterfaceResource],
            resolve_reference(
                reference,
                lambda id: self.get_interface(id, options=options),
                lambda match: self.list_interfaces(
                    query=cast(
                        m.ListInterfacesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "interface",
            ),
        )

    def get_interface_address(
        self, interface_id: str, address_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInterfaceAddressResponse]:
        "Get interface address"
        return cast(
            ApiResponse[m.GetInterfaceAddressResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInterfaceAddress"],
                "json",
                {"interface_id": interface_id, "address_id": address_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInternetGatewayResponse]:
        "Get internet gateway"
        return cast(
            ApiResponse[m.GetInternetGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_internet_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInternetGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInternetGatewayResource]:
        return cast(
            ApiResponse[m.GetInternetGatewayResource],
            resolve_reference(
                reference,
                lambda id: self.get_internet_gateway(id, options=options),
                lambda match: self.list_internet_gateways(
                    query=cast(
                        m.ListInternetGatewaysQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "internet_gateway",
            ),
        )

    def get_nat_gateway(
        self, nat_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetNATGatewayResponse]:
        "Get NAT gateway"
        return cast(
            ApiResponse[m.GetNATGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getNATGateway"],
                "json",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_nat_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetNATGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetNATGatewayResource]:
        return cast(
            ApiResponse[m.GetNATGatewayResource],
            resolve_reference(
                reference,
                lambda id: self.get_nat_gateway(id, options=options),
                lambda match: self.list_nat_gateways(
                    query=cast(
                        m.ListNATGatewaysQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "nat_gateway",
            ),
        )

    def get_route(
        self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRouteResponse]:
        "Get route"
        return cast(
            ApiResponse[m.GetRouteResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getRoute"],
                "json",
                {"route_table_id": route_table_id, "route_id": route_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_route_by_reference(
        self,
        route_table_id: str,
        reference: str,
        *,
        scope: m.GetRouteScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRouteResource]:
        return cast(
            ApiResponse[m.GetRouteResource],
            resolve_reference(
                reference,
                lambda id: self.get_route(route_table_id, id, options=options),
                lambda match: self.list_routes(
                    route_table_id,
                    query=cast(m.ListRoutesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "route",
            ),
        )

    def get_route_table(
        self, route_table_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRouteTableResponse]:
        "Get route table"
        return cast(
            ApiResponse[m.GetRouteTableResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getRouteTable"],
                "json",
                {"route_table_id": route_table_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_route_table_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRouteTableScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRouteTableResource]:
        return cast(
            ApiResponse[m.GetRouteTableResource],
            resolve_reference(
                reference,
                lambda id: self.get_route_table(id, options=options),
                lambda match: self.list_route_tables(
                    query=cast(
                        m.ListRouteTablesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "route_table",
            ),
        )

    def get_security_group(
        self, security_group_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSecurityGroupResponse]:
        "Get security group"
        return cast(
            ApiResponse[m.GetSecurityGroupResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSecurityGroup"],
                "json",
                {"security_group_id": security_group_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_security_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSecurityGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecurityGroupResource]:
        return cast(
            ApiResponse[m.GetSecurityGroupResource],
            resolve_reference(
                reference,
                lambda id: self.get_security_group(id, options=options),
                lambda match: self.list_security_groups(
                    query=cast(
                        m.ListSecurityGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "security_group",
            ),
        )

    def get_security_group_rule(
        self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSecurityGroupRuleResponse]:
        "Get security group rule"
        return cast(
            ApiResponse[m.GetSecurityGroupRuleResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSecurityGroupRule"],
                "json",
                {"security_group_id": security_group_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_security_group_rule_by_reference(
        self,
        security_group_id: str,
        reference: str,
        *,
        scope: m.GetSecurityGroupRuleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecurityGroupRuleResource]:
        return cast(
            ApiResponse[m.GetSecurityGroupRuleResource],
            resolve_reference(
                reference,
                lambda id: self.get_security_group_rule(security_group_id, id, options=options),
                lambda match: self.list_security_group_rules(
                    security_group_id,
                    query=cast(
                        m.ListSecurityGroupRulesQuery,
                        {**reference_scope(scope), **match, "limit": 2},
                    ),
                    options=options,
                ),
                True,
                "rule",
            ),
        )

    def get_subnet(
        self, subnet_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSubnetResponse]:
        "Get subnet"
        return cast(
            ApiResponse[m.GetSubnetResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSubnet"],
                "json",
                {"subnet_id": subnet_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_subnet_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSubnetScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSubnetResource]:
        return cast(
            ApiResponse[m.GetSubnetResource],
            resolve_reference(
                reference,
                lambda id: self.get_subnet(id, options=options),
                lambda match: self.list_subnets(
                    query=cast(m.ListSubnetsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "subnet",
            ),
        )

    def get_vpc(
        self, vpc_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetVpcResponse]:
        "Get VPC"
        return cast(
            ApiResponse[m.GetVpcResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getVpc"],
                "json",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_vpc_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetVpcScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetVpcResource]:
        return cast(
            ApiResponse[m.GetVpcResource],
            resolve_reference(
                reference,
                lambda id: self.get_vpc(id, options=options),
                lambda match: self.list_vpcs(
                    query=cast(m.ListVpcsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "vpc",
            ),
        )

    def list_egress_only_gateway_routes(
        self,
        egress_only_gateway_id: str,
        *,
        query: m.ListEgressOnlyGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListEgressOnlyGatewayRoutesResponse, m.ListEgressOnlyGatewayRoutesItem]:
        "List egress-only gateway routes"
        return cast(
            Page[m.ListEgressOnlyGatewayRoutesResponse, m.ListEgressOnlyGatewayRoutesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listEgressOnlyGatewayRoutes"],
                "page",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_egress_only_gateway_routes_all(
        self,
        egress_only_gateway_id: str,
        *,
        query: m.ListEgressOnlyGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListEgressOnlyGatewayRoutesItem]:
        return iterate_pages(
            lambda marker: self.list_egress_only_gateway_routes(
                egress_only_gateway_id,
                query=cast(m.ListEgressOnlyGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_egress_only_gateways(
        self,
        *,
        query: m.ListEgressOnlyGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListEgressOnlyGatewaysResponse, m.ListEgressOnlyGatewaysItem]:
        "List egress-only gateways"
        return cast(
            Page[m.ListEgressOnlyGatewaysResponse, m.ListEgressOnlyGatewaysItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listEgressOnlyGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_egress_only_gateways_all(
        self,
        *,
        query: m.ListEgressOnlyGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListEgressOnlyGatewaysItem]:
        return iterate_pages(
            lambda marker: self.list_egress_only_gateways(
                query=cast(m.ListEgressOnlyGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_floating_ips(
        self, *, query: m.ListFloatingIpsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListFloatingIpsResponse, m.ListFloatingIpsItem]:
        "List floating IPs"
        return cast(
            Page[m.ListFloatingIpsResponse, m.ListFloatingIpsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listFloatingIps"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_floating_ips_all(
        self, *, query: m.ListFloatingIpsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListFloatingIpsItem]:
        return iterate_pages(
            lambda marker: self.list_floating_ips(
                query=cast(m.ListFloatingIpsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_interface_addresses(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListInterfaceAddressesResponse, m.ListInterfaceAddressesItem]:
        "List interface addresses"
        return cast(
            Page[m.ListInterfaceAddressesResponse, m.ListInterfaceAddressesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaceAddresses"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_interface_prefixes(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListInterfacePrefixesResponse, m.ListInterfacePrefixesItem]:
        "List interface prefixes"
        return cast(
            Page[m.ListInterfacePrefixesResponse, m.ListInterfacePrefixesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfacePrefixes"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_interface_security_groups(
        self,
        interface_id: str,
        *,
        query: m.ListInterfaceSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInterfaceSecurityGroupsResponse, m.ListInterfaceSecurityGroupsItem]:
        "List interface security-group membership"
        return cast(
            Page[m.ListInterfaceSecurityGroupsResponse, m.ListInterfaceSecurityGroupsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaceSecurityGroups"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_interfaces(
        self, *, query: m.ListInterfacesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInterfacesResponse, m.ListInterfacesItem]:
        "List interfaces"
        return cast(
            Page[m.ListInterfacesResponse, m.ListInterfacesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaces"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_interfaces_all(
        self, *, query: m.ListInterfacesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListInterfacesItem]:
        return iterate_pages(
            lambda marker: self.list_interfaces(
                query=cast(m.ListInterfacesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_internet_gateway_routes(
        self,
        internet_gateway_id: str,
        *,
        query: m.ListInternetGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInternetGatewayRoutesResponse, m.ListInternetGatewayRoutesItem]:
        "List internet gateway routes"
        return cast(
            Page[m.ListInternetGatewayRoutesResponse, m.ListInternetGatewayRoutesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInternetGatewayRoutes"],
                "page",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_internet_gateway_routes_all(
        self,
        internet_gateway_id: str,
        *,
        query: m.ListInternetGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListInternetGatewayRoutesItem]:
        return iterate_pages(
            lambda marker: self.list_internet_gateway_routes(
                internet_gateway_id,
                query=cast(m.ListInternetGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_internet_gateways(
        self,
        *,
        query: m.ListInternetGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInternetGatewaysResponse, m.ListInternetGatewaysItem]:
        "List internet gateways"
        return cast(
            Page[m.ListInternetGatewaysResponse, m.ListInternetGatewaysItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInternetGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_internet_gateways_all(
        self,
        *,
        query: m.ListInternetGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListInternetGatewaysItem]:
        return iterate_pages(
            lambda marker: self.list_internet_gateways(
                query=cast(m.ListInternetGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_nat_gateway_routes(
        self,
        nat_gateway_id: str,
        *,
        query: m.ListNATGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListNATGatewayRoutesResponse, m.ListNATGatewayRoutesItem]:
        "List NAT gateway routes"
        return cast(
            Page[m.ListNATGatewayRoutesResponse, m.ListNATGatewayRoutesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listNATGatewayRoutes"],
                "page",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_nat_gateway_routes_all(
        self,
        nat_gateway_id: str,
        *,
        query: m.ListNATGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListNATGatewayRoutesItem]:
        return iterate_pages(
            lambda marker: self.list_nat_gateway_routes(
                nat_gateway_id,
                query=cast(m.ListNATGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_nat_gateways(
        self, *, query: m.ListNATGatewaysQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListNATGatewaysResponse, m.ListNATGatewaysItem]:
        "List NAT gateways"
        return cast(
            Page[m.ListNATGatewaysResponse, m.ListNATGatewaysItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listNATGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_nat_gateways_all(
        self, *, query: m.ListNATGatewaysQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListNATGatewaysItem]:
        return iterate_pages(
            lambda marker: self.list_nat_gateways(
                query=cast(m.ListNATGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_prefix_pools(
        self, vpc_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListPrefixPoolsResponse, m.ListPrefixPoolsItem]:
        "List prefix pools"
        return cast(
            Page[m.ListPrefixPoolsResponse, m.ListPrefixPoolsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listPrefixPools"],
                "page",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    def list_route_tables(
        self, *, query: m.ListRouteTablesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRouteTablesResponse, m.ListRouteTablesItem]:
        "List route tables"
        return cast(
            Page[m.ListRouteTablesResponse, m.ListRouteTablesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listRouteTables"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_route_tables_all(
        self, *, query: m.ListRouteTablesQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListRouteTablesItem]:
        return iterate_pages(
            lambda marker: self.list_route_tables(
                query=cast(m.ListRouteTablesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_routes(
        self,
        route_table_id: str,
        *,
        query: m.ListRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRoutesResponse, m.ListRoutesItem]:
        "List routes"
        return cast(
            Page[m.ListRoutesResponse, m.ListRoutesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listRoutes"],
                "page",
                {"route_table_id": route_table_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_routes_all(
        self,
        route_table_id: str,
        *,
        query: m.ListRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListRoutesItem]:
        return iterate_pages(
            lambda marker: self.list_routes(
                route_table_id,
                query=cast(m.ListRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_security_group_rules(
        self,
        security_group_id: str,
        *,
        query: m.ListSecurityGroupRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSecurityGroupRulesResponse, m.ListSecurityGroupRulesItem]:
        "List security group rules"
        return cast(
            Page[m.ListSecurityGroupRulesResponse, m.ListSecurityGroupRulesItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSecurityGroupRules"],
                "page",
                {"security_group_id": security_group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_security_group_rules_all(
        self,
        security_group_id: str,
        *,
        query: m.ListSecurityGroupRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListSecurityGroupRulesItem]:
        return iterate_pages(
            lambda marker: self.list_security_group_rules(
                security_group_id,
                query=cast(m.ListSecurityGroupRulesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_security_groups(
        self,
        *,
        query: m.ListSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSecurityGroupsResponse, m.ListSecurityGroupsItem]:
        "List security groups"
        return cast(
            Page[m.ListSecurityGroupsResponse, m.ListSecurityGroupsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSecurityGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_security_groups_all(
        self,
        *,
        query: m.ListSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListSecurityGroupsItem]:
        return iterate_pages(
            lambda marker: self.list_security_groups(
                query=cast(m.ListSecurityGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_subnets(
        self, *, query: m.ListSubnetsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSubnetsResponse, m.ListSubnetsItem]:
        "List subnets"
        return cast(
            Page[m.ListSubnetsResponse, m.ListSubnetsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSubnets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_subnets_all(
        self, *, query: m.ListSubnetsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListSubnetsItem]:
        return iterate_pages(
            lambda marker: self.list_subnets(
                query=cast(m.ListSubnetsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_vpcs(
        self, *, query: m.ListVpcsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVpcsResponse, m.ListVpcsItem]:
        "List VPCs"
        return cast(
            Page[m.ListVpcsResponse, m.ListVpcsItem],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listVpcs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_vpcs_all(
        self, *, query: m.ListVpcsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListVpcsItem]:
        return iterate_pages(
            lambda marker: self.list_vpcs(
                query=cast(m.ListVpcsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def set_interface_security_groups(
        self,
        interface_id: str,
        body: m.SetInterfaceSecurityGroupsBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetInterfaceSecurityGroupsResponse]:
        "Set interface security-group membership"
        return cast(
            ApiResponse[m.SetInterfaceSecurityGroupsResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["setInterfaceSecurityGroups"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    def update_egress_only_gateway(
        self,
        egress_only_gateway_id: str,
        body: m.UpdateEgressOnlyGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateEgressOnlyGatewayResponse]:
        "Update egress-only gateway"
        return cast(
            ApiResponse[m.UpdateEgressOnlyGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateEgressOnlyGateway"],
                "json",
                {"egress_only_gateway_id": egress_only_gateway_id},
                body,
                None,
                options,
            ),
        )

    def update_floating_ip(
        self,
        floating_ip_id: str,
        body: m.UpdateFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateFloatingIpResponse]:
        "Update floating IP"
        return cast(
            ApiResponse[m.UpdateFloatingIpResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    def update_interface(
        self,
        interface_id: str,
        body: m.UpdateInterfaceBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateInterfaceResponse]:
        "Update interface"
        return cast(
            ApiResponse[m.UpdateInterfaceResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateInterface"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    def update_internet_gateway(
        self,
        internet_gateway_id: str,
        body: m.UpdateInternetGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateInternetGatewayResponse]:
        "Update internet gateway"
        return cast(
            ApiResponse[m.UpdateInternetGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                body,
                None,
                options,
            ),
        )

    def update_nat_gateway(
        self,
        nat_gateway_id: str,
        body: m.UpdateNATGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateNATGatewayResponse]:
        "Update NAT gateway"
        return cast(
            ApiResponse[m.UpdateNATGatewayResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateNATGateway"],
                "json",
                {"nat_gateway_id": nat_gateway_id},
                body,
                None,
                options,
            ),
        )

    def update_route(
        self,
        route_table_id: str,
        route_id: str,
        body: m.UpdateRouteBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRouteResponse]:
        "Update route"
        return cast(
            ApiResponse[m.UpdateRouteResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateRoute"],
                "json",
                {"route_table_id": route_table_id, "route_id": route_id},
                body,
                None,
                options,
            ),
        )

    def update_route_table(
        self,
        route_table_id: str,
        body: m.UpdateRouteTableBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRouteTableResponse]:
        "Update route table"
        return cast(
            ApiResponse[m.UpdateRouteTableResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateRouteTable"],
                "json",
                {"route_table_id": route_table_id},
                body,
                None,
                options,
            ),
        )

    def update_security_group(
        self,
        security_group_id: str,
        body: m.UpdateSecurityGroupBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSecurityGroupResponse]:
        "Update security group"
        return cast(
            ApiResponse[m.UpdateSecurityGroupResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateSecurityGroup"],
                "json",
                {"security_group_id": security_group_id},
                body,
                None,
                options,
            ),
        )

    def update_subnet(
        self, subnet_id: str, body: m.UpdateSubnetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSubnetResponse]:
        "Update subnet"
        return cast(
            ApiResponse[m.UpdateSubnetResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateSubnet"],
                "json",
                {"subnet_id": subnet_id},
                body,
                None,
                options,
            ),
        )

    def update_vpc(
        self, vpc_id: str, body: m.UpdateVpcBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateVpcResponse]:
        "Update VPC"
        return cast(
            ApiResponse[m.UpdateVpcResponse],
            self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateVpc"],
                "json",
                {"vpc_id": vpc_id},
                body,
                None,
                options,
            ),
        )


class AsyncNetworkService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach_floating_ip(
        self,
        floating_ip_id: str,
        body: m.AttachFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachFloatingIpResponse]:
        "Attach a floating IP to an interface"
        return cast(
            ApiResponse[m.AttachFloatingIpResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["attachFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    async def attach_internet_gateway(
        self,
        internet_gateway_id: str,
        body: m.AttachInternetGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachInternetGatewayResponse]:
        "Attach internet gateway to a VPC"
        return cast(
            ApiResponse[m.AttachInternetGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["attachInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                body,
                None,
                options,
            ),
        )

    async def create_egress_only_gateway(
        self, body: m.CreateEgressOnlyGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateEgressOnlyGatewayResponse]:
        "Create egress-only gateway"
        return cast(
            ApiResponse[m.CreateEgressOnlyGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createEgressOnlyGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_floating_ip(
        self, body: m.CreateFloatingIpBody | Unset = UNSET, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateFloatingIpResponse]:
        "Allocate floating IP"
        return cast(
            ApiResponse[m.CreateFloatingIpResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createFloatingIp"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_interface(
        self, body: m.CreateInterfaceBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInterfaceResponse]:
        "Create interface"
        return cast(
            ApiResponse[m.CreateInterfaceResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterface"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_interface_address(
        self,
        interface_id: str,
        body: m.CreateInterfaceAddressBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateInterfaceAddressResponse]:
        "Create interface address"
        return cast(
            ApiResponse[m.CreateInterfaceAddressResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterfaceAddress"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    async def create_interface_prefix(
        self,
        interface_id: str,
        body: m.CreateInterfacePrefixBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateInterfacePrefixResponse]:
        "Create interface prefix"
        return cast(
            ApiResponse[m.CreateInterfacePrefixResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInterfacePrefix"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    async def create_internet_gateway(
        self, body: m.CreateInternetGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateInternetGatewayResponse]:
        "Create internet gateway"
        return cast(
            ApiResponse[m.CreateInternetGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createInternetGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_nat_gateway(
        self, body: m.CreateNATGatewayBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateNATGatewayResponse]:
        "Create NAT gateway"
        return cast(
            ApiResponse[m.CreateNATGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createNATGateway"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_prefix_pool(
        self, vpc_id: str, body: m.CreatePrefixPoolBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreatePrefixPoolResponse]:
        "Create prefix pool"
        return cast(
            ApiResponse[m.CreatePrefixPoolResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createPrefixPool"],
                "json",
                {"vpc_id": vpc_id},
                body,
                None,
                options,
            ),
        )

    async def create_route(
        self, route_table_id: str, body: m.CreateRouteBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRouteResponse]:
        "Create route"
        return cast(
            ApiResponse[m.CreateRouteResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createRoute"],
                "json",
                {"route_table_id": route_table_id},
                body,
                None,
                options,
            ),
        )

    async def create_route_table(
        self, body: m.CreateRouteTableBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateRouteTableResponse]:
        "Create route table"
        return cast(
            ApiResponse[m.CreateRouteTableResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createRouteTable"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_security_group(
        self, body: m.CreateSecurityGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSecurityGroupResponse]:
        "Create security group"
        return cast(
            ApiResponse[m.CreateSecurityGroupResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSecurityGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_security_group_rule(
        self,
        security_group_id: str,
        body: m.CreateSecurityGroupRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateSecurityGroupRuleResponse]:
        "Create security group rule"
        return cast(
            ApiResponse[m.CreateSecurityGroupRuleResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSecurityGroupRule"],
                "json",
                {"security_group_id": security_group_id},
                body,
                None,
                options,
            ),
        )

    async def create_subnet(
        self, body: m.CreateSubnetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateSubnetResponse]:
        "Create subnet"
        return cast(
            ApiResponse[m.CreateSubnetResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createSubnet"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_vpc(
        self, body: m.CreateVpcBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateVpcResponse]:
        "Create VPC"
        return cast(
            ApiResponse[m.CreateVpcResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["createVpc"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_egress_only_gateway(
        self, egress_only_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete egress-only gateway"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteEgressOnlyGateway"],
                "discard",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_floating_ip(
        self, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Release floating IP"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteFloatingIp"],
                "discard",
                {"floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_interface(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete interface"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterface"],
                "discard",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_interface_address(
        self, interface_id: str, address_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete interface address"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterfaceAddress"],
                "discard",
                {"interface_id": interface_id, "address_id": address_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_interface_prefix(
        self, interface_id: str, prefix_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete interface prefix"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInterfacePrefix"],
                "discard",
                {"interface_id": interface_id, "prefix_id": prefix_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete internet gateway"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteInternetGateway"],
                "discard",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_nat_gateway(
        self, nat_gateway_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete NAT gateway"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteNATGateway"],
                "discard",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_prefix_pool(
        self, vpc_id: str, pool_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete prefix pool"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deletePrefixPool"],
                "discard",
                {"vpc_id": vpc_id, "pool_id": pool_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_route(
        self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete route"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteRoute"],
                "discard",
                {"route_table_id": route_table_id, "route_id": route_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_route_table(
        self, route_table_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete route table"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteRouteTable"],
                "discard",
                {"route_table_id": route_table_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_security_group(
        self, security_group_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete security group"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSecurityGroup"],
                "discard",
                {"security_group_id": security_group_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_security_group_rule(
        self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete security group rule"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSecurityGroupRule"],
                "discard",
                {"security_group_id": security_group_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_subnet(self, subnet_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete subnet"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteSubnet"],
                "discard",
                {"subnet_id": subnet_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_vpc(self, vpc_id: str, *, options: RequestOptions | None = None) -> None:
        "Delete VPC"
        return cast(
            None,
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["deleteVpc"],
                "discard",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_floating_ip(
        self,
        floating_ip_id: str,
        body: m.DetachFloatingIpBody | Unset = UNSET,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.DetachFloatingIpResponse]:
        "Detach a floating IP"
        return cast(
            ApiResponse[m.DetachFloatingIpResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["detachFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    async def detach_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.DetachInternetGatewayResponse]:
        "Detach internet gateway from its VPC"
        return cast(
            ApiResponse[m.DetachInternetGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["detachInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_egress_only_gateway(
        self, egress_only_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetEgressOnlyGatewayResponse]:
        "Get egress-only gateway"
        return cast(
            ApiResponse[m.GetEgressOnlyGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getEgressOnlyGateway"],
                "json",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_egress_only_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetEgressOnlyGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetEgressOnlyGatewayResource]:
        return cast(
            ApiResponse[m.GetEgressOnlyGatewayResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_egress_only_gateway(id, options=options),
                lambda match: self.list_egress_only_gateways(
                    query=cast(
                        m.ListEgressOnlyGatewaysQuery,
                        {**reference_scope(scope), **match, "limit": 2},
                    ),
                    options=options,
                ),
                True,
                "egress_only_gateway",
            ),
        )

    async def get_floating_ip(
        self, floating_ip_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetFloatingIpResponse]:
        "Get floating IP"
        return cast(
            ApiResponse[m.GetFloatingIpResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_floating_ip_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetFloatingIpScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetFloatingIpResource]:
        return cast(
            ApiResponse[m.GetFloatingIpResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_floating_ip(id, options=options),
                lambda match: self.list_floating_ips(
                    query=cast(
                        m.ListFloatingIpsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "floating_ip",
            ),
        )

    async def get_interface(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInterfaceResponse]:
        "Get interface"
        return cast(
            ApiResponse[m.GetInterfaceResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInterface"],
                "json",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_interface_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInterfaceScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInterfaceResource]:
        return cast(
            ApiResponse[m.GetInterfaceResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_interface(id, options=options),
                lambda match: self.list_interfaces(
                    query=cast(
                        m.ListInterfacesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "interface",
            ),
        )

    async def get_interface_address(
        self, interface_id: str, address_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInterfaceAddressResponse]:
        "Get interface address"
        return cast(
            ApiResponse[m.GetInterfaceAddressResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInterfaceAddress"],
                "json",
                {"interface_id": interface_id, "address_id": address_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_internet_gateway(
        self, internet_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetInternetGatewayResponse]:
        "Get internet gateway"
        return cast(
            ApiResponse[m.GetInternetGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_internet_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetInternetGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetInternetGatewayResource]:
        return cast(
            ApiResponse[m.GetInternetGatewayResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_internet_gateway(id, options=options),
                lambda match: self.list_internet_gateways(
                    query=cast(
                        m.ListInternetGatewaysQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "internet_gateway",
            ),
        )

    async def get_nat_gateway(
        self, nat_gateway_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetNATGatewayResponse]:
        "Get NAT gateway"
        return cast(
            ApiResponse[m.GetNATGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getNATGateway"],
                "json",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_nat_gateway_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetNATGatewayScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetNATGatewayResource]:
        return cast(
            ApiResponse[m.GetNATGatewayResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_nat_gateway(id, options=options),
                lambda match: self.list_nat_gateways(
                    query=cast(
                        m.ListNATGatewaysQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "nat_gateway",
            ),
        )

    async def get_route(
        self, route_table_id: str, route_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRouteResponse]:
        "Get route"
        return cast(
            ApiResponse[m.GetRouteResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getRoute"],
                "json",
                {"route_table_id": route_table_id, "route_id": route_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_route_by_reference(
        self,
        route_table_id: str,
        reference: str,
        *,
        scope: m.GetRouteScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRouteResource]:
        return cast(
            ApiResponse[m.GetRouteResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_route(route_table_id, id, options=options),
                lambda match: self.list_routes(
                    route_table_id,
                    query=cast(m.ListRoutesQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "route",
            ),
        )

    async def get_route_table(
        self, route_table_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRouteTableResponse]:
        "Get route table"
        return cast(
            ApiResponse[m.GetRouteTableResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getRouteTable"],
                "json",
                {"route_table_id": route_table_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_route_table_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetRouteTableScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRouteTableResource]:
        return cast(
            ApiResponse[m.GetRouteTableResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_route_table(id, options=options),
                lambda match: self.list_route_tables(
                    query=cast(
                        m.ListRouteTablesQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "route_table",
            ),
        )

    async def get_security_group(
        self, security_group_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSecurityGroupResponse]:
        "Get security group"
        return cast(
            ApiResponse[m.GetSecurityGroupResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSecurityGroup"],
                "json",
                {"security_group_id": security_group_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_security_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSecurityGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecurityGroupResource]:
        return cast(
            ApiResponse[m.GetSecurityGroupResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_security_group(id, options=options),
                lambda match: self.list_security_groups(
                    query=cast(
                        m.ListSecurityGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "security_group",
            ),
        )

    async def get_security_group_rule(
        self, security_group_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSecurityGroupRuleResponse]:
        "Get security group rule"
        return cast(
            ApiResponse[m.GetSecurityGroupRuleResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSecurityGroupRule"],
                "json",
                {"security_group_id": security_group_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_security_group_rule_by_reference(
        self,
        security_group_id: str,
        reference: str,
        *,
        scope: m.GetSecurityGroupRuleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSecurityGroupRuleResource]:
        return cast(
            ApiResponse[m.GetSecurityGroupRuleResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_security_group_rule(security_group_id, id, options=options),
                lambda match: self.list_security_group_rules(
                    security_group_id,
                    query=cast(
                        m.ListSecurityGroupRulesQuery,
                        {**reference_scope(scope), **match, "limit": 2},
                    ),
                    options=options,
                ),
                True,
                "rule",
            ),
        )

    async def get_subnet(
        self, subnet_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetSubnetResponse]:
        "Get subnet"
        return cast(
            ApiResponse[m.GetSubnetResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getSubnet"],
                "json",
                {"subnet_id": subnet_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_subnet_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetSubnetScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetSubnetResource]:
        return cast(
            ApiResponse[m.GetSubnetResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_subnet(id, options=options),
                lambda match: self.list_subnets(
                    query=cast(m.ListSubnetsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "subnet",
            ),
        )

    async def get_vpc(
        self, vpc_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetVpcResponse]:
        "Get VPC"
        return cast(
            ApiResponse[m.GetVpcResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["getVpc"],
                "json",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_vpc_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetVpcScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetVpcResource]:
        return cast(
            ApiResponse[m.GetVpcResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_vpc(id, options=options),
                lambda match: self.list_vpcs(
                    query=cast(m.ListVpcsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "vpc",
            ),
        )

    async def list_egress_only_gateway_routes(
        self,
        egress_only_gateway_id: str,
        *,
        query: m.ListEgressOnlyGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListEgressOnlyGatewayRoutesResponse, m.ListEgressOnlyGatewayRoutesItem]:
        "List egress-only gateway routes"
        return cast(
            Page[m.ListEgressOnlyGatewayRoutesResponse, m.ListEgressOnlyGatewayRoutesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listEgressOnlyGatewayRoutes"],
                "page",
                {"egress_only_gateway_id": egress_only_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_egress_only_gateway_routes_all(
        self,
        egress_only_gateway_id: str,
        *,
        query: m.ListEgressOnlyGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListEgressOnlyGatewayRoutesItem]:
        return aiterate_pages(
            lambda marker: self.list_egress_only_gateway_routes(
                egress_only_gateway_id,
                query=cast(m.ListEgressOnlyGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_egress_only_gateways(
        self,
        *,
        query: m.ListEgressOnlyGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListEgressOnlyGatewaysResponse, m.ListEgressOnlyGatewaysItem]:
        "List egress-only gateways"
        return cast(
            Page[m.ListEgressOnlyGatewaysResponse, m.ListEgressOnlyGatewaysItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listEgressOnlyGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_egress_only_gateways_all(
        self,
        *,
        query: m.ListEgressOnlyGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListEgressOnlyGatewaysItem]:
        return aiterate_pages(
            lambda marker: self.list_egress_only_gateways(
                query=cast(m.ListEgressOnlyGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_floating_ips(
        self, *, query: m.ListFloatingIpsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListFloatingIpsResponse, m.ListFloatingIpsItem]:
        "List floating IPs"
        return cast(
            Page[m.ListFloatingIpsResponse, m.ListFloatingIpsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listFloatingIps"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_floating_ips_all(
        self, *, query: m.ListFloatingIpsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListFloatingIpsItem]:
        return aiterate_pages(
            lambda marker: self.list_floating_ips(
                query=cast(m.ListFloatingIpsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_interface_addresses(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListInterfaceAddressesResponse, m.ListInterfaceAddressesItem]:
        "List interface addresses"
        return cast(
            Page[m.ListInterfaceAddressesResponse, m.ListInterfaceAddressesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaceAddresses"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_interface_prefixes(
        self, interface_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListInterfacePrefixesResponse, m.ListInterfacePrefixesItem]:
        "List interface prefixes"
        return cast(
            Page[m.ListInterfacePrefixesResponse, m.ListInterfacePrefixesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfacePrefixes"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_interface_security_groups(
        self,
        interface_id: str,
        *,
        query: m.ListInterfaceSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInterfaceSecurityGroupsResponse, m.ListInterfaceSecurityGroupsItem]:
        "List interface security-group membership"
        return cast(
            Page[m.ListInterfaceSecurityGroupsResponse, m.ListInterfaceSecurityGroupsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaceSecurityGroups"],
                "page",
                {"interface_id": interface_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_interfaces(
        self, *, query: m.ListInterfacesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListInterfacesResponse, m.ListInterfacesItem]:
        "List interfaces"
        return cast(
            Page[m.ListInterfacesResponse, m.ListInterfacesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInterfaces"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_interfaces_all(
        self, *, query: m.ListInterfacesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListInterfacesItem]:
        return aiterate_pages(
            lambda marker: self.list_interfaces(
                query=cast(m.ListInterfacesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_internet_gateway_routes(
        self,
        internet_gateway_id: str,
        *,
        query: m.ListInternetGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInternetGatewayRoutesResponse, m.ListInternetGatewayRoutesItem]:
        "List internet gateway routes"
        return cast(
            Page[m.ListInternetGatewayRoutesResponse, m.ListInternetGatewayRoutesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInternetGatewayRoutes"],
                "page",
                {"internet_gateway_id": internet_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_internet_gateway_routes_all(
        self,
        internet_gateway_id: str,
        *,
        query: m.ListInternetGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListInternetGatewayRoutesItem]:
        return aiterate_pages(
            lambda marker: self.list_internet_gateway_routes(
                internet_gateway_id,
                query=cast(m.ListInternetGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_internet_gateways(
        self,
        *,
        query: m.ListInternetGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListInternetGatewaysResponse, m.ListInternetGatewaysItem]:
        "List internet gateways"
        return cast(
            Page[m.ListInternetGatewaysResponse, m.ListInternetGatewaysItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listInternetGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_internet_gateways_all(
        self,
        *,
        query: m.ListInternetGatewaysQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListInternetGatewaysItem]:
        return aiterate_pages(
            lambda marker: self.list_internet_gateways(
                query=cast(m.ListInternetGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_nat_gateway_routes(
        self,
        nat_gateway_id: str,
        *,
        query: m.ListNATGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListNATGatewayRoutesResponse, m.ListNATGatewayRoutesItem]:
        "List NAT gateway routes"
        return cast(
            Page[m.ListNATGatewayRoutesResponse, m.ListNATGatewayRoutesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listNATGatewayRoutes"],
                "page",
                {"nat_gateway_id": nat_gateway_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_nat_gateway_routes_all(
        self,
        nat_gateway_id: str,
        *,
        query: m.ListNATGatewayRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListNATGatewayRoutesItem]:
        return aiterate_pages(
            lambda marker: self.list_nat_gateway_routes(
                nat_gateway_id,
                query=cast(m.ListNATGatewayRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_nat_gateways(
        self, *, query: m.ListNATGatewaysQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListNATGatewaysResponse, m.ListNATGatewaysItem]:
        "List NAT gateways"
        return cast(
            Page[m.ListNATGatewaysResponse, m.ListNATGatewaysItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listNATGateways"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_nat_gateways_all(
        self, *, query: m.ListNATGatewaysQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListNATGatewaysItem]:
        return aiterate_pages(
            lambda marker: self.list_nat_gateways(
                query=cast(m.ListNATGatewaysQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_prefix_pools(
        self, vpc_id: str, *, options: RequestOptions | None = None
    ) -> Page[m.ListPrefixPoolsResponse, m.ListPrefixPoolsItem]:
        "List prefix pools"
        return cast(
            Page[m.ListPrefixPoolsResponse, m.ListPrefixPoolsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listPrefixPools"],
                "page",
                {"vpc_id": vpc_id},
                UNSET,
                None,
                options,
            ),
        )

    async def list_route_tables(
        self, *, query: m.ListRouteTablesQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListRouteTablesResponse, m.ListRouteTablesItem]:
        "List route tables"
        return cast(
            Page[m.ListRouteTablesResponse, m.ListRouteTablesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listRouteTables"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_route_tables_all(
        self, *, query: m.ListRouteTablesQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListRouteTablesItem]:
        return aiterate_pages(
            lambda marker: self.list_route_tables(
                query=cast(m.ListRouteTablesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_routes(
        self,
        route_table_id: str,
        *,
        query: m.ListRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRoutesResponse, m.ListRoutesItem]:
        "List routes"
        return cast(
            Page[m.ListRoutesResponse, m.ListRoutesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listRoutes"],
                "page",
                {"route_table_id": route_table_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_routes_all(
        self,
        route_table_id: str,
        *,
        query: m.ListRoutesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListRoutesItem]:
        return aiterate_pages(
            lambda marker: self.list_routes(
                route_table_id,
                query=cast(m.ListRoutesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_security_group_rules(
        self,
        security_group_id: str,
        *,
        query: m.ListSecurityGroupRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSecurityGroupRulesResponse, m.ListSecurityGroupRulesItem]:
        "List security group rules"
        return cast(
            Page[m.ListSecurityGroupRulesResponse, m.ListSecurityGroupRulesItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSecurityGroupRules"],
                "page",
                {"security_group_id": security_group_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_security_group_rules_all(
        self,
        security_group_id: str,
        *,
        query: m.ListSecurityGroupRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListSecurityGroupRulesItem]:
        return aiterate_pages(
            lambda marker: self.list_security_group_rules(
                security_group_id,
                query=cast(m.ListSecurityGroupRulesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_security_groups(
        self,
        *,
        query: m.ListSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListSecurityGroupsResponse, m.ListSecurityGroupsItem]:
        "List security groups"
        return cast(
            Page[m.ListSecurityGroupsResponse, m.ListSecurityGroupsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSecurityGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_security_groups_all(
        self,
        *,
        query: m.ListSecurityGroupsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListSecurityGroupsItem]:
        return aiterate_pages(
            lambda marker: self.list_security_groups(
                query=cast(m.ListSecurityGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_subnets(
        self, *, query: m.ListSubnetsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListSubnetsResponse, m.ListSubnetsItem]:
        "List subnets"
        return cast(
            Page[m.ListSubnetsResponse, m.ListSubnetsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listSubnets"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_subnets_all(
        self, *, query: m.ListSubnetsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListSubnetsItem]:
        return aiterate_pages(
            lambda marker: self.list_subnets(
                query=cast(m.ListSubnetsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_vpcs(
        self, *, query: m.ListVpcsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListVpcsResponse, m.ListVpcsItem]:
        "List VPCs"
        return cast(
            Page[m.ListVpcsResponse, m.ListVpcsItem],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["listVpcs"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_vpcs_all(
        self, *, query: m.ListVpcsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListVpcsItem]:
        return aiterate_pages(
            lambda marker: self.list_vpcs(
                query=cast(m.ListVpcsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def set_interface_security_groups(
        self,
        interface_id: str,
        body: m.SetInterfaceSecurityGroupsBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.SetInterfaceSecurityGroupsResponse]:
        "Set interface security-group membership"
        return cast(
            ApiResponse[m.SetInterfaceSecurityGroupsResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["setInterfaceSecurityGroups"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    async def update_egress_only_gateway(
        self,
        egress_only_gateway_id: str,
        body: m.UpdateEgressOnlyGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateEgressOnlyGatewayResponse]:
        "Update egress-only gateway"
        return cast(
            ApiResponse[m.UpdateEgressOnlyGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateEgressOnlyGateway"],
                "json",
                {"egress_only_gateway_id": egress_only_gateway_id},
                body,
                None,
                options,
            ),
        )

    async def update_floating_ip(
        self,
        floating_ip_id: str,
        body: m.UpdateFloatingIpBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateFloatingIpResponse]:
        "Update floating IP"
        return cast(
            ApiResponse[m.UpdateFloatingIpResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateFloatingIp"],
                "json",
                {"floating_ip_id": floating_ip_id},
                body,
                None,
                options,
            ),
        )

    async def update_interface(
        self,
        interface_id: str,
        body: m.UpdateInterfaceBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateInterfaceResponse]:
        "Update interface"
        return cast(
            ApiResponse[m.UpdateInterfaceResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateInterface"],
                "json",
                {"interface_id": interface_id},
                body,
                None,
                options,
            ),
        )

    async def update_internet_gateway(
        self,
        internet_gateway_id: str,
        body: m.UpdateInternetGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateInternetGatewayResponse]:
        "Update internet gateway"
        return cast(
            ApiResponse[m.UpdateInternetGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateInternetGateway"],
                "json",
                {"internet_gateway_id": internet_gateway_id},
                body,
                None,
                options,
            ),
        )

    async def update_nat_gateway(
        self,
        nat_gateway_id: str,
        body: m.UpdateNATGatewayBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateNATGatewayResponse]:
        "Update NAT gateway"
        return cast(
            ApiResponse[m.UpdateNATGatewayResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateNATGateway"],
                "json",
                {"nat_gateway_id": nat_gateway_id},
                body,
                None,
                options,
            ),
        )

    async def update_route(
        self,
        route_table_id: str,
        route_id: str,
        body: m.UpdateRouteBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRouteResponse]:
        "Update route"
        return cast(
            ApiResponse[m.UpdateRouteResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateRoute"],
                "json",
                {"route_table_id": route_table_id, "route_id": route_id},
                body,
                None,
                options,
            ),
        )

    async def update_route_table(
        self,
        route_table_id: str,
        body: m.UpdateRouteTableBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRouteTableResponse]:
        "Update route table"
        return cast(
            ApiResponse[m.UpdateRouteTableResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateRouteTable"],
                "json",
                {"route_table_id": route_table_id},
                body,
                None,
                options,
            ),
        )

    async def update_security_group(
        self,
        security_group_id: str,
        body: m.UpdateSecurityGroupBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateSecurityGroupResponse]:
        "Update security group"
        return cast(
            ApiResponse[m.UpdateSecurityGroupResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateSecurityGroup"],
                "json",
                {"security_group_id": security_group_id},
                body,
                None,
                options,
            ),
        )

    async def update_subnet(
        self, subnet_id: str, body: m.UpdateSubnetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateSubnetResponse]:
        "Update subnet"
        return cast(
            ApiResponse[m.UpdateSubnetResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateSubnet"],
                "json",
                {"subnet_id": subnet_id},
                body,
                None,
                options,
            ),
        )

    async def update_vpc(
        self, vpc_id: str, body: m.UpdateVpcBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateVpcResponse]:
        "Update VPC"
        return cast(
            ApiResponse[m.UpdateVpcResponse],
            await self._transport.request(
                "network",
                "https://network.{region}.basaltic.sh",
                _OPS["updateVpc"],
                "json",
                {"vpc_id": vpc_id},
                body,
                None,
                options,
            ),
        )
