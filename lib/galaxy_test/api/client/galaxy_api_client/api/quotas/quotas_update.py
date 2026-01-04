from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.update_quota_params import UpdateQuotaParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: UpdateQuotaParams,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/quotas/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[MessageExceptionModel | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQuotaParams,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | str]:
    """Updates an existing quota.

     Updates an existing quota.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateQuotaParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQuotaParams,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | str | None:
    """Updates an existing quota.

     Updates an existing quota.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateQuotaParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | str
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQuotaParams,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | str]:
    """Updates an existing quota.

     Updates an existing quota.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateQuotaParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateQuotaParams,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | str | None:
    """Updates an existing quota.

     Updates an existing quota.

    Args:
        id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (UpdateQuotaParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
