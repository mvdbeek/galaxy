from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.tool_data_field import ToolDataField
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_name: str,
    field_name: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tool_data/{table_name}/fields/{field_name}".format(
            table_name=quote(str(table_name), safe=""),
            field_name=quote(str(field_name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ToolDataField | None:
    if response.status_code == 200:
        response_200 = ToolDataField.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ToolDataField]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    field_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolDataField]:
    """Get information about a particular field in a tool data table

     Displays information about a data table field.

    Args:
        table_name (str): The name of the tool data table
        field_name (str): The name of the tool data table field
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolDataField]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        field_name=field_name,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_name: str,
    field_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolDataField | None:
    """Get information about a particular field in a tool data table

     Displays information about a data table field.

    Args:
        table_name (str): The name of the tool data table
        field_name (str): The name of the tool data table field
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolDataField
    """

    return sync_detailed(
        table_name=table_name,
        field_name=field_name,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    table_name: str,
    field_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolDataField]:
    """Get information about a particular field in a tool data table

     Displays information about a data table field.

    Args:
        table_name (str): The name of the tool data table
        field_name (str): The name of the tool data table field
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolDataField]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        field_name=field_name,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_name: str,
    field_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolDataField | None:
    """Get information about a particular field in a tool data table

     Displays information about a data table field.

    Args:
        table_name (str): The name of the tool data table
        field_name (str): The name of the tool data table field
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolDataField
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            field_name=field_name,
            client=client,
            run_as=run_as,
        )
    ).parsed
