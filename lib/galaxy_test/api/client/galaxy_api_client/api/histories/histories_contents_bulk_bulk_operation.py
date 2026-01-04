from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.history_content_bulk_operation_payload import HistoryContentBulkOperationPayload
from ...models.history_content_bulk_operation_result import HistoryContentBulkOperationResult
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    body: HistoryContentBulkOperationPayload,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_q: list[str] | None | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    elif isinstance(q, list):
        json_q = q

    else:
        json_q = q
    params["q"] = json_q

    json_qv: list[str] | None | Unset
    if isinstance(qv, Unset):
        json_qv = UNSET
    elif isinstance(qv, list):
        json_qv = qv

    else:
        json_qv = qv
    params["qv"] = json_qv

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/histories/{history_id}/contents/bulk".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HistoryContentBulkOperationResult | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = HistoryContentBulkOperationResult.from_dict(response.json())

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
) -> Response[HistoryContentBulkOperationResult | MessageExceptionModel]:
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
    body: HistoryContentBulkOperationPayload,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[HistoryContentBulkOperationResult | MessageExceptionModel]:
    """Executes an operation on a set of items contained in the given History.

     Executes an operation on a set of items contained in the given History.

    The items to be processed can be explicitly set or determined by a dynamic query.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (HistoryContentBulkOperationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HistoryContentBulkOperationResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        q=q,
        qv=qv,
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
    body: HistoryContentBulkOperationPayload,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> HistoryContentBulkOperationResult | MessageExceptionModel | None:
    """Executes an operation on a set of items contained in the given History.

     Executes an operation on a set of items contained in the given History.

    The items to be processed can be explicitly set or determined by a dynamic query.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (HistoryContentBulkOperationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HistoryContentBulkOperationResult | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        body=body,
        q=q,
        qv=qv,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: HistoryContentBulkOperationPayload,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[HistoryContentBulkOperationResult | MessageExceptionModel]:
    """Executes an operation on a set of items contained in the given History.

     Executes an operation on a set of items contained in the given History.

    The items to be processed can be explicitly set or determined by a dynamic query.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (HistoryContentBulkOperationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HistoryContentBulkOperationResult | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        q=q,
        qv=qv,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: HistoryContentBulkOperationPayload,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> HistoryContentBulkOperationResult | MessageExceptionModel | None:
    """Executes an operation on a set of items contained in the given History.

     Executes an operation on a set of items contained in the given History.

    The items to be processed can be explicitly set or determined by a dynamic query.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (HistoryContentBulkOperationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HistoryContentBulkOperationResult | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
            q=q,
            qv=qv,
            run_as=run_as,
        )
    ).parsed
