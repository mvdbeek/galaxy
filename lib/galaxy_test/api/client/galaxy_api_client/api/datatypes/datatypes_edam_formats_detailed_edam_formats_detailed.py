from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.datatypes_edam_details_dict import DatatypesEDAMDetailsDict
from ...models.message_exception_model import MessageExceptionModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datatypes/edam_formats/detailed",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatatypesEDAMDetailsDict | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DatatypesEDAMDetailsDict.from_dict(response.json())

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
) -> Response[DatatypesEDAMDetailsDict | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatatypesEDAMDetailsDict | MessageExceptionModel]:
    """Returns a dictionary of datatypes and EDAM format details

     Gets a map of datatypes and their corresponding EDAM formats.
    EDAM formats contain the EDAM iri, label, and definition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatatypesEDAMDetailsDict | MessageExceptionModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> DatatypesEDAMDetailsDict | MessageExceptionModel | None:
    """Returns a dictionary of datatypes and EDAM format details

     Gets a map of datatypes and their corresponding EDAM formats.
    EDAM formats contain the EDAM iri, label, and definition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatatypesEDAMDetailsDict | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[DatatypesEDAMDetailsDict | MessageExceptionModel]:
    """Returns a dictionary of datatypes and EDAM format details

     Gets a map of datatypes and their corresponding EDAM formats.
    EDAM formats contain the EDAM iri, label, and definition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatatypesEDAMDetailsDict | MessageExceptionModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> DatatypesEDAMDetailsDict | MessageExceptionModel | None:
    """Returns a dictionary of datatypes and EDAM format details

     Gets a map of datatypes and their corresponding EDAM formats.
    EDAM formats contain the EDAM iri, label, and definition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatatypesEDAMDetailsDict | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
