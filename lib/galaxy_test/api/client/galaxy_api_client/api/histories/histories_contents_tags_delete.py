from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    history_content_id: str,
    tag_name: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}".format(
            history_id=quote(str(history_id), safe=""),
            history_content_id=quote(str(history_content_id), safe=""),
            tag_name=quote(str(tag_name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
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
) -> Response[MessageExceptionModel | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    history_content_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | bool]:
    """Delete tag based on history_content_id

    Args:
        history_id (str):
        history_content_id (str):  Example: 0123456789ABCDEF.
        tag_name (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | bool]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        history_content_id=history_content_id,
        tag_name=tag_name,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    history_content_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | bool | None:
    """Delete tag based on history_content_id

    Args:
        history_id (str):
        history_content_id (str):  Example: 0123456789ABCDEF.
        tag_name (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | bool
    """

    return sync_detailed(
        history_id=history_id,
        history_content_id=history_content_id,
        tag_name=tag_name,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    history_content_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | bool]:
    """Delete tag based on history_content_id

    Args:
        history_id (str):
        history_content_id (str):  Example: 0123456789ABCDEF.
        tag_name (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | bool]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        history_content_id=history_content_id,
        tag_name=tag_name,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    history_content_id: str,
    tag_name: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | bool | None:
    """Delete tag based on history_content_id

    Args:
        history_id (str):
        history_content_id (str):  Example: 0123456789ABCDEF.
        tag_name (str):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | bool
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            history_content_id=history_content_id,
            tag_name=tag_name,
            client=client,
            run_as=run_as,
        )
    ).parsed
