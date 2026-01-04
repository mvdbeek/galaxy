from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.history_content_type import HistoryContentType
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories/{history_id}/contents/{type_}s/{id}/jobs_summary".format(
            history_id=quote(str(history_id), safe=""),
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageExceptionModel | None:
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
) -> Response[MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Return detailed information about an `HDA` or `HDCAs` jobs.

     Return detailed information about an `HDA` or `HDCAs` jobs.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        id=id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Return detailed information about an `HDA` or `HDCAs` jobs.

     Return detailed information about an `HDA` or `HDCAs` jobs.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        type_=type_,
        id=id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Return detailed information about an `HDA` or `HDCAs` jobs.

     Return detailed information about an `HDA` or `HDCAs` jobs.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        id=id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Return detailed information about an `HDA` or `HDCAs` jobs.

     Return detailed information about an `HDA` or `HDCAs` jobs.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            type_=type_,
            id=id,
            client=client,
            run_as=run_as,
        )
    ).parsed
