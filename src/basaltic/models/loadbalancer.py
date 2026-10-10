"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachListenerCertificateRequestInput = TypedDict(
    "AttachListenerCertificateRequestInput",
    {"certificate": "Required[str]", "is_default": "NotRequired[bool]"},
    total=False,
)
AttachListenerCertificateBody: TypeAlias = "AttachListenerCertificateRequestInput"
ListenerResponse = TypedDict("ListenerResponse", {"listener": "NotRequired[Listener]"}, total=False)
Listener = TypedDict(
    "Listener",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "load_balancer_id": "Required[str]",
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "port": "Required[int]",
        "certificates": "NotRequired[list[ListenerCertificate]]",
        "default_target_group_id": "NotRequired[str]",
        "exposure": "Required[Literal['public_only', 'private_only', 'both']]",
        "tags": "Required[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
ListenerCertificate = TypedDict(
    "ListenerCertificate",
    {
        "id": "Required[str]",
        "certificate_crn": "Required[str]",
        "is_default": "Required[bool]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
AttachListenerCertificateResponse: TypeAlias = "ListenerResponse"
AttachTargetRequestInput = TypedDict(
    "AttachTargetRequestInput", {"target": "Required[str]", "port": "NotRequired[int]"}, total=False
)
AttachTargetBody: TypeAlias = "AttachTargetRequestInput"
TargetResponse = TypedDict("TargetResponse", {"target": "NotRequired[Target]"}, total=False)
Target = TypedDict(
    "Target",
    {
        "id": "Required[str]",
        "target_group_id": "Required[str]",
        "target_ref": "Required[str]",
        "port": "NotRequired[int]",
        "health": "Required[Literal['initial', 'healthy', 'unhealthy', 'draining']]",
        "last_seen_at": "NotRequired[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
AttachTargetResponse: TypeAlias = "TargetResponse"
CreateListenerRequestInput = TypedDict(
    "CreateListenerRequestInput",
    {
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "port": "Required[int]",
        "certificates": "NotRequired[list[CreateListenerCertificateInput]]",
        "default_target_group": "NotRequired[str]",
        "exposure": "NotRequired[Literal['public_only', 'private_only', 'both']]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
CreateListenerCertificateInput = TypedDict(
    "CreateListenerCertificateInput", {"certificate": "Required[str]"}, total=False
)
TagsInput: TypeAlias = "dict[str, str]"
CreateListenerBody: TypeAlias = "CreateListenerRequestInput"
CreateListenerResponse: TypeAlias = "ListenerResponse"
CreateLoadBalancerRequestInput = TypedDict(
    "CreateLoadBalancerRequestInput",
    {
        "desired_count": "NotRequired[int]",
        "min_count": "NotRequired[int]",
        "max_count": "NotRequired[int]",
        "autoscaling": "NotRequired[AutoscalingPolicyInput]",
        "name": "Required[str]",
        "type": "Required[Literal['application', 'network']]",
        "vpc": "Required[str]",
        "subnet": "Required[str]",
        "flavor": "Required[str]",
        "replica_count": "NotRequired[int]",
        "floating_ip": "NotRequired[str]",
        "floating_ips": "NotRequired[list[str]]",
        "security_groups": "Required[list[str]]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
AutoscalingPolicyInput = TypedDict(
    "AutoscalingPolicyInput",
    {
        "enabled": "Required[bool]",
        "metrics": "Required[list[ScalingMetricInput]]",
        "warmup_seconds": "NotRequired[int]",
        "cooldown_seconds": "NotRequired[int]",
        "scale_down_stabilization_seconds": "NotRequired[int]",
        "max_scale_out_step": "NotRequired[int]",
        "max_scale_in_step": "NotRequired[int]",
        "drain_seconds": "NotRequired[int]",
    },
    total=False,
)
ScalingMetricInput = TypedDict(
    "ScalingMetricInput",
    {
        "source": "Required[Literal['cpu', 'telemetry']]",
        "target_type": "Required[Literal['utilization', 'average_value']]",
        "target_value": "Required[float]",
        "name": "NotRequired[str]",
        "labels": "NotRequired[dict[str, str]]",
        "sample_aggregation": "NotRequired[Literal['last', 'avg', 'max', 'rate']]",
        "series_aggregation": "NotRequired[Literal['sum', 'avg', 'max']]",
        "expected_series": "NotRequired[int]",
        "window_seconds": "NotRequired[int]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
CreateLoadBalancerBody: TypeAlias = "CreateLoadBalancerRequestInput"
LoadBalancerResponse = TypedDict(
    "LoadBalancerResponse", {"load_balancer": "NotRequired[LoadBalancer]"}, total=False
)
LoadBalancer = TypedDict(
    "LoadBalancer",
    {
        "rollout_surge": "NotRequired[bool]",
        "desired_count": "Required[int]",
        "min_count": "Required[int]",
        "max_count": "Required[int]",
        "autoscaling": "NotRequired[AutoscalingPolicy]",
        "autoscaling_status": "NotRequired[AutoscalingStatus]",
        "id": "Required[str]",
        "crn": "Required[str]",
        "account_id": "Required[str]",
        "name": "Required[str]",
        "type": "Required[Literal['application', 'network']]",
        "status": "Required[Literal['provisioning', 'active', 'error', 'deleting']]",
        "faults": "Required[list[Fault]]",
        "subnet": "Required[Subnet | Literal[None] | None]",
        "flavor_id": "Required[str]",
        "replica_count": "Required[int]",
        "internal_ipv4": "NotRequired[str]",
        "internal_ipv6": "NotRequired[str]",
        "public_ipv6": "NotRequired[str]",
        "floating_ip_id": "NotRequired[str]",
        "floating_ips": "Required[list[FloatingIp]]",
        "dns_name": "NotRequired[str]",
        "tags": "Required[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
AutoscalingPolicy = TypedDict(
    "AutoscalingPolicy",
    {
        "enabled": "Required[bool]",
        "metrics": "Required[list[ScalingMetric]]",
        "warmup_seconds": "NotRequired[int]",
        "cooldown_seconds": "NotRequired[int]",
        "scale_down_stabilization_seconds": "NotRequired[int]",
        "max_scale_out_step": "NotRequired[int]",
        "max_scale_in_step": "NotRequired[int]",
        "drain_seconds": "NotRequired[int]",
    },
    total=False,
)
ScalingMetric = TypedDict(
    "ScalingMetric",
    {
        "source": "Required[Literal['cpu', 'telemetry']]",
        "target_type": "Required[Literal['utilization', 'average_value']]",
        "target_value": "Required[float]",
        "name": "NotRequired[str]",
        "labels": "NotRequired[dict[str, str]]",
        "sample_aggregation": "NotRequired[Literal['last', 'avg', 'max', 'rate']]",
        "series_aggregation": "NotRequired[Literal['sum', 'avg', 'max']]",
        "expected_series": "NotRequired[int]",
        "window_seconds": "NotRequired[int]",
        "max_age_seconds": "NotRequired[int]",
    },
    total=False,
)
AutoscalingStatus = TypedDict(
    "AutoscalingStatus",
    {
        "status": "Required[Literal['pending', 'disabled', 'stable', 'scaling', 'waiting', 'warming_up', 'metrics_unavailable', 'stabilizing', 'cooldown', 'draining']]",
        "reason": "Required[str]",
        "evaluated_at": "NotRequired[str]",
        "last_scaled_at": "NotRequired[str]",
        "history": "Required[list[AutoscalingStatusHistoryItem]]",
    },
    total=False,
)
AutoscalingStatusHistoryItem = TypedDict(
    "AutoscalingStatusHistoryItem",
    {
        "at": "Required[str]",
        "from": "Required[int]",
        "to": "Required[int]",
        "reason": "Required[str]",
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
RouteTableSummary: TypeAlias = "RouteTableSummaryObject | None"
RouteTableSummaryObject = TypedDict(
    "RouteTableSummaryObject",
    {"id": "Required[str]", "crn": "Required[str]", "name": "Required[str]"},
    total=False,
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
CreateLoadBalancerResponse: TypeAlias = "LoadBalancerResponse"
CreateRuleRequestInput = TypedDict(
    "CreateRuleRequestInput",
    {
        "priority": "Required[int]",
        "conditions": "Required[list[RuleConditionInput]]",
        "target_group": "Required[str]",
    },
    total=False,
)
RuleConditionInput = TypedDict(
    "RuleConditionInput",
    {
        "field": "Required[Literal['host', 'path', 'header', 'query', 'method']]",
        "op": "Required[Literal['exact', 'prefix', 'glob', 'regex']]",
        "name": "NotRequired[str]",
        "values": "Required[list[str]]",
    },
    total=False,
)
CreateRuleBody: TypeAlias = "CreateRuleRequestInput"
RuleResponse = TypedDict("RuleResponse", {"rule": "NotRequired[Rule]"}, total=False)
Rule = TypedDict(
    "Rule",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "listener_id": "Required[str]",
        "priority": "Required[int]",
        "conditions": "Required[list[RuleCondition]]",
        "target_group_id": "Required[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
RuleCondition = TypedDict(
    "RuleCondition",
    {
        "field": "Required[Literal['host', 'path', 'header', 'query', 'method']]",
        "op": "Required[Literal['exact', 'prefix', 'glob', 'regex']]",
        "name": "NotRequired[str]",
        "values": "Required[list[str]]",
    },
    total=False,
)
CreateRuleResponse: TypeAlias = "RuleResponse"
CreateTargetGroupRequestInput = TypedDict(
    "CreateTargetGroupRequestInput",
    {
        "name": "Required[str]",
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "target_type": "NotRequired[Literal['ip', 'instance', 'function']]",
        "port": "Required[int]",
        "health_check": "NotRequired[HealthCheckInput]",
        "proxy_protocol": "NotRequired[bool]",
        "session_affinity": "NotRequired[SessionAffinityInput]",
        "target_mode": "NotRequired[Literal['static', 'pool']]",
        "instance_pool": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
HealthCheckInput = TypedDict(
    "HealthCheckInput",
    {
        "enabled": "NotRequired[bool]",
        "protocol": "NotRequired[Literal['http', 'https', 'tcp', 'udp', '']]",
        "path": "NotRequired[str]",
        "port": "NotRequired[int]",
        "interval_sec": "NotRequired[int]",
        "timeout_sec": "NotRequired[int]",
        "healthy_threshold": "NotRequired[int]",
        "unhealthy_threshold": "NotRequired[int]",
        "matcher": "NotRequired[str]",
    },
    total=False,
)
SessionAffinityInput = TypedDict(
    "SessionAffinityInput",
    {
        "type": "Required[Literal['none', 'cookie', 'source_ip']]",
        "cookie_name": "NotRequired[str]",
        "duration_sec": "NotRequired[int]",
    },
    total=False,
)
CreateTargetGroupBody: TypeAlias = "CreateTargetGroupRequestInput"
TargetGroupResponse = TypedDict(
    "TargetGroupResponse", {"target_group": "NotRequired[TargetGroup]"}, total=False
)
TargetGroup = TypedDict(
    "TargetGroup",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "account_id": "Required[str]",
        "name": "Required[str]",
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "target_type": "Required[Literal['ip', 'instance', 'function']]",
        "port": "Required[int]",
        "health_check": "Required[HealthCheck]",
        "proxy_protocol": "Required[bool]",
        "session_affinity": "Required[SessionAffinity]",
        "target_mode": "Required[Literal['static', 'pool']]",
        "instance_pool_id": "NotRequired[str]",
        "tags": "Required[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
HealthCheck = TypedDict(
    "HealthCheck",
    {
        "enabled": "NotRequired[bool]",
        "protocol": "NotRequired[Literal['http', 'https', 'tcp', 'udp', '']]",
        "path": "NotRequired[str]",
        "port": "NotRequired[int]",
        "interval_sec": "NotRequired[int]",
        "timeout_sec": "NotRequired[int]",
        "healthy_threshold": "NotRequired[int]",
        "unhealthy_threshold": "NotRequired[int]",
        "matcher": "NotRequired[str]",
    },
    total=False,
)
SessionAffinity = TypedDict(
    "SessionAffinity",
    {
        "type": "Required[Literal['none', 'cookie', 'source_ip']]",
        "cookie_name": "NotRequired[str]",
        "duration_sec": "NotRequired[int]",
    },
    total=False,
)
CreateTargetGroupResponse: TypeAlias = "TargetGroupResponse"
GetListenerResponse: TypeAlias = "ListenerResponse"
GetListenerResource: TypeAlias = "Listener"
GetListenerScope = TypedDict("GetListenerScope", {}, total=False)
GetLoadBalancerResponse: TypeAlias = "LoadBalancerResponse"
GetLoadBalancerResource: TypeAlias = "LoadBalancer"
GetLoadBalancerScope = TypedDict(
    "GetLoadBalancerScope",
    {
        "status": "NotRequired[Literal['provisioning', 'active', 'error', 'deleting']]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
GetRuleResponse: TypeAlias = "RuleResponse"
GetRuleResource: TypeAlias = "Rule"
GetRuleScope = TypedDict("GetRuleScope", {}, total=False)
GetTargetResponse: TypeAlias = "TargetResponse"
GetTargetResource: TypeAlias = "Target"
GetTargetScope = TypedDict("GetTargetScope", {}, total=False)
GetTargetGroupResponse: TypeAlias = "TargetGroupResponse"
GetTargetGroupResource: TypeAlias = "TargetGroup"
GetTargetGroupScope = TypedDict(
    "GetTargetGroupScope",
    {
        "protocol": "NotRequired[Literal['http', 'https', 'tcp', 'udp']]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
ListListenersParameters = TypedDict(
    "ListListenersParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListListenersQuery: TypeAlias = "ListListenersParameters"
ListenerListResponse = TypedDict(
    "ListenerListResponse", {"listeners": "NotRequired[list[Listener]]"}, total=False
)
ListListenersResponse: TypeAlias = "ListenerListResponse"
ListListenersItem: TypeAlias = "Listener"
ListLoadBalancerReplicasParameters = TypedDict(
    "ListLoadBalancerReplicasParameters",
    {"name": "NotRequired[str]", "crn": "NotRequired[str]"},
    total=False,
)
ListLoadBalancerReplicasQuery: TypeAlias = "ListLoadBalancerReplicasParameters"
LoadBalancerReplicasResponse = TypedDict(
    "LoadBalancerReplicasResponse",
    {"replicas": "NotRequired[list[LoadBalancerReplica]]"},
    total=False,
)
LoadBalancerReplica = TypedDict(
    "LoadBalancerReplica",
    {
        "retirement": "NotRequired[Retirement]",
        "instance_id": "Required[str]",
        "replica_index": "Required[int]",
        "created_at": "Required[str]",
        "flavor_id": "Required[str]",
        "status": "Required[Literal['initializing', 'healthy', 'unhealthy', 'draining']]",
        "proxy_ok": "Required[bool]",
        "agent_version": "NotRequired[str]",
        "last_seen": "NotRequired[str]",
    },
    total=False,
)
Retirement = TypedDict(
    "Retirement",
    {
        "requested_at": "Required[str]",
        "drain_seconds": "Required[int]",
        "agent_acknowledged_at": "NotRequired[str]",
        "drain_until": "NotRequired[str]",
    },
    total=False,
)
ListLoadBalancerReplicasResponse: TypeAlias = "LoadBalancerReplicasResponse"
ListLoadBalancerReplicasItem: TypeAlias = "LoadBalancerReplica"
ListLoadBalancersParameters = TypedDict(
    "ListLoadBalancersParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "status": "NotRequired[Literal['provisioning', 'active', 'error', 'deleting']]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListLoadBalancersQuery: TypeAlias = "ListLoadBalancersParameters"
LoadBalancerListResponse = TypedDict(
    "LoadBalancerListResponse",
    {"load_balancers": "NotRequired[list[LoadBalancer]]", "meta": "NotRequired[PaginationMeta]"},
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
ListLoadBalancersResponse: TypeAlias = "LoadBalancerListResponse"
ListLoadBalancersItem: TypeAlias = "LoadBalancer"
ListRulesParameters = TypedDict(
    "ListRulesParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListRulesQuery: TypeAlias = "ListRulesParameters"
RuleListResponse = TypedDict("RuleListResponse", {"rules": "NotRequired[list[Rule]]"}, total=False)
ListRulesResponse: TypeAlias = "RuleListResponse"
ListRulesItem: TypeAlias = "Rule"
ListTargetGroupsParameters = TypedDict(
    "ListTargetGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "protocol": "NotRequired[Literal['http', 'https', 'tcp', 'udp']]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListTargetGroupsQuery: TypeAlias = "ListTargetGroupsParameters"
TargetGroupListResponse = TypedDict(
    "TargetGroupListResponse",
    {"target_groups": "NotRequired[list[TargetGroup]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
ListTargetGroupsResponse: TypeAlias = "TargetGroupListResponse"
ListTargetGroupsItem: TypeAlias = "TargetGroup"
ListTargetsParameters = TypedDict(
    "ListTargetsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListTargetsQuery: TypeAlias = "ListTargetsParameters"
TargetListResponse = TypedDict(
    "TargetListResponse", {"targets": "NotRequired[list[Target]]"}, total=False
)
ListTargetsResponse: TypeAlias = "TargetListResponse"
ListTargetsItem: TypeAlias = "Target"
UpdateListenerRequestInput = TypedDict(
    "UpdateListenerRequestInput",
    {
        "certificate": "NotRequired[str]",
        "default_target_group": "NotRequired[str]",
        "clear_default_target_group": "NotRequired[bool]",
        "exposure": "NotRequired[Literal['public_only', 'private_only', 'both']]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateListenerBody: TypeAlias = "UpdateListenerRequestInput"
UpdateListenerResponse: TypeAlias = "ListenerResponse"
UpdateLoadBalancerRequestInput = TypedDict(
    "UpdateLoadBalancerRequestInput",
    {
        "desired_count": "NotRequired[int]",
        "min_count": "NotRequired[int]",
        "max_count": "NotRequired[int]",
        "autoscaling": "NotRequired[AutoscalingPolicyInput]",
        "replica_count": "NotRequired[int]",
        "flavor": "NotRequired[str]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
UpdateLoadBalancerBody: TypeAlias = "UpdateLoadBalancerRequestInput"
UpdateLoadBalancerResponse: TypeAlias = "LoadBalancerResponse"
UpdateRuleRequestInput = TypedDict(
    "UpdateRuleRequestInput",
    {
        "priority": "Required[int]",
        "conditions": "Required[list[RuleConditionInput]]",
        "target_group": "Required[str]",
    },
    total=False,
)
UpdateRuleBody: TypeAlias = "UpdateRuleRequestInput"
UpdateRuleResponse: TypeAlias = "RuleResponse"
UpdateTargetGroupRequestInput = TypedDict(
    "UpdateTargetGroupRequestInput",
    {
        "health_check": "NotRequired[HealthCheckPatchInput]",
        "proxy_protocol": "NotRequired[bool]",
        "session_affinity": "NotRequired[SessionAffinityInput]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
HealthCheckPatchInput = TypedDict(
    "HealthCheckPatchInput",
    {
        "enabled": "NotRequired[bool]",
        "protocol": "NotRequired[ProtocolInput]",
        "path": "NotRequired[PathInput]",
        "port": "NotRequired[int]",
        "interval_sec": "NotRequired[IntervalSecInput]",
        "timeout_sec": "NotRequired[TimeoutSecInput]",
        "healthy_threshold": "NotRequired[HealthyThresholdInput]",
        "unhealthy_threshold": "NotRequired[UnhealthyThresholdInput]",
        "matcher": "NotRequired[MatcherInput]",
    },
    total=False,
)
ProtocolInput: TypeAlias = "Literal['http', 'https', 'tcp', 'udp', '']"
PathInput: TypeAlias = "str"
IntervalSecInput: TypeAlias = "int"
TimeoutSecInput: TypeAlias = "int"
HealthyThresholdInput: TypeAlias = "int"
UnhealthyThresholdInput: TypeAlias = "int"
MatcherInput: TypeAlias = "str"
UpdateTargetGroupBody: TypeAlias = "UpdateTargetGroupRequestInput"
UpdateTargetGroupResponse: TypeAlias = "TargetGroupResponse"
