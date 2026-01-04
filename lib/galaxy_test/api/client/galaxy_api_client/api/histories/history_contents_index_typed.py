from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hda_custom import HDACustom
from ...models.hda_detailed import HDADetailed
from ...models.hda_inaccessible import HDAInaccessible
from ...models.hda_summary import HDASummary
from ...models.hdca_custom import HDCACustom
from ...models.hdca_detailed import HDCADetailed
from ...models.hdca_summary import HDCASummary
from ...models.history_content_type import HistoryContentType
from ...models.history_contents_index_typed_accept import HistoryContentsIndexTypedAccept
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    type_: HistoryContentType,
    *,
    v: None | str | Unset = UNSET,
    details: None | str | Unset = UNSET,
    ids: None | str | Unset = UNSET,
    types: list[str] | None | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    visible: bool | None | Unset = UNSET,
    shareable: bool | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    accept: HistoryContentsIndexTypedAccept | Unset = HistoryContentsIndexTypedAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["accept"] = str(accept)

    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_v: None | str | Unset
    if isinstance(v, Unset):
        json_v = UNSET
    else:
        json_v = v
    params["v"] = json_v

    json_details: None | str | Unset
    if isinstance(details, Unset):
        json_details = UNSET
    else:
        json_details = details
    params["details"] = json_details

    json_ids: None | str | Unset
    if isinstance(ids, Unset):
        json_ids = UNSET
    else:
        json_ids = ids
    params["ids"] = json_ids

    json_types: list[str] | None | Unset
    if isinstance(types, Unset):
        json_types = UNSET
    elif isinstance(types, list):
        json_types = types

    else:
        json_types = types
    params["types"] = json_types

    json_deleted: bool | None | Unset
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

    json_visible: bool | None | Unset
    if isinstance(visible, Unset):
        json_visible = UNSET
    else:
        json_visible = visible
    params["visible"] = json_visible

    json_shareable: bool | None | Unset
    if isinstance(shareable, Unset):
        json_shareable = UNSET
    else:
        json_shareable = shareable
    params["shareable"] = json_shareable

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
        "url": "/api/histories/{history_id}/contents/{type_}s".format(
            history_id=quote(str(history_id), safe=""),
            type_=quote(str(type_), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_history_contents_result_item_data in _response_200:

            def _parse_componentsschemas_history_contents_result_item(
                data: object,
            ) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_0 = HDACustom.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_1 = HDADetailed.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_2 = HDASummary.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_3 = HDAInaccessible.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_4 = HDCACustom.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_history_contents_result_item_type_5 = HDCADetailed.from_dict(data)

                    return componentsschemas_history_contents_result_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_history_contents_result_item_type_6 = HDCASummary.from_dict(data)

                return componentsschemas_history_contents_result_item_type_6

            componentsschemas_history_contents_result_item = _parse_componentsschemas_history_contents_result_item(
                componentsschemas_history_contents_result_item_data
            )

            response_200.append(componentsschemas_history_contents_result_item)

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
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    type_: HistoryContentType,
    *,
    client: AuthenticatedClient,
    v: None | str | Unset = UNSET,
    details: None | str | Unset = UNSET,
    ids: None | str | Unset = UNSET,
    types: list[str] | None | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    visible: bool | None | Unset = UNSET,
    shareable: bool | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    accept: HistoryContentsIndexTypedAccept | Unset = HistoryContentsIndexTypedAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
]:
    """Returns the contents of the given history filtered by type.

     Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.

    - The contents can be filtered and queried using the appropriate parameters.
    - The amount of information returned for each item can be customized.

    **Note**: Anonymous users are allowed to get their current history contents.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        v (None | str | Unset): Only `dev` value is allowed. Set it to use the latest version of
            this endpoint. **All parameters marked as `deprecated` will be ignored when this parameter
            is set.**
        details (None | str | Unset): Legacy name for the `dataset_details` parameter.
        ids (None | str | Unset): A comma-separated list of encoded `HDA/HDCA` IDs. If this list
            is provided, only information about the specific datasets will be returned. Also, setting
            this value will return `all` details of the content item.
        types (list[str] | None | Unset): A list or comma-separated list of kinds of contents to
            return (currently just `dataset` and `dataset_collection` are available). If unset, all
            types will be returned.
        deleted (bool | None | Unset): Whether to return deleted or undeleted datasets only. Leave
            unset for both.
        visible (bool | None | Unset): Whether to return visible or hidden datasets only. Leave
            unset for both.
        shareable (bool | None | Unset): Whether to return only shareable or not shareable
            datasets. Leave unset for both.
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
        accept (HistoryContentsIndexTypedAccept | Unset): Accept header to determine the response
            format. Default is 'application/json'. Default:
            HistoryContentsIndexTypedAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        v=v,
        details=details,
        ids=ids,
        types=types,
        deleted=deleted,
        visible=visible,
        shareable=shareable,
        view=view,
        keys=keys,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        accept=accept,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    type_: HistoryContentType,
    *,
    client: AuthenticatedClient,
    v: None | str | Unset = UNSET,
    details: None | str | Unset = UNSET,
    ids: None | str | Unset = UNSET,
    types: list[str] | None | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    visible: bool | None | Unset = UNSET,
    shareable: bool | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    accept: HistoryContentsIndexTypedAccept | Unset = HistoryContentsIndexTypedAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> (
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | None
):
    """Returns the contents of the given history filtered by type.

     Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.

    - The contents can be filtered and queried using the appropriate parameters.
    - The amount of information returned for each item can be customized.

    **Note**: Anonymous users are allowed to get their current history contents.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        v (None | str | Unset): Only `dev` value is allowed. Set it to use the latest version of
            this endpoint. **All parameters marked as `deprecated` will be ignored when this parameter
            is set.**
        details (None | str | Unset): Legacy name for the `dataset_details` parameter.
        ids (None | str | Unset): A comma-separated list of encoded `HDA/HDCA` IDs. If this list
            is provided, only information about the specific datasets will be returned. Also, setting
            this value will return `all` details of the content item.
        types (list[str] | None | Unset): A list or comma-separated list of kinds of contents to
            return (currently just `dataset` and `dataset_collection` are available). If unset, all
            types will be returned.
        deleted (bool | None | Unset): Whether to return deleted or undeleted datasets only. Leave
            unset for both.
        visible (bool | None | Unset): Whether to return visible or hidden datasets only. Leave
            unset for both.
        shareable (bool | None | Unset): Whether to return only shareable or not shareable
            datasets. Leave unset for both.
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
        accept (HistoryContentsIndexTypedAccept | Unset): Accept header to determine the response
            format. Default is 'application/json'. Default:
            HistoryContentsIndexTypedAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    """

    return sync_detailed(
        history_id=history_id,
        type_=type_,
        client=client,
        v=v,
        details=details,
        ids=ids,
        types=types,
        deleted=deleted,
        visible=visible,
        shareable=shareable,
        view=view,
        keys=keys,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        accept=accept,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    type_: HistoryContentType,
    *,
    client: AuthenticatedClient,
    v: None | str | Unset = UNSET,
    details: None | str | Unset = UNSET,
    ids: None | str | Unset = UNSET,
    types: list[str] | None | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    visible: bool | None | Unset = UNSET,
    shareable: bool | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    accept: HistoryContentsIndexTypedAccept | Unset = HistoryContentsIndexTypedAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
]:
    """Returns the contents of the given history filtered by type.

     Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.

    - The contents can be filtered and queried using the appropriate parameters.
    - The amount of information returned for each item can be customized.

    **Note**: Anonymous users are allowed to get their current history contents.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        v (None | str | Unset): Only `dev` value is allowed. Set it to use the latest version of
            this endpoint. **All parameters marked as `deprecated` will be ignored when this parameter
            is set.**
        details (None | str | Unset): Legacy name for the `dataset_details` parameter.
        ids (None | str | Unset): A comma-separated list of encoded `HDA/HDCA` IDs. If this list
            is provided, only information about the specific datasets will be returned. Also, setting
            this value will return `all` details of the content item.
        types (list[str] | None | Unset): A list or comma-separated list of kinds of contents to
            return (currently just `dataset` and `dataset_collection` are available). If unset, all
            types will be returned.
        deleted (bool | None | Unset): Whether to return deleted or undeleted datasets only. Leave
            unset for both.
        visible (bool | None | Unset): Whether to return visible or hidden datasets only. Leave
            unset for both.
        shareable (bool | None | Unset): Whether to return only shareable or not shareable
            datasets. Leave unset for both.
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
        accept (HistoryContentsIndexTypedAccept | Unset): Accept header to determine the response
            format. Default is 'application/json'. Default:
            HistoryContentsIndexTypedAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        type_=type_,
        v=v,
        details=details,
        ids=ids,
        types=types,
        deleted=deleted,
        visible=visible,
        shareable=shareable,
        view=view,
        keys=keys,
        q=q,
        qv=qv,
        offset=offset,
        limit=limit,
        order=order,
        accept=accept,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    type_: HistoryContentType,
    *,
    client: AuthenticatedClient,
    v: None | str | Unset = UNSET,
    details: None | str | Unset = UNSET,
    ids: None | str | Unset = UNSET,
    types: list[str] | None | Unset = UNSET,
    deleted: bool | None | Unset = UNSET,
    visible: bool | None | Unset = UNSET,
    shareable: bool | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    limit: int | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    accept: HistoryContentsIndexTypedAccept | Unset = HistoryContentsIndexTypedAccept.APPLICATIONJSON,
    run_as: None | str | Unset = UNSET,
) -> (
    MessageExceptionModel
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | None
):
    """Returns the contents of the given history filtered by type.

     Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.

    - The contents can be filtered and queried using the appropriate parameters.
    - The amount of information returned for each item can be customized.

    **Note**: Anonymous users are allowed to get their current history contents.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType): Available types of History contents.
        v (None | str | Unset): Only `dev` value is allowed. Set it to use the latest version of
            this endpoint. **All parameters marked as `deprecated` will be ignored when this parameter
            is set.**
        details (None | str | Unset): Legacy name for the `dataset_details` parameter.
        ids (None | str | Unset): A comma-separated list of encoded `HDA/HDCA` IDs. If this list
            is provided, only information about the specific datasets will be returned. Also, setting
            this value will return `all` details of the content item.
        types (list[str] | None | Unset): A list or comma-separated list of kinds of contents to
            return (currently just `dataset` and `dataset_collection` are available). If unset, all
            types will be returned.
        deleted (bool | None | Unset): Whether to return deleted or undeleted datasets only. Leave
            unset for both.
        visible (bool | None | Unset): Whether to return visible or hidden datasets only. Leave
            unset for both.
        shareable (bool | None | Unset): Whether to return only shareable or not shareable
            datasets. Leave unset for both.
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
        accept (HistoryContentsIndexTypedAccept | Unset): Accept header to determine the response
            format. Default is 'application/json'. Default:
            HistoryContentsIndexTypedAccept.APPLICATIONJSON.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            type_=type_,
            client=client,
            v=v,
            details=details,
            ids=ids,
            types=types,
            deleted=deleted,
            visible=visible,
            shareable=shareable,
            view=view,
            keys=keys,
            q=q,
            qv=qv,
            offset=offset,
            limit=limit,
            order=order,
            accept=accept,
            run_as=run_as,
        )
    ).parsed
