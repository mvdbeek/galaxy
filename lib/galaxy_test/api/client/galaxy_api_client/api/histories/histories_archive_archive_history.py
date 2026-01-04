from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_history_request_payload import ArchiveHistoryRequestPayload
from ...models.archived_history_detailed import ArchivedHistoryDetailed
from ...models.archived_history_summary import ArchivedHistorySummary
from ...models.custom_archived_history_view import CustomArchivedHistoryView
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    body: ArchiveHistoryRequestPayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/histories/{history_id}/archive".format(
            history_id=quote(str(history_id), safe=""),
        ),
    }

    if isinstance(body, ArchiveHistoryRequestPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CustomArchivedHistoryView.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ArchivedHistoryDetailed.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = ArchivedHistorySummary.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

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
) -> Response[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel]:
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
    body: ArchiveHistoryRequestPayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel]:
    """Archive a history.

     Marks the given history as 'archived' and returns the history.

    Archiving a history will remove it from the list of active histories of the user but it will still
    be
    accessible via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.

    Associating an export record:

    - Optionally, an export record (containing information about a recent snapshot of the history) can
    be associated with the
    archived history by providing an `archive_export_id` in the payload. The export record must belong
    to the history and
    must be in the ready state.
    - When associating an export record, the history can be purged after it has been archived using the
    `purge_history` flag.

    If the history is already archived, this endpoint will return a 409 Conflict error, indicating that
    the history is already archived.
    If the history was not purged after it was archived, you can restore it using the
    `/api/histories/{id}/archive/restore` endpoint.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ArchiveHistoryRequestPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel]
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
    body: ArchiveHistoryRequestPayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel | None:
    """Archive a history.

     Marks the given history as 'archived' and returns the history.

    Archiving a history will remove it from the list of active histories of the user but it will still
    be
    accessible via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.

    Associating an export record:

    - Optionally, an export record (containing information about a recent snapshot of the history) can
    be associated with the
    archived history by providing an `archive_export_id` in the payload. The export record must belong
    to the history and
    must be in the ready state.
    - When associating an export record, the history can be purged after it has been archived using the
    `purge_history` flag.

    If the history is already archived, this endpoint will return a 409 Conflict error, indicating that
    the history is already archived.
    If the history was not purged after it was archived, you can restore it using the
    `/api/histories/{id}/archive/restore` endpoint.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ArchiveHistoryRequestPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel
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
    body: ArchiveHistoryRequestPayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel]:
    """Archive a history.

     Marks the given history as 'archived' and returns the history.

    Archiving a history will remove it from the list of active histories of the user but it will still
    be
    accessible via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.

    Associating an export record:

    - Optionally, an export record (containing information about a recent snapshot of the history) can
    be associated with the
    archived history by providing an `archive_export_id` in the payload. The export record must belong
    to the history and
    must be in the ready state.
    - When associating an export record, the history can be purged after it has been archived using the
    `purge_history` flag.

    If the history is already archived, this endpoint will return a 409 Conflict error, indicating that
    the history is already archived.
    If the history was not purged after it was archived, you can restore it using the
    `/api/histories/{id}/archive/restore` endpoint.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ArchiveHistoryRequestPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel]
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
    body: ArchiveHistoryRequestPayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel | None:
    """Archive a history.

     Marks the given history as 'archived' and returns the history.

    Archiving a history will remove it from the list of active histories of the user but it will still
    be
    accessible via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.

    Associating an export record:

    - Optionally, an export record (containing information about a recent snapshot of the history) can
    be associated with the
    archived history by providing an `archive_export_id` in the payload. The export record must belong
    to the history and
    must be in the ready state.
    - When associating an export record, the history can be purged after it has been archived using the
    `purge_history` flag.

    If the history is already archived, this endpoint will return a 409 Conflict error, indicating that
    the history is already archived.
    If the history was not purged after it was archived, you can restore it using the
    `/api/histories/{id}/archive/restore` endpoint.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ArchiveHistoryRequestPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
