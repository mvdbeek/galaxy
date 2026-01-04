from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dynamic_unprivileged_tool_create_payload import DynamicUnprivilegedToolCreatePayload
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DynamicUnprivilegedToolCreatePayload,
    history_id: str,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["history_id"] = history_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/unprivileged_tools/build",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DynamicUnprivilegedToolCreatePayload,
    history_id: str,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Build

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DynamicUnprivilegedToolCreatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        history_id=history_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DynamicUnprivilegedToolCreatePayload,
    history_id: str,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Build

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DynamicUnprivilegedToolCreatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        body=body,
        history_id=history_id,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DynamicUnprivilegedToolCreatePayload,
    history_id: str,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Build

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DynamicUnprivilegedToolCreatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        history_id=history_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DynamicUnprivilegedToolCreatePayload,
    history_id: str,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Build

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (DynamicUnprivilegedToolCreatePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            history_id=history_id,
            run_as=run_as,
        )
    ).parsed
