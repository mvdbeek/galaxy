from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_libraries_contents_create_form import BodyLibrariesContentsCreateForm
from ...models.library_contents_create_dataset_response import LibraryContentsCreateDatasetResponse
from ...models.library_contents_create_file_response import LibraryContentsCreateFileResponse
from ...models.library_contents_create_folder_response import LibraryContentsCreateFolderResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: str,
    *,
    body: BodyLibrariesContentsCreateForm,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/libraries/{library_id}/contents".format(
            library_id=quote(str(library_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            LibraryContentsCreateDatasetResponse
            | list[LibraryContentsCreateDatasetResponse]
            | list[LibraryContentsCreateFileResponse]
            | list[LibraryContentsCreateFolderResponse]
        ):
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for componentsschemas_library_contents_create_folder_list_response_item_data in _response_200_type_0:
                    componentsschemas_library_contents_create_folder_list_response_item = (
                        LibraryContentsCreateFolderResponse.from_dict(
                            componentsschemas_library_contents_create_folder_list_response_item_data
                        )
                    )

                    response_200_type_0.append(componentsschemas_library_contents_create_folder_list_response_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = []
                _response_200_type_1 = data
                for componentsschemas_library_contents_create_file_list_response_item_data in _response_200_type_1:
                    componentsschemas_library_contents_create_file_list_response_item = (
                        LibraryContentsCreateFileResponse.from_dict(
                            componentsschemas_library_contents_create_file_list_response_item_data
                        )
                    )

                    response_200_type_1.append(componentsschemas_library_contents_create_file_list_response_item)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_2 = []
                _response_200_type_2 = data
                for (
                    componentsschemas_library_contents_create_dataset_collection_response_item_data
                ) in _response_200_type_2:
                    componentsschemas_library_contents_create_dataset_collection_response_item = (
                        LibraryContentsCreateDatasetResponse.from_dict(
                            componentsschemas_library_contents_create_dataset_collection_response_item_data
                        )
                    )

                    response_200_type_2.append(
                        componentsschemas_library_contents_create_dataset_collection_response_item
                    )

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_3 = LibraryContentsCreateDatasetResponse.from_dict(data)

            return response_200_type_3

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
) -> Response[
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
]:
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
    body: BodyLibrariesContentsCreateForm,
    run_as: None | str | Unset = UNSET,
) -> Response[
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
]:
    """Create a new library file or folder.

     This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
    /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BodyLibrariesContentsCreateForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsCreateDatasetResponse | list[LibraryContentsCreateDatasetResponse] | list[LibraryContentsCreateFileResponse] | list[LibraryContentsCreateFolderResponse] | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        body=body,
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
    body: BodyLibrariesContentsCreateForm,
    run_as: None | str | Unset = UNSET,
) -> (
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
    | None
):
    """Create a new library file or folder.

     This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
    /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BodyLibrariesContentsCreateForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsCreateDatasetResponse | list[LibraryContentsCreateDatasetResponse] | list[LibraryContentsCreateFileResponse] | list[LibraryContentsCreateFolderResponse] | MessageExceptionModel
    """

    return sync_detailed(
        library_id=library_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyLibrariesContentsCreateForm,
    run_as: None | str | Unset = UNSET,
) -> Response[
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
]:
    """Create a new library file or folder.

     This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
    /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BodyLibrariesContentsCreateForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsCreateDatasetResponse | list[LibraryContentsCreateDatasetResponse] | list[LibraryContentsCreateFileResponse] | list[LibraryContentsCreateFolderResponse] | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyLibrariesContentsCreateForm,
    run_as: None | str | Unset = UNSET,
) -> (
    LibraryContentsCreateDatasetResponse
    | list[LibraryContentsCreateDatasetResponse]
    | list[LibraryContentsCreateFileResponse]
    | list[LibraryContentsCreateFolderResponse]
    | MessageExceptionModel
    | None
):
    """Create a new library file or folder.

     This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
    /api/folders/{folder_id}/contents instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (BodyLibrariesContentsCreateForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsCreateDatasetResponse | list[LibraryContentsCreateDatasetResponse] | list[LibraryContentsCreateFileResponse] | list[LibraryContentsCreateFolderResponse] | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
