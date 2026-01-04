from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cleanup_storage_items_request import CleanupStorageItemsRequest
from ...models.message_exception_model import MessageExceptionModel
from ...models.storage_items_cleanup_result import StorageItemsCleanupResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CleanupStorageItemsRequest,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/storage/histories",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | StorageItemsCleanupResult | None:
    if response.status_code == 200:
        response_200 = StorageItemsCleanupResult.from_dict(response.json())

        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = MessageExceptionModel.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = MessageExceptionModel.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessageExceptionModel | StorageItemsCleanupResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CleanupStorageItemsRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | StorageItemsCleanupResult]:
    """Purges a set of histories by ID. The histories must be owned by the user.

     **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CleanupStorageItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | StorageItemsCleanupResult]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CleanupStorageItemsRequest,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | StorageItemsCleanupResult | None:
    """Purges a set of histories by ID. The histories must be owned by the user.

     **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CleanupStorageItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | StorageItemsCleanupResult
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CleanupStorageItemsRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | StorageItemsCleanupResult]:
    """Purges a set of histories by ID. The histories must be owned by the user.

     **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CleanupStorageItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | StorageItemsCleanupResult]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CleanupStorageItemsRequest,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | StorageItemsCleanupResult | None:
    """Purges a set of histories by ID. The histories must be owned by the user.

     **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CleanupStorageItemsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | StorageItemsCleanupResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
