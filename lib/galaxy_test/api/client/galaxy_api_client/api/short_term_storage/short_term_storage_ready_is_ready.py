from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import Response


def _get_kwargs(
    storage_request_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/short_term_storage/{storage_request_id}/ready".format(
            storage_request_id=quote(str(storage_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
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
) -> Response[MessageExceptionModel | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MessageExceptionModel | bool]:
    """Determine if specified storage request ID is ready for download.

    Args:
        storage_request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | bool]
    """

    kwargs = _get_kwargs(
        storage_request_id=storage_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> MessageExceptionModel | bool | None:
    """Determine if specified storage request ID is ready for download.

    Args:
        storage_request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | bool
    """

    return sync_detailed(
        storage_request_id=storage_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MessageExceptionModel | bool]:
    """Determine if specified storage request ID is ready for download.

    Args:
        storage_request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | bool]
    """

    kwargs = _get_kwargs(
        storage_request_id=storage_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_request_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> MessageExceptionModel | bool | None:
    """Determine if specified storage request ID is ready for download.

    Args:
        storage_request_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | bool
    """

    return (
        await asyncio_detailed(
            storage_request_id=storage_request_id,
            client=client,
        )
    ).parsed
