"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import loadbalancer as m
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
    "attachListenerCertificate": Operation(
        id="attachListenerCertificate",
        method="POST",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/certificates",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "attachTarget": Operation(
        id="attachTarget",
        method="POST",
        path="/v1/target-groups/{id}/targets",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createListener": Operation(
        id="createListener",
        method="POST",
        path="/v1/load-balancers/{id}/listeners",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createLoadBalancer": Operation(
        id="createLoadBalancer",
        method="POST",
        path="/v1/load-balancers",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createRule": Operation(
        id="createRule",
        method="POST",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/rules",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createTargetGroup": Operation(
        id="createTargetGroup",
        method="POST",
        path="/v1/target-groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteListener": Operation(
        id="deleteListener",
        method="DELETE",
        path="/v1/load-balancers/{id}/listeners/{listener_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteLoadBalancer": Operation(
        id="deleteLoadBalancer",
        method="DELETE",
        path="/v1/load-balancers/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteRuleInListener": Operation(
        id="deleteRuleInListener",
        method="DELETE",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteTargetGroup": Operation(
        id="deleteTargetGroup",
        method="DELETE",
        path="/v1/target-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachListenerCertificate": Operation(
        id="detachListenerCertificate",
        method="DELETE",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/certificates/{certificate_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "detachTarget": Operation(
        id="detachTarget",
        method="DELETE",
        path="/v1/target-groups/{id}/targets/{target_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getListener": Operation(
        id="getListener",
        method="GET",
        path="/v1/load-balancers/{id}/listeners/{listener_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getLoadBalancer": Operation(
        id="getLoadBalancer",
        method="GET",
        path="/v1/load-balancers/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRule": Operation(
        id="getRule",
        method="GET",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getTarget": Operation(
        id="getTarget",
        method="GET",
        path="/v1/target-groups/{id}/targets/{target_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getTargetGroup": Operation(
        id="getTargetGroup",
        method="GET",
        path="/v1/target-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "listListeners": Operation(
        id="listListeners",
        method="GET",
        path="/v1/load-balancers/{id}/listeners",
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
        itemsKey="listeners",
    ),
    "listLoadBalancerReplicas": Operation(
        id="listLoadBalancerReplicas",
        method="GET",
        path="/v1/load-balancers/{id}/replicas",
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
        itemsKey="replicas",
    ),
    "listLoadBalancers": Operation(
        id="listLoadBalancers",
        method="GET",
        path="/v1/load-balancers",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "status": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="load_balancers",
    ),
    "listRules": Operation(
        id="listRules",
        method="GET",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/rules",
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
        itemsKey="rules",
    ),
    "listTargetGroups": Operation(
        id="listTargetGroups",
        method="GET",
        path="/v1/target-groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "protocol": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="target_groups",
    ),
    "listTargets": Operation(
        id="listTargets",
        method="GET",
        path="/v1/target-groups/{id}/targets",
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
        itemsKey="targets",
    ),
    "updateListener": Operation(
        id="updateListener",
        method="PATCH",
        path="/v1/load-balancers/{id}/listeners/{listener_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateLoadBalancer": Operation(
        id="updateLoadBalancer",
        method="PATCH",
        path="/v1/load-balancers/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateRule": Operation(
        id="updateRule",
        method="PATCH",
        path="/v1/load-balancers/{id}/listeners/{listener_id}/rules/{rule_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateTargetGroup": Operation(
        id="updateTargetGroup",
        method="PATCH",
        path="/v1/target-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
}


class LoadbalancerService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach_listener_certificate(
        self,
        id: str,
        listener_id: str,
        body: m.AttachListenerCertificateBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachListenerCertificateResponse]:
        "Attach an additional certificate to an HTTPS listener"
        return cast(
            ApiResponse[m.AttachListenerCertificateResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["attachListenerCertificate"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    def attach_target(
        self, id: str, body: m.AttachTargetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AttachTargetResponse]:
        "Attach a target to this group"
        return cast(
            ApiResponse[m.AttachTargetResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["attachTarget"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    def create_listener(
        self, id: str, body: m.CreateListenerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateListenerResponse]:
        "Create a listener on this load balancer"
        return cast(
            ApiResponse[m.CreateListenerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createListener"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    def create_load_balancer(
        self, body: m.CreateLoadBalancerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateLoadBalancerResponse]:
        "Create a load balancer"
        return cast(
            ApiResponse[m.CreateLoadBalancerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createLoadBalancer"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_rule(
        self,
        id: str,
        listener_id: str,
        body: m.CreateRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateRuleResponse]:
        "Create a routing rule on this listener (HTTP/HTTPS only)"
        return cast(
            ApiResponse[m.CreateRuleResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createRule"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    def create_target_group(
        self, body: m.CreateTargetGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTargetGroupResponse]:
        "Create a target group"
        return cast(
            ApiResponse[m.CreateTargetGroupResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createTargetGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_listener(
        self, id: str, listener_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a listener"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteListener"],
                "discard",
                {"id": id, "listener_id": listener_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_load_balancer(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a load balancer"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteLoadBalancer"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_rule_in_listener(
        self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a routing rule"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteRuleInListener"],
                "discard",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_target_group(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a target group"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteTargetGroup"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_listener_certificate(
        self,
        id: str,
        listener_id: str,
        certificate_id: str,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Detach a certificate from an HTTPS listener"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["detachListenerCertificate"],
                "discard",
                {"id": id, "listener_id": listener_id, "certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    def detach_target(
        self, id: str, target_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a target"
        return cast(
            None,
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["detachTarget"],
                "discard",
                {"id": id, "target_id": target_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_listener(
        self, id: str, listener_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetListenerResponse]:
        "Get a listener"
        return cast(
            ApiResponse[m.GetListenerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getListener"],
                "json",
                {"id": id, "listener_id": listener_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_listener_by_reference(
        self,
        id: str,
        reference: str,
        *,
        scope: m.GetListenerScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetListenerResource]:
        return cast(
            ApiResponse[m.GetListenerResource],
            resolve_reference(
                reference,
                lambda id: self.get_listener(id, id, options=options),
                lambda match: self.list_listeners(
                    id,
                    query=cast(m.ListListenersQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "listener",
            ),
        )

    def get_load_balancer(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLoadBalancerResponse]:
        "Get a load balancer"
        return cast(
            ApiResponse[m.GetLoadBalancerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getLoadBalancer"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def get_load_balancer_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetLoadBalancerScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetLoadBalancerResource]:
        return cast(
            ApiResponse[m.GetLoadBalancerResource],
            resolve_reference(
                reference,
                lambda id: self.get_load_balancer(id, options=options),
                lambda match: self.list_load_balancers(
                    query=cast(
                        m.ListLoadBalancersQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "load_balancer",
            ),
        )

    def get_rule(
        self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRuleResponse]:
        "Get a routing rule"
        return cast(
            ApiResponse[m.GetRuleResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getRule"],
                "json",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_rule_by_reference(
        self,
        id: str,
        listener_id: str,
        reference: str,
        *,
        scope: m.GetRuleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRuleResource]:
        return cast(
            ApiResponse[m.GetRuleResource],
            resolve_reference(
                reference,
                lambda id: self.get_rule(id, listener_id, id, options=options),
                lambda match: self.list_rules(
                    id,
                    listener_id,
                    query=cast(m.ListRulesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "rule",
            ),
        )

    def get_target(
        self, id: str, target_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTargetResponse]:
        "Get a target"
        return cast(
            ApiResponse[m.GetTargetResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getTarget"],
                "json",
                {"id": id, "target_id": target_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_target_by_reference(
        self,
        id: str,
        reference: str,
        *,
        scope: m.GetTargetScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetTargetResource]:
        return cast(
            ApiResponse[m.GetTargetResource],
            resolve_reference(
                reference,
                lambda id: self.get_target(id, id, options=options),
                lambda match: self.list_targets(
                    id,
                    query=cast(m.ListTargetsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "target",
            ),
        )

    def get_target_group(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTargetGroupResponse]:
        "Get a target group"
        return cast(
            ApiResponse[m.GetTargetGroupResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getTargetGroup"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def get_target_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetTargetGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetTargetGroupResource]:
        return cast(
            ApiResponse[m.GetTargetGroupResource],
            resolve_reference(
                reference,
                lambda id: self.get_target_group(id, options=options),
                lambda match: self.list_target_groups(
                    query=cast(
                        m.ListTargetGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "target_group",
            ),
        )

    def list_listeners(
        self,
        id: str,
        *,
        query: m.ListListenersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListListenersResponse, m.ListListenersItem]:
        "List this load balancer's listeners"
        return cast(
            Page[m.ListListenersResponse, m.ListListenersItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listListeners"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    def list_load_balancer_replicas(
        self,
        id: str,
        *,
        query: m.ListLoadBalancerReplicasQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListLoadBalancerReplicasResponse, m.ListLoadBalancerReplicasItem]:
        "List the LB's instance replicas with live health"
        return cast(
            Page[m.ListLoadBalancerReplicasResponse, m.ListLoadBalancerReplicasItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listLoadBalancerReplicas"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    def list_load_balancers(
        self,
        *,
        query: m.ListLoadBalancersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListLoadBalancersResponse, m.ListLoadBalancersItem]:
        "List load balancers"
        return cast(
            Page[m.ListLoadBalancersResponse, m.ListLoadBalancersItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listLoadBalancers"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_load_balancers_all(
        self,
        *,
        query: m.ListLoadBalancersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListLoadBalancersItem]:
        return iterate_pages(
            lambda marker: self.list_load_balancers(
                query=cast(m.ListLoadBalancersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_rules(
        self,
        id: str,
        listener_id: str,
        *,
        query: m.ListRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRulesResponse, m.ListRulesItem]:
        "List this listener's rules"
        return cast(
            Page[m.ListRulesResponse, m.ListRulesItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listRules"],
                "page",
                {"id": id, "listener_id": listener_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_target_groups(
        self, *, query: m.ListTargetGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTargetGroupsResponse, m.ListTargetGroupsItem]:
        "List target groups"
        return cast(
            Page[m.ListTargetGroupsResponse, m.ListTargetGroupsItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listTargetGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_target_groups_all(
        self, *, query: m.ListTargetGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListTargetGroupsItem]:
        return iterate_pages(
            lambda marker: self.list_target_groups(
                query=cast(m.ListTargetGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_targets(
        self,
        id: str,
        *,
        query: m.ListTargetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTargetsResponse, m.ListTargetsItem]:
        "List targets in this group"
        return cast(
            Page[m.ListTargetsResponse, m.ListTargetsItem],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listTargets"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    def update_listener(
        self,
        id: str,
        listener_id: str,
        body: m.UpdateListenerBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateListenerResponse]:
        "Patch a listener (rotate cert, change default target group)"
        return cast(
            ApiResponse[m.UpdateListenerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateListener"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    def update_load_balancer(
        self, id: str, body: m.UpdateLoadBalancerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateLoadBalancerResponse]:
        "Scale or resize a load balancer"
        return cast(
            ApiResponse[m.UpdateLoadBalancerResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateLoadBalancer"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    def update_rule(
        self,
        id: str,
        listener_id: str,
        rule_id: str,
        body: m.UpdateRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRuleResponse]:
        "Update a routing rule (full replace)"
        return cast(
            ApiResponse[m.UpdateRuleResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateRule"],
                "json",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                body,
                None,
                options,
            ),
        )

    def update_target_group(
        self, id: str, body: m.UpdateTargetGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTargetGroupResponse]:
        "Update target group health checks, framing, or stickiness"
        return cast(
            ApiResponse[m.UpdateTargetGroupResponse],
            self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateTargetGroup"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )


class AsyncLoadbalancerService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach_listener_certificate(
        self,
        id: str,
        listener_id: str,
        body: m.AttachListenerCertificateBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.AttachListenerCertificateResponse]:
        "Attach an additional certificate to an HTTPS listener"
        return cast(
            ApiResponse[m.AttachListenerCertificateResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["attachListenerCertificate"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    async def attach_target(
        self, id: str, body: m.AttachTargetBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.AttachTargetResponse]:
        "Attach a target to this group"
        return cast(
            ApiResponse[m.AttachTargetResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["attachTarget"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    async def create_listener(
        self, id: str, body: m.CreateListenerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateListenerResponse]:
        "Create a listener on this load balancer"
        return cast(
            ApiResponse[m.CreateListenerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createListener"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    async def create_load_balancer(
        self, body: m.CreateLoadBalancerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateLoadBalancerResponse]:
        "Create a load balancer"
        return cast(
            ApiResponse[m.CreateLoadBalancerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createLoadBalancer"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_rule(
        self,
        id: str,
        listener_id: str,
        body: m.CreateRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.CreateRuleResponse]:
        "Create a routing rule on this listener (HTTP/HTTPS only)"
        return cast(
            ApiResponse[m.CreateRuleResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createRule"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    async def create_target_group(
        self, body: m.CreateTargetGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateTargetGroupResponse]:
        "Create a target group"
        return cast(
            ApiResponse[m.CreateTargetGroupResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["createTargetGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_listener(
        self, id: str, listener_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a listener"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteListener"],
                "discard",
                {"id": id, "listener_id": listener_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_load_balancer(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a load balancer"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteLoadBalancer"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_rule_in_listener(
        self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Delete a routing rule"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteRuleInListener"],
                "discard",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_target_group(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a target group"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["deleteTargetGroup"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_listener_certificate(
        self,
        id: str,
        listener_id: str,
        certificate_id: str,
        *,
        options: RequestOptions | None = None,
    ) -> None:
        "Detach a certificate from an HTTPS listener"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["detachListenerCertificate"],
                "discard",
                {"id": id, "listener_id": listener_id, "certificate_id": certificate_id},
                UNSET,
                None,
                options,
            ),
        )

    async def detach_target(
        self, id: str, target_id: str, *, options: RequestOptions | None = None
    ) -> None:
        "Detach a target"
        return cast(
            None,
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["detachTarget"],
                "discard",
                {"id": id, "target_id": target_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_listener(
        self, id: str, listener_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetListenerResponse]:
        "Get a listener"
        return cast(
            ApiResponse[m.GetListenerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getListener"],
                "json",
                {"id": id, "listener_id": listener_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_listener_by_reference(
        self,
        id: str,
        reference: str,
        *,
        scope: m.GetListenerScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetListenerResource]:
        return cast(
            ApiResponse[m.GetListenerResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_listener(id, id, options=options),
                lambda match: self.list_listeners(
                    id,
                    query=cast(m.ListListenersQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "listener",
            ),
        )

    async def get_load_balancer(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLoadBalancerResponse]:
        "Get a load balancer"
        return cast(
            ApiResponse[m.GetLoadBalancerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getLoadBalancer"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_load_balancer_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetLoadBalancerScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetLoadBalancerResource]:
        return cast(
            ApiResponse[m.GetLoadBalancerResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_load_balancer(id, options=options),
                lambda match: self.list_load_balancers(
                    query=cast(
                        m.ListLoadBalancersQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "load_balancer",
            ),
        )

    async def get_rule(
        self, id: str, listener_id: str, rule_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRuleResponse]:
        "Get a routing rule"
        return cast(
            ApiResponse[m.GetRuleResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getRule"],
                "json",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_rule_by_reference(
        self,
        id: str,
        listener_id: str,
        reference: str,
        *,
        scope: m.GetRuleScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetRuleResource]:
        return cast(
            ApiResponse[m.GetRuleResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_rule(id, listener_id, id, options=options),
                lambda match: self.list_rules(
                    id,
                    listener_id,
                    query=cast(m.ListRulesQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "rule",
            ),
        )

    async def get_target(
        self, id: str, target_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTargetResponse]:
        "Get a target"
        return cast(
            ApiResponse[m.GetTargetResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getTarget"],
                "json",
                {"id": id, "target_id": target_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_target_by_reference(
        self,
        id: str,
        reference: str,
        *,
        scope: m.GetTargetScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetTargetResource]:
        return cast(
            ApiResponse[m.GetTargetResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_target(id, id, options=options),
                lambda match: self.list_targets(
                    id,
                    query=cast(m.ListTargetsQuery, {**reference_scope(scope), **match}),
                    options=options,
                ),
                True,
                "target",
            ),
        )

    async def get_target_group(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTargetGroupResponse]:
        "Get a target group"
        return cast(
            ApiResponse[m.GetTargetGroupResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["getTargetGroup"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_target_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetTargetGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetTargetGroupResource]:
        return cast(
            ApiResponse[m.GetTargetGroupResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_target_group(id, options=options),
                lambda match: self.list_target_groups(
                    query=cast(
                        m.ListTargetGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "target_group",
            ),
        )

    async def list_listeners(
        self,
        id: str,
        *,
        query: m.ListListenersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListListenersResponse, m.ListListenersItem]:
        "List this load balancer's listeners"
        return cast(
            Page[m.ListListenersResponse, m.ListListenersItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listListeners"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_load_balancer_replicas(
        self,
        id: str,
        *,
        query: m.ListLoadBalancerReplicasQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListLoadBalancerReplicasResponse, m.ListLoadBalancerReplicasItem]:
        "List the LB's instance replicas with live health"
        return cast(
            Page[m.ListLoadBalancerReplicasResponse, m.ListLoadBalancerReplicasItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listLoadBalancerReplicas"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_load_balancers(
        self,
        *,
        query: m.ListLoadBalancersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListLoadBalancersResponse, m.ListLoadBalancersItem]:
        "List load balancers"
        return cast(
            Page[m.ListLoadBalancersResponse, m.ListLoadBalancersItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listLoadBalancers"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_load_balancers_all(
        self,
        *,
        query: m.ListLoadBalancersQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListLoadBalancersItem]:
        return aiterate_pages(
            lambda marker: self.list_load_balancers(
                query=cast(m.ListLoadBalancersQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_rules(
        self,
        id: str,
        listener_id: str,
        *,
        query: m.ListRulesQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListRulesResponse, m.ListRulesItem]:
        "List this listener's rules"
        return cast(
            Page[m.ListRulesResponse, m.ListRulesItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listRules"],
                "page",
                {"id": id, "listener_id": listener_id},
                UNSET,
                query,
                options,
            ),
        )

    async def list_target_groups(
        self, *, query: m.ListTargetGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListTargetGroupsResponse, m.ListTargetGroupsItem]:
        "List target groups"
        return cast(
            Page[m.ListTargetGroupsResponse, m.ListTargetGroupsItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listTargetGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_target_groups_all(
        self, *, query: m.ListTargetGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListTargetGroupsItem]:
        return aiterate_pages(
            lambda marker: self.list_target_groups(
                query=cast(m.ListTargetGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_targets(
        self,
        id: str,
        *,
        query: m.ListTargetsQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTargetsResponse, m.ListTargetsItem]:
        "List targets in this group"
        return cast(
            Page[m.ListTargetsResponse, m.ListTargetsItem],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["listTargets"],
                "page",
                {"id": id},
                UNSET,
                query,
                options,
            ),
        )

    async def update_listener(
        self,
        id: str,
        listener_id: str,
        body: m.UpdateListenerBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateListenerResponse]:
        "Patch a listener (rotate cert, change default target group)"
        return cast(
            ApiResponse[m.UpdateListenerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateListener"],
                "json",
                {"id": id, "listener_id": listener_id},
                body,
                None,
                options,
            ),
        )

    async def update_load_balancer(
        self, id: str, body: m.UpdateLoadBalancerBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateLoadBalancerResponse]:
        "Scale or resize a load balancer"
        return cast(
            ApiResponse[m.UpdateLoadBalancerResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateLoadBalancer"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    async def update_rule(
        self,
        id: str,
        listener_id: str,
        rule_id: str,
        body: m.UpdateRuleBody,
        *,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.UpdateRuleResponse]:
        "Update a routing rule (full replace)"
        return cast(
            ApiResponse[m.UpdateRuleResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateRule"],
                "json",
                {"id": id, "listener_id": listener_id, "rule_id": rule_id},
                body,
                None,
                options,
            ),
        )

    async def update_target_group(
        self, id: str, body: m.UpdateTargetGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTargetGroupResponse]:
        "Update target group health checks, framing, or stickiness"
        return cast(
            ApiResponse[m.UpdateTargetGroupResponse],
            await self._transport.request(
                "loadbalancer",
                "https://loadbalancer.{region}.basaltic.sh",
                _OPS["updateTargetGroup"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )
