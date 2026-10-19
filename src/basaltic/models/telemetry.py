"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

CreateAlertRequestInput = TypedDict(
    "CreateAlertRequestInput",
    {
        "name": "Required[str]",
        "topic": "Required[str]",
        "expression": "Required[AlertExpressionInput]",
        "operator": "Required[Literal['gt', 'gte', 'lt', 'lte']]",
        "threshold": "Required[float]",
        "window_seconds": "Required[int]",
        "for_seconds": "Required[int]",
        "enabled": "NotRequired[bool]",
        "silenced_until": "NotRequired[str | None]",
    },
    total=False,
)
AlertExpressionInput = TypedDict(
    "AlertExpressionInput",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'min', 'max', 'sum', 'last', 'count', 'rate', 'increase']]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
        "denominator": "NotRequired[AlertQueryInput]",
        "scale": "Required[float]",
        "unit": "NotRequired[str]",
    },
    total=False,
)
AlertQueryInput = TypedDict(
    "AlertQueryInput",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'min', 'max', 'sum', 'last', 'count', 'rate', 'increase']]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
    },
    total=False,
)
CreateAlertBody: TypeAlias = "CreateAlertRequestInput"
AlertResponse = TypedDict("AlertResponse", {"alert": "Required[Alert]"}, total=False)
Alert = TypedDict(
    "Alert",
    {
        "expression": "Required[AlertExpression]",
        "operator": "Required[Literal['gt', 'gte', 'lt', 'lte']]",
        "threshold": "Required[float]",
        "window_seconds": "Required[int]",
        "for_seconds": "Required[int]",
        "enabled": "Required[bool]",
        "silenced_until": "Required[str | None]",
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "topic": "Required[ResourceRef]",
        "state": "Required[Literal['ok', 'pending', 'firing', 'no_data', 'error']]",
        "last_value": "Required[float | None]",
        "evaluated_at": "NotRequired[str]",
        "state_changed_at": "NotRequired[str]",
        "pending_since": "NotRequired[str]",
        "evaluation_error": "NotRequired[str]",
        "delivery_error": "NotRequired[str]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
AlertExpression = TypedDict(
    "AlertExpression",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'min', 'max', 'sum', 'last', 'count', 'rate', 'increase']]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
        "denominator": "NotRequired[AlertQuery]",
        "scale": "Required[float]",
        "unit": "NotRequired[str]",
    },
    total=False,
)
AlertQuery = TypedDict(
    "AlertQuery",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'min', 'max', 'sum', 'last', 'count', 'rate', 'increase']]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
    },
    total=False,
)
ResourceRef = TypedDict(
    "ResourceRef",
    {"id": "Required[str]", "crn": "Required[str]", "name": "NotRequired[str]"},
    total=False,
)
CreateAlertResponse: TypeAlias = "AlertResponse"
CreateLogGroupRequestInput = TypedDict(
    "CreateLogGroupRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "retention_days": "NotRequired[Literal[1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653, None] | None]",
        "kms_key": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateLogGroupBody: TypeAlias = "CreateLogGroupRequestInput"
LogGroupResponse = TypedDict("LogGroupResponse", {"log_group": "Required[LogGroup]"}, total=False)
LogGroup = TypedDict(
    "LogGroup",
    {
        "kms_key": "NotRequired[ResourceRef]",
        "id": "Required[str]",
        "crn": "Required[str]",
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "retention_days": "Required[Literal[1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653, None] | None]",
        "tags": "Required[dict[str, str]]",
        "created_at": "Required[str]",
        "updated_at": "Required[str]",
    },
    total=False,
)
CreateLogGroupResponse: TypeAlias = "LogGroupResponse"
GetAlertResponse: TypeAlias = "AlertResponse"
GetAlertResource: TypeAlias = "Alert"
GetAlertScope = TypedDict(
    "GetAlertScope",
    {
        "state": "NotRequired[Literal['ok', 'pending', 'firing', 'no_data', 'error', 'silenced', 'disabled']]",
        "limit": "NotRequired[int]",
    },
    total=False,
)
LogResponse = TypedDict("LogResponse", {"log": "Required[LogRecord]"}, total=False)
LogRecord = TypedDict(
    "LogRecord",
    {
        "id": "Required[str]",
        "timestamp": "Required[str]",
        "log_group": "Required[ResourceRef]",
        "log_stream": "Required[str]",
        "severity": "Required[Literal['TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']]",
        "severity_number": "Required[int]",
        "body": "Required[str]",
        "attributes": "NotRequired[dict[str, str]]",
        "resource": "NotRequired[dict[str, str]]",
        "trace_id": "NotRequired[str]",
        "span_id": "NotRequired[str]",
    },
    total=False,
)
GetLogResponse: TypeAlias = "LogResponse"
GetLogGroupResponse: TypeAlias = "LogGroupResponse"
GetLogGroupResource: TypeAlias = "LogGroup"
GetLogGroupScope = TypedDict("GetLogGroupScope", {"limit": "NotRequired[int]"}, total=False)
RetainedDataResponse = TypedDict(
    "RetainedDataResponse",
    {"retained_data": "Required[RetainedDataResponseRetainedData]"},
    total=False,
)
RetainedDataResponseRetainedData = TypedDict(
    "RetainedDataResponseRetainedData",
    {"has_data": "Required[bool]", "blocks_deletion": "NotRequired[bool]"},
    total=False,
)
GetRetainedTelemetryPresenceResponse: TypeAlias = "RetainedDataResponse"
TraceResponse = TypedDict("TraceResponse", {"trace": "Required[TraceSummary]"}, total=False)
TraceSummary = TypedDict(
    "TraceSummary",
    {
        "trace_id": "Required[str]",
        "root_span_id": "Required[str]",
        "root_name": "Required[str]",
        "root_service": "Required[str]",
        "start_time": "Required[str]",
        "duration_ms": "Required[float]",
        "span_count": "Required[int]",
        "error_count": "Required[int]",
        "service_count": "Required[int]",
    },
    total=False,
)
GetTraceResponse: TypeAlias = "TraceResponse"
TraceSettingsResponse = TypedDict(
    "TraceSettingsResponse", {"trace_settings": "Required[TraceSettings]"}, total=False
)
TraceSettings = TypedDict(
    "TraceSettings",
    {
        "retention_days": "Required[Literal[1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653]]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
        "kms_key": "NotRequired[ResourceRef]",
    },
    total=False,
)
GetTraceSettingsResponse: TypeAlias = "TraceSettingsResponse"
IngestRequestInput = TypedDict(
    "IngestRequestInput", {"logs": "Required[list[IngestRecordInput]]"}, total=False
)
IngestRecordInput = TypedDict(
    "IngestRecordInput",
    {
        "timestamp": "NotRequired[str]",
        "log_group": "Required[str]",
        "log_stream": "Required[str]",
        "severity": "NotRequired[str]",
        "body": "Required[str]",
        "attributes": "NotRequired[dict[str, str]]",
        "resource": "NotRequired[dict[str, str]]",
        "trace_id": "NotRequired[str]",
        "span_id": "NotRequired[str]",
    },
    total=False,
)
IngestLogsBody: TypeAlias = "IngestRequestInput"
IngestResponse = TypedDict("IngestResponse", {"ingestion": "Required[IngestResult]"}, total=False)
IngestResult = TypedDict(
    "IngestResult",
    {
        "accepted": "Required[int]",
        "rejected": "Required[int]",
        "errors": "NotRequired[list[IngestError]]",
    },
    total=False,
)
IngestError = TypedDict(
    "IngestError",
    {"index": "Required[int]", "code": "Required[str]", "message": "Required[str]"},
    total=False,
)
IngestLogsResponse: TypeAlias = "IngestResponse"
IngestSpansRequestInput = TypedDict(
    "IngestSpansRequestInput", {"spans": "Required[list[SpanIngestRecordInput]]"}, total=False
)
SpanIngestRecordInput = TypedDict(
    "SpanIngestRecordInput",
    {
        "trace_id": "Required[str]",
        "span_id": "Required[str]",
        "parent_span_id": "NotRequired[str]",
        "name": "Required[str]",
        "kind": "NotRequired[Literal['INTERNAL', 'SERVER', 'CLIENT', 'PRODUCER', 'CONSUMER']]",
        "service_name": "NotRequired[str]",
        "start_time": "Required[str]",
        "end_time": "Required[str]",
        "status_code": "NotRequired[Literal['UNSET', 'OK', 'ERROR']]",
        "status_message": "NotRequired[str]",
        "attributes": "NotRequired[dict[str, str]]",
        "resource": "NotRequired[dict[str, str]]",
        "events": "NotRequired[list[SpanEventInput]]",
        "links": "NotRequired[list[SpanLinkInput]]",
    },
    total=False,
)
SpanEventInput = TypedDict(
    "SpanEventInput",
    {
        "timestamp": "NotRequired[str]",
        "name": "Required[str]",
        "attributes": "NotRequired[dict[str, str]]",
    },
    total=False,
)
SpanLinkInput = TypedDict(
    "SpanLinkInput", {"trace_id": "Required[str]", "span_id": "Required[str]"}, total=False
)
IngestSpansBody: TypeAlias = "IngestSpansRequestInput"
IngestSpansResponse: TypeAlias = "IngestResponse"
ListAlertsParameters = TypedDict(
    "ListAlertsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "state": "NotRequired[Literal['ok', 'pending', 'firing', 'no_data', 'error', 'silenced', 'disabled']]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListAlertsQuery: TypeAlias = "ListAlertsParameters"
AlertListResponse = TypedDict(
    "AlertListResponse",
    {"alerts": "Required[list[Alert]]", "meta": "Required[PaginationMeta]"},
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
ListAlertsResponse: TypeAlias = "AlertListResponse"
ListAlertsItem: TypeAlias = "Alert"
ListLogGroupsParameters = TypedDict(
    "ListLogGroupsParameters",
    {
        "name": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListLogGroupsQuery: TypeAlias = "ListLogGroupsParameters"
LogGroupListResponse = TypedDict(
    "LogGroupListResponse",
    {"log_groups": "Required[list[LogGroup]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListLogGroupsResponse: TypeAlias = "LogGroupListResponse"
ListLogGroupsItem: TypeAlias = "LogGroup"
ListMetricNamesParameters = TypedDict(
    "ListMetricNamesParameters",
    {
        "start": "Required[str]",
        "end": "Required[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListMetricNamesQuery: TypeAlias = "ListMetricNamesParameters"
MetricNamesResponse = TypedDict(
    "MetricNamesResponse",
    {"metric_names": "Required[list[str]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListMetricNamesResponse: TypeAlias = "MetricNamesResponse"
ListMetricNamesItem: TypeAlias = "str"
ListMetricNamesPostRequest = TypedDict(
    "ListMetricNamesPostRequest",
    {
        "start": "Required[str]",
        "end": "Required[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListMetricNamesPostBody: TypeAlias = "ListMetricNamesPostRequest"
ListMetricNamesPostResponse: TypeAlias = "MetricNamesResponse"
ListMetricSeriesParameters = TypedDict(
    "ListMetricSeriesParameters",
    {
        "metric": "Required[str]",
        "start": "Required[str]",
        "end": "Required[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListMetricSeriesQuery: TypeAlias = "ListMetricSeriesParameters"
MetricSeriesResponse = TypedDict(
    "MetricSeriesResponse",
    {"series": "Required[list[dict[str, str]]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
ListMetricSeriesResponse: TypeAlias = "MetricSeriesResponse"
ListMetricSeriesItem: TypeAlias = "dict[str, str]"
ListMetricSeriesPostRequest = TypedDict(
    "ListMetricSeriesPostRequest",
    {
        "metric": "Required[str]",
        "start": "Required[str]",
        "end": "Required[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
ListMetricSeriesPostBody: TypeAlias = "ListMetricSeriesPostRequest"
ListMetricSeriesPostResponse: TypeAlias = "MetricSeriesResponse"
ListTraceSpansParameters = TypedDict(
    "ListTraceSpansParameters",
    {"limit": "NotRequired[int]", "marker": "NotRequired[str]"},
    total=False,
)
ListTraceSpansQuery: TypeAlias = "ListTraceSpansParameters"
SpanListResponse = TypedDict(
    "SpanListResponse",
    {"spans": "Required[list[Span]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
Span = TypedDict(
    "Span",
    {
        "trace_id": "Required[str]",
        "span_id": "Required[str]",
        "parent_span_id": "NotRequired[str]",
        "name": "Required[str]",
        "kind": "Required[Literal['INTERNAL', 'SERVER', 'CLIENT', 'PRODUCER', 'CONSUMER']]",
        "service_name": "Required[str]",
        "start_time": "Required[str]",
        "end_time": "Required[str]",
        "duration_ms": "Required[float]",
        "status_code": "Required[Literal['UNSET', 'OK', 'ERROR']]",
        "status_message": "NotRequired[str]",
        "attributes": "NotRequired[dict[str, str]]",
        "resource": "NotRequired[dict[str, str]]",
        "events": "NotRequired[list[SpanEvent]]",
        "links": "NotRequired[list[SpanLink]]",
    },
    total=False,
)
SpanEvent = TypedDict(
    "SpanEvent",
    {
        "timestamp": "NotRequired[str]",
        "name": "Required[str]",
        "attributes": "NotRequired[dict[str, str]]",
    },
    total=False,
)
SpanLink = TypedDict(
    "SpanLink", {"trace_id": "Required[str]", "span_id": "Required[str]"}, total=False
)
ListTraceSpansResponse: TypeAlias = "SpanListResponse"
ListTraceSpansItem: TypeAlias = "Span"
QueryMetricsInstantParameters = TypedDict(
    "QueryMetricsInstantParameters",
    {
        "metric": "Required[str]",
        "agg": "NotRequired[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "step": "NotRequired[str]",
        "time": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsInstantQuery: TypeAlias = "QueryMetricsInstantParameters"
MetricQueryResponse = TypedDict(
    "MetricQueryResponse", {"query_result": "Required[MetricQueryResult]"}, total=False
)
MetricQueryResult = TypedDict(
    "MetricQueryResult",
    {"metric": "Required[str]", "series": "Required[list[MetricQuerySeries]]"},
    total=False,
)
MetricQuerySeries = TypedDict(
    "MetricQuerySeries",
    {"labels": "Required[dict[str, str]]", "points": "Required[list[MetricPoint]]"},
    total=False,
)
MetricPoint = TypedDict(
    "MetricPoint", {"timestamp": "Required[float]", "value": "Required[str]"}, total=False
)
QueryMetricsInstantResponse: TypeAlias = "MetricQueryResponse"
QueryMetricsInstantPostRequest = TypedDict(
    "QueryMetricsInstantPostRequest",
    {
        "metric": "Required[str]",
        "agg": "NotRequired[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "step": "NotRequired[str]",
        "time": "NotRequired[str]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
    },
    total=False,
)
QueryMetricsInstantPostBody: TypeAlias = "QueryMetricsInstantPostRequest"
QueryMetricsInstantPostResponse: TypeAlias = "MetricQueryResponse"
QueryMetricsRangeParameters = TypedDict(
    "QueryMetricsRangeParameters",
    {
        "metric": "Required[str]",
        "agg": "NotRequired[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "start": "Required[str]",
        "end": "Required[str]",
        "step": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsRangeQuery: TypeAlias = "QueryMetricsRangeParameters"
QueryMetricsRangeResponse: TypeAlias = "MetricQueryResponse"
QueryMetricsRangePostRequest = TypedDict(
    "QueryMetricsRangePostRequest",
    {
        "metric": "Required[str]",
        "agg": "NotRequired[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "start": "Required[str]",
        "end": "Required[str]",
        "step": "NotRequired[str]",
        "match": "NotRequired[list[str]]",
        "by": "NotRequired[list[str]]",
    },
    total=False,
)
QueryMetricsRangePostBody: TypeAlias = "QueryMetricsRangePostRequest"
QueryMetricsRangePostResponse: TypeAlias = "MetricQueryResponse"
SearchLogsParameters = TypedDict(
    "SearchLogsParameters",
    {
        "from": "Required[str]",
        "to": "Required[str]",
        "log_group": "NotRequired[str]",
        "log_stream": "NotRequired[str]",
        "min_severity": "NotRequired[Literal['TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']]",
        "region": "NotRequired[str]",
        "q": "NotRequired[str]",
        "trace_id": "NotRequired[str]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
SearchLogsQuery: TypeAlias = "SearchLogsParameters"
LogListResponse = TypedDict(
    "LogListResponse",
    {"logs": "Required[list[LogRecord]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
SearchLogsResponse: TypeAlias = "LogListResponse"
SearchTracesParameters = TypedDict(
    "SearchTracesParameters",
    {
        "from": "Required[str]",
        "to": "Required[str]",
        "service": "NotRequired[str]",
        "operation": "NotRequired[str]",
        "status_code": "NotRequired[Literal['UNSET', 'OK', 'ERROR']]",
        "min_duration_ms": "NotRequired[float]",
        "limit": "NotRequired[int]",
        "marker": "NotRequired[str]",
    },
    total=False,
)
SearchTracesQuery: TypeAlias = "SearchTracesParameters"
TraceListResponse = TypedDict(
    "TraceListResponse",
    {"traces": "Required[list[TraceSummary]]", "meta": "Required[PaginationMeta]"},
    total=False,
)
SearchTracesResponse: TypeAlias = "TraceListResponse"
UpdateAlertRequestInput = TypedDict(
    "UpdateAlertRequestInput",
    {
        "topic": "NotRequired[str]",
        "expression": "NotRequired[AlertExpressionInput]",
        "operator": "NotRequired[Literal['gt', 'gte', 'lt', 'lte']]",
        "threshold": "NotRequired[float]",
        "window_seconds": "NotRequired[int]",
        "for_seconds": "NotRequired[int]",
        "enabled": "NotRequired[bool]",
        "silenced_until": "NotRequired[str | None]",
    },
    total=False,
)
UpdateAlertBody: TypeAlias = "UpdateAlertRequestInput"
UpdateAlertResponse: TypeAlias = "AlertResponse"
UpdateLogGroupRequestInput = TypedDict(
    "UpdateLogGroupRequestInput",
    {
        "description": "NotRequired[str | None]",
        "retention_days": "NotRequired[Literal[1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653, None] | None]",
        "kms_key": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
UpdateLogGroupBody: TypeAlias = "UpdateLogGroupRequestInput"
UpdateLogGroupResponse: TypeAlias = "LogGroupResponse"
UpdateTraceSettingsRequestInput = TypedDict(
    "UpdateTraceSettingsRequestInput",
    {
        "retention_days": "NotRequired[Literal[1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, 3653, None] | None]",
        "kms_key": "NotRequired[str | None]",
    },
    total=False,
)
UpdateTraceSettingsBody: TypeAlias = "UpdateTraceSettingsRequestInput"
UpdateTraceSettingsResponse: TypeAlias = "TraceSettingsResponse"
