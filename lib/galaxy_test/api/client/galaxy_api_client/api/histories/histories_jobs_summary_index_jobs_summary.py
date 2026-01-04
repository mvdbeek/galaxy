from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    ids: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_ids: None | str | Unset
    if isinstance(ids, Unset):
        json_ids = UNSET
    else:
        json_ids = ids
    params["ids"] = json_ids

    json_types: None | str | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    else:
        json_types = types
    params["types"] = json_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories/{history_id}/jobs_summary".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageExceptionModel | None:
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
) -> Response[MessageExceptionModel]:
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
    ids: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

     Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        ids (None | str | Unset): A comma-separated list of encoded ids of job summary objects to
            return - if `ids` is specified types must also be specified and have same length.
        types (None | str | Unset): A comma-separated list of type of object represented by
            elements in the `ids` array - any of `Job`, `ImplicitCollectionJob`, or
            `WorkflowInvocation`.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        ids=ids,
        types=types,
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
    ids: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

     Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        ids (None | str | Unset): A comma-separated list of encoded ids of job summary objects to
            return - if `ids` is specified types must also be specified and have same length.
        types (None | str | Unset): A comma-separated list of type of object represented by
            elements in the `ids` array - any of `Job`, `ImplicitCollectionJob`, or
            `WorkflowInvocation`.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        ids=ids,
        types=types,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    ids: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

     Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        ids (None | str | Unset): A comma-separated list of encoded ids of job summary objects to
            return - if `ids` is specified types must also be specified and have same length.
        types (None | str | Unset): A comma-separated list of type of object represented by
            elements in the `ids` array - any of `Job`, `ImplicitCollectionJob`, or
            `WorkflowInvocation`.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        ids=ids,
        types=types,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    ids: None | str | Unset = UNSET,
    types: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

     Return job state summary info for jobs, implicit groups jobs for collections or workflow
    invocations.

    **Warning**: We allow anyone to fetch job state information about any object they
    can guess an encoded ID for - it isn't considered protected data. This keeps
    polling IDs as part of state calculation for large histories and collections as
    efficient as possible.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        ids (None | str | Unset): A comma-separated list of encoded ids of job summary objects to
            return - if `ids` is specified types must also be specified and have same length.
        types (None | str | Unset): A comma-separated list of type of object represented by
            elements in the `ids` array - any of `Job`, `ImplicitCollectionJob`, or
            `WorkflowInvocation`.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            ids=ids,
            types=types,
            run_as=run_as,
        )
    ).parsed
