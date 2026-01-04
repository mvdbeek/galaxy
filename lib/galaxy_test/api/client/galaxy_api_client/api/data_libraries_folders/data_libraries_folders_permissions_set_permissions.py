from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_folder_current_permissions import LibraryFolderCurrentPermissions
from ...models.library_folder_permission_action import LibraryFolderPermissionAction
from ...models.library_folder_permissions_payload import LibraryFolderPermissionsPayload
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: LibraryFolderPermissionsPayload,
    action: LibraryFolderPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    elif isinstance(action, LibraryFolderPermissionAction):
        json_action = action.value
    else:
        json_action = action
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/folders/{id}/permissions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = LibraryFolderCurrentPermissions.from_dict(response.json())

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
) -> Response[LibraryFolderCurrentPermissions | MessageExceptionModel]:
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
    body: LibraryFolderPermissionsPayload,
    action: LibraryFolderPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderCurrentPermissions | MessageExceptionModel]:
    """Sets the permissions to manage a library folder.

     Sets the permissions to manage a library folder.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryFolderPermissionAction | None | Unset): Indicates what action should be
            performed on the Library. Currently only `set_permissions` is supported.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryFolderPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderCurrentPermissions | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        action=action,
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
    body: LibraryFolderPermissionsPayload,
    action: LibraryFolderPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    """Sets the permissions to manage a library folder.

     Sets the permissions to manage a library folder.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryFolderPermissionAction | None | Unset): Indicates what action should be
            performed on the Library. Currently only `set_permissions` is supported.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryFolderPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderCurrentPermissions | MessageExceptionModel
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        action=action,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: LibraryFolderPermissionsPayload,
    action: LibraryFolderPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryFolderCurrentPermissions | MessageExceptionModel]:
    """Sets the permissions to manage a library folder.

     Sets the permissions to manage a library folder.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryFolderPermissionAction | None | Unset): Indicates what action should be
            performed on the Library. Currently only `set_permissions` is supported.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryFolderPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryFolderCurrentPermissions | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        action=action,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: LibraryFolderPermissionsPayload,
    action: LibraryFolderPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryFolderCurrentPermissions | MessageExceptionModel | None:
    """Sets the permissions to manage a library folder.

     Sets the permissions to manage a library folder.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryFolderPermissionAction | None | Unset): Indicates what action should be
            performed on the Library. Currently only `set_permissions` is supported.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LibraryFolderPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryFolderCurrentPermissions | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            action=action,
            run_as=run_as,
        )
    ).parsed
