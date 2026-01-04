from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.response_configuration_encode_encode_id import ResponseConfigurationEncodeEncodeId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    decoded_id: int,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/configuration/encode/{decoded_id}".format(
            decoded_id=quote(str(decoded_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ResponseConfigurationEncodeEncodeId | None:
    if response.status_code == 200:
        response_200 = ResponseConfigurationEncodeEncodeId.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ResponseConfigurationEncodeEncodeId]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    decoded_id: int,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ResponseConfigurationEncodeEncodeId]:
    """Encode a given id

     Decode a given id.

    Args:
        decoded_id (int): Decoded id to be encoded
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ResponseConfigurationEncodeEncodeId]
    """

    kwargs = _get_kwargs(
        decoded_id=decoded_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    decoded_id: int,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ResponseConfigurationEncodeEncodeId | None:
    """Encode a given id

     Decode a given id.

    Args:
        decoded_id (int): Decoded id to be encoded
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ResponseConfigurationEncodeEncodeId
    """

    return sync_detailed(
        decoded_id=decoded_id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    decoded_id: int,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ResponseConfigurationEncodeEncodeId]:
    """Encode a given id

     Decode a given id.

    Args:
        decoded_id (int): Decoded id to be encoded
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ResponseConfigurationEncodeEncodeId]
    """

    kwargs = _get_kwargs(
        decoded_id=decoded_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    decoded_id: int,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ResponseConfigurationEncodeEncodeId | None:
    """Encode a given id

     Decode a given id.

    Args:
        decoded_id (int): Decoded id to be encoded
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ResponseConfigurationEncodeEncodeId
    """

    return (
        await asyncio_detailed(
            decoded_id=decoded_id,
            client=client,
            run_as=run_as,
        )
    ).parsed
