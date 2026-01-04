from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.concrete_object_store_model import ConcreteObjectStoreModel
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_store_id: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/object_stores/{object_store_id}".format(
            object_store_id=quote(str(object_store_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConcreteObjectStoreModel | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = ConcreteObjectStoreModel.from_dict(response.json())

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
) -> Response[ConcreteObjectStoreModel | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_store_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[ConcreteObjectStoreModel | MessageExceptionModel]:
    """Get information about a concrete object store configured with Galaxy.

    Args:
        object_store_id (str): The concrete object store ID.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConcreteObjectStoreModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        object_store_id=object_store_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_store_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> ConcreteObjectStoreModel | MessageExceptionModel | None:
    """Get information about a concrete object store configured with Galaxy.

    Args:
        object_store_id (str): The concrete object store ID.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConcreteObjectStoreModel | MessageExceptionModel
    """

    return sync_detailed(
        object_store_id=object_store_id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    object_store_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[ConcreteObjectStoreModel | MessageExceptionModel]:
    """Get information about a concrete object store configured with Galaxy.

    Args:
        object_store_id (str): The concrete object store ID.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConcreteObjectStoreModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        object_store_id=object_store_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_store_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> ConcreteObjectStoreModel | MessageExceptionModel | None:
    """Get information about a concrete object store configured with Galaxy.

    Args:
        object_store_id (str): The concrete object store ID.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConcreteObjectStoreModel | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            object_store_id=object_store_id,
            client=client,
            run_as=run_as,
        )
    ).parsed
