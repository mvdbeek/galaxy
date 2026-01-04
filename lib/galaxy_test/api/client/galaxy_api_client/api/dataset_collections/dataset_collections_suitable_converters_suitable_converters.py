from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_collections_suitable_converters_suitable_converters_instance_type import (
    DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType,
)
from ...models.message_exception_model import MessageExceptionModel
from ...models.suitable_converter import SuitableConverter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hdca_id: str,
    *,
    instance_type: DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType
    | Unset = DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY,
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
        "url": "/api/dataset_collections/{hdca_id}/suitable_converters".format(
            hdca_id=quote(str(hdca_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[SuitableConverter] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_suitable_converters_item_data in _response_200:
            componentsschemas_suitable_converters_item = SuitableConverter.from_dict(
                componentsschemas_suitable_converters_item_data
            )

            response_200.append(componentsschemas_suitable_converters_item)

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
) -> Response[MessageExceptionModel | list[SuitableConverter]]:
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
    instance_type: DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType
    | Unset = DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[SuitableConverter]]:
    """Returns a list of applicable converters for all datatypes in the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType |
            Unset): The type of collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[SuitableConverter]]
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
    instance_type: DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType
    | Unset = DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[SuitableConverter] | None:
    """Returns a list of applicable converters for all datatypes in the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType |
            Unset): The type of collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[SuitableConverter]
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
    instance_type: DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType
    | Unset = DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[SuitableConverter]]:
    """Returns a list of applicable converters for all datatypes in the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType |
            Unset): The type of collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[SuitableConverter]]
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
    instance_type: DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType
    | Unset = DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[SuitableConverter] | None:
    """Returns a list of applicable converters for all datatypes in the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType |
            Unset): The type of collection instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType.HISTORY.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[SuitableConverter]
    """

    return (
        await asyncio_detailed(
            hdca_id=hdca_id,
            client=client,
            instance_type=instance_type,
            run_as=run_as,
        )
    ).parsed
