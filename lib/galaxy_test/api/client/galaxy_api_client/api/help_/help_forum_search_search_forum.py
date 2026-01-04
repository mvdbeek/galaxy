from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.help_forum_search_response import HelpForumSearchResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/help/forum/search",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HelpForumSearchResponse | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = HelpForumSearchResponse.from_dict(response.json())

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
) -> Response[HelpForumSearchResponse | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    run_as: None | str | Unset = UNSET,
) -> Response[HelpForumSearchResponse | MessageExceptionModel]:
    """Search the Galaxy Help forum.

     **Warning**: This API is unstable and may change without notice.

    Args:
        query (str): Search query to use for searching the Galaxy Help forum.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HelpForumSearchResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        query=query,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    run_as: None | str | Unset = UNSET,
) -> HelpForumSearchResponse | MessageExceptionModel | None:
    """Search the Galaxy Help forum.

     **Warning**: This API is unstable and may change without notice.

    Args:
        query (str): Search query to use for searching the Galaxy Help forum.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HelpForumSearchResponse | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        query=query,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    run_as: None | str | Unset = UNSET,
) -> Response[HelpForumSearchResponse | MessageExceptionModel]:
    """Search the Galaxy Help forum.

     **Warning**: This API is unstable and may change without notice.

    Args:
        query (str): Search query to use for searching the Galaxy Help forum.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HelpForumSearchResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        query=query,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    run_as: None | str | Unset = UNSET,
) -> HelpForumSearchResponse | MessageExceptionModel | None:
    """Search the Galaxy Help forum.

     **Warning**: This API is unstable and may change without notice.

    Args:
        query (str): Search query to use for searching the Galaxy Help forum.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HelpForumSearchResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            run_as=run_as,
        )
    ).parsed
