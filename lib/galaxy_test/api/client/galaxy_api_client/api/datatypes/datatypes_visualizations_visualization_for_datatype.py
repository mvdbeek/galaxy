from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.datatype_visualization_mapping import DatatypeVisualizationMapping
from ...models.message_exception_model import MessageExceptionModel
from ...types import Response


def _get_kwargs(
    datatype: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datatypes/{datatype}/visualizations".format(
            datatype=quote(str(datatype), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[DatatypeVisualizationMapping] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_datatype_visualization_mappings_list_item_data in _response_200:
            componentsschemas_datatype_visualization_mappings_list_item = DatatypeVisualizationMapping.from_dict(
                componentsschemas_datatype_visualization_mappings_list_item_data
            )

            response_200.append(componentsschemas_datatype_visualization_mappings_list_item)

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
) -> Response[MessageExceptionModel | list[DatatypeVisualizationMapping]]:
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
) -> Response[MessageExceptionModel | list[DatatypeVisualizationMapping]]:
    """Returns the visualization mapping for a specific datatype

     Gets the visualization mapping for a specific datatype.

    Mappings are defined in the datatypes_conf.xml configuration file.

    Args:
        datatype (str): Datatype extension to get visualization mapping for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[DatatypeVisualizationMapping]]
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
) -> MessageExceptionModel | list[DatatypeVisualizationMapping] | None:
    """Returns the visualization mapping for a specific datatype

     Gets the visualization mapping for a specific datatype.

    Mappings are defined in the datatypes_conf.xml configuration file.

    Args:
        datatype (str): Datatype extension to get visualization mapping for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[DatatypeVisualizationMapping]
    """

    return sync_detailed(
        datatype=datatype,
        client=client,
    ).parsed


async def asyncio_detailed(
    datatype: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MessageExceptionModel | list[DatatypeVisualizationMapping]]:
    """Returns the visualization mapping for a specific datatype

     Gets the visualization mapping for a specific datatype.

    Mappings are defined in the datatypes_conf.xml configuration file.

    Args:
        datatype (str): Datatype extension to get visualization mapping for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[DatatypeVisualizationMapping]]
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
) -> MessageExceptionModel | list[DatatypeVisualizationMapping] | None:
    """Returns the visualization mapping for a specific datatype

     Gets the visualization mapping for a specific datatype.

    Mappings are defined in the datatypes_conf.xml configuration file.

    Args:
        datatype (str): Datatype extension to get visualization mapping for

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[DatatypeVisualizationMapping]
    """

    return (
        await asyncio_detailed(
            datatype=datatype,
            client=client,
        )
    ).parsed
