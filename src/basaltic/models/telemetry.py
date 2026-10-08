"""Generated API models. Dictionary keys retain their wire names."""

from __future__ import annotations

from typing import Literal, NotRequired, Required, TypeAlias, TypedDict

CreateLogGroupRequestInput = TypedDict(
    "CreateLogGroupRequestInput",
    {
        "name": "Required[str]",
        "description": "NotRequired[str]",
        "retention_days": "NotRequired[int | None]",
        "kms_key": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
CreateLogGroupBody: TypeAlias = "CreateLogGroupRequestInput"
LogGroupResponse = TypedDict(
    "LogGroupResponse", {"log_group": "NotRequired[LogGroup]"}, total=False
)
LogGroup = TypedDict(
    "LogGroup",
    {
        "id": "NotRequired[str]",
        "crn": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "description": "NotRequired[str]",
        "retention_days": "NotRequired[int | None]",
        "kms_key_unavailable": "NotRequired[bool]",
        "kms_key_crn": "NotRequired[str]",
        "tags": "NotRequired[dict[str, str]]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
    },
    total=False,
)
CreateLogGroupResponse: TypeAlias = "LogGroupResponse"
LogResponse = TypedDict("LogResponse", {"log": "NotRequired[LogRecord]"}, total=False)
LogRecord = TypedDict(
    "LogRecord",
    {
        "id": "NotRequired[str]",
        "timestamp": "NotRequired[str]",
        "organization_id": "NotRequired[str]",
        "account_id": "NotRequired[str]",
        "log_group_id": "NotRequired[str]",
        "log_group": "NotRequired[str]",
        "log_stream": "NotRequired[str]",
        "severity": "NotRequired[Literal['TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']]",
        "severity_number": "NotRequired[int]",
        "body": "NotRequired[str]",
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
GetRetainedTelemetryPresenceResult = TypedDict(
    "GetRetainedTelemetryPresenceResult", {"has_resources": "Required[bool]"}, total=False
)
GetRetainedTelemetryPresenceResponse: TypeAlias = "GetRetainedTelemetryPresenceResult"
TraceResponse = TypedDict(
    "TraceResponse",
    {"trace_id": "NotRequired[str]", "spans": "NotRequired[list[Span]]"},
    total=False,
)
Span = TypedDict(
    "Span",
    {
        "trace_id": "NotRequired[str]",
        "span_id": "NotRequired[str]",
        "parent_span_id": "NotRequired[str]",
        "name": "NotRequired[str]",
        "kind": "NotRequired[Literal['INTERNAL', 'SERVER', 'CLIENT', 'PRODUCER', 'CONSUMER']]",
        "service_name": "NotRequired[str]",
        "start_time": "NotRequired[str]",
        "end_time": "NotRequired[str]",
        "duration_ms": "NotRequired[float]",
        "status_code": "NotRequired[Literal['UNSET', 'OK', 'ERROR']]",
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
GetTraceResponse: TypeAlias = "TraceResponse"
TraceSettingsResponse = TypedDict(
    "TraceSettingsResponse", {"trace_settings": "NotRequired[TraceSettings]"}, total=False
)
TraceSettings = TypedDict(
    "TraceSettings",
    {
        "account_id": "NotRequired[str]",
        "retention_days": "NotRequired[int | None]",
        "kms_key_unavailable": "NotRequired[bool]",
        "kms_key_crn": "NotRequired[str]",
        "created_at": "NotRequired[str]",
        "updated_at": "NotRequired[str]",
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
IngestResult = TypedDict(
    "IngestResult",
    {
        "accepted": "NotRequired[int]",
        "rejected": "NotRequired[int]",
        "errors": "NotRequired[list[str]]",
    },
    total=False,
)
IngestLogsResponse: TypeAlias = "IngestResult"
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
IngestSpansResponse: TypeAlias = "IngestResult"
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
    {"log_groups": "NotRequired[list[LogGroup]]", "meta": "NotRequired[PaginationMeta]"},
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
ListLogGroupsResponse: TypeAlias = "LogGroupListResponse"
ListLogGroupsItem: TypeAlias = "LogGroup"
ListMetricNamesParameters = TypedDict(
    "ListMetricNamesParameters", {"start": "Required[str]", "end": "Required[str]"}, total=False
)
ListMetricNamesQuery: TypeAlias = "ListMetricNamesParameters"
ListMetricNamesResult = TypedDict(
    "ListMetricNamesResult",
    {"status": "NotRequired[str]", "data": "NotRequired[list[str]]"},
    total=False,
)
ListMetricNamesResponse: TypeAlias = "ListMetricNamesResult"
ListMetricNamesItem: TypeAlias = "str"
ListMetricNamesPostRequest = TypedDict(
    "ListMetricNamesPostRequest", {"start": "Required[str]", "end": "Required[str]"}, total=False
)
ListMetricNamesPostBody: TypeAlias = "ListMetricNamesPostRequest"
ListMetricNamesPostResult = TypedDict(
    "ListMetricNamesPostResult",
    {"status": "NotRequired[str]", "data": "NotRequired[list[str]]"},
    total=False,
)
ListMetricNamesPostResponse: TypeAlias = "ListMetricNamesPostResult"
ListMetricSeriesParameters = TypedDict(
    "ListMetricSeriesParameters",
    {"metric": "Required[str]", "start": "Required[str]", "end": "Required[str]"},
    total=False,
)
ListMetricSeriesQuery: TypeAlias = "ListMetricSeriesParameters"
ListMetricSeriesResponse: TypeAlias = "dict[str, object]"
ListMetricSeriesPostRequest = TypedDict(
    "ListMetricSeriesPostRequest",
    {"metric": "Required[str]", "start": "Required[str]", "end": "Required[str]"},
    total=False,
)
ListMetricSeriesPostBody: TypeAlias = "ListMetricSeriesPostRequest"
ListMetricSeriesPostResponse: TypeAlias = "dict[str, object]"
UpdateTraceSettingsRequestInput = TypedDict(
    "UpdateTraceSettingsRequestInput",
    {
        "retention_days": "NotRequired[int | None]",
        "clear_retention": "NotRequired[bool]",
        "kms_key": "NotRequired[str | None]",
    },
    total=False,
)
PutTraceSettingsBody: TypeAlias = "UpdateTraceSettingsRequestInput"
PutTraceSettingsResponse: TypeAlias = "TraceSettingsResponse"
QueryMetricsInstantParameters = TypedDict(
    "QueryMetricsInstantParameters",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "step": "NotRequired[str]",
        "time": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsInstantQuery: TypeAlias = "QueryMetricsInstantParameters"
QueryMetricsInstantResponse: TypeAlias = "dict[str, object]"
QueryMetricsInstantPostRequest = TypedDict(
    "QueryMetricsInstantPostRequest",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "step": "NotRequired[str]",
        "time": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsInstantPostBody: TypeAlias = "QueryMetricsInstantPostRequest"
QueryMetricsInstantPostResponse: TypeAlias = "dict[str, object]"
QueryMetricsRangeParameters = TypedDict(
    "QueryMetricsRangeParameters",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "start": "Required[str]",
        "end": "Required[str]",
        "step": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsRangeQuery: TypeAlias = "QueryMetricsRangeParameters"
QueryMetricsRangeResponse: TypeAlias = "dict[str, object]"
QueryMetricsRangePostRequest = TypedDict(
    "QueryMetricsRangePostRequest",
    {
        "metric": "Required[str]",
        "agg": "Required[Literal['avg', 'sum', 'min', 'max', 'count', 'last', 'rate', 'increase']]",
        "match[]": "NotRequired[list[str]]",
        "by[]": "NotRequired[list[str]]",
        "start": "Required[str]",
        "end": "Required[str]",
        "step": "NotRequired[str]",
    },
    total=False,
)
QueryMetricsRangePostBody: TypeAlias = "QueryMetricsRangePostRequest"
QueryMetricsRangePostResponse: TypeAlias = "dict[str, object]"
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
    {"logs": "NotRequired[list[LogRecord]]", "meta": "NotRequired[PaginationMeta]"},
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
    {"traces": "NotRequired[list[TraceSummary]]", "meta": "NotRequired[PaginationMeta]"},
    total=False,
)
TraceSummary = TypedDict(
    "TraceSummary",
    {
        "trace_id": "NotRequired[str]",
        "root_span_id": "NotRequired[str]",
        "root_name": "NotRequired[str]",
        "root_service": "NotRequired[str]",
        "start_time": "NotRequired[str]",
        "duration_ms": "NotRequired[float]",
        "span_count": "NotRequired[int]",
        "error_count": "NotRequired[int]",
        "service_count": "NotRequired[int]",
    },
    total=False,
)
SearchTracesResponse: TypeAlias = "TraceListResponse"
UpdateLogGroupRequestInput = TypedDict(
    "UpdateLogGroupRequestInput",
    {
        "description": "NotRequired[str | None]",
        "retention_days": "NotRequired[int]",
        "clear_retention": "NotRequired[bool]",
        "kms_key": "NotRequired[str | None]",
        "tags": "NotRequired[dict[str, str]]",
    },
    total=False,
)
UpdateLogGroupBody: TypeAlias = "UpdateLogGroupRequestInput"
UpdateLogGroupResponse: TypeAlias = "LogGroupResponse"
