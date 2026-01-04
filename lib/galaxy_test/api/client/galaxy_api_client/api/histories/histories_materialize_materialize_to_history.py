from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.materialize_dataset_instance_api_request import MaterializeDatasetInstanceAPIRequest
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    body: MaterializeDatasetInstanceAPIRequest,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/histories/{history_id}/materialize".format(
            history_id=quote(str(history_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = AsyncTaskResultSummary.from_dict(response.json())

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
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: MaterializeDatasetInstanceAPIRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Materialize a deferred library or HDA dataset into real, usable dataset in specified history.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (MaterializeDatasetInstanceAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: MaterializeDatasetInstanceAPIRequest,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Materialize a deferred library or HDA dataset into real, usable dataset in specified history.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (MaterializeDatasetInstanceAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: MaterializeDatasetInstanceAPIRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Materialize a deferred library or HDA dataset into real, usable dataset in specified history.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (MaterializeDatasetInstanceAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: MaterializeDatasetInstanceAPIRequest,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Materialize a deferred library or HDA dataset into real, usable dataset in specified history.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (MaterializeDatasetInstanceAPIRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
