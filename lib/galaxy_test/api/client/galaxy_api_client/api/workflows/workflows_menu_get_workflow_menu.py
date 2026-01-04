from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_deleted: bool | None | Unset = False,
    show_hidden: bool | None | Unset = False,
    missing_tools: bool | None | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_show_deleted: bool | None | Unset
    if isinstance(show_deleted, Unset):
        json_show_deleted = UNSET
    else:
        json_show_deleted = show_deleted
    params["show_deleted"] = json_show_deleted

    json_show_hidden: bool | None | Unset
    if isinstance(show_hidden, Unset):
        json_show_hidden = UNSET
    else:
        json_show_hidden = show_hidden
    params["show_hidden"] = json_show_hidden

    json_missing_tools: bool | None | Unset
    if isinstance(missing_tools, Unset):
        json_missing_tools = UNSET
    else:
        json_missing_tools = missing_tools
    params["missing_tools"] = json_missing_tools

    json_show_published: bool | None | Unset
    if isinstance(show_published, Unset):
        json_show_published = UNSET
    else:
        json_show_published = show_published
    params["show_published"] = json_show_published

    json_show_shared: bool | None | Unset
    if isinstance(show_shared, Unset):
        json_show_shared = UNSET
    else:
        json_show_shared = show_shared
    params["show_shared"] = json_show_shared

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/workflows/menu",
        "params": params,
    }

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
    show_deleted: bool | None | Unset = False,
    show_hidden: bool | None | Unset = False,
    missing_tools: bool | None | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Get workflows present in the tools panel.

    Args:
        show_deleted (bool | None | Unset): Whether to restrict result to deleted workflows.
            Default: False.
        show_hidden (bool | None | Unset): Whether to restrict result to hidden workflows.
            Default: False.
        missing_tools (bool | None | Unset): Whether to include a list of missing tools per
            workflow entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | None | Unset = False,
    show_hidden: bool | None | Unset = False,
    missing_tools: bool | None | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Get workflows present in the tools panel.

    Args:
        show_deleted (bool | None | Unset): Whether to restrict result to deleted workflows.
            Default: False.
        show_hidden (bool | None | Unset): Whether to restrict result to hidden workflows.
            Default: False.
        missing_tools (bool | None | Unset): Whether to include a list of missing tools per
            workflow entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | None | Unset = False,
    show_hidden: bool | None | Unset = False,
    missing_tools: bool | None | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Get workflows present in the tools panel.

    Args:
        show_deleted (bool | None | Unset): Whether to restrict result to deleted workflows.
            Default: False.
        show_hidden (bool | None | Unset): Whether to restrict result to hidden workflows.
            Default: False.
        missing_tools (bool | None | Unset): Whether to include a list of missing tools per
            workflow entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | None | Unset = False,
    show_hidden: bool | None | Unset = False,
    missing_tools: bool | None | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Get workflows present in the tools panel.

    Args:
        show_deleted (bool | None | Unset): Whether to restrict result to deleted workflows.
            Default: False.
        show_hidden (bool | None | Unset): Whether to restrict result to hidden workflows.
            Default: False.
        missing_tools (bool | None | Unset): Whether to include a list of missing tools per
            workflow entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            show_deleted=show_deleted,
            show_hidden=show_hidden,
            missing_tools=missing_tools,
            show_published=show_published,
            show_shared=show_shared,
            run_as=run_as,
        )
    ).parsed
