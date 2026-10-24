"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

AttachListenerCertificateRequestInput = TypedDict(
    "AttachListenerCertificateRequestInput",
    {"certificate": "Required[str]", "is_default": "NotRequired[bool]"},
    total=False,
)
AttachListenerCertificateBody: TypeAlias = "AttachListenerCertificateRequestInput"
ListenerCertificateResponse = TypedDict(
    "ListenerCertificateResponse", {"certificate": "Required[ResourceRef]"}, total=False
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
AttachListenerCertificateResponse: TypeAlias = "ListenerCertificateResponse"
AttachTargetRequestInput = TypedDict(
    "AttachTargetRequestInput", {"target": "Required[str]", "port": "NotRequired[int]"}, total=False
)
AttachTargetBody: TypeAlias = "AttachTargetRequestInput"
TargetResponse = TypedDict("TargetResponse", {"target": "Required[Target]"}, total=False)
Target: TypeAlias = "TargetVariant1 | TargetVariant2"
TargetVariant1 = TypedDict(
    "TargetVariant1",
    {
        "id": "Required[str]",
        "instance": "Required[ResourceRef]",
        "address": "NotRequired[str]",
        "port": "NotRequired[int]",
        "health": "Required[Literal['initial', 'healthy', 'unhealthy', 'draining']]",
        "last_seen_at": "NotRequired[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
TargetVariant2 = TypedDict(
    "TargetVariant2",
    {
        "id": "Required[str]",
        "instance": "NotRequired[ResourceRef]",
        "address": "Required[str]",
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
        "certificates": "NotRequired[list[str]]",
        "default_target_group": "NotRequired[str]",
        "exposure": "NotRequired[Literal['public_only', 'private_only', 'both']]",
        "tags": "NotRequired[TagsInput]",
    },
    total=False,
)
TagsInput: TypeAlias = "dict[str, str]"
CreateListenerBody: TypeAlias = "CreateListenerRequestInput"
ListenerResponse = TypedDict("ListenerResponse", {"listener": "Required[Listener]"}, total=False)
Listener = TypedDict(
    "Listener",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "port": "Required[int]",
        "exposure": "Required[Literal['public_only', 'private_only', 'both']]",
        "tags": "Required[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "default_certificate": "Required[ResourceRef | Literal[None] | None]",
        "default_target_group": "Required[ResourceRef | Literal[None] | None]",
    },
    total=False,
)
Tags: TypeAlias = "dict[str, str]"
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
        "subnets": "Required[list[str]]",
        "flavor": "Required[str]",
        "replica_count": "NotRequired[int]",
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
    "LoadBalancerResponse", {"load_balancer": "Required[LoadBalancer]"}, total=False
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
        "name": "Required[str]",
        "type": "Required[Literal['application', 'network']]",
        "status": "Required[Literal['provisioning', 'active', 'error', 'deleting']]",
        "faults": "Required[list[Fault]]",
        "subnets": "Required[list[ResourceRef]]",
        "replica_count": "Required[int]",
        "floating_ips": "Required[list[FloatingIPRef]]",
        "dns_name": "NotRequired[str]",
        "tags": "Required[Tags]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "flavor": "Required[ResourceRef]",
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
        "status": "Required[Literal['pending', 'disabled', 'stable', 'scaling', 'waiting', 'warming_up', 'metrics_unavailable', 'stabilizing', 'cooldown', 'draining', 'scale_in_blocked']]",
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
RuleResponse = TypedDict("RuleResponse", {"rule": "Required[Rule]"}, total=False)
Rule = TypedDict(
    "Rule",
    {
        "crn": "Required[str]",
        "id": "Required[str]",
        "priority": "Required[int]",
        "conditions": "Required[list[RuleCondition]]",
        "target_group": "Required[ResourceRef]",
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
    "TargetGroupResponse", {"target_group": "Required[TargetGroup]"}, total=False
)
TargetGroup = TypedDict(
    "TargetGroup",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "protocol": "Required[Literal['http', 'https', 'tcp', 'udp']]",
        "target_type": "Required[Literal['ip', 'instance', 'function']]",
        "port": "Required[int]",
        "health_check": "Required[HealthCheck]",
        "proxy_protocol": "Required[bool]",
        "session_affinity": "Required[SessionAffinity]",
        "target_mode": "Required[Literal['static', 'pool']]",
        "instance_pool": "NotRequired[ResourceRef]",
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
ListenerCertificateListResponse = TypedDict(
    "ListenerCertificateListResponse",
    {"certificates": "Required[list[Certificate]]", "meta": "Required[PaginationMeta]"},
    total=False,
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
ListListenerCertificatesResponse: TypeAlias = "ListenerCertificateListResponse"
ListListenerCertificatesItem: TypeAlias = "Certificate"
ListListenersParameters = TypedDict(
    "ListListenersParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListListenersQuery: TypeAlias = "ListListenersParameters"
ListenerListResponse = TypedDict(
    "ListenerListResponse",
    {"listeners": "Required[list[Listener]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListListenersResponse: TypeAlias = "ListenerListResponse"
ListListenersItem: TypeAlias = "Listener"
ListLoadBalancerInstancesParameters = TypedDict(
    "ListLoadBalancerInstancesParameters",
    {
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
        "name": "NotRequired[str]",
        "current_state": "NotRequired[CurrentStateInput]",
        "flavor": "NotRequired[str]",
        "image": "NotRequired[str]",
    },
    total=False,
)
CurrentStateInput: TypeAlias = "Literal['pending', 'building', 'running', 'stopping', 'stopped', 'rebooting', 'migrating', 'deleting', 'deleted', 'error', 'crashed', 'paused', 'suspended']"
ListLoadBalancerInstancesQuery: TypeAlias = "ListLoadBalancerInstancesParameters"
LoadBalancerInstancesResponse = TypedDict(
    "LoadBalancerInstancesResponse",
    {"instances": "Required[list[LoadBalancerInstance]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
LoadBalancerInstance = TypedDict(
    "LoadBalancerInstance",
    {
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "task_state": "NotRequired[str | None]",
        "flavor": "Required[ResourceRef]",
        "image": "Required[ResourceRef | Literal[None] | None]",
        "user_data": "NotRequired[str]",
        "iam_role": "Required[ResourceRef | Literal[None] | None]",
        "metadata": "NotRequired[Metadata]",
        "tags": "NotRequired[Tags]",
        "faults": "Required[list[Fault]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
        "launched_at": "NotRequired[str | None]",
        "terminated_at": "NotRequired[str | None]",
        "desired_state": "Required[Literal['running', 'stopped', 'deleted']]",
        "current_state": "Required[CurrentState]",
        "retirement": "NotRequired[Retirement]",
        "status": "Required[Literal['initializing', 'healthy', 'unhealthy', 'draining']]",
        "proxy_ok": "Required[bool]",
        "agent_version": "NotRequired[str]",
        "last_seen": "NotRequired[str]",
    },
    total=False,
)
Metadata: TypeAlias = "dict[str, str]"
CurrentState: TypeAlias = "Literal['pending', 'building', 'running', 'stopping', 'stopped', 'rebooting', 'migrating', 'deleting', 'deleted', 'error', 'crashed', 'paused', 'suspended']"
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
ListLoadBalancerInstancesResponse: TypeAlias = "LoadBalancerInstancesResponse"
ListLoadBalancerInstancesItem: TypeAlias = "LoadBalancerInstance"
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
    {"load_balancers": "Required[list[LoadBalancer]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListLoadBalancersResponse: TypeAlias = "LoadBalancerListResponse"
ListLoadBalancersItem: TypeAlias = "LoadBalancer"
ListRulesParameters = TypedDict(
    "ListRulesParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListRulesQuery: TypeAlias = "ListRulesParameters"
RuleListResponse = TypedDict(
    "RuleListResponse",
    {"rules": "Required[list[Rule]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
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
    {"target_groups": "Required[list[TargetGroup]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListTargetGroupsResponse: TypeAlias = "TargetGroupListResponse"
ListTargetGroupsItem: TypeAlias = "TargetGroup"
ListTargetsParameters = TypedDict(
    "ListTargetsParameters", {"name": "NotRequired[str]", "crn": "NotRequired[str]"}, total=False
)
ListTargetsQuery: TypeAlias = "ListTargetsParameters"
TargetListResponse = TypedDict(
    "TargetListResponse",
    {"targets": "Required[list[Target]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListTargetsResponse: TypeAlias = "TargetListResponse"
ListTargetsItem: TypeAlias = "Target"
UpdateListenerRequestInput = TypedDict(
    "UpdateListenerRequestInput",
    {
        "default_target_group": "NotRequired[str | None]",
        "exposure": "NotRequired[Literal['public_only', 'private_only', 'both']]",
        "tags": "NotRequired[TagsInput]",
        "default_certificate": "NotRequired[str]",
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
