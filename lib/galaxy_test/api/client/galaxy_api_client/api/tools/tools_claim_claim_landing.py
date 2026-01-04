from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.claim_landing_payload import ClaimLandingPayload
from ...models.message_exception_model import MessageExceptionModel
from ...models.tool_landing_request import ToolLandingRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    body: ClaimLandingPayload | None,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tool_landings/{uuid}/claim".format(
            uuid=quote(str(uuid), safe=""),
        ),
    }

    if isinstance(body, ClaimLandingPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ToolLandingRequest | None:
    if response.status_code == 200:
        response_200 = ToolLandingRequest.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ToolLandingRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: ClaimLandingPayload | None,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolLandingRequest]:
    """Claim Landing

    Args:
        uuid (UUID): The UUID used to identify a persisted landing request.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ClaimLandingPayload | None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolLandingRequest]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: ClaimLandingPayload | None,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolLandingRequest | None:
    """Claim Landing

    Args:
        uuid (UUID): The UUID used to identify a persisted landing request.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ClaimLandingPayload | None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolLandingRequest
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: ClaimLandingPayload | None,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ToolLandingRequest]:
    """Claim Landing

    Args:
        uuid (UUID): The UUID used to identify a persisted landing request.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ClaimLandingPayload | None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ToolLandingRequest]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient,
    body: ClaimLandingPayload | None,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ToolLandingRequest | None:
    """Claim Landing

    Args:
        uuid (UUID): The UUID used to identify a persisted landing request.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ClaimLandingPayload | None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ToolLandingRequest
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
