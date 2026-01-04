from http import HTTPStatus
from typing import Any, Literal, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_quota_usage import UserQuotaUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: Literal["current"] | str,
    label: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/{user_id}/usage/{label}".format(
            user_id=quote(str(user_id), safe=""),
            label=quote(str(label), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | None | UserQuotaUsage | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | UserQuotaUsage:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = UserQuotaUsage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserQuotaUsage, data)

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
) -> Response[MessageExceptionModel | None | UserQuotaUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: Literal["current"] | str,
    label: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | None | UserQuotaUsage]:
    """Return the user's quota usage summary for a given quota source label

    Args:
        user_id (Literal['current'] | str): The ID of the user to get or 'current'.
        label (str): The label corresponding to the quota source to fetch usage information about.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | None | UserQuotaUsage]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        label=label,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: Literal["current"] | str,
    label: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None | UserQuotaUsage | None:
    """Return the user's quota usage summary for a given quota source label

    Args:
        user_id (Literal['current'] | str): The ID of the user to get or 'current'.
        label (str): The label corresponding to the quota source to fetch usage information about.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | None | UserQuotaUsage
    """

    return sync_detailed(
        user_id=user_id,
        label=label,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    user_id: Literal["current"] | str,
    label: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | None | UserQuotaUsage]:
    """Return the user's quota usage summary for a given quota source label

    Args:
        user_id (Literal['current'] | str): The ID of the user to get or 'current'.
        label (str): The label corresponding to the quota source to fetch usage information about.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | None | UserQuotaUsage]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        label=label,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: Literal["current"] | str,
    label: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None | UserQuotaUsage | None:
    """Return the user's quota usage summary for a given quota source label

    Args:
        user_id (Literal['current'] | str): The ID of the user to get or 'current'.
        label (str): The label corresponding to the quota source to fetch usage information about.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | None | UserQuotaUsage
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            label=label,
            client=client,
            run_as=run_as,
        )
    ).parsed
