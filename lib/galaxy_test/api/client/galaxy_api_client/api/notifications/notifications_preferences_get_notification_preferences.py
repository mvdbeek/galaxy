from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/notifications/preferences",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageExceptionModel | None:
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
) -> Response[MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Returns the current user's preferences for notifications.

     Anonymous users cannot have notification preferences. They will receive only broadcasted
    notifications.

    - The settings will contain all possible channels, but the client should only show the ones that are
    really supported by the server.
      The supported channels are returned in the `supported-channels` header.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Returns the current user's preferences for notifications.

     Anonymous users cannot have notification preferences. They will receive only broadcasted
    notifications.

    - The settings will contain all possible channels, but the client should only show the ones that are
    really supported by the server.
      The supported channels are returned in the `supported-channels` header.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Returns the current user's preferences for notifications.

     Anonymous users cannot have notification preferences. They will receive only broadcasted
    notifications.

    - The settings will contain all possible channels, but the client should only show the ones that are
    really supported by the server.
      The supported channels are returned in the `supported-channels` header.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Returns the current user's preferences for notifications.

     Anonymous users cannot have notification preferences. They will receive only broadcasted
    notifications.

    - The settings will contain all possible channels, but the client should only show the ones that are
    really supported by the server.
      The supported channels are returned in the `supported-channels` header.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            run_as=run_as,
        )
    ).parsed
