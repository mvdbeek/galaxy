from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_libraries_folders_contents_index_sort_by import DataLibrariesFoldersContentsIndexSortBy
from ...models.library_folder_contents_index_result import LibraryFolderContentsIndexResult
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    folder_id: str,
    *,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    search_text: None | str | Unset = UNSET,
    include_deleted: bool | None | Unset = False,
    order_by: DataLibrariesFoldersContentsIndexSortBy | Unset = DataLibrariesFoldersContentsIndexSortBy.NAME,
    sort_desc: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_search_text: None | str | Unset
    if isinstance(search_text, Unset):
        json_search_text = UNSET
    else:
        json_search_text = search_text
    params["search_text"] = json_search_text

    json_include_deleted: bool | None | Unset
    if isinstance(include_deleted, Unset):
        json_include_deleted = UNSET
    else:
        json_include_deleted = include_deleted
    params["include_deleted"] = json_include_deleted

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_sort_desc: bool | None | Unset
    if isinstance(sort_desc, Unset):
        json_sort_desc = UNSET
    else:
        json_sort_desc = sort_desc
    params["sort_desc"] = json_sort_desc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/folders/{folder_id}/contents".format(
            folder_id=quote(str(folder_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryFolderContentsIndexResult | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = LibraryFolderContentsIndexResult.from_dict(response.json())

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
) -> Response[LibraryFolderContentsIndexResult | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    search_text: None | str | Unset = UNSET,
    include_deleted: bool | None | Unset = False,
    order_by: DataLibrariesFoldersContentsIndexSortBy | Unset = DataLibrariesFoldersContentsIndexSortBy.NAME,
    sort_desc: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderContentsIndexResult | MessageExceptionModel]:
    """Returns a list of a folder's contents (files and sub-folders) with additional metadata about the
    folder.

     Returns a list of a folder's contents (files and sub-folders).

    Additional metadata for the folder is provided in the response as a separate object containing data
    for breadcrumb path building, permissions and other folder's details.

    *Note*: When sorting, folders always have priority (they show-up before any dataset regardless of
    the sorting).

    **Security note**:
    - Accessing a library folder or sub-folder requires only access to the parent library.
    - Deleted folders can only be accessed by admins or users with `MODIFY` permission.
    - Datasets may be public, private or restricted (to a group of users). Listing deleted datasets has
    the same requirements as folders.

    Args:
        folder_id (str):  Example: 0123456789ABCDEF.
        limit (int | Unset): Maximum number of contents to return. Default: 10.
        offset (int | Unset): Return contents from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, contents between position 200-299 will be
            returned. Default: 0.
        search_text (None | str | Unset): Used to filter the contents. Only the folders and files
            which name contains this text will be returned.
        include_deleted (bool | None | Unset): Returns also deleted contents. Deleted contents can
            only be retrieved by Administrators or users with Default: False.
        order_by (DataLibrariesFoldersContentsIndexSortBy | Unset): Sort results by specified
            field. Default: DataLibrariesFoldersContentsIndexSortBy.NAME.
        sort_desc (bool | None | Unset): Sort results in descending order. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderContentsIndexResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        limit=limit,
        offset=offset,
        search_text=search_text,
        include_deleted=include_deleted,
        order_by=order_by,
        sort_desc=sort_desc,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    search_text: None | str | Unset = UNSET,
    include_deleted: bool | None | Unset = False,
    order_by: DataLibrariesFoldersContentsIndexSortBy | Unset = DataLibrariesFoldersContentsIndexSortBy.NAME,
    sort_desc: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderContentsIndexResult | MessageExceptionModel | None:
    """Returns a list of a folder's contents (files and sub-folders) with additional metadata about the
    folder.

     Returns a list of a folder's contents (files and sub-folders).

    Additional metadata for the folder is provided in the response as a separate object containing data
    for breadcrumb path building, permissions and other folder's details.

    *Note*: When sorting, folders always have priority (they show-up before any dataset regardless of
    the sorting).

    **Security note**:
    - Accessing a library folder or sub-folder requires only access to the parent library.
    - Deleted folders can only be accessed by admins or users with `MODIFY` permission.
    - Datasets may be public, private or restricted (to a group of users). Listing deleted datasets has
    the same requirements as folders.

    Args:
        folder_id (str):  Example: 0123456789ABCDEF.
        limit (int | Unset): Maximum number of contents to return. Default: 10.
        offset (int | Unset): Return contents from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, contents between position 200-299 will be
            returned. Default: 0.
        search_text (None | str | Unset): Used to filter the contents. Only the folders and files
            which name contains this text will be returned.
        include_deleted (bool | None | Unset): Returns also deleted contents. Deleted contents can
            only be retrieved by Administrators or users with Default: False.
        order_by (DataLibrariesFoldersContentsIndexSortBy | Unset): Sort results by specified
            field. Default: DataLibrariesFoldersContentsIndexSortBy.NAME.
        sort_desc (bool | None | Unset): Sort results in descending order. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderContentsIndexResult | MessageExceptionModel
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
        limit=limit,
        offset=offset,
        search_text=search_text,
        include_deleted=include_deleted,
        order_by=order_by,
        sort_desc=sort_desc,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    search_text: None | str | Unset = UNSET,
    include_deleted: bool | None | Unset = False,
    order_by: DataLibrariesFoldersContentsIndexSortBy | Unset = DataLibrariesFoldersContentsIndexSortBy.NAME,
    sort_desc: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderContentsIndexResult | MessageExceptionModel]:
    """Returns a list of a folder's contents (files and sub-folders) with additional metadata about the
    folder.

     Returns a list of a folder's contents (files and sub-folders).

    Additional metadata for the folder is provided in the response as a separate object containing data
    for breadcrumb path building, permissions and other folder's details.

    *Note*: When sorting, folders always have priority (they show-up before any dataset regardless of
    the sorting).

    **Security note**:
    - Accessing a library folder or sub-folder requires only access to the parent library.
    - Deleted folders can only be accessed by admins or users with `MODIFY` permission.
    - Datasets may be public, private or restricted (to a group of users). Listing deleted datasets has
    the same requirements as folders.

    Args:
        folder_id (str):  Example: 0123456789ABCDEF.
        limit (int | Unset): Maximum number of contents to return. Default: 10.
        offset (int | Unset): Return contents from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, contents between position 200-299 will be
            returned. Default: 0.
        search_text (None | str | Unset): Used to filter the contents. Only the folders and files
            which name contains this text will be returned.
        include_deleted (bool | None | Unset): Returns also deleted contents. Deleted contents can
            only be retrieved by Administrators or users with Default: False.
        order_by (DataLibrariesFoldersContentsIndexSortBy | Unset): Sort results by specified
            field. Default: DataLibrariesFoldersContentsIndexSortBy.NAME.
        sort_desc (bool | None | Unset): Sort results in descending order. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderContentsIndexResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        limit=limit,
        offset=offset,
        search_text=search_text,
        include_deleted=include_deleted,
        order_by=order_by,
        sort_desc=sort_desc,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    folder_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    search_text: None | str | Unset = UNSET,
    include_deleted: bool | None | Unset = False,
    order_by: DataLibrariesFoldersContentsIndexSortBy | Unset = DataLibrariesFoldersContentsIndexSortBy.NAME,
    sort_desc: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderContentsIndexResult | MessageExceptionModel | None:
    """Returns a list of a folder's contents (files and sub-folders) with additional metadata about the
    folder.

     Returns a list of a folder's contents (files and sub-folders).

    Additional metadata for the folder is provided in the response as a separate object containing data
    for breadcrumb path building, permissions and other folder's details.

    *Note*: When sorting, folders always have priority (they show-up before any dataset regardless of
    the sorting).

    **Security note**:
    - Accessing a library folder or sub-folder requires only access to the parent library.
    - Deleted folders can only be accessed by admins or users with `MODIFY` permission.
    - Datasets may be public, private or restricted (to a group of users). Listing deleted datasets has
    the same requirements as folders.

    Args:
        folder_id (str):  Example: 0123456789ABCDEF.
        limit (int | Unset): Maximum number of contents to return. Default: 10.
        offset (int | Unset): Return contents from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, contents between position 200-299 will be
            returned. Default: 0.
        search_text (None | str | Unset): Used to filter the contents. Only the folders and files
            which name contains this text will be returned.
        include_deleted (bool | None | Unset): Returns also deleted contents. Deleted contents can
            only be retrieved by Administrators or users with Default: False.
        order_by (DataLibrariesFoldersContentsIndexSortBy | Unset): Sort results by specified
            field. Default: DataLibrariesFoldersContentsIndexSortBy.NAME.
        sort_desc (bool | None | Unset): Sort results in descending order. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderContentsIndexResult | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
            limit=limit,
            offset=offset,
            search_text=search_text,
            include_deleted=include_deleted,
            order_by=order_by,
            sort_desc=sort_desc,
            run_as=run_as,
        )
    ).parsed
