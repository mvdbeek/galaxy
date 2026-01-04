from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_history_archive_payload import ExportHistoryArchivePayload
from ...models.job_export_history_archive_model import JobExportHistoryArchiveModel
from ...models.job_id_response import JobIdResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    body: ExportHistoryArchivePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/histories/{history_id}/exports".format(
            history_id=quote(str(history_id), safe=""),
        ),
    }

    if isinstance(body, ExportHistoryArchivePayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> JobExportHistoryArchiveModel | JobIdResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = JobExportHistoryArchiveModel.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = JobIdResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
) -> Response[Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel]:
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
    body: ExportHistoryArchivePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel]:
    """Start job (if needed) to create history export for corresponding history.

     This will start a job to create a history export archive.

    Calling this endpoint multiple times will return the 202 status code until the archive
    has been completely generated and is ready to download. When ready, it will return
    the 200 status code along with the download link information.

    If the history will be exported to a `directory_uri`, instead of returning the download
    link information, the Job ID will be returned so it can be queried to determine when
    the file has been written.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ExportHistoryArchivePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
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
    body: ExportHistoryArchivePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel | None:
    """Start job (if needed) to create history export for corresponding history.

     This will start a job to create a history export archive.

    Calling this endpoint multiple times will return the 202 status code until the archive
    has been completely generated and is ready to download. When ready, it will return
    the 200 status code along with the download link information.

    If the history will be exported to a `directory_uri`, instead of returning the download
    link information, the Job ID will be returned so it can be queried to determine when
    the file has been written.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ExportHistoryArchivePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: ExportHistoryArchivePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel]:
    """Start job (if needed) to create history export for corresponding history.

     This will start a job to create a history export archive.

    Calling this endpoint multiple times will return the 202 status code until the archive
    has been completely generated and is ready to download. When ready, it will return
    the 200 status code along with the download link information.

    If the history will be exported to a `directory_uri`, instead of returning the download
    link information, the Job ID will be returned so it can be queried to determine when
    the file has been written.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ExportHistoryArchivePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: ExportHistoryArchivePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel | None:
    """Start job (if needed) to create history export for corresponding history.

     This will start a job to create a history export archive.

    Calling this endpoint multiple times will return the 202 status code until the archive
    has been completely generated and is ready to download. When ready, it will return
    the 200 status code along with the download link information.

    If the history will be exported to a `directory_uri`, instead of returning the download
    link information, the Job ID will be returned so it can be queried to determine when
    the file has been written.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ExportHistoryArchivePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JobExportHistoryArchiveModel | JobIdResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
