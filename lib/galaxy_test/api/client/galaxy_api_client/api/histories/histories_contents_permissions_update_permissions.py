from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_association_roles import DatasetAssociationRoles
from ...models.message_exception_model import MessageExceptionModel
from ...models.update_dataset_permissions_payload import UpdateDatasetPermissionsPayload
from ...models.update_dataset_permissions_payload_alias_b import UpdateDatasetPermissionsPayloadAliasB
from ...models.update_dataset_permissions_payload_alias_c import UpdateDatasetPermissionsPayloadAliasC
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    dataset_id: str,
    *,
    body: UpdateDatasetPermissionsPayload
    | UpdateDatasetPermissionsPayloadAliasB
    | UpdateDatasetPermissionsPayloadAliasC,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/histories/{history_id}/contents/{dataset_id}/permissions".format(
            history_id=quote(str(history_id), safe=""),
            dataset_id=quote(str(dataset_id), safe=""),
        ),
    }

    if isinstance(body, UpdateDatasetPermissionsPayload):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, UpdateDatasetPermissionsPayloadAliasB):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetAssociationRoles | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DatasetAssociationRoles.from_dict(response.json())

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
) -> Response[DatasetAssociationRoles | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDatasetPermissionsPayload
    | UpdateDatasetPermissionsPayloadAliasB
    | UpdateDatasetPermissionsPayloadAliasC,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetAssociationRoles | MessageExceptionModel]:
    """Set permissions of the given history dataset to the given role ids.

     Set permissions of the given history dataset to the given role ids.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        dataset_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateDatasetPermissionsPayload | UpdateDatasetPermissionsPayloadAliasB |
            UpdateDatasetPermissionsPayloadAliasC):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetAssociationRoles | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        dataset_id=dataset_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDatasetPermissionsPayload
    | UpdateDatasetPermissionsPayloadAliasB
    | UpdateDatasetPermissionsPayloadAliasC,
    run_as: None | str | Unset = UNSET,
) -> DatasetAssociationRoles | MessageExceptionModel | None:
    """Set permissions of the given history dataset to the given role ids.

     Set permissions of the given history dataset to the given role ids.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        dataset_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateDatasetPermissionsPayload | UpdateDatasetPermissionsPayloadAliasB |
            UpdateDatasetPermissionsPayloadAliasC):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetAssociationRoles | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        dataset_id=dataset_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDatasetPermissionsPayload
    | UpdateDatasetPermissionsPayloadAliasB
    | UpdateDatasetPermissionsPayloadAliasC,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetAssociationRoles | MessageExceptionModel]:
    """Set permissions of the given history dataset to the given role ids.

     Set permissions of the given history dataset to the given role ids.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        dataset_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateDatasetPermissionsPayload | UpdateDatasetPermissionsPayloadAliasB |
            UpdateDatasetPermissionsPayloadAliasC):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetAssociationRoles | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        dataset_id=dataset_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDatasetPermissionsPayload
    | UpdateDatasetPermissionsPayloadAliasB
    | UpdateDatasetPermissionsPayloadAliasC,
    run_as: None | str | Unset = UNSET,
) -> DatasetAssociationRoles | MessageExceptionModel | None:
    """Set permissions of the given history dataset to the given role ids.

     Set permissions of the given history dataset to the given role ids.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        dataset_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateDatasetPermissionsPayload | UpdateDatasetPermissionsPayloadAliasB |
            UpdateDatasetPermissionsPayloadAliasC):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetAssociationRoles | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            dataset_id=dataset_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
