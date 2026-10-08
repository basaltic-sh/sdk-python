# Basaltic Python SDK

Typed synchronous and asynchronous clients for the Basaltic Cloud API. Python 3.11+
with HTTPX; covers 401 operations across 15 services. Includes typed request and
response dictionaries, access-key authentication, pagination, resource references,
and streamed uploads/downloads.

```sh
pip install basaltic-sdk-python
```

```python
from basaltic import Client

# Reads BASALTIC_ACCESS_KEY_ID, BASALTIC_SECRET_ACCESS_KEY, BASALTIC_REGION
# and optionally BASALTIC_ACCOUNT_ID from the environment.
with Client() as client:
    for instance in client.compute.list_instances_all(query={"limit": 100}):
        print(instance.get("id"), instance.get("name"))
```

```python
import asyncio
from basaltic import AsyncClient

async def main() -> None:
    async with AsyncClient() as client:
        async for instance in client.compute.list_instances_all():
            print(instance.get("id"))

asyncio.run(main())
```

Use one async client per event loop. Requests are native asyncio operations; they
do not run the synchronous client in a background thread. Both clients reuse HTTP
connections and automatically cache access tokens. Concurrent token requests share
one exchange; cancelling an async caller does not cancel another caller's exchange.

## Configuration

Pass configuration as keywords or as a `Config` object:

```python
from basaltic import Client, Config, RequestOptions

config = Config(
    access_key_id="your-access-key-id",
    secret_access_key="your-secret-access-key",
    region="your-region",
    account_id="your-account-id",
    read_environment=False,
)
with Client(config) as client:
    response = client.compute.get_instance(
        "instance-id", options=RequestOptions(timeout=10, max_attempts=2)
    )
    print(response.data["instance"], response.request_id)
```

You may instead supply `access_token` (`BASALTIC_ACCESS_TOKEN`) or a `token_provider`
implementing `get_token() -> str` for `Client`, or `async def get_token() -> str` for
`AsyncClient`. An optional synchronous `invalidate(rejected_token)` enables one
refresh after a 401 response. Explicit key credentials override an ambient bearer
token. `anonymous=True` allows only operations that do not require authentication.

`region`, `account_id`, and `domain` use `BASALTIC_REGION`, `BASALTIC_ACCOUNT_ID`, and
`BASALTIC_DOMAIN` when omitted. Regional services require a region unless overridden.
Use `endpoints={"compute": "https://..."}` or `BASALTIC_ENDPOINT_URL_COMPUTE` for
service endpoints, and `token_url` for a custom OAuth endpoint. Custom endpoints
receive credentials: configure only trusted servers. `read_environment=False`
disables environment configuration. Default clients also disable HTTPX proxy and
certificate environment variables; inject an HTTPX client when those are needed.

`RequestOptions` can override account scope (empty string clears it), timeout,
attempt count, and idempotency key, or add headers such as `If-Match`. Managed
headers including Authorization, Cookie, Host and content type cannot be overridden.
SDK requests do not inherit an injected HTTPX client's default authentication,
cookies, headers, or redirect behavior. Injected clients remain caller-owned.

## Types and responses

Methods use snake_case. JSON dictionary keys retain the API's wire spelling.
Request and response types live in `basaltic.models.<service>` and are `TypedDict`
shapes and type aliases, not runtime model constructors. Pass ordinary dictionaries.
The package includes `py.typed` for mypy and other type checkers.

```python
from basaltic import Client
from basaltic.models.compute import ListInstancesQuery

query: ListInstancesQuery = {"name": "web", "limit": 20}
with Client() as client:
    page = client.compute.list_instances(query=query)
    print(page.items, page.has_more, page.marker)
    print(page.data)  # original JSON envelope, including unknown server fields
    print(page.status_code, page.request_id, page.response.headers)
```

