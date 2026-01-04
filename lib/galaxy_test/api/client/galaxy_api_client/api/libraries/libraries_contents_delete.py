from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_contents_delete_payload import LibraryContentsDeletePayload
from ...models.library_contents_delete_response import LibraryContentsDeleteResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: str,
    id: str,
    *,
    body: LibraryContentsDeletePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/libraries/{library_id}/contents/{id}".format(
            library_id=quote(str(library_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, LibraryContentsDeletePayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryContentsDeleteResponse | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = LibraryContentsDeleteResponse.from_dict(response.json())

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
) -> Response[LibraryContentsDeleteResponse | MessageExceptionModel]:
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
    body: LibraryContentsDeletePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryContentsDeleteResponse | MessageExceptionModel]:
    """Delete a library file or folder.

     This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryContentsDeletePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsDeleteResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        id=id,
        body=body,
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
    body: LibraryContentsDeletePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryContentsDeleteResponse | MessageExceptionModel | None:
    """Delete a library file or folder.

     This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryContentsDeletePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsDeleteResponse | MessageExceptionModel
    """

    return sync_detailed(
        library_id=library_id,
        id=id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: LibraryContentsDeletePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryContentsDeleteResponse | MessageExceptionModel]:
    """Delete a library file or folder.

     This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryContentsDeletePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryContentsDeleteResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        id=id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body: LibraryContentsDeletePayload | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryContentsDeleteResponse | MessageExceptionModel | None:
    """Delete a library file or folder.

     This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

    Args:
        library_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryContentsDeletePayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryContentsDeleteResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            id=id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
