from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_folder_details import LibraryFolderDetails
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    undelete: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_undelete: bool | None | Unset
    if isinstance(undelete, Unset):
        json_undelete = UNSET
    else:
        json_undelete = undelete
    params["undelete"] = json_undelete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/folders/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryFolderDetails | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = LibraryFolderDetails.from_dict(response.json())

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
) -> Response[LibraryFolderDetails | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    undelete: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderDetails | MessageExceptionModel]:
    """Marks the specified library folder as deleted (or undeleted).

     Marks the specified library folder as deleted (or undeleted).

    Args:
        id (str):  Example: 0123456789ABCDEF.
        undelete (bool | None | Unset): Whether to restore a deleted library folder.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderDetails | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        undelete=undelete,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    undelete: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderDetails | MessageExceptionModel | None:
    """Marks the specified library folder as deleted (or undeleted).

     Marks the specified library folder as deleted (or undeleted).

    Args:
        id (str):  Example: 0123456789ABCDEF.
        undelete (bool | None | Unset): Whether to restore a deleted library folder.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderDetails | MessageExceptionModel
    """

    return sync_detailed(
        id=id,
        client=client,
        undelete=undelete,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    undelete: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderDetails | MessageExceptionModel]:
    """Marks the specified library folder as deleted (or undeleted).

     Marks the specified library folder as deleted (or undeleted).

    Args:
        id (str):  Example: 0123456789ABCDEF.
        undelete (bool | None | Unset): Whether to restore a deleted library folder.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderDetails | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        undelete=undelete,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    undelete: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderDetails | MessageExceptionModel | None:
    """Marks the specified library folder as deleted (or undeleted).

     Marks the specified library folder as deleted (or undeleted).

    Args:
        id (str):  Example: 0123456789ABCDEF.
        undelete (bool | None | Unset): Whether to restore a deleted library folder.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderDetails | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            undelete=undelete,
            run_as=run_as,
        )
    ).parsed
