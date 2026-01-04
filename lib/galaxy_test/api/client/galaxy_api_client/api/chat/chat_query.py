from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_payload import ChatPayload
from ...models.chat_response import ChatResponse
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ChatPayload | None | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    agent_type: str | Unset = "auto",
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_job_id: None | str | Unset
    if isinstance(job_id, Unset):
        json_job_id = UNSET
    else:
        json_job_id = job_id
    params["job_id"] = json_job_id

    json_query: None | str | Unset
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    params["agent_type"] = agent_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/chat",
        "params": params,
    }

    if isinstance(body, ChatPayload):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatResponse | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = ChatResponse.from_dict(response.json())

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
) -> Response[ChatResponse | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatPayload | None | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    agent_type: str | Unset = "auto",
    run_as: None | str | Unset = UNSET,
) -> Response[ChatResponse | MessageExceptionModel]:
    """Query

     **Warning**: This API is unstable and may change without notice.

    Args:
        job_id (None | str | Unset):
        query (None | str | Unset): Query string for general chat
        agent_type (str | Unset): Agent type to use for the query Default: 'auto'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ChatPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        job_id=job_id,
        query=query,
        agent_type=agent_type,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ChatPayload | None | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    agent_type: str | Unset = "auto",
    run_as: None | str | Unset = UNSET,
) -> ChatResponse | MessageExceptionModel | None:
    """Query

     **Warning**: This API is unstable and may change without notice.

    Args:
        job_id (None | str | Unset):
        query (None | str | Unset): Query string for general chat
        agent_type (str | Unset): Agent type to use for the query Default: 'auto'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ChatPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatResponse | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        body=body,
        job_id=job_id,
        query=query,
        agent_type=agent_type,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatPayload | None | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    agent_type: str | Unset = "auto",
    run_as: None | str | Unset = UNSET,
) -> Response[ChatResponse | MessageExceptionModel]:
    """Query

     **Warning**: This API is unstable and may change without notice.

    Args:
        job_id (None | str | Unset):
        query (None | str | Unset): Query string for general chat
        agent_type (str | Unset): Agent type to use for the query Default: 'auto'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ChatPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatResponse | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        body=body,
        job_id=job_id,
        query=query,
        agent_type=agent_type,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChatPayload | None | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    query: None | str | Unset = UNSET,
    agent_type: str | Unset = "auto",
    run_as: None | str | Unset = UNSET,
) -> ChatResponse | MessageExceptionModel | None:
    """Query

     **Warning**: This API is unstable and may change without notice.

    Args:
        job_id (None | str | Unset):
        query (None | str | Unset): Query string for general chat
        agent_type (str | Unset): Agent type to use for the query Default: 'auto'.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ChatPayload | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatResponse | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            job_id=job_id,
            query=query,
            agent_type=agent_type,
            run_as=run_as,
        )
    ).parsed
