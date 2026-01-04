from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.tour_details import TourDetails
from ...types import Response


def _get_kwargs(
    tour_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tours/{tour_id}".format(
            tour_id=quote(str(tour_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | TourDetails | None:
    if response.status_code == 200:
        response_200 = TourDetails.from_dict(response.json())

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
) -> Response[MessageExceptionModel | TourDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tour_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MessageExceptionModel | TourDetails]:
    """Show

     Return a tour definition.

    Args:
        tour_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | TourDetails]
    """

    kwargs = _get_kwargs(
        tour_id=tour_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tour_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MessageExceptionModel | TourDetails | None:
    """Show

     Return a tour definition.

    Args:
        tour_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | TourDetails
    """

    return sync_detailed(
        tour_id=tour_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tour_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MessageExceptionModel | TourDetails]:
    """Show

     Return a tour definition.

    Args:
        tour_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | TourDetails]
    """

    kwargs = _get_kwargs(
        tour_id=tour_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tour_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MessageExceptionModel | TourDetails | None:
    """Show

     Return a tour definition.

    Args:
        tour_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | TourDetails
    """

    return (
        await asyncio_detailed(
            tour_id=tour_id,
            client=client,
        )
    ).parsed
