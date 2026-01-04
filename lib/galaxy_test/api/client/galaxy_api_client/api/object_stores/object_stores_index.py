from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concrete_object_store_model import ConcreteObjectStoreModel
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_concrete_object_store_model import UserConcreteObjectStoreModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    selectable: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["selectable"] = selectable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/object_stores",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> ConcreteObjectStoreModel | UserConcreteObjectStoreModel:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = ConcreteObjectStoreModel.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = UserConcreteObjectStoreModel.from_dict(data)

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
) -> Response[MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    selectable: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]:
    """Get a list of (currently only concrete) object stores configured with this Galaxy instance.

    Args:
        selectable (bool | Unset): Restrict index query to user selectable object stores, the
            current implementation requires this to be true. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]
    """

    kwargs = _get_kwargs(
        selectable=selectable,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    selectable: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel] | None:
    """Get a list of (currently only concrete) object stores configured with this Galaxy instance.

    Args:
        selectable (bool | Unset): Restrict index query to user selectable object stores, the
            current implementation requires this to be true. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]
    """

    return sync_detailed(
        client=client,
        selectable=selectable,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    selectable: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]:
    """Get a list of (currently only concrete) object stores configured with this Galaxy instance.

    Args:
        selectable (bool | Unset): Restrict index query to user selectable object stores, the
            current implementation requires this to be true. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]
    """

    kwargs = _get_kwargs(
        selectable=selectable,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    selectable: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel] | None:
    """Get a list of (currently only concrete) object stores configured with this Galaxy instance.

    Args:
        selectable (bool | Unset): Restrict index query to user selectable object stores, the
            current implementation requires this to be true. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            selectable=selectable,
            run_as=run_as,
        )
    ).parsed
