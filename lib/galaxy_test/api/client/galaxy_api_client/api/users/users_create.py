from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.created_user_model import CreatedUserModel
from ...models.message_exception_model import MessageExceptionModel
from ...models.remote_user_creation_payload import RemoteUserCreationPayload
from ...models.user_creation_payload import UserCreationPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RemoteUserCreationPayload | UserCreationPayload,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users",
    }

    if isinstance(body, UserCreationPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatedUserModel | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = CreatedUserModel.from_dict(response.json())

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
) -> Response[CreatedUserModel | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RemoteUserCreationPayload | UserCreationPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[CreatedUserModel | MessageExceptionModel]:
    """Create a new Galaxy user. Only admins can create users for now.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RemoteUserCreationPayload | UserCreationPayload): The values to add create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedUserModel | MessageExceptionModel]
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
    body: RemoteUserCreationPayload | UserCreationPayload,
    run_as: None | str | Unset = UNSET,
) -> CreatedUserModel | MessageExceptionModel | None:
    """Create a new Galaxy user. Only admins can create users for now.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RemoteUserCreationPayload | UserCreationPayload): The values to add create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedUserModel | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RemoteUserCreationPayload | UserCreationPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[CreatedUserModel | MessageExceptionModel]:
    """Create a new Galaxy user. Only admins can create users for now.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RemoteUserCreationPayload | UserCreationPayload): The values to add create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedUserModel | MessageExceptionModel]
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
    body: RemoteUserCreationPayload | UserCreationPayload,
    run_as: None | str | Unset = UNSET,
) -> CreatedUserModel | MessageExceptionModel | None:
    """Create a new Galaxy user. Only admins can create users for now.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RemoteUserCreationPayload | UserCreationPayload): The values to add create a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedUserModel | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
