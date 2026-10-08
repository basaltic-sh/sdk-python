import asyncio
import concurrent.futures
import json
import os
import unittest
from unittest.mock import patch

import httpx

from basaltic import (
    AmbiguousReferenceError,
    ApiError,
    AsyncClient,
    AuthenticationError,
    Client,
    ClientCredentials,
    Config,
    ProtocolError,
    RequestOptions,
    RequestTimeoutError,
    TransportError,
)
from basaltic._common import UNSET, Operation, prepare, retry_delay


def operation(**changes):
    values = dict(
        id="example",
        method="GET",
        path="/v1/things/{id}",
        authenticated=True,
        requiredQuery=[],
        requiredHeaders=[],
        queryEncoding={},
        bodyRequired=False,
        contentType="application/json",
        accept="application/json",
    )
    return Operation(**dict(values, **changes))


class Bytes(httpx.SyncByteStream):
    def __init__(self, body=b"download", error=None):
        self.body, self.error, self.closed = body, error, False

    def __iter__(self):
        if self.error:
            raise self.error
        yield self.body

    def close(self):
        self.closed = True


class AsyncBytes(httpx.AsyncByteStream):
    def __init__(self, body=b"download", error=None):
        self.body, self.error, self.closed = body, error, False

    async def __aiter__(self):
        if self.error:
            raise self.error
        yield self.body

    async def aclose(self):
        self.closed = True


class ConfigurationTests(unittest.TestCase):
    def test_explicit_keys_override_ambient_token_and_endpoint_prefix(self):
        with patch.dict(
            os.environ,
            {
                "BASALTIC_ACCESS_TOKEN": "ambient",
                "BASALTIC_ENDPOINT_URL_COMPUTE": "https://test.local/api/",
            },
        ):
            c = Config(access_key_id="key", secret_access_key="secret")
        self.assertEqual(c.access_token, "")
        self.assertEqual(c.endpoint("compute", ""), "https://test.local/api")
        self.assertNotIn("secret", repr(c))
        with self.assertRaises(TypeError):
            c.endpoints["compute"] = "https://other.test"

    def test_invalid_configuration_and_request_overrides(self):
        for opts in [
            {"timeout": 0},
            {"timeout": float("nan")},
            {"max_attempts": True},
            {"max_attempts": 11},
            {"domain": "example/path"},
            {"access_token": "bad\ntoken"},
            {"access_token": "nonasciiü"},
            {"endpoints": {"compute": "https://user:password@host"}},
            {"endpoints": {"compute": "https://host?query=1"}},
            {"endpoints": {"compute": "https://host:invalid"}},
        ]:
            with self.subTest(opts=opts), self.assertRaises(ValueError):
                Config(anonymous=True, read_environment=False, **opts)
        with self.assertRaises(ValueError):
            Config(read_environment=False)
        c = Config(access_token="token", read_environment=False)
        with self.assertRaises(ValueError):
            c.endpoint("compute", "https://compute.{region}.basaltic.sh")
        for options in [
            RequestOptions(headers={"Authorization": "custom"}),
            RequestOptions(account_id="account\r\nextra"),
            RequestOptions(idempotency_key="bad\nkey"),
            RequestOptions(headers={"X-Test": "bad\x00"}),
            RequestOptions(timeout=-1),
            RequestOptions(max_attempts=0),
        ]:
            with self.subTest(options=options), self.assertRaises(ValueError):
                prepare(
                    c,
                    "test",
                    "https://example.test",
                    operation(),
                    {"id": "x"},
                    UNSET,
                    None,
                    options,
                )

    def test_wire_shapes_and_required_fields(self):
        c = Config(access_token="token", account_id="a", read_environment=False)
        op = operation(
            requiredQuery=["limit"],
            queryEncoding={"tags": {"explode": False, "style": "pipeDelimited"}},
        )
        p = prepare(
            c,
            "test",
            "https://example.test",
            op,
            {"id": "a/b ?%ü"},
            False,
            {"limit": 0, "enabled": False, "empty": "", "missing": None, "tags": ["a", "b"]},
            RequestOptions(account_id="", timeout=2),
        )
        r = p.request("token")
        self.assertEqual(
            r.url.raw_path,
            b"/v1/things/a%2Fb%20%3F%25%C3%BC?limit=0&enabled=false&empty=&tags=a%7Cb",
        )
        self.assertEqual(r.content, b"false")
        self.assertNotIn("x-account-id", r.headers)
        self.assertEqual(r.extensions["timeout"]["read"], 2)
        for body, expected in [(None, b"null"), ({}, b"{}"), ([], b"[]"), (0, b"0")]:
            self.assertEqual(
                prepare(c, "s", "https://test", operation(), {"id": "x"}, body, None, None)
                .request("")
                .content,
                expected,
            )
        for body in [None, UNSET]:
            with self.assertRaises(ValueError):
                prepare(
                    c,
                    "s",
                    "https://test",
                    operation(bodyRequired=True),
                    {"id": "x"},
                    body,
                    None,
                    None,
                )
        with self.assertRaises(ValueError):
            prepare(c, "s", "https://test", op, {"id": "x"}, UNSET, None, None)
        for id in ["", ".", ".."]:
            with self.assertRaises(ValueError):
                prepare(c, "s", "https://test", operation(), {"id": id}, UNSET, None, None)
        op = operation(
            contentType="application/x-www-form-urlencoded", requiredHeaders=["If-Match"]
        )
        r = prepare(
            c,
            "s",
            "https://test",
            op,
            {"id": "x"},
            {"token": "a+b", "enabled": False},
            None,
            RequestOptions(headers={"if-match": "etag"}),
        ).request("")
        self.assertEqual(r.content, b"token=a%2Bb&enabled=false")
        with self.assertRaises(ValueError):
            prepare(c, "s", "https://test", op, {"id": "x"}, UNSET, None, None)

    def test_retry_after_is_bounded(self):
        c = Config(anonymous=True, read_environment=False, max_delay=20, base_delay=1)
        self.assertEqual(retry_delay(c, 2, "4", 0.5), 4)
        self.assertEqual(retry_delay(c, 2, "Thu, 01 Jan 1970 00:00:10 GMT", 0.5, now=0), 10)
        self.assertEqual(retry_delay(c, 2, "invalid", 0.5), 1)
        self.assertIsNone(retry_delay(c, 2, "21", 0.5))
        self.assertIsNone(retry_delay(c, 2, "9" * 1000, 0.5))


