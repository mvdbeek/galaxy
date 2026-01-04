from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.stored_item import StoredItem
from ...models.stored_item_order_by import StoredItemOrderBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | StoredItemOrderBy | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    elif isinstance(order, StoredItemOrderBy):
        json_order = order.value
    else:
        json_order = order
    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/storage/histories/discarded",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[StoredItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StoredItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[MessageExceptionModel | list[StoredItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | StoredItemOrderBy | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[StoredItem]]:
    """Returns all discarded histories associated with the given user.

    Args:
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | StoredItemOrderBy | Unset): String containing one of the valid ordering
            attributes followed by '-asc' or '-dsc' for ascending and descending order respectively.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[StoredItem]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | StoredItemOrderBy | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[StoredItem] | None:
    """Returns all discarded histories associated with the given user.

    Args:
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | StoredItemOrderBy | Unset): String containing one of the valid ordering
            attributes followed by '-asc' or '-dsc' for ascending and descending order respectively.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[StoredItem]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | StoredItemOrderBy | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[StoredItem]]:
    """Returns all discarded histories associated with the given user.

    Args:
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | StoredItemOrderBy | Unset): String containing one of the valid ordering
            attributes followed by '-asc' or '-dsc' for ascending and descending order respectively.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[StoredItem]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | StoredItemOrderBy | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[StoredItem] | None:
    """Returns all discarded histories associated with the given user.

    Args:
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | StoredItemOrderBy | Unset): String containing one of the valid ordering
            attributes followed by '-asc' or '-dsc' for ascending and descending order respectively.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[StoredItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            order=order,
            run_as=run_as,
        )
    ).parsed
