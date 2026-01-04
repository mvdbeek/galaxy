from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_source_type import DatasetSourceType
from ...models.job_metric import JobMetric
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    hda_ldda: DatasetSourceType | None | Unset = DatasetSourceType.HDA,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_hda_ldda: None | str | Unset
    if isinstance(hda_ldda, Unset):
        json_hda_ldda = UNSET
    elif isinstance(hda_ldda, DatasetSourceType):
        json_hda_ldda = hda_ldda.value
    else:
        json_hda_ldda = hda_ldda
    params["hda_ldda"] = json_hda_ldda

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/{job_id}/metrics".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[JobMetric | None] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> JobMetric | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = JobMetric.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(JobMetric | None, data)

            response_200_item = _parse_response_200_item(response_200_item_data)

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
) -> Response[MessageExceptionModel | list[JobMetric | None]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | None | Unset = DatasetSourceType.HDA,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobMetric | None]]:
    """Return job metrics for specified job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | None | Unset): Whether this dataset belongs to a history
            (HDA) or a library (LDDA). Default: DatasetSourceType.HDA.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobMetric | None]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        hda_ldda=hda_ldda,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | None | Unset = DatasetSourceType.HDA,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobMetric | None] | None:
    """Return job metrics for specified job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | None | Unset): Whether this dataset belongs to a history
            (HDA) or a library (LDDA). Default: DatasetSourceType.HDA.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobMetric | None]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        hda_ldda=hda_ldda,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | None | Unset = DatasetSourceType.HDA,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobMetric | None]]:
    """Return job metrics for specified job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | None | Unset): Whether this dataset belongs to a history
            (HDA) or a library (LDDA). Default: DatasetSourceType.HDA.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobMetric | None]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        hda_ldda=hda_ldda,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,
    hda_ldda: DatasetSourceType | None | Unset = DatasetSourceType.HDA,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobMetric | None] | None:
    """Return job metrics for specified job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        hda_ldda (DatasetSourceType | None | Unset): Whether this dataset belongs to a history
            (HDA) or a library (LDDA). Default: DatasetSourceType.HDA.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobMetric | None]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            hda_ldda=hda_ldda,
            run_as=run_as,
        )
    ).parsed