class SyncTests(unittest.TestCase):
    def client(self, handler, **options):
        http = httpx.Client(
            transport=httpx.MockTransport(handler),
            auth=("ambient", "secret"),
            headers={"X-Ambient": "bad"},
            cookies={"ambient": "bad"},
            follow_redirects=True,
        )
        self.addCleanup(http.close)
        return Client(
            http_client=http,
            read_environment=False,
            region="test-1",
            **dict({"access_token": "token", "base_delay": 0}, **options),
        )

    def test_envelopes_safe_injection_and_no_redirect(self):
        requests = []

        def handler(r):
            requests.append(r)
            return httpx.Response(
                200, json={"instance": {"id": "x"}}, headers={"X-Request-Id": "req"}
            )

        c = self.client(handler)
        result = c.compute.get_instance("x")
        self.assertEqual(result.data, {"instance": {"id": "x"}})
        self.assertEqual(result.request_id, "req")
        self.assertTrue(result.response.is_closed)
        self.assertEqual(requests[0].headers["authorization"], "Bearer token")
        for h in ["cookie", "x-ambient"]:
            self.assertNotIn(h, requests[0].headers)
        c.close()
        self.assertFalse(c._http.is_closed)
        d = self.client(
            lambda r: httpx.Response(302, headers={"Location": "https://attacker.test"})
        )
        with self.assertRaises(ApiError) as e:
            d.compute.get_instance("x")
        self.assertEqual(e.exception.status_code, 302)
        owned = Client(access_token="token", read_environment=False)
        owned.close()
        self.assertTrue(owned._http.is_closed)

    def test_retries_only_replayable_requests(self):
        for method, key, expected in [
            ("get", None, 3),
            ("post", None, 1),
            ("post", "stable", 3),
            ("stream", "stable", 1),
        ]:
            calls = []
            streams = []

            def handler(r):
                calls.append(r)
                s = Bytes(b'{"error":{"code":"BUSY"}}')
                streams.append(s)
                return httpx.Response(503, stream=s)

            c = self.client(handler, max_attempts=3)
            with self.subTest(method=method), self.assertRaises(ApiError):
                if method == "get":
                    c.compute.get_instance("x")
                elif method == "stream":
                    c.storage.put_object(
                        "bucket",
                        "key",
                        iter([b"data"]),
                        options=RequestOptions(idempotency_key=key),
                    )
                else:
                    c.compute.create_instance({}, options=RequestOptions(idempotency_key=key))
            self.assertEqual(len(calls), expected)
            self.assertTrue(all(s.closed for s in streams))
            if key:
                self.assertTrue(all(r.headers["Idempotency-Key"] == key for r in calls))
        calls = []
        c = self.client(
            lambda r: calls.append(r) or httpx.Response(429, headers={"Retry-After": "999"})
        )
        with self.assertRaises(ApiError):
            c.compute.get_instance("x")
        self.assertEqual(len(calls), 1)

    def test_transport_errors_read_timeouts_and_redaction(self):
        for error in [httpx.ConnectError("token secret"), httpx.ReadTimeout("token secret")]:
            stream = Bytes(error=error)
            c = self.client(lambda r: httpx.Response(200, stream=stream), max_attempts=1)
            with self.assertRaises(TransportError) as caught:
                c.compute.get_instance("x")
            e = caught.exception
            self.assertNotIn("secret", str(e))
            self.assertIsNone(e.__context__)
            self.assertIsNone(e.__cause__)
            self.assertTrue(stream.closed)
            if isinstance(error, httpx.ReadTimeout):
                self.assertIsInstance(e, RequestTimeoutError)

    def test_protocol_errors_and_api_classifications(self):
        for body in [b"not json", b"null", b"42", b'{"wrong":[]}']:
            c = self.client(lambda r: httpx.Response(200, content=body))
            with self.assertRaises(ProtocolError):
                c.compute.list_instances()
        c = self.client(
            lambda r: httpx.Response(
                403,
                json={"error": {"code": "QUOTA_EXCEEDED", "message": "quota", "request_id": "r"}},
            )
        )
        with self.assertRaises(ApiError) as caught:
            c.compute.get_instance("x")
        e = caught.exception
        self.assertTrue(e.is_quota_exceeded())
        self.assertFalse(e.is_access_denied())
        self.assertEqual(e.operation_id, "getInstance")
        self.assertEqual(e.request_id, "r")
        self.assertFalse(hasattr(e, "request"))

    def test_lazy_pagination_keeps_filters_and_rejects_cycles(self):
        requests = []

        def handler(r):
            requests.append(r)
            return httpx.Response(
                200,
                json={
                    "instances": [{"id": str(len(requests))}],
                    "meta": {"has_more": len(requests) < 2, "marker": "next"},
                },
            )

        c = self.client(handler)
        query = {"name": "web", "limit": 1, "marker": "initial"}
        it = c.compute.list_instances_all(query=query)
        self.assertEqual(len(requests), 0)
        self.assertEqual([x["id"] for x in it], ["1", "2"])
        self.assertEqual([r.url.params["marker"] for r in requests], ["initial", "next"])
        self.assertTrue(all(r.url.params["name"] == "web" for r in requests))
        self.assertEqual(query["marker"], "initial")
        c = self.client(
            lambda r: httpx.Response(
                200, json={"instances": [], "meta": {"has_more": True, "marker": "same"}}
            )
        )
        with self.assertRaises(ProtocolError):
            list(c.compute.list_instances_all())
        c = self.client(
            lambda r: httpx.Response(200, json={"instances": [], "meta": {"has_more": True}})
        )
        with self.assertRaises(ProtocolError):
            list(c.compute.list_instances_all())

    def test_reference_scope_and_ambiguity_without_uuid_fallback(self):
        requests = []
        c = self.client(
            lambda r: requests.append(r) or httpx.Response(200, json={"instances": [{"id": "x"}]})
        )
        self.assertEqual(
            c.compute.get_instance_by_reference("web", scope={"flavor": "small"}).data,
            {"id": "x"},
        )
        self.assertEqual(
            dict(requests[-1].url.params), {"flavor": "small", "name": "web", "limit": "2"}
        )
        for payload, error in [
            ({"instances": []}, ApiError),
            ({"instances": [{}, {}]}, AmbiguousReferenceError),
            ({"instances": [{}], "meta": {"has_more": True}}, AmbiguousReferenceError),
        ]:
            c = self.client(lambda r: httpx.Response(200, json=payload))
            with self.assertRaises(error):
                c.compute.get_instance_by_reference("web")
        requests = []
        c = self.client(lambda r: requests.append(r) or httpx.Response(404))
        with self.assertRaises(ApiError):
            c.compute.get_instance_by_reference("00000000-0000-0000-0000-000000000001")
        self.assertEqual(len(requests), 1)
        self.assertFalse(requests[0].url.query)

    def test_binary_response_ownership_and_websocket_preparation(self):
        stream = Bytes()
        requests = []
        c = self.client(lambda r: requests.append(r) or httpx.Response(200, stream=stream))
        response = c.storage.get_object("bucket", "folder/file")
        self.assertFalse(response.is_closed)
        self.assertFalse(stream.closed)
        self.assertIn(b"folder%2Ffile", requests[0].url.raw_path)
        self.assertEqual(response.read(), b"download")
        response.close()
        self.assertTrue(stream.closed)
        prepared = prepare(
            c.config,
            "compute",
            "https://compute.test",
            operation(path="/v1/socket"),
            {},
            UNSET,
            None,
            None,
        ).websocket("token")
        self.assertEqual(prepared.url, "wss://compute.test/v1/socket")
        self.assertEqual(prepared.headers["Authorization"], "Bearer token")

    def test_oauth_singleflight_expiry_and_stale_invalidation(self):
        calls = []
        now = [0.0]

        def handler(r):
            calls.append(r)
            return httpx.Response(
                200, json={"access_token": "token" + str(len(calls)), "expires_in": 10}
            )

        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            provider = ClientCredentials(
                access_key_id="key",
                secret_access_key="secret",
                token_url="https://auth/token",
                http_client=http,
                clock=lambda: now[0],
            )
            with concurrent.futures.ThreadPoolExecutor(8) as pool:
                self.assertEqual(
                    set(pool.map(lambda _: provider.get_token(), range(20))), {"token1"}
                )
            self.assertEqual(len(calls), 1)
            self.assertEqual(calls[0].content, b"grant_type=client_credentials")
            self.assertEqual(calls[0].headers["Authorization"], "Basic a2V5OnNlY3JldA==")
            now[0] = 9
            self.assertEqual(provider.get_token(), "token2")
            provider.invalidate("token1")
            self.assertEqual(provider.get_token(), "token2")
            provider.invalidate("token2")
            self.assertEqual(provider.get_token(), "token3")

    def test_oauth_rejection_redaction_and_one_refresh(self):
        for payload in [
            {"error": "invalid_client", "error_description": "SECRET"},
            {"access_token": "bad token"},
            {"access_token": "token", "expires_in": False},
            {"access_token": "token", "expires_in": float("inf")},
        ]:
            c = self.client(
                lambda r: httpx.Response(200, content=json.dumps(payload).encode()),
                access_token="",
                access_key_id="key",
                secret_access_key="SECRET",
            )
            with self.assertRaises(AuthenticationError) as caught:
                c.compute.get_instance("x")
            self.assertNotIn("SECRET", str(caught.exception))
            self.assertIsNone(caught.exception.__context__)
        paths = []

        def handler(r):
            paths.append(r.url.path)
            if r.url.path.endswith("/token"):
                return httpx.Response(200, json={"access_token": "token"})
            return httpx.Response(401)

        c = self.client(handler, access_token="", access_key_id="key", secret_access_key="secret")
        with self.assertRaises(ApiError):
            c.compute.get_instance("x")
        self.assertEqual(paths, ["/v1/oauth/token", "/v1/instances/x"] * 2)