JSON responses are decoded and closed before return. `ApiResponse.data` preserves
the server envelope; it does not coerce dates, UUIDs or enum strings. Types describe
the reviewed API schema; they are not runtime validators. Contentless operations
return `None`. Methods whose successful response can be binary, including HEAD,
return an unread `httpx.Response` which the caller must close.

See [all API methods](https://github.com/basaltic-sh/sdk-python/blob/main/docs/api.md). Services: audit, billing, catalog, certificate,
compute, dns, iam, kms, loadbalancer, network, quota, secrets, storage, telemetry,
and workspace.

## Pagination and references

`list_*_all()` returns a lazy iterator; its async counterpart is an async iterator
and is not itself awaited. Filters and account scope remain unchanged between pages.
A missing or repeated continuation marker raises `ProtocolError` instead of silently
returning incomplete results.

Supported resource getters also provide `get_*_by_reference(reference, scope=...)`.
A UUID calls the getter directly. A CRN or name uses exact-match list filters and
returns an unwrapped resource. No match raises `ApiError`; multiple matches raise
`AmbiguousReferenceError`. Use parent arguments or `scope` to narrow a resource's
workspace or other parent. A failed UUID lookup does not fall back to a name lookup.

## Retries, deadlines and errors

The default is at most four attempts with exponential jitter, starting at 0.2 seconds
and capped at 20 seconds. GET, HEAD, OPTIONS, PUT and DELETE can retry transport errors
and HTTP 429/500/502/503/504. POST and PATCH require an explicit idempotency key for
these retries. Retry-After is honored; a wait above `max_delay` returns the error.
An authentication failure can refresh credentials once within the same attempt limit.
Streaming uploads are attempted once even with an idempotency key.

```python
from basaltic import ApiError, RequestOptions, new_idempotency_key

# Create once per logical mutation, and reuse if your application retries it.
options = RequestOptions(idempotency_key=new_idempotency_key())
# client.compute.create_instance(body, options=options)
```

`timeout` defaults to 30 seconds for each HTTPX connect/read/write/pool phase on
each attempt, including token exchange. It is not a total operation deadline.
Use `asyncio.timeout(seconds)` around an async call for a total deadline including
backoff. Async cancellation propagates without wrapping. Stream reads after return
are owned by the caller and can raise native HTTPX errors.

API errors expose `status_code`, `error_code`, `request_id`, `operation_id`, and
classification helpers such as `is_not_found()`, `is_conflict()`, `is_rate_limited()`
and `is_quota_exceeded()`. `AuthenticationError`, `TransportError`, and
`RequestTimeoutError` redact raw request objects and exception chains. API error
messages and response headers are server data; avoid logging sensitive application
payloads or response objects indiscriminately.

## Streaming and WebSockets

```python
with Client() as client:
    response = client.storage.get_object("bucket", "folder/file")
    try:
        with open("download.bin", "wb") as output:
            for chunk in response.iter_bytes():
                output.write(chunk)
    finally:
        response.close()
```

In async code, use `await get_object(...)`, `async for ... in response.aiter_bytes()`
and `await response.aclose()` in `finally`. Uploads accept bytes, bytearray,
memoryview, or a sync/async iterable of byte chunks appropriate to the client.
Keep an SDK-owned client open while consuming its response streams.

WebSocket methods return `WebSocketConnection(url, headers)`; pass these to your
WebSocket library. They prepare the endpoint and authentication but do not connect
or manage the socket. Connection headers contain credentials and must not be logged.

## Releases and security

This repository contains official release snapshots. We do not accept pull requests
or code contributions. Packages are built from the matching GitHub release tag after
public checks pass, and published to PyPI through GitHub OIDC with attestations.

Report security issues privately to **security@basaltic.sh**; see [SECURITY.md](https://github.com/basaltic-sh/sdk-python/blob/main/SECURITY.md).
Licensed under Apache-2.0.

## Checks

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt -e .
python scripts/check.py
python scripts/check_package.py
```
