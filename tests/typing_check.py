"""Static consumer contract. Checked by mypy; never executed against the API."""

from collections.abc import AsyncIterator, Iterator
from typing import assert_type

import httpx

from basaltic import ApiResponse, AsyncClient, Client, Page, RequestOptions
from basaltic.models import compute


def synchronous(client: Client) -> None:
    query: compute.ListInstancesQuery = {"name": "web", "limit": 20}
    assert_type(
        client.compute.list_instances(query=query),
        Page[compute.ListInstancesResponse, compute.ListInstancesItem],
    )
    assert_type(client.compute.list_instances_all(), Iterator[compute.ListInstancesItem])
    assert_type(client.compute.get_instance("id"), ApiResponse[compute.GetInstanceResponse])
    assert_type(client.storage.get_object("bucket", "key"), httpx.Response)
    client.compute.list_instances(query={"limit": "bad"})  # type: ignore[arg-type]
    client.compute.list_instances(query={"unknown": True})  # type: ignore[arg-type]
    client.compute.create_instance({})  # type: ignore[typeddict-item]
    client.compute.get_instance()  # type: ignore[call-arg]
    client.compute.get_instance("id", options=RequestOptions(max_attempts="bad"))  # type: ignore[arg-type]


async def asynchronous(client: AsyncClient) -> None:
    assert_type(await client.compute.get_instance("id"), ApiResponse[compute.GetInstanceResponse])
    assert_type(client.compute.list_instances_all(), AsyncIterator[compute.ListInstancesItem])
    assert_type(await client.storage.get_object("bucket", "key"), httpx.Response)
    async for item in client.compute.list_instances_all():
        assert_type(item, compute.ListInstancesItem)
    async with AsyncClient(access_token="token") as owned:
        assert_type(owned, AsyncClient)
