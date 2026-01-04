from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.histories_exports_index_exports_accept import HistoriesExportsIndexExportsAccept
from ...models.job_export_history_archive_model import JobExportHistoryArchiveModel
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    accept: HistoriesExportsIndexExportsAccept | Unset = HistoriesExportsIndexExportsAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = str(accept)

    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories/{history_id}/exports".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[JobExportHistoryArchiveModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_job_export_history_archive_list_response_item_data in _response_200:
            componentsschemas_job_export_history_archive_list_response_item = JobExportHistoryArchiveModel.from_dict(
                componentsschemas_job_export_history_archive_list_response_item_data
            )

            response_200.append(componentsschemas_job_export_history_archive_list_response_item)

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
) -> Response[MessageExceptionModel | list[JobExportHistoryArchiveModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    accept: HistoriesExportsIndexExportsAccept | Unset = HistoriesExportsIndexExportsAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobExportHistoryArchiveModel]]:
    """Get previous history exports.

     By default the legacy job-based history exports (jeha) are returned.

    Change the `accept` content type header to return the new task-based history exports.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        accept (HistoriesExportsIndexExportsAccept | Unset): Accept header to determine the
            response format. Default is 'application/json'. Default:
            HistoriesExportsIndexExportsAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobExportHistoryArchiveModel]]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        limit=limit,
        offset=offset,
        accept=accept,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    accept: HistoriesExportsIndexExportsAccept | Unset = HistoriesExportsIndexExportsAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobExportHistoryArchiveModel] | None:
    """Get previous history exports.

     By default the legacy job-based history exports (jeha) are returned.

    Change the `accept` content type header to return the new task-based history exports.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        accept (HistoriesExportsIndexExportsAccept | Unset): Accept header to determine the
            response format. Default is 'application/json'. Default:
            HistoriesExportsIndexExportsAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobExportHistoryArchiveModel]
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        limit=limit,
        offset=offset,
        accept=accept,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    accept: HistoriesExportsIndexExportsAccept | Unset = HistoriesExportsIndexExportsAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobExportHistoryArchiveModel]]:
    """Get previous history exports.

     By default the legacy job-based history exports (jeha) are returned.

    Change the `accept` content type header to return the new task-based history exports.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        accept (HistoriesExportsIndexExportsAccept | Unset): Accept header to determine the
            response format. Default is 'application/json'. Default:
            HistoriesExportsIndexExportsAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobExportHistoryArchiveModel]]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        limit=limit,
        offset=offset,
        accept=accept,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    accept: HistoriesExportsIndexExportsAccept | Unset = HistoriesExportsIndexExportsAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobExportHistoryArchiveModel] | None:
    """Get previous history exports.

     By default the legacy job-based history exports (jeha) are returned.

    Change the `accept` content type header to return the new task-based history exports.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        accept (HistoriesExportsIndexExportsAccept | Unset): Accept header to determine the
            response format. Default is 'application/json'. Default:
            HistoriesExportsIndexExportsAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobExportHistoryArchiveModel]
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            limit=limit,
            offset=offset,
            accept=accept,
            run_as=run_as,
        )
    ).parsed
