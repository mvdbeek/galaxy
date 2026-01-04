from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import Response


def _get_kwargs(
    datatype: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datatypes/{datatype}".format(
            datatype=quote(str(datatype), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datatype: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | MessageExceptionModel]:
    """Get details for a specific datatype

     Gets detailed information about a specific datatype.

    Includes information about:
    - Basic properties (description, mime type, etc.)
    - Available converters
    - EDAM mappings
    - Preferred visualization

    Args:
        datatype (str): Datatype extension to get information for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        datatype=datatype,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datatype: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | MessageExceptionModel | None:
    """Get details for a specific datatype

     Gets detailed information about a specific datatype.

    Includes information about:
    - Basic properties (description, mime type, etc.)
    - Available converters
    - EDAM mappings
    - Preferred visualization

    Args:
        datatype (str): Datatype extension to get information for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        datatype=datatype,
        client=client,
    ).parsed


async def asyncio_detailed(
    datatype: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | MessageExceptionModel]:
    """Get details for a specific datatype

     Gets detailed information about a specific datatype.

    Includes information about:
    - Basic properties (description, mime type, etc.)
    - Available converters
    - EDAM mappings
    - Preferred visualization

    Args:
        datatype (str): Datatype extension to get information for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        datatype=datatype,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datatype: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | MessageExceptionModel | None:
    """Get details for a specific datatype

     Gets detailed information about a specific datatype.

    Includes information about:
    - Basic properties (description, mime type, etc.)
    - Available converters
    - EDAM mappings
    - Preferred visualization

    Args:
        datatype (str): Datatype extension to get information for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            datatype=datatype,
            client=client,
        )
    ).parsed
