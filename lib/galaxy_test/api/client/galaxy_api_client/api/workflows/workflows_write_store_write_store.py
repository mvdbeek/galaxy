from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.message_exception_model import MessageExceptionModel
from ...models.write_invocation_store_to_payload import WriteInvocationStoreToPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invocation_id: str,
    *,
    body: WriteInvocationStoreToPayload,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/invocations/{invocation_id}/write_store".format(
            invocation_id=quote(str(invocation_id), safe=""),
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
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    body: WriteInvocationStoreToPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Prepare a workflow invocation export-style download and write to supplied URI.

    Args:
        invocation_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (WriteInvocationStoreToPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        invocation_id=invocation_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    body: WriteInvocationStoreToPayload,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Prepare a workflow invocation export-style download and write to supplied URI.

    Args:
        invocation_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (WriteInvocationStoreToPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return sync_detailed(
        invocation_id=invocation_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    body: WriteInvocationStoreToPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | MessageExceptionModel]:
    """Prepare a workflow invocation export-style download and write to supplied URI.

    Args:
        invocation_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (WriteInvocationStoreToPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        invocation_id=invocation_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    body: WriteInvocationStoreToPayload,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | MessageExceptionModel | None:
    """Prepare a workflow invocation export-style download and write to supplied URI.

    Args:
        invocation_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (WriteInvocationStoreToPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            invocation_id=invocation_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
