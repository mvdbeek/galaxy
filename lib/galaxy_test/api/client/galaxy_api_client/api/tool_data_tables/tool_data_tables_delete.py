from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.tool_data_details import ToolDataDetails
from ...models.tool_data_item import ToolDataItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_name: str,
    *,
    body: ToolDataItem,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/tool_data/{table_name}".format(
            table_name=quote(str(table_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ToolDataDetails | None:
    if response.status_code == 200:
        response_200 = ToolDataDetails.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ToolDataDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: ToolDataItem,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolDataDetails]:
    """Removes an item from a data table

     Removes an item from a data table and reloads it to return its updated details.

    Args:
        table_name (str): The name of the tool data table
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ToolDataItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolDataDetails]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: ToolDataItem,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolDataDetails | None:
    """Removes an item from a data table

     Removes an item from a data table and reloads it to return its updated details.

    Args:
        table_name (str): The name of the tool data table
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ToolDataItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolDataDetails
    """

    return sync_detailed(
        table_name=table_name,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: ToolDataItem,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolDataDetails]:
    """Removes an item from a data table

     Removes an item from a data table and reloads it to return its updated details.

    Args:
        table_name (str): The name of the tool data table
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ToolDataItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolDataDetails]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: ToolDataItem,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolDataDetails | None:
    """Removes an item from a data table

     Removes an item from a data table and reloads it to return its updated details.

    Args:
        table_name (str): The name of the tool data table
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ToolDataItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolDataDetails
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
