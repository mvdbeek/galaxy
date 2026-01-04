from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_user_model import DetailedUserModel
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_deletion_payload import UserDeletionPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    body: None | Unset | UserDeletionPayload = UNSET,
    purge: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["purge"] = purge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/users/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, UserDeletionPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DetailedUserModel | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DetailedUserModel.from_dict(response.json())

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
) -> Response[DetailedUserModel | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserDeletionPayload = UNSET,
    purge: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[DetailedUserModel | MessageExceptionModel]:
    """Delete a user. Only admins can delete others or purge users.

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        purge (bool | Unset): Whether to definitely remove this user. Only deleted users can be
            purged. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (None | Unset | UserDeletionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetailedUserModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        purge=purge,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserDeletionPayload = UNSET,
    purge: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> DetailedUserModel | MessageExceptionModel | None:
    """Delete a user. Only admins can delete others or purge users.

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        purge (bool | Unset): Whether to definitely remove this user. Only deleted users can be
            purged. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (None | Unset | UserDeletionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetailedUserModel | MessageExceptionModel
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
        purge=purge,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserDeletionPayload = UNSET,
    purge: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[DetailedUserModel | MessageExceptionModel]:
    """Delete a user. Only admins can delete others or purge users.

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        purge (bool | Unset): Whether to definitely remove this user. Only deleted users can be
            purged. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (None | Unset | UserDeletionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetailedUserModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        purge=purge,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | UserDeletionPayload = UNSET,
    purge: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> DetailedUserModel | MessageExceptionModel | None:
    """Delete a user. Only admins can delete others or purge users.

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        purge (bool | Unset): Whether to definitely remove this user. Only deleted users can be
            purged. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (None | Unset | UserDeletionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetailedUserModel | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
            purge=purge,
            run_as=run_as,
        )
    ).parsed
