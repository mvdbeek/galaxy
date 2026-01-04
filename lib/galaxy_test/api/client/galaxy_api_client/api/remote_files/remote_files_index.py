from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.remote_directory import RemoteDirectory
from ...models.remote_file import RemoteFile
from ...models.remote_files_disable_mode import RemoteFilesDisableMode
from ...models.remote_files_format import RemoteFilesFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    target: str | Unset = "ftpdir",
    format_: None | RemoteFilesFormat | Unset = RemoteFilesFormat.URI,
    recursive: bool | None | Unset = UNSET,
    disable: None | RemoteFilesDisableMode | Unset = UNSET,
    writeable: bool | None | Unset = UNSET,
    write_intent: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["target"] = target

    json_format_: None | str | Unset
    if isinstance(format_, Unset):
        json_format_ = UNSET
    elif isinstance(format_, RemoteFilesFormat):
        json_format_ = format_.value
    else:
        json_format_ = format_
    params["format"] = json_format_

    json_recursive: bool | None | Unset
    if isinstance(recursive, Unset):
        json_recursive = UNSET
    else:
        json_recursive = recursive
    params["recursive"] = json_recursive

    json_disable: None | str | Unset
    if isinstance(disable, Unset):
        json_disable = UNSET
    elif isinstance(disable, RemoteFilesDisableMode):
        json_disable = disable.value
    else:
        json_disable = disable
    params["disable"] = json_disable

    json_writeable: bool | None | Unset
    if isinstance(writeable, Unset):
        json_writeable = UNSET
    else:
        json_writeable = writeable
    params["writeable"] = json_writeable

    json_write_intent: bool | None | Unset
    if isinstance(write_intent, Unset):
        json_write_intent = UNSET
    else:
        json_write_intent = write_intent
    params["write_intent"] = json_write_intent

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

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote_files",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile] | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> list[Any] | list[RemoteDirectory | RemoteFile]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for componentsschemas_list_uri_response_item_data in _response_200_type_0:

                    def _parse_componentsschemas_list_uri_response_item(data: object) -> RemoteDirectory | RemoteFile:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_list_uri_response_item_type_0 = RemoteFile.from_dict(data)

                            return componentsschemas_list_uri_response_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_list_uri_response_item_type_1 = RemoteDirectory.from_dict(data)

                        return componentsschemas_list_uri_response_item_type_1

                    componentsschemas_list_uri_response_item = _parse_componentsschemas_list_uri_response_item(
                        componentsschemas_list_uri_response_item_data
                    )

                    response_200_type_0.append(componentsschemas_list_uri_response_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = cast(list[Any], data)

            return response_200_type_1

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
) -> Response[MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target: str | Unset = "ftpdir",
    format_: None | RemoteFilesFormat | Unset = RemoteFilesFormat.URI,
    recursive: bool | None | Unset = UNSET,
    disable: None | RemoteFilesDisableMode | Unset = UNSET,
    writeable: bool | None | Unset = UNSET,
    write_intent: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]]:
    """Displays remote files available to the user.

     Lists all remote files available to the user from different sources.

    The total count of files and directories is returned in the 'total_matches' header.

    Args:
        target (str | Unset): The source to load datasets from. Possible values: ftpdir, userdir,
            importdir Default: 'ftpdir'.
        format_ (None | RemoteFilesFormat | Unset): The requested format of returned data. Either
            `flat` to simply list all the files, `jstree` to get a tree representation of the files,
            or the default `uri` to list files and directories by their URI. Default:
            RemoteFilesFormat.URI.
        recursive (bool | None | Unset): Whether to recursively lists all sub-directories. This
            will be `True` by default depending on the `target`.
        disable (None | RemoteFilesDisableMode | Unset): (This only applies when `format` is
            `jstree`) The value can be either `folders` or `files` and it will disable the
            corresponding nodes of the tree.
        writeable (bool | None | Unset): Deprecated, please use `write_intent` instead.
        write_intent (bool | None | Unset): Whether the query is made with the intention of
            writing to the source. If set to True, only entries that can be written to will be
            returned.
        limit (int | None | Unset): Maximum number of entries to return.
        offset (int | None | Unset): Number of entries to skip.
        query (None | str | Unset): Search query to filter entries by. The syntax could be
            different depending on the target source.
        sort_by (None | str | Unset): Sort the entries by the specified field.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]]
    """

    kwargs = _get_kwargs(
        target=target,
        format_=format_,
        recursive=recursive,
        disable=disable,
        writeable=writeable,
        write_intent=write_intent,
        limit=limit,
        offset=offset,
        query=query,
        sort_by=sort_by,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target: str | Unset = "ftpdir",
    format_: None | RemoteFilesFormat | Unset = RemoteFilesFormat.URI,
    recursive: bool | None | Unset = UNSET,
    disable: None | RemoteFilesDisableMode | Unset = UNSET,
    writeable: bool | None | Unset = UNSET,
    write_intent: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile] | None:
    """Displays remote files available to the user.

     Lists all remote files available to the user from different sources.

    The total count of files and directories is returned in the 'total_matches' header.

    Args:
        target (str | Unset): The source to load datasets from. Possible values: ftpdir, userdir,
            importdir Default: 'ftpdir'.
        format_ (None | RemoteFilesFormat | Unset): The requested format of returned data. Either
            `flat` to simply list all the files, `jstree` to get a tree representation of the files,
            or the default `uri` to list files and directories by their URI. Default:
            RemoteFilesFormat.URI.
        recursive (bool | None | Unset): Whether to recursively lists all sub-directories. This
            will be `True` by default depending on the `target`.
        disable (None | RemoteFilesDisableMode | Unset): (This only applies when `format` is
            `jstree`) The value can be either `folders` or `files` and it will disable the
            corresponding nodes of the tree.
        writeable (bool | None | Unset): Deprecated, please use `write_intent` instead.
        write_intent (bool | None | Unset): Whether the query is made with the intention of
            writing to the source. If set to True, only entries that can be written to will be
            returned.
        limit (int | None | Unset): Maximum number of entries to return.
        offset (int | None | Unset): Number of entries to skip.
        query (None | str | Unset): Search query to filter entries by. The syntax could be
            different depending on the target source.
        sort_by (None | str | Unset): Sort the entries by the specified field.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]
    """

    return sync_detailed(
        client=client,
        target=target,
        format_=format_,
        recursive=recursive,
        disable=disable,
        writeable=writeable,
        write_intent=write_intent,
        limit=limit,
        offset=offset,
        query=query,
        sort_by=sort_by,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target: str | Unset = "ftpdir",
    format_: None | RemoteFilesFormat | Unset = RemoteFilesFormat.URI,
    recursive: bool | None | Unset = UNSET,
    disable: None | RemoteFilesDisableMode | Unset = UNSET,
    writeable: bool | None | Unset = UNSET,
    write_intent: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]]:
    """Displays remote files available to the user.

     Lists all remote files available to the user from different sources.

    The total count of files and directories is returned in the 'total_matches' header.

    Args:
        target (str | Unset): The source to load datasets from. Possible values: ftpdir, userdir,
            importdir Default: 'ftpdir'.
        format_ (None | RemoteFilesFormat | Unset): The requested format of returned data. Either
            `flat` to simply list all the files, `jstree` to get a tree representation of the files,
            or the default `uri` to list files and directories by their URI. Default:
            RemoteFilesFormat.URI.
        recursive (bool | None | Unset): Whether to recursively lists all sub-directories. This
            will be `True` by default depending on the `target`.
        disable (None | RemoteFilesDisableMode | Unset): (This only applies when `format` is
            `jstree`) The value can be either `folders` or `files` and it will disable the
            corresponding nodes of the tree.
        writeable (bool | None | Unset): Deprecated, please use `write_intent` instead.
        write_intent (bool | None | Unset): Whether the query is made with the intention of
            writing to the source. If set to True, only entries that can be written to will be
            returned.
        limit (int | None | Unset): Maximum number of entries to return.
        offset (int | None | Unset): Number of entries to skip.
        query (None | str | Unset): Search query to filter entries by. The syntax could be
            different depending on the target source.
        sort_by (None | str | Unset): Sort the entries by the specified field.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]]
    """

    kwargs = _get_kwargs(
        target=target,
        format_=format_,
        recursive=recursive,
        disable=disable,
        writeable=writeable,
        write_intent=write_intent,
        limit=limit,
        offset=offset,
        query=query,
        sort_by=sort_by,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target: str | Unset = "ftpdir",
    format_: None | RemoteFilesFormat | Unset = RemoteFilesFormat.URI,
    recursive: bool | None | Unset = UNSET,
    disable: None | RemoteFilesDisableMode | Unset = UNSET,
    writeable: bool | None | Unset = UNSET,
    write_intent: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    query: None | str | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile] | None:
    """Displays remote files available to the user.

     Lists all remote files available to the user from different sources.

    The total count of files and directories is returned in the 'total_matches' header.

    Args:
        target (str | Unset): The source to load datasets from. Possible values: ftpdir, userdir,
            importdir Default: 'ftpdir'.
        format_ (None | RemoteFilesFormat | Unset): The requested format of returned data. Either
            `flat` to simply list all the files, `jstree` to get a tree representation of the files,
            or the default `uri` to list files and directories by their URI. Default:
            RemoteFilesFormat.URI.
        recursive (bool | None | Unset): Whether to recursively lists all sub-directories. This
            will be `True` by default depending on the `target`.
        disable (None | RemoteFilesDisableMode | Unset): (This only applies when `format` is
            `jstree`) The value can be either `folders` or `files` and it will disable the
            corresponding nodes of the tree.
        writeable (bool | None | Unset): Deprecated, please use `write_intent` instead.
        write_intent (bool | None | Unset): Whether the query is made with the intention of
            writing to the source. If set to True, only entries that can be written to will be
            returned.
        limit (int | None | Unset): Maximum number of entries to return.
        offset (int | None | Unset): Number of entries to skip.
        query (None | str | Unset): Search query to filter entries by. The syntax could be
            different depending on the target source.
        sort_by (None | str | Unset): Sort the entries by the specified field.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[Any] | list[RemoteDirectory | RemoteFile]
    """

    return (
        await asyncio_detailed(
            client=client,
            target=target,
            format_=format_,
            recursive=recursive,
            disable=disable,
            writeable=writeable,
            write_intent=write_intent,
            limit=limit,
            offset=offset,
            query=query,
            sort_by=sort_by,
            run_as=run_as,
        )
    ).parsed
