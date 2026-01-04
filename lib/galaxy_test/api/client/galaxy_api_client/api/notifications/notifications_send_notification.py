from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.message_exception_model import MessageExceptionModel
from ...models.notification_create_request import NotificationCreateRequest
from ...models.notification_created_response import NotificationCreatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/notifications",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> AsyncTaskResultSummary | NotificationCreatedResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = NotificationCreatedResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AsyncTaskResultSummary.from_dict(data)

            return response_200_type_1

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
) -> Response[AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel]:
    """Sends a notification to a list of recipients (users, groups or roles).

     Sends a notification to a list of recipients (users, groups or roles).

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel | None:
    """Sends a notification to a list of recipients (users, groups or roles).

     Sends a notification to a list of recipients (users, groups or roles).

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> Response[AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel]:
    """Sends a notification to a list of recipients (users, groups or roles).

     Sends a notification to a list of recipients (users, groups or roles).

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NotificationCreateRequest,
    run_as: None | str | Unset = UNSET,
) -> AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel | None:
    """Sends a notification to a list of recipients (users, groups or roles).

     Sends a notification to a list of recipients (users, groups or roles).

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (NotificationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskResultSummary | NotificationCreatedResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
