from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.import_tool_data_bundle import ImportToolDataBundle
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ImportToolDataBundle,
    tool_data_file_path: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_tool_data_file_path: None | str | Unset
    if isinstance(tool_data_file_path, Unset):
        json_tool_data_file_path = UNSET
    else:
        json_tool_data_file_path = tool_data_file_path
    params["tool_data_file_path"] = json_tool_data_file_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tool_data",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = AsyncTaskResultSummary.from_dict(response.json())

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
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportToolDataBundle,
    tool_data_file_path: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Import a data manager bundle

    Args:
        tool_data_file_path (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ImportToolDataBundle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        tool_data_file_path=tool_data_file_path,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ImportToolDataBundle,
    tool_data_file_path: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Import a data manager bundle

    Args:
        tool_data_file_path (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ImportToolDataBundle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        body=body,
        tool_data_file_path=tool_data_file_path,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ImportToolDataBundle,
    tool_data_file_path: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Import a data manager bundle

    Args:
        tool_data_file_path (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ImportToolDataBundle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        tool_data_file_path=tool_data_file_path,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ImportToolDataBundle,
    tool_data_file_path: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Import a data manager bundle

    Args:
        tool_data_file_path (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ImportToolDataBundle):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            tool_data_file_path=tool_data_file_path,
            run_as=run_as,
        )
    ).parsed
