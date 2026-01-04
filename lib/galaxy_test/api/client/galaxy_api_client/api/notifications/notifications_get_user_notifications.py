from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_notification_response import UserNotificationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/notifications",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[UserNotificationResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_user_notification_list_response_item_data in _response_200:
            componentsschemas_user_notification_list_response_item = UserNotificationResponse.from_dict(
                componentsschemas_user_notification_list_response_item_data
            )

            response_200.append(componentsschemas_user_notification_list_response_item)

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
) -> Response[MessageExceptionModel | list[UserNotificationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[UserNotificationResponse]]:
    """Returns the list of notifications associated with the user.

     Anonymous users cannot receive personal notifications, only broadcasted notifications.

    You can use the `limit` and `offset` parameters to paginate through the notifications.

    Args:
        limit (int | None | Unset):  Default: 20.
        offset (int | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[UserNotificationResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[UserNotificationResponse] | None:
    """Returns the list of notifications associated with the user.

     Anonymous users cannot receive personal notifications, only broadcasted notifications.

    You can use the `limit` and `offset` parameters to paginate through the notifications.

    Args:
        limit (int | None | Unset):  Default: 20.
        offset (int | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[UserNotificationResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[UserNotificationResponse]]:
    """Returns the list of notifications associated with the user.

     Anonymous users cannot receive personal notifications, only broadcasted notifications.

    You can use the `limit` and `offset` parameters to paginate through the notifications.

    Args:
        limit (int | None | Unset):  Default: 20.
        offset (int | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[UserNotificationResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[UserNotificationResponse] | None:
    """Returns the list of notifications associated with the user.

     Anonymous users cannot receive personal notifications, only broadcasted notifications.

    You can use the `limit` and `offset` parameters to paginate through the notifications.

    Args:
        limit (int | None | Unset):  Default: 20.
        offset (int | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[UserNotificationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            run_as=run_as,
        )
    ).parsed
