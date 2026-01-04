from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.broadcast_notification_create_request import BroadcastNotificationCreateRequest
from ...models.message_exception_model import MessageExceptionModel
from ...models.notification_created_response import NotificationCreatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BroadcastNotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/notifications/broadcast",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | NotificationCreatedResponse | None:
    if response.status_code == 200:
        response_200 = NotificationCreatedResponse.from_dict(response.json())

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
) -> Response[MessageExceptionModel | NotificationCreatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BroadcastNotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | NotificationCreatedResponse]:
    """Broadcasts a notification to every user in the system.

     Broadcasted notifications are a special kind of notification that are always accessible to all
    users, including anonymous users.
    They are typically used to display important information such as maintenance windows or new
    features.
    These notifications are displayed differently from regular notifications, usually in a banner at the
    top or bottom of the page.

    Broadcasted notifications can include action links that are displayed as buttons.
    This allows users to easily perform tasks such as filling out surveys, accepting legal agreements,
    or accessing new tutorials.

    Some key features of broadcasted notifications include:
    - They are not associated with a specific user, so they cannot be deleted or marked as read.
    - They can be scheduled to be displayed in the future or to expire after a certain time.
    - By default, broadcasted notifications are published immediately and expire six months after
    publication.
    - Only admins can create, edit, reschedule, or expire broadcasted notifications as needed.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BroadcastNotificationCreateRequest): A notification create request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | NotificationCreatedResponse]
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
    body: BroadcastNotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | NotificationCreatedResponse | None:
    """Broadcasts a notification to every user in the system.

     Broadcasted notifications are a special kind of notification that are always accessible to all
    users, including anonymous users.
    They are typically used to display important information such as maintenance windows or new
    features.
    These notifications are displayed differently from regular notifications, usually in a banner at the
    top or bottom of the page.

    Broadcasted notifications can include action links that are displayed as buttons.
    This allows users to easily perform tasks such as filling out surveys, accepting legal agreements,
    or accessing new tutorials.

    Some key features of broadcasted notifications include:
    - They are not associated with a specific user, so they cannot be deleted or marked as read.
    - They can be scheduled to be displayed in the future or to expire after a certain time.
    - By default, broadcasted notifications are published immediately and expire six months after
    publication.
    - Only admins can create, edit, reschedule, or expire broadcasted notifications as needed.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BroadcastNotificationCreateRequest): A notification create request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | NotificationCreatedResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BroadcastNotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | NotificationCreatedResponse]:
    """Broadcasts a notification to every user in the system.

     Broadcasted notifications are a special kind of notification that are always accessible to all
    users, including anonymous users.
    They are typically used to display important information such as maintenance windows or new
    features.
    These notifications are displayed differently from regular notifications, usually in a banner at the
    top or bottom of the page.

    Broadcasted notifications can include action links that are displayed as buttons.
    This allows users to easily perform tasks such as filling out surveys, accepting legal agreements,
    or accessing new tutorials.

    Some key features of broadcasted notifications include:
    - They are not associated with a specific user, so they cannot be deleted or marked as read.
    - They can be scheduled to be displayed in the future or to expire after a certain time.
    - By default, broadcasted notifications are published immediately and expire six months after
    publication.
    - Only admins can create, edit, reschedule, or expire broadcasted notifications as needed.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BroadcastNotificationCreateRequest): A notification create request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | NotificationCreatedResponse]
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
    body: BroadcastNotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | NotificationCreatedResponse | None:
    """Broadcasts a notification to every user in the system.

     Broadcasted notifications are a special kind of notification that are always accessible to all
    users, including anonymous users.
    They are typically used to display important information such as maintenance windows or new
    features.
    These notifications are displayed differently from regular notifications, usually in a banner at the
    top or bottom of the page.

    Broadcasted notifications can include action links that are displayed as buttons.
    This allows users to easily perform tasks such as filling out surveys, accepting legal agreements,
    or accessing new tutorials.

    Some key features of broadcasted notifications include:
    - They are not associated with a specific user, so they cannot be deleted or marked as read.
    - They can be scheduled to be displayed in the future or to expire after a certain time.
    - By default, broadcasted notifications are published immediately and expire six months after
    publication.
    - Only admins can create, edit, reschedule, or expire broadcasted notifications as needed.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BroadcastNotificationCreateRequest): A notification create request specific for
            broadcasting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | NotificationCreatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
