from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_contents_show_dataset_response import LibraryContentsShowDatasetResponse
from ...models.library_contents_show_folder_response import LibraryContentsShowFolderResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: str,
    id: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/libraries/{library_id}/contents/{id}".format(
            library_id=quote(str(library_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LibraryContentsShowFolderResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = LibraryContentsShowDatasetResponse.from_dict(data)

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
) -> Response[LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel]:
    """Return a library file or folder.

     This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        id=id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel | None:
    """Return a library file or folder.

     This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel
    """

    return sync_detailed(
        library_id=library_id,
        id=id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel]:
    """Return a library file or folder.

     This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        id=id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel | None:
    """Return a library file or folder.

     This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsShowDatasetResponse | LibraryContentsShowFolderResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            id=id,
            client=client,
            run_as=run_as,
        )
    ).parsed
