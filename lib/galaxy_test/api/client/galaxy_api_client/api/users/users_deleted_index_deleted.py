from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.limited_user_model import LimitedUserModel
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_model import UserModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    f_email: None | str | Unset = UNSET,
    f_name: None | str | Unset = UNSET,
    f_any: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_f_email: None | str | Unset
    if isinstance(f_email, Unset):
        json_f_email = UNSET
    else:
        json_f_email = f_email
    params["f_email"] = json_f_email

    json_f_name: None | str | Unset
    if isinstance(f_name, Unset):
        json_f_name = UNSET
    else:
        json_f_name = f_name
    params["f_name"] = json_f_name

    json_f_any: None | str | Unset
    if isinstance(f_any, Unset):
        json_f_any = UNSET
    else:
        json_f_any = f_any
    params["f_any"] = json_f_any

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/deleted",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[LimitedUserModel | UserModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> LimitedUserModel | UserModel:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = UserModel.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = LimitedUserModel.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

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
) -> Response[MessageExceptionModel | list[LimitedUserModel | UserModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    f_email: None | str | Unset = UNSET,
    f_name: None | str | Unset = UNSET,
    f_any: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[LimitedUserModel | UserModel]]:
    """Get Deleted Users

     Return a collection of deleted users. Only admins can see deleted users.

    Args:
        f_email (None | str | Unset): An email address to filter on
        f_name (None | str | Unset): An username address to filter on
        f_any (None | str | Unset): Filter on username OR email
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[LimitedUserModel | UserModel]]
    """

    kwargs = _get_kwargs(
        f_email=f_email,
        f_name=f_name,
        f_any=f_any,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    f_email: None | str | Unset = UNSET,
    f_name: None | str | Unset = UNSET,
    f_any: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[LimitedUserModel | UserModel] | None:
    """Get Deleted Users

     Return a collection of deleted users. Only admins can see deleted users.

    Args:
        f_email (None | str | Unset): An email address to filter on
        f_name (None | str | Unset): An username address to filter on
        f_any (None | str | Unset): Filter on username OR email
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[LimitedUserModel | UserModel]
    """

    return sync_detailed(
        client=client,
        f_email=f_email,
        f_name=f_name,
        f_any=f_any,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    f_email: None | str | Unset = UNSET,
    f_name: None | str | Unset = UNSET,
    f_any: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[LimitedUserModel | UserModel]]:
    """Get Deleted Users

     Return a collection of deleted users. Only admins can see deleted users.

    Args:
        f_email (None | str | Unset): An email address to filter on
        f_name (None | str | Unset): An username address to filter on
        f_any (None | str | Unset): Filter on username OR email
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[LimitedUserModel | UserModel]]
    """

    kwargs = _get_kwargs(
        f_email=f_email,
        f_name=f_name,
        f_any=f_any,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    f_email: None | str | Unset = UNSET,
    f_name: None | str | Unset = UNSET,
    f_any: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[LimitedUserModel | UserModel] | None:
    """Get Deleted Users

     Return a collection of deleted users. Only admins can see deleted users.

    Args:
        f_email (None | str | Unset): An email address to filter on
        f_name (None | str | Unset): An username address to filter on
        f_any (None | str | Unset): Filter on username OR email
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[LimitedUserModel | UserModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            f_email=f_email,
            f_name=f_name,
            f_any=f_any,
            run_as=run_as,
        )
    ).parsed
