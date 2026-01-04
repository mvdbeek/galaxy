from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_collection_attributes_result import DatasetCollectionAttributesResult
from ...models.dataset_collections_attributes_attributes_instance_type import (
    DatasetCollectionsAttributesAttributesInstanceType,
)
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hdca_id: str,
    *,
    instance_type: DatasetCollectionsAttributesAttributesInstanceType
    | Unset = DatasetCollectionsAttributesAttributesInstanceType.HISTORY,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dataset_collections/{hdca_id}/attributes".format(
            hdca_id=quote(str(hdca_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetCollectionAttributesResult | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DatasetCollectionAttributesResult.from_dict(response.json())

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
) -> Response[DatasetCollectionAttributesResult | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsAttributesAttributesInstanceType
    | Unset = DatasetCollectionsAttributesAttributesInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetCollectionAttributesResult | MessageExceptionModel]:
    """Returns `dbkey`/`extension` attributes for all the collection elements.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsAttributesAttributesInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsAttributesAttributesInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCollectionAttributesResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        instance_type=instance_type,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsAttributesAttributesInstanceType
    | Unset = DatasetCollectionsAttributesAttributesInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> DatasetCollectionAttributesResult | MessageExceptionModel | None:
    """Returns `dbkey`/`extension` attributes for all the collection elements.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsAttributesAttributesInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsAttributesAttributesInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCollectionAttributesResult | MessageExceptionModel
    """

    return sync_detailed(
        hdca_id=hdca_id,
        client=client,
        instance_type=instance_type,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsAttributesAttributesInstanceType
    | Unset = DatasetCollectionsAttributesAttributesInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetCollectionAttributesResult | MessageExceptionModel]:
    """Returns `dbkey`/`extension` attributes for all the collection elements.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsAttributesAttributesInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsAttributesAttributesInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetCollectionAttributesResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        instance_type=instance_type,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsAttributesAttributesInstanceType
    | Unset = DatasetCollectionsAttributesAttributesInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> DatasetCollectionAttributesResult | MessageExceptionModel | None:
    """Returns `dbkey`/`extension` attributes for all the collection elements.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsAttributesAttributesInstanceType | Unset): The type of
            collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsAttributesAttributesInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetCollectionAttributesResult | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            hdca_id=hdca_id,
            client=client,
            instance_type=instance_type,
            run_as=run_as,
        )
    ).parsed
