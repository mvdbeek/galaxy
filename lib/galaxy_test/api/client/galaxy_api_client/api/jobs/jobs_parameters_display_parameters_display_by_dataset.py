from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_source_type import DatasetSourceType
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    *,
    hda_ldda: DatasetSourceType | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_hda_ldda: str | Unset = UNSET
    if not isinstance(hda_ldda, Unset):
        json_hda_ldda = hda_ldda.value

    params["hda_ldda"] = json_hda_ldda

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasets/{dataset_id}/parameters_display".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageExceptionModel | None:
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
) -> Response[MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Resolve parameters as a list for nested display.

     **Warning**: This API is unstable and may change without notice.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        hda_ldda=hda_ldda,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Resolve parameters as a list for nested display.

     **Warning**: This API is unstable and may change without notice.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        hda_ldda=hda_ldda,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Resolve parameters as a list for nested display.

     **Warning**: This API is unstable and may change without notice.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        hda_ldda=hda_ldda,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Resolve parameters as a list for nested display.

     **Warning**: This API is unstable and may change without notice.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            hda_ldda=hda_ldda,
            run_as=run_as,
        )
    ).parsed
