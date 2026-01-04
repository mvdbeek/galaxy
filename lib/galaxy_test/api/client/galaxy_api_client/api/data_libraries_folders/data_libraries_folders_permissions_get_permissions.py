from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_available_permissions import LibraryAvailablePermissions
from ...models.library_folder_current_permissions import LibraryFolderCurrentPermissions
from ...models.library_permission_scope import LibraryPermissionScope
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    scope: LibraryPermissionScope | None | Unset = UNSET,
    page: int | Unset = 1,
    page_limit: int | Unset = 10,
    q: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    elif isinstance(scope, LibraryPermissionScope):
        json_scope = scope.value
    else:
        json_scope = scope
    params["scope"] = json_scope

    params["page"] = page

    params["page_limit"] = page_limit

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/folders/{id}/permissions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> LibraryAvailablePermissions | LibraryFolderCurrentPermissions:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LibraryFolderCurrentPermissions.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = LibraryAvailablePermissions.from_dict(data)

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
) -> Response[LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel]:
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
    scope: LibraryPermissionScope | None | Unset = UNSET,
    page: int | Unset = 1,
    page_limit: int | Unset = 10,
    q: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel]:
    """Gets the current or available permissions of a particular library folder.

     Gets the current or available permissions of a particular library.
    The results can be paginated and additionally filtered by a query.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        scope (LibraryPermissionScope | None | Unset): The scope of the permissions to retrieve.
            Either the `current` permissions or the `available`.
        page (int | Unset): The page number to retrieve when paginating the available roles.
            Default: 1.
        page_limit (int | Unset): The maximum number of permissions per page when paginating.
            Default: 10.
        q (None | str | Unset): Optional search text to retrieve only the roles matching this
            query.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        scope=scope,
        page=page,
        page_limit=page_limit,
        q=q,
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
    scope: LibraryPermissionScope | None | Unset = UNSET,
    page: int | Unset = 1,
    page_limit: int | Unset = 10,
    q: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    """Gets the current or available permissions of a particular library folder.

     Gets the current or available permissions of a particular library.
    The results can be paginated and additionally filtered by a query.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        scope (LibraryPermissionScope | None | Unset): The scope of the permissions to retrieve.
            Either the `current` permissions or the `available`.
        page (int | Unset): The page number to retrieve when paginating the available roles.
            Default: 1.
        page_limit (int | Unset): The maximum number of permissions per page when paginating.
            Default: 10.
        q (None | str | Unset): Optional search text to retrieve only the roles matching this
            query.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel
    """

    return sync_detailed(
        id=id,
        client=client,
        scope=scope,
        page=page,
        page_limit=page_limit,
        q=q,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    scope: LibraryPermissionScope | None | Unset = UNSET,
    page: int | Unset = 1,
    page_limit: int | Unset = 10,
    q: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel]:
    """Gets the current or available permissions of a particular library folder.

     Gets the current or available permissions of a particular library.
    The results can be paginated and additionally filtered by a query.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        scope (LibraryPermissionScope | None | Unset): The scope of the permissions to retrieve.
            Either the `current` permissions or the `available`.
        page (int | Unset): The page number to retrieve when paginating the available roles.
            Default: 1.
        page_limit (int | Unset): The maximum number of permissions per page when paginating.
            Default: 10.
        q (None | str | Unset): Optional search text to retrieve only the roles matching this
            query.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        scope=scope,
        page=page,
        page_limit=page_limit,
        q=q,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    scope: LibraryPermissionScope | None | Unset = UNSET,
    page: int | Unset = 1,
    page_limit: int | Unset = 10,
    q: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    """Gets the current or available permissions of a particular library folder.

     Gets the current or available permissions of a particular library.
    The results can be paginated and additionally filtered by a query.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        scope (LibraryPermissionScope | None | Unset): The scope of the permissions to retrieve.
            Either the `current` permissions or the `available`.
        page (int | Unset): The page number to retrieve when paginating the available roles.
            Default: 1.
        page_limit (int | Unset): The maximum number of permissions per page when paginating.
            Default: 10.
        q (None | str | Unset): Optional search text to retrieve only the roles matching this
            query.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryAvailablePermissions | LibraryFolderCurrentPermissions | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            scope=scope,
            page=page,
            page_limit=page_limit,
            q=q,
            run_as=run_as,
        )
    ).parsed
