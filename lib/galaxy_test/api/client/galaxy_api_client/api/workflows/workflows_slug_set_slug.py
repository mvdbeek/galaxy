from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.set_slug_payload import SetSlugPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    body: SetSlugPayload,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/workflows/{workflow_id}/slug".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: SetSlugPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Set a new slug for this shared item.

     Sets a new slug to access this item by URL. The new slug must be unique.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (SetSlugPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: SetSlugPayload,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Set a new slug for this shared item.

     Sets a new slug to access this item by URL. The new slug must be unique.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (SetSlugPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: SetSlugPayload,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Set a new slug for this shared item.

     Sets a new slug to access this item by URL. The new slug must be unique.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (SetSlugPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: SetSlugPayload,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Set a new slug for this shared item.

     Sets a new slug to access this item by URL. The new slug must be unique.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (SetSlugPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
