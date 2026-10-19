"""Generated typed API methods; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from typing import cast

from .._common import UNSET, AsyncBinaryBody, BinaryBody, Operation
from .._transport import AsyncTransport, SyncTransport
from ..config import RequestOptions
from ..models import telemetry as m
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
    "createAlert": Operation(
        id="createAlert",
        method="POST",
        path="/v1/alerts",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "createLogGroup": Operation(
        id="createLogGroup",
        method="POST",
        path="/v1/log-groups",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "deleteAlert": Operation(
        id="deleteAlert",
        method="DELETE",
        path="/v1/alerts/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteLogGroup": Operation(
        id="deleteLogGroup",
        method="DELETE",
        path="/v1/log-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "deleteTraceSettings": Operation(
        id="deleteTraceSettings",
        method="DELETE",
        path="/v1/trace-settings",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getAlert": Operation(
        id="getAlert",
        method="GET",
        path="/v1/alerts/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getLog": Operation(
        id="getLog",
        method="GET",
        path="/v1/logs/{log_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getLogGroup": Operation(
        id="getLogGroup",
        method="GET",
        path="/v1/log-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getRetainedTelemetryPresence": Operation(
        id="getRetainedTelemetryPresence",
        method="GET",
        path="/v1/retained-data",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getTrace": Operation(
        id="getTrace",
        method="GET",
        path="/v1/traces/{trace_id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "getTraceSettings": Operation(
        id="getTraceSettings",
        method="GET",
        path="/v1/trace-settings",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "ingestLogs": Operation(
        id="ingestLogs",
        method="POST",
        path="/v1/logs",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "ingestSpans": Operation(
        id="ingestSpans",
        method="POST",
        path="/v1/spans",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "listAlerts": Operation(
        id="listAlerts",
        method="GET",
        path="/v1/alerts",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "name": {"style": "form", "explode": True},
            "crn": {"style": "form", "explode": True},
            "state": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="alerts",
    ),
    "listLogGroups": Operation(
        id="listLogGroups",
        method="GET",
        path="/v1/log-groups",
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
        itemsKey="log_groups",
    ),
    "listMetricNames": Operation(
        id="listMetricNames",
        method="GET",
        path="/v1/metrics/names",
        authenticated=True,
        requiredQuery=["start", "end"],
        requiredHeaders=[],
        queryEncoding={
            "start": {"style": "form", "explode": True},
            "end": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="metric_names",
    ),
    "listMetricNamesPost": Operation(
        id="listMetricNamesPost",
        method="POST",
        path="/v1/metrics/names",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "listMetricSeries": Operation(
        id="listMetricSeries",
        method="GET",
        path="/v1/metrics/series",
        authenticated=True,
        requiredQuery=["metric", "start", "end"],
        requiredHeaders=[],
        queryEncoding={
            "metric": {"style": "form", "explode": True},
            "start": {"style": "form", "explode": True},
            "end": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="series",
    ),
    "listMetricSeriesPost": Operation(
        id="listMetricSeriesPost",
        method="POST",
        path="/v1/metrics/series",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "listTraceSpans": Operation(
        id="listTraceSpans",
        method="GET",
        path="/v1/traces/{trace_id}/spans",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
        itemsKey="spans",
    ),
    "queryMetricsInstant": Operation(
        id="queryMetricsInstant",
        method="GET",
        path="/v1/metrics/query",
        authenticated=True,
        requiredQuery=["metric"],
        requiredHeaders=[],
        queryEncoding={
            "metric": {"style": "form", "explode": True},
            "agg": {"style": "form", "explode": True},
            "match[]": {"style": "form", "explode": True},
            "by[]": {"style": "form", "explode": True},
            "step": {"style": "form", "explode": True},
            "time": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "queryMetricsInstantPost": Operation(
        id="queryMetricsInstantPost",
        method="POST",
        path="/v1/metrics/query",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "queryMetricsRange": Operation(
        id="queryMetricsRange",
        method="GET",
        path="/v1/metrics/query-range",
        authenticated=True,
        requiredQuery=["metric", "start", "end"],
        requiredHeaders=[],
        queryEncoding={
            "metric": {"style": "form", "explode": True},
            "agg": {"style": "form", "explode": True},
            "match[]": {"style": "form", "explode": True},
            "by[]": {"style": "form", "explode": True},
            "start": {"style": "form", "explode": True},
            "end": {"style": "form", "explode": True},
            "step": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "queryMetricsRangePost": Operation(
        id="queryMetricsRangePost",
        method="POST",
        path="/v1/metrics/query-range",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "searchLogs": Operation(
        id="searchLogs",
        method="GET",
        path="/v1/logs",
        authenticated=True,
        requiredQuery=["from", "to"],
        requiredHeaders=[],
        queryEncoding={
            "from": {"style": "form", "explode": True},
            "to": {"style": "form", "explode": True},
            "log_group": {"style": "form", "explode": True},
            "log_stream": {"style": "form", "explode": True},
            "min_severity": {"style": "form", "explode": True},
            "region": {"style": "form", "explode": True},
            "q": {"style": "form", "explode": True},
            "trace_id": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "searchTraces": Operation(
        id="searchTraces",
        method="GET",
        path="/v1/traces",
        authenticated=True,
        requiredQuery=["from", "to"],
        requiredHeaders=[],
        queryEncoding={
            "from": {"style": "form", "explode": True},
            "to": {"style": "form", "explode": True},
            "service": {"style": "form", "explode": True},
            "operation": {"style": "form", "explode": True},
            "status_code": {"style": "form", "explode": True},
            "min_duration_ms": {"style": "form", "explode": True},
            "limit": {"style": "form", "explode": True},
            "marker": {"style": "form", "explode": True},
        },
        bodyRequired=False,
        contentType="",
        accept="application/json",
    ),
    "updateAlert": Operation(
        id="updateAlert",
        method="PATCH",
        path="/v1/alerts/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateLogGroup": Operation(
        id="updateLogGroup",
        method="PATCH",
        path="/v1/log-groups/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "updateTraceSettings": Operation(
        id="updateTraceSettings",
        method="PATCH",
        path="/v1/trace-settings",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/json",
        accept="application/json",
    ),
    "writeMetrics": Operation(
        id="writeMetrics",
        method="POST",
        path="/v1/metrics/write",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=True,
        contentType="application/x-protobuf",
        accept="application/json",
    ),
}


class TelemetryService:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create_alert(
        self, body: m.CreateAlertBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateAlertResponse]:
        "Create a metric alert"
        return cast(
            ApiResponse[m.CreateAlertResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["createAlert"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def create_log_group(
        self, body: m.CreateLogGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateLogGroupResponse]:
        "Create a log group"
        return cast(
            ApiResponse[m.CreateLogGroupResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["createLogGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def delete_alert(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a metric alert"
        return cast(
            None,
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteAlert"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_log_group(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a log group"
        return cast(
            None,
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteLogGroup"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def delete_trace_settings(self, *, options: RequestOptions | None = None) -> None:
        "Delete trace settings"
        return cast(
            None,
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteTraceSettings"],
                "discard",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_alert(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAlertResponse]:
        "Get a metric alert"
        return cast(
            ApiResponse[m.GetAlertResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getAlert"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def get_alert_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAlertScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAlertResource]:
        return cast(
            ApiResponse[m.GetAlertResource],
            resolve_reference(
                reference,
                lambda id: self.get_alert(id, options=options),
                lambda match: self.list_alerts(
                    query=cast(m.ListAlertsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "alert",
            ),
        )

    def get_log(
        self, log_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLogResponse]:
        "Get a single log record by id"
        return cast(
            ApiResponse[m.GetLogResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getLog"],
                "json",
                {"log_id": log_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_log_group(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLogGroupResponse]:
        "Get a log group by id"
        return cast(
            ApiResponse[m.GetLogGroupResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getLogGroup"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    def get_log_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetLogGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetLogGroupResource]:
        return cast(
            ApiResponse[m.GetLogGroupResource],
            resolve_reference(
                reference,
                lambda id: self.get_log_group(id, options=options),
                lambda match: self.list_log_groups(
                    query=cast(
                        m.ListLogGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "log_group",
            ),
        )

    def get_retained_telemetry_presence(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRetainedTelemetryPresenceResponse]:
        "Check retained telemetry presence"
        return cast(
            ApiResponse[m.GetRetainedTelemetryPresenceResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getRetainedTelemetryPresence"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def get_trace(
        self, trace_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTraceResponse]:
        "Get a trace"
        return cast(
            ApiResponse[m.GetTraceResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getTrace"],
                "json",
                {"trace_id": trace_id},
                UNSET,
                None,
                options,
            ),
        )

    def get_trace_settings(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTraceSettingsResponse]:
        "Get the caller account's trace settings"
        return cast(
            ApiResponse[m.GetTraceSettingsResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getTraceSettings"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    def ingest_logs(
        self, body: m.IngestLogsBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.IngestLogsResponse]:
        "Ingest a batch of log records"
        return cast(
            ApiResponse[m.IngestLogsResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["ingestLogs"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def ingest_spans(
        self, body: m.IngestSpansBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.IngestSpansResponse]:
        "Ingest a batch of trace spans"
        return cast(
            ApiResponse[m.IngestSpansResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["ingestSpans"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def list_alerts(
        self, *, query: m.ListAlertsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAlertsResponse, m.ListAlertsItem]:
        "List metric alerts"
        return cast(
            Page[m.ListAlertsResponse, m.ListAlertsItem],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listAlerts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_alerts_all(
        self, *, query: m.ListAlertsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListAlertsItem]:
        return iterate_pages(
            lambda marker: self.list_alerts(
                query=cast(m.ListAlertsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    def list_log_groups(
        self, *, query: m.ListLogGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListLogGroupsResponse, m.ListLogGroupsItem]:
        "List log groups (or look up one by name)"
        return cast(
            Page[m.ListLogGroupsResponse, m.ListLogGroupsItem],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listLogGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_log_groups_all(
        self, *, query: m.ListLogGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Iterator[m.ListLogGroupsItem]:
        return iterate_pages(
            lambda marker: self.list_log_groups(
                query=cast(m.ListLogGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_metric_names(
        self, *, query: m.ListMetricNamesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListMetricNamesResponse, m.ListMetricNamesItem]:
        "List metric names"
        return cast(
            Page[m.ListMetricNamesResponse, m.ListMetricNamesItem],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricNames"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_metric_names_all(
        self, *, query: m.ListMetricNamesQuery, options: RequestOptions | None = None
    ) -> Iterator[m.ListMetricNamesItem]:
        return iterate_pages(
            lambda marker: self.list_metric_names(
                query=cast(m.ListMetricNamesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_metric_names_post(
        self, body: m.ListMetricNamesPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ListMetricNamesPostResponse]:
        "List metric names (JSON)"
        return cast(
            ApiResponse[m.ListMetricNamesPostResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricNamesPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def list_metric_series(
        self, *, query: m.ListMetricSeriesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListMetricSeriesResponse, m.ListMetricSeriesItem]:
        "List metric series"
        return cast(
            Page[m.ListMetricSeriesResponse, m.ListMetricSeriesItem],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricSeries"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_metric_series_all(
        self, *, query: m.ListMetricSeriesQuery, options: RequestOptions | None = None
    ) -> Iterator[m.ListMetricSeriesItem]:
        return iterate_pages(
            lambda marker: self.list_metric_series(
                query=cast(m.ListMetricSeriesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def list_metric_series_post(
        self, body: m.ListMetricSeriesPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ListMetricSeriesPostResponse]:
        "List metric series (JSON)"
        return cast(
            ApiResponse[m.ListMetricSeriesPostResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricSeriesPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def list_trace_spans(
        self,
        trace_id: str,
        *,
        query: m.ListTraceSpansQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTraceSpansResponse, m.ListTraceSpansItem]:
        "List spans in a trace"
        return cast(
            Page[m.ListTraceSpansResponse, m.ListTraceSpansItem],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listTraceSpans"],
                "page",
                {"trace_id": trace_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_trace_spans_all(
        self,
        trace_id: str,
        *,
        query: m.ListTraceSpansQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Iterator[m.ListTraceSpansItem]:
        return iterate_pages(
            lambda marker: self.list_trace_spans(
                trace_id,
                query=cast(m.ListTraceSpansQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    def query_metrics_instant(
        self, *, query: m.QueryMetricsInstantQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsInstantResponse]:
        "Run an instant metric query"
        return cast(
            ApiResponse[m.QueryMetricsInstantResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsInstant"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def query_metrics_instant_post(
        self, body: m.QueryMetricsInstantPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsInstantPostResponse]:
        "Run an instant metric query (JSON)"
        return cast(
            ApiResponse[m.QueryMetricsInstantPostResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsInstantPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def query_metrics_range(
        self, *, query: m.QueryMetricsRangeQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsRangeResponse]:
        "Run a range metric query"
        return cast(
            ApiResponse[m.QueryMetricsRangeResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsRange"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def query_metrics_range_post(
        self, body: m.QueryMetricsRangePostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsRangePostResponse]:
        "Run a range metric query (JSON)"
        return cast(
            ApiResponse[m.QueryMetricsRangePostResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsRangePost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def search_logs(
        self, *, query: m.SearchLogsQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.SearchLogsResponse]:
        "Search log records"
        return cast(
            ApiResponse[m.SearchLogsResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["searchLogs"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def search_traces(
        self, *, query: m.SearchTracesQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.SearchTracesResponse]:
        "List traces"
        return cast(
            ApiResponse[m.SearchTracesResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["searchTraces"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def update_alert(
        self, id: str, body: m.UpdateAlertBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateAlertResponse]:
        "Update a metric alert"
        return cast(
            ApiResponse[m.UpdateAlertResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateAlert"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    def update_log_group(
        self, id: str, body: m.UpdateLogGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateLogGroupResponse]:
        "Update a log group"
        return cast(
            ApiResponse[m.UpdateLogGroupResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateLogGroup"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    def update_trace_settings(
        self, body: m.UpdateTraceSettingsBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTraceSettingsResponse]:
        "Update the caller account's trace settings"
        return cast(
            ApiResponse[m.UpdateTraceSettingsResponse],
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateTraceSettings"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    def write_metrics(self, body: BinaryBody, *, options: RequestOptions | None = None) -> None:
        "Prometheus remote_write ingest"
        return cast(
            None,
            self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["writeMetrics"],
                "discard",
                {},
                body,
                None,
                options,
            ),
        )


class AsyncTelemetryService:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_alert(
        self, body: m.CreateAlertBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateAlertResponse]:
        "Create a metric alert"
        return cast(
            ApiResponse[m.CreateAlertResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["createAlert"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def create_log_group(
        self, body: m.CreateLogGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.CreateLogGroupResponse]:
        "Create a log group"
        return cast(
            ApiResponse[m.CreateLogGroupResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["createLogGroup"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def delete_alert(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a metric alert"
        return cast(
            None,
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteAlert"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_log_group(self, id: str, *, options: RequestOptions | None = None) -> None:
        "Delete a log group"
        return cast(
            None,
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteLogGroup"],
                "discard",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def delete_trace_settings(self, *, options: RequestOptions | None = None) -> None:
        "Delete trace settings"
        return cast(
            None,
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["deleteTraceSettings"],
                "discard",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_alert(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetAlertResponse]:
        "Get a metric alert"
        return cast(
            ApiResponse[m.GetAlertResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getAlert"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_alert_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetAlertScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetAlertResource]:
        return cast(
            ApiResponse[m.GetAlertResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_alert(id, options=options),
                lambda match: self.list_alerts(
                    query=cast(m.ListAlertsQuery, {**reference_scope(scope), **match, "limit": 2}),
                    options=options,
                ),
                True,
                "alert",
            ),
        )

    async def get_log(
        self, log_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLogResponse]:
        "Get a single log record by id"
        return cast(
            ApiResponse[m.GetLogResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getLog"],
                "json",
                {"log_id": log_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_log_group(
        self, id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetLogGroupResponse]:
        "Get a log group by id"
        return cast(
            ApiResponse[m.GetLogGroupResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getLogGroup"],
                "json",
                {"id": id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_log_group_by_reference(
        self,
        reference: str,
        *,
        scope: m.GetLogGroupScope | None = None,
        options: RequestOptions | None = None,
    ) -> ApiResponse[m.GetLogGroupResource]:
        return cast(
            ApiResponse[m.GetLogGroupResource],
            await aresolve_reference(
                reference,
                lambda id: self.get_log_group(id, options=options),
                lambda match: self.list_log_groups(
                    query=cast(
                        m.ListLogGroupsQuery, {**reference_scope(scope), **match, "limit": 2}
                    ),
                    options=options,
                ),
                True,
                "log_group",
            ),
        )

    async def get_retained_telemetry_presence(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetRetainedTelemetryPresenceResponse]:
        "Check retained telemetry presence"
        return cast(
            ApiResponse[m.GetRetainedTelemetryPresenceResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getRetainedTelemetryPresence"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def get_trace(
        self, trace_id: str, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTraceResponse]:
        "Get a trace"
        return cast(
            ApiResponse[m.GetTraceResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getTrace"],
                "json",
                {"trace_id": trace_id},
                UNSET,
                None,
                options,
            ),
        )

    async def get_trace_settings(
        self, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.GetTraceSettingsResponse]:
        "Get the caller account's trace settings"
        return cast(
            ApiResponse[m.GetTraceSettingsResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["getTraceSettings"],
                "json",
                {},
                UNSET,
                None,
                options,
            ),
        )

    async def ingest_logs(
        self, body: m.IngestLogsBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.IngestLogsResponse]:
        "Ingest a batch of log records"
        return cast(
            ApiResponse[m.IngestLogsResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["ingestLogs"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def ingest_spans(
        self, body: m.IngestSpansBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.IngestSpansResponse]:
        "Ingest a batch of trace spans"
        return cast(
            ApiResponse[m.IngestSpansResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["ingestSpans"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def list_alerts(
        self, *, query: m.ListAlertsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListAlertsResponse, m.ListAlertsItem]:
        "List metric alerts"
        return cast(
            Page[m.ListAlertsResponse, m.ListAlertsItem],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listAlerts"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_alerts_all(
        self, *, query: m.ListAlertsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListAlertsItem]:
        return aiterate_pages(
            lambda marker: self.list_alerts(
                query=cast(m.ListAlertsQuery, {**(query or {}), "marker": marker}), options=options
            ),
            (query or {}).get("marker", ""),
        )

    async def list_log_groups(
        self, *, query: m.ListLogGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> Page[m.ListLogGroupsResponse, m.ListLogGroupsItem]:
        "List log groups (or look up one by name)"
        return cast(
            Page[m.ListLogGroupsResponse, m.ListLogGroupsItem],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listLogGroups"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_log_groups_all(
        self, *, query: m.ListLogGroupsQuery | None = None, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListLogGroupsItem]:
        return aiterate_pages(
            lambda marker: self.list_log_groups(
                query=cast(m.ListLogGroupsQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_metric_names(
        self, *, query: m.ListMetricNamesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListMetricNamesResponse, m.ListMetricNamesItem]:
        "List metric names"
        return cast(
            Page[m.ListMetricNamesResponse, m.ListMetricNamesItem],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricNames"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_metric_names_all(
        self, *, query: m.ListMetricNamesQuery, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListMetricNamesItem]:
        return aiterate_pages(
            lambda marker: self.list_metric_names(
                query=cast(m.ListMetricNamesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_metric_names_post(
        self, body: m.ListMetricNamesPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ListMetricNamesPostResponse]:
        "List metric names (JSON)"
        return cast(
            ApiResponse[m.ListMetricNamesPostResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricNamesPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def list_metric_series(
        self, *, query: m.ListMetricSeriesQuery, options: RequestOptions | None = None
    ) -> Page[m.ListMetricSeriesResponse, m.ListMetricSeriesItem]:
        "List metric series"
        return cast(
            Page[m.ListMetricSeriesResponse, m.ListMetricSeriesItem],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricSeries"],
                "page",
                {},
                UNSET,
                query,
                options,
            ),
        )

    def list_metric_series_all(
        self, *, query: m.ListMetricSeriesQuery, options: RequestOptions | None = None
    ) -> AsyncIterator[m.ListMetricSeriesItem]:
        return aiterate_pages(
            lambda marker: self.list_metric_series(
                query=cast(m.ListMetricSeriesQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def list_metric_series_post(
        self, body: m.ListMetricSeriesPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.ListMetricSeriesPostResponse]:
        "List metric series (JSON)"
        return cast(
            ApiResponse[m.ListMetricSeriesPostResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listMetricSeriesPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def list_trace_spans(
        self,
        trace_id: str,
        *,
        query: m.ListTraceSpansQuery | None = None,
        options: RequestOptions | None = None,
    ) -> Page[m.ListTraceSpansResponse, m.ListTraceSpansItem]:
        "List spans in a trace"
        return cast(
            Page[m.ListTraceSpansResponse, m.ListTraceSpansItem],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["listTraceSpans"],
                "page",
                {"trace_id": trace_id},
                UNSET,
                query,
                options,
            ),
        )

    def list_trace_spans_all(
        self,
        trace_id: str,
        *,
        query: m.ListTraceSpansQuery | None = None,
        options: RequestOptions | None = None,
    ) -> AsyncIterator[m.ListTraceSpansItem]:
        return aiterate_pages(
            lambda marker: self.list_trace_spans(
                trace_id,
                query=cast(m.ListTraceSpansQuery, {**(query or {}), "marker": marker}),
                options=options,
            ),
            (query or {}).get("marker", ""),
        )

    async def query_metrics_instant(
        self, *, query: m.QueryMetricsInstantQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsInstantResponse]:
        "Run an instant metric query"
        return cast(
            ApiResponse[m.QueryMetricsInstantResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsInstant"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def query_metrics_instant_post(
        self, body: m.QueryMetricsInstantPostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsInstantPostResponse]:
        "Run an instant metric query (JSON)"
        return cast(
            ApiResponse[m.QueryMetricsInstantPostResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsInstantPost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def query_metrics_range(
        self, *, query: m.QueryMetricsRangeQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsRangeResponse]:
        "Run a range metric query"
        return cast(
            ApiResponse[m.QueryMetricsRangeResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsRange"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def query_metrics_range_post(
        self, body: m.QueryMetricsRangePostBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.QueryMetricsRangePostResponse]:
        "Run a range metric query (JSON)"
        return cast(
            ApiResponse[m.QueryMetricsRangePostResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["queryMetricsRangePost"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def search_logs(
        self, *, query: m.SearchLogsQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.SearchLogsResponse]:
        "Search log records"
        return cast(
            ApiResponse[m.SearchLogsResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["searchLogs"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def search_traces(
        self, *, query: m.SearchTracesQuery, options: RequestOptions | None = None
    ) -> ApiResponse[m.SearchTracesResponse]:
        "List traces"
        return cast(
            ApiResponse[m.SearchTracesResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["searchTraces"],
                "json",
                {},
                UNSET,
                query,
                options,
            ),
        )

    async def update_alert(
        self, id: str, body: m.UpdateAlertBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateAlertResponse]:
        "Update a metric alert"
        return cast(
            ApiResponse[m.UpdateAlertResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateAlert"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    async def update_log_group(
        self, id: str, body: m.UpdateLogGroupBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateLogGroupResponse]:
        "Update a log group"
        return cast(
            ApiResponse[m.UpdateLogGroupResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateLogGroup"],
                "json",
                {"id": id},
                body,
                None,
                options,
            ),
        )

    async def update_trace_settings(
        self, body: m.UpdateTraceSettingsBody, *, options: RequestOptions | None = None
    ) -> ApiResponse[m.UpdateTraceSettingsResponse]:
        "Update the caller account's trace settings"
        return cast(
            ApiResponse[m.UpdateTraceSettingsResponse],
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["updateTraceSettings"],
                "json",
                {},
                body,
                None,
                options,
            ),
        )

    async def write_metrics(
        self, body: AsyncBinaryBody, *, options: RequestOptions | None = None
    ) -> None:
        "Prometheus remote_write ingest"
        return cast(
            None,
            await self._transport.request(
                "telemetry",
                "https://telemetry.{region}.basaltic.sh",
                _OPS["writeMetrics"],
                "discard",
                {},
                body,
                None,
                options,
            ),
        )
