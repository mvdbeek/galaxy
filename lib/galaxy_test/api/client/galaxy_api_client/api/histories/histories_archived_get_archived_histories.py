from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archived_history_detailed import ArchivedHistoryDetailed
from ...models.archived_history_summary import ArchivedHistorySummary
from ...models.custom_archived_history_view import CustomArchivedHistoryView
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
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

    json_view: None | str | Unset
    if isinstance(view, Unset):
        json_view = UNSET
    else:
        json_view = view
    params["view"] = json_view

    json_keys: None | str | Unset
    if isinstance(keys, Unset):
        json_keys = UNSET
    else:
        json_keys = keys
    params["keys"] = json_keys

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
        "url": "/api/histories/archived",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = CustomArchivedHistoryView.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_1 = ArchivedHistoryDetailed.from_dict(data)

                    return response_200_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_2 = ArchivedHistorySummary.from_dict(data)

                return response_200_item_type_2

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[
    MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]
]:
    """Get a list of all archived histories for the current user.

     Get a list of all archived histories for the current user.

    Archived histories are histories are not part of the active histories of the user but they can be
    accessed using this endpoint.

    Args:
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
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
        Response[MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]]
    """

    kwargs = _get_kwargs(
        view=view,
        keys=keys,
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
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView] | None:
    """Get a list of all archived histories for the current user.

     Get a list of all archived histories for the current user.

    Archived histories are histories are not part of the active histories of the user but they can be
    accessed using this endpoint.

    Args:
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
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
        MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]
    """

    return sync_detailed(
        client=client,
        view=view,
        keys=keys,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]
]:
    """Get a list of all archived histories for the current user.

     Get a list of all archived histories for the current user.

    Archived histories are histories are not part of the active histories of the user but they can be
    accessed using this endpoint.

    Args:
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
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
        Response[MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]]
    """

    kwargs = _get_kwargs(
        view=view,
        keys=keys,
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
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView] | None:
    """Get a list of all archived histories for the current user.

     Get a list of all archived histories for the current user.

    Archived histories are histories are not part of the active histories of the user but they can be
    accessed using this endpoint.

    Args:
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
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
        MessageExceptionModel | list[ArchivedHistoryDetailed | ArchivedHistorySummary | CustomArchivedHistoryView]
    """

    return (
        await asyncio_detailed(
            client=client,
            view=view,
            keys=keys,
            q=q,
            qv=qv,
            offset=offset,
            limit=limit,
            order=order,
            run_as=run_as,
        )
    ).parsed
