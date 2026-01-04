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
    filename: str,
    format_: str,
    *,
    dry_run: bool | None | Unset = True,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_dry_run: bool | None | Unset
    if isinstance(dry_run, Unset):
        json_dry_run = UNSET
    else:
        json_dry_run = dry_run
    params["dry_run"] = json_dry_run

    json_q: list[str] | None | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    elif isinstance(q, list):
        json_q = q

    else:
        json_q = q
    params["q"] = json_q

    json_qv: list[str] | None | Unset
    if isinstance(qv, Unset):
        json_qv = UNSET
    elif isinstance(qv, list):
        json_qv = qv

    else:
        json_qv = qv
    params["qv"] = json_qv

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    else:
        json_order = order
    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories/{history_id}/contents/archive/{filename}.{format_}".format(
            history_id=quote(str(history_id), safe=""),
            filename=quote(str(filename), safe=""),
            format_=quote(str(format_), safe=""),
        ),
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
    history_id: str,
    filename: str,
    format_: str,
    *,
    client: AuthenticatedClient,
    dry_run: bool | None | Unset = True,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Build and return a compressed archive of the selected history contents.

     **Warning**: This API is unstable and may change without notice.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        filename (str): The name that the Archive will have (defaults to history name).
        format_ (str): Output format of the archive.
        dry_run (bool | None | Unset): Whether to return the archive and file paths only (as JSON)
            and not an actual archive file. Default: True.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
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
        filename=filename,
        format_=format_,
        dry_run=dry_run,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    filename: str,
    format_: str,
    *,
    client: AuthenticatedClient,
    dry_run: bool | None | Unset = True,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Build and return a compressed archive of the selected history contents.

     **Warning**: This API is unstable and may change without notice.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        filename (str): The name that the Archive will have (defaults to history name).
        format_ (str): Output format of the archive.
        dry_run (bool | None | Unset): Whether to return the archive and file paths only (as JSON)
            and not an actual archive file. Default: True.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
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
        filename=filename,
        format_=format_,
        client=client,
        dry_run=dry_run,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    filename: str,
    format_: str,
    *,
    client: AuthenticatedClient,
    dry_run: bool | None | Unset = True,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Build and return a compressed archive of the selected history contents.

     **Warning**: This API is unstable and may change without notice.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        filename (str): The name that the Archive will have (defaults to history name).
        format_ (str): Output format of the archive.
        dry_run (bool | None | Unset): Whether to return the archive and file paths only (as JSON)
            and not an actual archive file. Default: True.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
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
        filename=filename,
        format_=format_,
        dry_run=dry_run,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    filename: str,
    format_: str,
    *,
    client: AuthenticatedClient,
    dry_run: bool | None | Unset = True,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Build and return a compressed archive of the selected history contents.

     **Warning**: This API is unstable and may change without notice.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        filename (str): The name that the Archive will have (defaults to history name).
        format_ (str): Output format of the archive.
        dry_run (bool | None | Unset): Whether to return the archive and file paths only (as JSON)
            and not an actual archive file. Default: True.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        limit (int | None | Unset): The maximum number of items to return.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
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
            filename=filename,
            format_=format_,
            client=client,
            dry_run=dry_run,
            q=q,
            qv=qv,
            offset=offset,
            limit=limit,
            order=order,
            run_as=run_as,
        )
    ).parsed
