from http import HTTPStatus
from typing import Any, Literal, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    jeha_id: Literal["latest"] | str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories/{history_id}/exports/{jeha_id}".format(
            history_id=quote(str(history_id), safe=""),
            jeha_id=quote(str(jeha_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    history_id: str,
    jeha_id: Literal["latest"] | str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """If ready and available, return raw contents of exported history as a downloadable archive.

     See ``PUT /api/histories/{id}/exports`` to initiate the creation
    of the history export - when ready, that route will return 200 status
    code (instead of 202) and this route can be used to download the archive.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        jeha_id (Literal['latest'] | str): The ID of the specific Job Export History Association
            or `latest` (default) to download the last generated archive.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        jeha_id=jeha_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    jeha_id: Literal["latest"] | str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """If ready and available, return raw contents of exported history as a downloadable archive.

     See ``PUT /api/histories/{id}/exports`` to initiate the creation
    of the history export - when ready, that route will return 200 status
    code (instead of 202) and this route can be used to download the archive.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        jeha_id (Literal['latest'] | str): The ID of the specific Job Export History Association
            or `latest` (default) to download the last generated archive.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        jeha_id=jeha_id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    jeha_id: Literal["latest"] | str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """If ready and available, return raw contents of exported history as a downloadable archive.

     See ``PUT /api/histories/{id}/exports`` to initiate the creation
    of the history export - when ready, that route will return 200 status
    code (instead of 202) and this route can be used to download the archive.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        jeha_id (Literal['latest'] | str): The ID of the specific Job Export History Association
            or `latest` (default) to download the last generated archive.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        jeha_id=jeha_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    jeha_id: Literal["latest"] | str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """If ready and available, return raw contents of exported history as a downloadable archive.

     See ``PUT /api/histories/{id}/exports`` to initiate the creation
    of the history export - when ready, that route will return 200 status
    code (instead of 202) and this route can be used to download the archive.

    **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
    `/api/histories/{id}/write_store` instead.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        jeha_id (Literal['latest'] | str): The ID of the specific Job Export History Association
            or `latest` (default) to download the last generated archive.
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
            history_id=history_id,
            jeha_id=jeha_id,
            client=client,
            run_as=run_as,
        )
    ).parsed
