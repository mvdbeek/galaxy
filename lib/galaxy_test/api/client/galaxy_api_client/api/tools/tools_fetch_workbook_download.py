from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.tools_fetch_workbook_download_collection_type import ToolsFetchWorkbookDownloadCollectionType
from ...models.tools_fetch_workbook_download_workbook_type import ToolsFetchWorkbookDownloadWorkbookType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: ToolsFetchWorkbookDownloadWorkbookType | Unset = ToolsFetchWorkbookDownloadWorkbookType.DATASETS,
    collection_type: ToolsFetchWorkbookDownloadCollectionType | Unset = ToolsFetchWorkbookDownloadCollectionType.LIST,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_collection_type: str | Unset = UNSET
    if not isinstance(collection_type, Unset):
        json_collection_type = collection_type.value

    params["collection_type"] = json_collection_type

    json_filename: None | str | Unset
    if isinstance(filename, Unset):
        json_filename = UNSET
    else:
        json_filename = filename
    params["filename"] = json_filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tools/fetch/workbook",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    type_: ToolsFetchWorkbookDownloadWorkbookType | Unset = ToolsFetchWorkbookDownloadWorkbookType.DATASETS,
    collection_type: ToolsFetchWorkbookDownloadCollectionType | Unset = ToolsFetchWorkbookDownloadCollectionType.LIST,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Generate a template workbook to use with the activity builder UI

    Args:
        type_ (ToolsFetchWorkbookDownloadWorkbookType | Unset): Generate a workbook for simple
            datasets or a collection. Default: ToolsFetchWorkbookDownloadWorkbookType.DATASETS.
        collection_type (ToolsFetchWorkbookDownloadCollectionType | Unset): Generate workbook for
            specified collection type (not all collection types are supported) Default:
            ToolsFetchWorkbookDownloadCollectionType.LIST.
        filename (None | str | Unset): Filename of the workbook download to generate
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        type_=type_,
        collection_type=collection_type,
        filename=filename,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    type_: ToolsFetchWorkbookDownloadWorkbookType | Unset = ToolsFetchWorkbookDownloadWorkbookType.DATASETS,
    collection_type: ToolsFetchWorkbookDownloadCollectionType | Unset = ToolsFetchWorkbookDownloadCollectionType.LIST,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Generate a template workbook to use with the activity builder UI

    Args:
        type_ (ToolsFetchWorkbookDownloadWorkbookType | Unset): Generate a workbook for simple
            datasets or a collection. Default: ToolsFetchWorkbookDownloadWorkbookType.DATASETS.
        collection_type (ToolsFetchWorkbookDownloadCollectionType | Unset): Generate workbook for
            specified collection type (not all collection types are supported) Default:
            ToolsFetchWorkbookDownloadCollectionType.LIST.
        filename (None | str | Unset): Filename of the workbook download to generate
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        type_=type_,
        collection_type=collection_type,
        filename=filename,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    type_: ToolsFetchWorkbookDownloadWorkbookType | Unset = ToolsFetchWorkbookDownloadWorkbookType.DATASETS,
    collection_type: ToolsFetchWorkbookDownloadCollectionType | Unset = ToolsFetchWorkbookDownloadCollectionType.LIST,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Generate a template workbook to use with the activity builder UI

    Args:
        type_ (ToolsFetchWorkbookDownloadWorkbookType | Unset): Generate a workbook for simple
            datasets or a collection. Default: ToolsFetchWorkbookDownloadWorkbookType.DATASETS.
        collection_type (ToolsFetchWorkbookDownloadCollectionType | Unset): Generate workbook for
            specified collection type (not all collection types are supported) Default:
            ToolsFetchWorkbookDownloadCollectionType.LIST.
        filename (None | str | Unset): Filename of the workbook download to generate
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        type_=type_,
        collection_type=collection_type,
        filename=filename,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    type_: ToolsFetchWorkbookDownloadWorkbookType | Unset = ToolsFetchWorkbookDownloadWorkbookType.DATASETS,
    collection_type: ToolsFetchWorkbookDownloadCollectionType | Unset = ToolsFetchWorkbookDownloadCollectionType.LIST,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Generate a template workbook to use with the activity builder UI

    Args:
        type_ (ToolsFetchWorkbookDownloadWorkbookType | Unset): Generate a workbook for simple
            datasets or a collection. Default: ToolsFetchWorkbookDownloadWorkbookType.DATASETS.
        collection_type (ToolsFetchWorkbookDownloadCollectionType | Unset): Generate workbook for
            specified collection type (not all collection types are supported) Default:
            ToolsFetchWorkbookDownloadCollectionType.LIST.
        filename (None | str | Unset): Filename of the workbook download to generate
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            collection_type=collection_type,
            filename=filename,
            run_as=run_as,
        )
    ).parsed
