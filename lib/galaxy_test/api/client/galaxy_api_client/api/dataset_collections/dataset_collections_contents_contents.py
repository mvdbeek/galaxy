from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_collections_contents_contents_instance_type import DatasetCollectionsContentsContentsInstanceType
from ...models.dce_summary import DCESummary
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hdca_id: str,
    parent_id: str,
    *,
    instance_type: DatasetCollectionsContentsContentsInstanceType
    | Unset = DatasetCollectionsContentsContentsInstanceType.HISTORY,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_instance_type: str | Unset = UNSET
    if not isinstance(instance_type, Unset):
        json_instance_type = instance_type.value

    params["instance_type"] = json_instance_type

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dataset_collections/{hdca_id}/contents/{parent_id}".format(
            hdca_id=quote(str(hdca_id), safe=""),
            parent_id=quote(str(parent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[DCESummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_dataset_collection_content_elements_item_data in _response_200:
            componentsschemas_dataset_collection_content_elements_item = DCESummary.from_dict(
                componentsschemas_dataset_collection_content_elements_item_data
            )

            response_200.append(componentsschemas_dataset_collection_content_elements_item)

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
) -> Response[MessageExceptionModel | list[DCESummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hdca_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsContentsContentsInstanceType
    | Unset = DatasetCollectionsContentsContentsInstanceType.HISTORY,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[DCESummary]]:
    """Returns direct child contents of indicated dataset collection parent ID.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        parent_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsContentsContentsInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsContentsContentsInstanceType.HISTORY.
        limit (int | None | Unset): The maximum number of content elements to return.
        offset (int | None | Unset): The number of content elements that will be skipped before
            returning.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[DCESummary]]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        parent_id=parent_id,
        instance_type=instance_type,
        limit=limit,
        offset=offset,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hdca_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsContentsContentsInstanceType
    | Unset = DatasetCollectionsContentsContentsInstanceType.HISTORY,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[DCESummary] | None:
    """Returns direct child contents of indicated dataset collection parent ID.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        parent_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsContentsContentsInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsContentsContentsInstanceType.HISTORY.
        limit (int | None | Unset): The maximum number of content elements to return.
        offset (int | None | Unset): The number of content elements that will be skipped before
            returning.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[DCESummary]
    """

    return sync_detailed(
        hdca_id=hdca_id,
        parent_id=parent_id,
        client=client,
        instance_type=instance_type,
        limit=limit,
        offset=offset,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    hdca_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsContentsContentsInstanceType
    | Unset = DatasetCollectionsContentsContentsInstanceType.HISTORY,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[DCESummary]]:
    """Returns direct child contents of indicated dataset collection parent ID.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        parent_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsContentsContentsInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsContentsContentsInstanceType.HISTORY.
        limit (int | None | Unset): The maximum number of content elements to return.
        offset (int | None | Unset): The number of content elements that will be skipped before
            returning.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[DCESummary]]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        parent_id=parent_id,
        instance_type=instance_type,
        limit=limit,
        offset=offset,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hdca_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsContentsContentsInstanceType
    | Unset = DatasetCollectionsContentsContentsInstanceType.HISTORY,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[DCESummary] | None:
    """Returns direct child contents of indicated dataset collection parent ID.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        parent_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsContentsContentsInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsContentsContentsInstanceType.HISTORY.
        limit (int | None | Unset): The maximum number of content elements to return.
        offset (int | None | Unset): The number of content elements that will be skipped before
            returning.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[DCESummary]
    """

    return (
        await asyncio_detailed(
            hdca_id=hdca_id,
            parent_id=parent_id,
            client=client,
            instance_type=instance_type,
            limit=limit,
            offset=offset,
            run_as=run_as,
        )
    ).parsed
