from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_collections_show_instance_type import DatasetCollectionsShowInstanceType
from ...models.hdca_custom import HDCACustom
from ...models.hdca_detailed import HDCADetailed
from ...models.hdca_summary import HDCASummary
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hdca_id: str,
    *,
    instance_type: DatasetCollectionsShowInstanceType | Unset = DatasetCollectionsShowInstanceType.HISTORY,
    view: str | Unset = "element",
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

    params["view"] = view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dataset_collections/{hdca_id}".format(
            hdca_id=quote(str(hdca_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> HDCACustom | HDCADetailed | HDCASummary:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = HDCACustom.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = HDCADetailed.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = HDCASummary.from_dict(data)

            return response_200_type_2

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
) -> Response[HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel]:
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
    instance_type: DatasetCollectionsShowInstanceType | Unset = DatasetCollectionsShowInstanceType.HISTORY,
    view: str | Unset = "element",
    run_as: None | str | Unset = UNSET,
) -> Response[HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel]:
    """Returns detailed information about the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsShowInstanceType | Unset): The type of collection
            instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsShowInstanceType.HISTORY.
        view (str | Unset): The view of collection instance to return. Default: 'element'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        instance_type=instance_type,
        view=view,
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
    instance_type: DatasetCollectionsShowInstanceType | Unset = DatasetCollectionsShowInstanceType.HISTORY,
    view: str | Unset = "element",
    run_as: None | str | Unset = UNSET,
) -> HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel | None:
    """Returns detailed information about the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsShowInstanceType | Unset): The type of collection
            instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsShowInstanceType.HISTORY.
        view (str | Unset): The view of collection instance to return. Default: 'element'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel
    """

    return sync_detailed(
        hdca_id=hdca_id,
        client=client,
        instance_type=instance_type,
        view=view,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsShowInstanceType | Unset = DatasetCollectionsShowInstanceType.HISTORY,
    view: str | Unset = "element",
    run_as: None | str | Unset = UNSET,
) -> Response[HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel]:
    """Returns detailed information about the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsShowInstanceType | Unset): The type of collection
            instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsShowInstanceType.HISTORY.
        view (str | Unset): The view of collection instance to return. Default: 'element'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        instance_type=instance_type,
        view=view,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    instance_type: DatasetCollectionsShowInstanceType | Unset = DatasetCollectionsShowInstanceType.HISTORY,
    view: str | Unset = "element",
    run_as: None | str | Unset = UNSET,
) -> HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel | None:
    """Returns detailed information about the given collection.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        instance_type (DatasetCollectionsShowInstanceType | Unset): The type of collection
            instance. Either `history` (default) or `library`. Default:
            DatasetCollectionsShowInstanceType.HISTORY.
        view (str | Unset): The view of collection instance to return. Default: 'element'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDCACustom | HDCADetailed | HDCASummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            hdca_id=hdca_id,
            client=client,
            instance_type=instance_type,
            view=view,
            run_as=run_as,
        )
    ).parsed
