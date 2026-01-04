from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_contents_index_dataset_response import LibraryContentsIndexDatasetResponse
from ...models.library_contents_index_folder_response import LibraryContentsIndexFolderResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/libraries/{library_id}/contents".format(
            library_id=quote(str(library_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_library_contents_index_list_response_item_data in _response_200:

            def _parse_componentsschemas_library_contents_index_list_response_item(
                data: object,
            ) -> LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_library_contents_index_list_response_item_type_0 = (
                        LibraryContentsIndexFolderResponse.from_dict(data)
                    )

                    return componentsschemas_library_contents_index_list_response_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_library_contents_index_list_response_item_type_1 = (
                    LibraryContentsIndexDatasetResponse.from_dict(data)
                )

                return componentsschemas_library_contents_index_list_response_item_type_1

            componentsschemas_library_contents_index_list_response_item = (
                _parse_componentsschemas_library_contents_index_list_response_item(
                    componentsschemas_library_contents_index_list_response_item_data
                )
            )

            response_200.append(componentsschemas_library_contents_index_list_response_item)

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
) -> Response[MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]]:
    """Return a list of library files and folders.

     This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse] | None:
    """Return a list of library files and folders.

     This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]
    """

    return sync_detailed(
        library_id=library_id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]]:
    """Return a list of library files and folders.

     This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse] | None:
    """Return a list of library files and folders.

     This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[LibraryContentsIndexDatasetResponse | LibraryContentsIndexFolderResponse]
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            client=client,
            run_as=run_as,
        )
    ).parsed
