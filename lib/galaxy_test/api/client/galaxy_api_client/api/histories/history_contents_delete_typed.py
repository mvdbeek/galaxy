from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_history_content_payload import DeleteHistoryContentPayload
from ...models.history_content_type import HistoryContentType
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    body: DeleteHistoryContentPayload | Unset = UNSET,
    purge: bool | None | Unset = False,
    recursive: bool | None | Unset = False,
    stop_job: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_purge: bool | None | Unset
    if isinstance(purge, Unset):
        json_purge = UNSET
    else:
        json_purge = purge
    params["purge"] = json_purge

    json_recursive: bool | None | Unset
    if isinstance(recursive, Unset):
        json_recursive = UNSET
    else:
        json_recursive = recursive
    params["recursive"] = json_recursive

    json_stop_job: bool | None | Unset
    if isinstance(stop_job, Unset):
        json_stop_job = UNSET
    else:
        json_stop_job = stop_job
    params["stop_job"] = json_stop_job

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/histories/{history_id}/contents/{type_}s/{id}".format(
            history_id=quote(str(history_id), safe=""),
            type_=quote(str(type_), safe=""),
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteHistoryContentPayload | Unset = UNSET,
    purge: bool | None | Unset = False,
    recursive: bool | None | Unset = False,
    stop_job: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Delete the history content with the given ``ID`` and path specified type.

     Delete the history content with the given ``ID`` and path specified type.

    **Note**: Currently does not stop any active jobs for which this dataset is an output.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        purge (bool | None | Unset): Whether to remove from disk the target HDA or child HDAs of
            the target HDCA. Default: False.
        recursive (bool | None | Unset): When deleting a dataset collection, whether to also
            delete containing datasets. Default: False.
        stop_job (bool | None | Unset): Whether to stop the creating job if all outputs of the job
            have been deleted. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DeleteHistoryContentPayload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        id=id,
        body=body,
        purge=purge,
        recursive=recursive,
        stop_job=stop_job,
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
    body: DeleteHistoryContentPayload | Unset = UNSET,
    purge: bool | None | Unset = False,
    recursive: bool | None | Unset = False,
    stop_job: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Delete the history content with the given ``ID`` and path specified type.

     Delete the history content with the given ``ID`` and path specified type.

    **Note**: Currently does not stop any active jobs for which this dataset is an output.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        purge (bool | None | Unset): Whether to remove from disk the target HDA or child HDAs of
            the target HDCA. Default: False.
        recursive (bool | None | Unset): When deleting a dataset collection, whether to also
            delete containing datasets. Default: False.
        stop_job (bool | None | Unset): Whether to stop the creating job if all outputs of the job
            have been deleted. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DeleteHistoryContentPayload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        type_=type_,
        id=id,
        client=client,
        body=body,
        purge=purge,
        recursive=recursive,
        stop_job=stop_job,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    type_: HistoryContentType,
    id: str,
    *,
    client: AuthenticatedClient,
    body: DeleteHistoryContentPayload | Unset = UNSET,
    purge: bool | None | Unset = False,
    recursive: bool | None | Unset = False,
    stop_job: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Delete the history content with the given ``ID`` and path specified type.

     Delete the history content with the given ``ID`` and path specified type.

    **Note**: Currently does not stop any active jobs for which this dataset is an output.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        purge (bool | None | Unset): Whether to remove from disk the target HDA or child HDAs of
            the target HDCA. Default: False.
        recursive (bool | None | Unset): When deleting a dataset collection, whether to also
            delete containing datasets. Default: False.
        stop_job (bool | None | Unset): Whether to stop the creating job if all outputs of the job
            have been deleted. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DeleteHistoryContentPayload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        id=id,
        body=body,
        purge=purge,
        recursive=recursive,
        stop_job=stop_job,
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
    body: DeleteHistoryContentPayload | Unset = UNSET,
    purge: bool | None | Unset = False,
    recursive: bool | None | Unset = False,
    stop_job: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Delete the history content with the given ``ID`` and path specified type.

     Delete the history content with the given ``ID`` and path specified type.

    **Note**: Currently does not stop any active jobs for which this dataset is an output.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
        purge (bool | None | Unset): Whether to remove from disk the target HDA or child HDAs of
            the target HDCA. Default: False.
        recursive (bool | None | Unset): When deleting a dataset collection, whether to also
            delete containing datasets. Default: False.
        stop_job (bool | None | Unset): Whether to stop the creating job if all outputs of the job
            have been deleted. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DeleteHistoryContentPayload | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            type_=type_,
            id=id,
            client=client,
            body=body,
            purge=purge,
            recursive=recursive,
            stop_job=stop_job,
            run_as=run_as,
        )
    ).parsed
