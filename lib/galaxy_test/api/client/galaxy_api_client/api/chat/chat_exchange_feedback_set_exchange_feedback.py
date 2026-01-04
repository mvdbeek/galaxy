from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.response_chat_exchange_feedback_set_exchange_feedback import (
    ResponseChatExchangeFeedbackSetExchangeFeedback,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    exchange_id: int,
    *,
    body: int,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/chat/exchange/{exchange_id}/feedback".format(
            exchange_id=quote(str(exchange_id), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback | None:
    if response.status_code == 200:
        response_200 = ResponseChatExchangeFeedbackSetExchangeFeedback.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exchange_id: int,
    *,
    client: AuthenticatedClient,
    body: int,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback]:
    """Set Exchange Feedback

     **Warning**: This API is unstable and may change without notice.

    Args:
        exchange_id (int):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (int): Feedback value: 0 for negative, 1 for positive

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exchange_id: int,
    *,
    client: AuthenticatedClient,
    body: int,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback | None:
    """Set Exchange Feedback

     **Warning**: This API is unstable and may change without notice.

    Args:
        exchange_id (int):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (int): Feedback value: 0 for negative, 1 for positive

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback
    """

    return sync_detailed(
        exchange_id=exchange_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    exchange_id: int,
    *,
    client: AuthenticatedClient,
    body: int,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback]:
    """Set Exchange Feedback

     **Warning**: This API is unstable and may change without notice.

    Args:
        exchange_id (int):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (int): Feedback value: 0 for negative, 1 for positive

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback]
    """

    kwargs = _get_kwargs(
        exchange_id=exchange_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exchange_id: int,
    *,
    client: AuthenticatedClient,
    body: int,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback | None:
    """Set Exchange Feedback

     **Warning**: This API is unstable and may change without notice.

    Args:
        exchange_id (int):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (int): Feedback value: 0 for negative, 1 for positive

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ResponseChatExchangeFeedbackSetExchangeFeedback
    """

    return (
        await asyncio_detailed(
            exchange_id=exchange_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
