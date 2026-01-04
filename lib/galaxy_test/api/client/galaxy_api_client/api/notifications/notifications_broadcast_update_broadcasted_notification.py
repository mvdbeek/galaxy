from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.notification_broadcast_update_request import NotificationBroadcastUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    notification_id: str,
    *,
    body: NotificationBroadcastUpdateRequest,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/notifications/broadcast/{notification_id}".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    notification_id: str,
    *,
    client: AuthenticatedClient,
    body: NotificationBroadcastUpdateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Updates the state of a broadcasted notification.

     Only Admins can update broadcasted notifications. This is useful to reschedule, edit or expire
    broadcasted notifications.

    Args:
        notification_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationBroadcastUpdateRequest): A notification update request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_id: str,
    *,
    client: AuthenticatedClient,
    body: NotificationBroadcastUpdateRequest,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Updates the state of a broadcasted notification.

     Only Admins can update broadcasted notifications. This is useful to reschedule, edit or expire
    broadcasted notifications.

    Args:
        notification_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationBroadcastUpdateRequest): A notification update request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        notification_id=notification_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    notification_id: str,
    *,
    client: AuthenticatedClient,
    body: NotificationBroadcastUpdateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Updates the state of a broadcasted notification.

     Only Admins can update broadcasted notifications. This is useful to reschedule, edit or expire
    broadcasted notifications.

    Args:
        notification_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationBroadcastUpdateRequest): A notification update request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_id: str,
    *,
    client: AuthenticatedClient,
    body: NotificationBroadcastUpdateRequest,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Updates the state of a broadcasted notification.

     Only Admins can update broadcasted notifications. This is useful to reschedule, edit or expire
    broadcasted notifications.

    Args:
        notification_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationBroadcastUpdateRequest): A notification update request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
