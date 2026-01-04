from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.installed_tool_shed_repository import InstalledToolShedRepository
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    changeset: None | str | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    uninstalled: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_changeset: None | str | Unset
    if isinstance(changeset, Unset):
        json_changeset = UNSET
    else:
        json_changeset = changeset
    params["changeset"] = json_changeset

    json_deleted: bool | None | Unset
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    json_uninstalled: bool | None | Unset
    if isinstance(uninstalled, Unset):
        json_uninstalled = UNSET
    else:
        json_uninstalled = uninstalled
    params["uninstalled"] = json_uninstalled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tool_shed_repositories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[InstalledToolShedRepository] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InstalledToolShedRepository.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[MessageExceptionModel | list[InstalledToolShedRepository]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    changeset: None | str | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    uninstalled: bool | None | Unset = UNSET,
) -> Response[MessageExceptionModel | list[InstalledToolShedRepository]]:
    """Lists installed tool shed repositories.

    Args:
        name (None | str | Unset): Filter by repository name.
        owner (None | str | Unset): Filter by repository owner.
        changeset (None | str | Unset): Filter by changeset revision.
        deleted (bool | None | Unset): Filter by whether the repository has been deleted.
        uninstalled (bool | None | Unset): Filter by whether the repository has been uninstalled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[InstalledToolShedRepository]]
    """

    kwargs = _get_kwargs(
        name=name,
        owner=owner,
        changeset=changeset,
        deleted=deleted,
        uninstalled=uninstalled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    changeset: None | str | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    uninstalled: bool | None | Unset = UNSET,
) -> MessageExceptionModel | list[InstalledToolShedRepository] | None:
    """Lists installed tool shed repositories.

    Args:
        name (None | str | Unset): Filter by repository name.
        owner (None | str | Unset): Filter by repository owner.
        changeset (None | str | Unset): Filter by changeset revision.
        deleted (bool | None | Unset): Filter by whether the repository has been deleted.
        uninstalled (bool | None | Unset): Filter by whether the repository has been uninstalled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[InstalledToolShedRepository]
    """

    return sync_detailed(
        client=client,
        name=name,
        owner=owner,
        changeset=changeset,
        deleted=deleted,
        uninstalled=uninstalled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    changeset: None | str | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    uninstalled: bool | None | Unset = UNSET,
) -> Response[MessageExceptionModel | list[InstalledToolShedRepository]]:
    """Lists installed tool shed repositories.

    Args:
        name (None | str | Unset): Filter by repository name.
        owner (None | str | Unset): Filter by repository owner.
        changeset (None | str | Unset): Filter by changeset revision.
        deleted (bool | None | Unset): Filter by whether the repository has been deleted.
        uninstalled (bool | None | Unset): Filter by whether the repository has been uninstalled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[InstalledToolShedRepository]]
    """

    kwargs = _get_kwargs(
        name=name,
        owner=owner,
        changeset=changeset,
        deleted=deleted,
        uninstalled=uninstalled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    changeset: None | str | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    uninstalled: bool | None | Unset = UNSET,
) -> MessageExceptionModel | list[InstalledToolShedRepository] | None:
    """Lists installed tool shed repositories.

    Args:
        name (None | str | Unset): Filter by repository name.
        owner (None | str | Unset): Filter by repository owner.
        changeset (None | str | Unset): Filter by changeset revision.
        deleted (bool | None | Unset): Filter by whether the repository has been deleted.
        uninstalled (bool | None | Unset): Filter by whether the repository has been uninstalled.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[InstalledToolShedRepository]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            owner=owner,
            changeset=changeset,
            deleted=deleted,
            uninstalled=uninstalled,
        )
    ).parsed
