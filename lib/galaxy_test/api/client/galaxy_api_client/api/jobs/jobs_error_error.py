from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_error_summary import JobErrorSummary
from ...models.message_exception_model import MessageExceptionModel
from ...models.report_job_error_payload import ReportJobErrorPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    body: ReportJobErrorPayload,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/jobs/{job_id}/error".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JobErrorSummary | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = JobErrorSummary.from_dict(response.json())

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
) -> Response[JobErrorSummary | MessageExceptionModel]:
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
    body: ReportJobErrorPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[JobErrorSummary | MessageExceptionModel]:
    """Submits a bug report via the API.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ReportJobErrorPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobErrorSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
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
    body: ReportJobErrorPayload,
    run_as: None | str | Unset = UNSET,
) -> JobErrorSummary | MessageExceptionModel | None:
    """Submits a bug report via the API.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ReportJobErrorPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobErrorSummary | MessageExceptionModel
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: ReportJobErrorPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[JobErrorSummary | MessageExceptionModel]:
    """Submits a bug report via the API.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ReportJobErrorPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JobErrorSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: ReportJobErrorPayload,
    run_as: None | str | Unset = UNSET,
) -> JobErrorSummary | MessageExceptionModel | None:
    """Submits a bug report via the API.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ReportJobErrorPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JobErrorSummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