class AsyncTests(unittest.IsolatedAsyncioTestCase):
    def client(self, handler, **options):
        http = httpx.AsyncClient(
            transport=httpx.MockTransport(handler),
            auth=("ambient", "secret"),
            cookies={"ambient": "bad"},
        )
        self.addAsyncCleanup(http.aclose)
        return AsyncClient(
            http_client=http,
            read_environment=False,
            region="test-1",
            **dict({"access_token": "token", "base_delay": 0}, **options),
        )

    async def test_async_wire_pagination_and_owned_lifetimes(self):
        requests = []

        async def handler(r):
            requests.append(r)
            return httpx.Response(
                200,
                json={
                    "instances": [{"id": str(len(requests))}],
                    "meta": {"has_more": len(requests) < 2, "marker": "next"},
                },
            )

        c = self.client(handler)
        it = c.compute.list_instances_all(query={"limit": 1})
        self.assertEqual(requests, [])
        self.assertEqual([x["id"] async for x in it], ["1", "2"])
        self.assertEqual(requests[0].headers["authorization"], "Bearer token")
        self.assertNotIn("cookie", requests[0].headers)
        await c.aclose()
        self.assertFalse(c._http.is_closed)
        async with AsyncClient(access_token="token", read_environment=False) as owned:
            self.assertIsInstance(owned, AsyncClient)
        self.assertTrue(owned._http.is_closed)

    async def test_async_retries_authentication_refresh_and_required_forms(self):
        for key, attempts in [(None, 1), ("stable", 3)]:
            calls = []
            c = self.client(lambda r: calls.append(r) or httpx.Response(503), max_attempts=3)
            with self.assertRaises(ApiError):
                await c.compute.create_instance({}, options=RequestOptions(idempotency_key=key))
            self.assertEqual(len(calls), attempts)
        paths = []

        async def handler(request):
            paths.append(request.url.path)
            if request.url.path.endswith("/token"):
                return httpx.Response(200, json={"access_token": "token" + str(len(paths))})
            if len(paths) == 2:
                return httpx.Response(401)
            self.assertEqual(request.headers["Authorization"], "Bearer token3")
            return httpx.Response(200, json={"instance": {"id": "x"}})

        c = self.client(handler, access_token="", access_key_id="key", secret_access_key="secret")
        self.assertEqual((await c.compute.get_instance("x")).data["instance"]["id"], "x")
        self.assertEqual(paths, ["/v1/oauth/token", "/v1/instances/x"] * 2)
        await c.aclose()

    async def test_async_cancellation_during_body_read_closes_stream(self):
        entered = asyncio.Event()

        class WaitingStream(AsyncBytes):
            async def __aiter__(self):
                entered.set()
                await asyncio.Event().wait()
                yield b"never"

        stream = WaitingStream()
        c = self.client(lambda r: httpx.Response(200, stream=stream))
        task = asyncio.create_task(c.compute.get_instance("x"))
        await entered.wait()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertTrue(stream.closed)

    async def test_async_reference_errors_and_binary(self):
        c = self.client(lambda r: httpx.Response(200, json={"instances": [{"id": "x"}]}))
        self.assertEqual((await c.compute.get_instance_by_reference("web")).data, {"id": "x"})
        stream = AsyncBytes()
        c = self.client(lambda r: httpx.Response(200, stream=stream))
        response = await c.storage.get_object("bucket", "key")
        self.assertFalse(stream.closed)
        self.assertEqual(await response.aread(), b"download")
        await response.aclose()
        self.assertTrue(stream.closed)
        stream = AsyncBytes(error=httpx.ReadTimeout("private token"))
        c = self.client(lambda r: httpx.Response(200, stream=stream), max_attempts=1)
        with self.assertRaises(RequestTimeoutError) as caught:
            await c.compute.get_instance("x")
        self.assertIsNone(caught.exception.__context__)
        self.assertTrue(stream.closed)

    async def test_async_retry_cancel_closes_response(self):
        stream = AsyncBytes()
        calls = []
        sleeping = asyncio.Event()
        c = self.client(lambda r: calls.append(r) or httpx.Response(503, stream=stream))

        async def sleep(_):
            sleeping.set()
            await asyncio.Event().wait()

        c._transport.sleep = sleep
        task = asyncio.create_task(c.compute.get_instance("x"))
        await sleeping.wait()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertTrue(stream.closed)
        self.assertEqual(len(calls), 1)

    async def test_async_streaming_upload_is_not_replayed(self):
        calls = []
        c = self.client(lambda r: calls.append(r) or httpx.Response(503))

        async def upload():
            yield b"content"

        with self.assertRaises(ApiError):
            await c.storage.put_object(
                "bucket", "key", upload(), options=RequestOptions(idempotency_key="stable")
            )
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0].content, b"content")

    async def test_async_oauth_singleflight_survives_one_cancelled_waiter(self):
        started = asyncio.Event()
        finish = asyncio.Event()
        calls = []

        async def handler(r):
            calls.append(r)
            started.set()
            await finish.wait()
            return httpx.Response(200, json={"access_token": "shared", "expires_in": 10})

        c = self.client(handler, access_token="", access_key_id="key", secret_access_key="secret")
        provider = c._transport.provider
        first = asyncio.create_task(provider.get_token())
        await started.wait()
        others = [asyncio.create_task(provider.get_token()) for _ in range(10)]
        await asyncio.sleep(0)
        first.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await first
        finish.set()
        self.assertEqual(await asyncio.gather(*others), ["shared"] * 10)
        self.assertEqual(len(calls), 1)
        await c.aclose()

    async def test_async_oauth_shutdown_cancels_pending_exchange(self):
        started = asyncio.Event()
        cancelled = asyncio.Event()

        async def handler(r):
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                cancelled.set()

        c = self.client(handler, access_token="", access_key_id="key", secret_access_key="secret")
        task = asyncio.create_task(c._transport.provider.get_token())
        await started.wait()
        await c.aclose()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertTrue(cancelled.is_set())

    async def test_async_oauth_http_exception_has_no_credential_chain(self):
        async def handler(r):
            raise httpx.ConnectError("SECRET", request=r)

        c = self.client(handler, access_token="", access_key_id="key", secret_access_key="SECRET")
        with self.assertRaises(AuthenticationError) as caught:
            await c.compute.get_instance("x")
        self.assertIsNone(caught.exception.__context__)
        self.assertIsNone(caught.exception.__cause__)
        self.assertNotIn("SECRET", str(caught.exception))
        await c.aclose()


if __name__ == "__main__":
    unittest.main()
