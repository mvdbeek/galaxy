from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.favorite_object import FavoriteObject
from ...models.favorite_object_type import FavoriteObjectType
from ...models.favorite_objects_summary import FavoriteObjectsSummary
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    object_type: FavoriteObjectType,
    *,
    body: FavoriteObject,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/users/{user_id}/favorites/{object_type}".format(
            user_id=quote(str(user_id), safe=""),
            object_type=quote(str(object_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FavoriteObjectsSummary | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = FavoriteObjectsSummary.from_dict(response.json())

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
) -> Response[FavoriteObjectsSummary | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    object_type: FavoriteObjectType,
    *,
    client: AuthenticatedClient,
    body: FavoriteObject,
    run_as: None | str | Unset = UNSET,
) -> Response[FavoriteObjectsSummary | MessageExceptionModel]:
    """Add the object to user's favorites

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        object_type (FavoriteObjectType):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (FavoriteObject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FavoriteObjectsSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    object_type: FavoriteObjectType,
    *,
    client: AuthenticatedClient,
    body: FavoriteObject,
    run_as: None | str | Unset = UNSET,
) -> FavoriteObjectsSummary | MessageExceptionModel | None:
    """Add the object to user's favorites

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        object_type (FavoriteObjectType):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (FavoriteObject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FavoriteObjectsSummary | MessageExceptionModel
    """

    return sync_detailed(
        user_id=user_id,
        object_type=object_type,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    object_type: FavoriteObjectType,
    *,
    client: AuthenticatedClient,
    body: FavoriteObject,
    run_as: None | str | Unset = UNSET,
) -> Response[FavoriteObjectsSummary | MessageExceptionModel]:
    """Add the object to user's favorites

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        object_type (FavoriteObjectType):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (FavoriteObject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FavoriteObjectsSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        object_type=object_type,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    object_type: FavoriteObjectType,
    *,
    client: AuthenticatedClient,
    body: FavoriteObject,
    run_as: None | str | Unset = UNSET,
) -> FavoriteObjectsSummary | MessageExceptionModel | None:
    """Add the object to user's favorites

    Args:
        user_id (str):  Example: 0123456789ABCDEF.
        object_type (FavoriteObjectType):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (FavoriteObject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FavoriteObjectsSummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            object_type=object_type,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
