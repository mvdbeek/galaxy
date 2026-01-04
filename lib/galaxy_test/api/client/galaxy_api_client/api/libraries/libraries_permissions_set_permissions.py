from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.legacy_library_permissions_payload import LegacyLibraryPermissionsPayload
from ...models.library_current_permissions import LibraryCurrentPermissions
from ...models.library_legacy_summary import LibraryLegacySummary
from ...models.library_permission_action import LibraryPermissionAction
from ...models.library_permissions_payload import LibraryPermissionsPayload
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: LegacyLibraryPermissionsPayload | LibraryPermissionsPayload,
    action: LibraryPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    elif isinstance(action, LibraryPermissionAction):
        json_action = action.value
    else:
        json_action = action
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/libraries/{id}/permissions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, LibraryPermissionsPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> LibraryCurrentPermissions | LibraryLegacySummary:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LibraryLegacySummary.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = LibraryCurrentPermissions.from_dict(data)

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
) -> Response[LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel]:
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
    body: LegacyLibraryPermissionsPayload | LibraryPermissionsPayload,
    action: LibraryPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel]:
    """Sets the permissions to access and manipulate a library.

     Sets the permissions to access and manipulate a library.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryPermissionAction | None | Unset): Indicates what action should be performed
            on the Library.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LegacyLibraryPermissionsPayload | LibraryPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel]
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
    body: LegacyLibraryPermissionsPayload | LibraryPermissionsPayload,
    action: LibraryPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel | None:
    """Sets the permissions to access and manipulate a library.

     Sets the permissions to access and manipulate a library.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryPermissionAction | None | Unset): Indicates what action should be performed
            on the Library.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LegacyLibraryPermissionsPayload | LibraryPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel
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
    body: LegacyLibraryPermissionsPayload | LibraryPermissionsPayload,
    action: LibraryPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel]:
    """Sets the permissions to access and manipulate a library.

     Sets the permissions to access and manipulate a library.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryPermissionAction | None | Unset): Indicates what action should be performed
            on the Library.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LegacyLibraryPermissionsPayload | LibraryPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel]
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
    body: LegacyLibraryPermissionsPayload | LibraryPermissionsPayload,
    action: LibraryPermissionAction | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel | None:
    """Sets the permissions to access and manipulate a library.

     Sets the permissions to access and manipulate a library.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        action (LibraryPermissionAction | None | Unset): Indicates what action should be performed
            on the Library.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (LegacyLibraryPermissionsPayload | LibraryPermissionsPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LibraryCurrentPermissions | LibraryLegacySummary | MessageExceptionModel
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
