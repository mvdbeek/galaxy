from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_history_get_chat_history_response_200_item import ChatHistoryGetChatHistoryResponse200Item
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat/history",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChatHistoryGetChatHistoryResponse200Item.from_dict(response_200_item_data)

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
) -> Response[MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]]:
    """Get Chat History

     **Warning**: This API is unstable and may change without notice.

    Args:
        limit (int | Unset): Maximum number of chats to return Default: 50.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item] | None:
    """Get Chat History

     **Warning**: This API is unstable and may change without notice.

    Args:
        limit (int | Unset): Maximum number of chats to return Default: 50.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]]:
    """Get Chat History

     **Warning**: This API is unstable and may change without notice.

    Args:
        limit (int | Unset): Maximum number of chats to return Default: 50.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item] | None:
    """Get Chat History

     **Warning**: This API is unstable and may change without notice.

    Args:
        limit (int | Unset): Maximum number of chats to return Default: 50.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[ChatHistoryGetChatHistoryResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            run_as=run_as,
        )
    ).parsed
