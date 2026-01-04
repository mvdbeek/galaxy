from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.histories_index_sort_attribute import HistoriesIndexSortAttribute
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    show_archived: bool | None | Unset = UNSET,
    sort_by: HistoriesIndexSortAttribute | Unset = HistoriesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    all_: bool | None | Unset = False,
    deleted: bool | None | Unset = False,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params["show_own"] = show_own

    params["show_published"] = show_published

    params["show_shared"] = show_shared

    json_show_archived: bool | None | Unset
    if isinstance(show_archived, Unset):
        json_show_archived = UNSET
    else:
        json_show_archived = show_archived
    params["show_archived"] = json_show_archived

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["sort_desc"] = sort_desc

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_all_: bool | None | Unset
    if isinstance(all_, Unset):
        json_all_ = UNSET
    else:
        json_all_ = all_
    params["all"] = json_all_

    json_deleted: bool | None | Unset
    if isinstance(deleted, Unset):
        json_deleted = UNSET
    else:
        json_deleted = deleted
    params["deleted"] = json_deleted

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

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    else:
        json_order = order
    params["order"] = json_order

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/histories",
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
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    show_archived: bool | None | Unset = UNSET,
    sort_by: HistoriesIndexSortAttribute | Unset = HistoriesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    all_: bool | None | Unset = False,
    deleted: bool | None | Unset = False,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Returns histories available to the current user.

    Args:
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        show_archived (bool | None | Unset): Whether to include archived histories.
        sort_by (HistoriesIndexSortAttribute | Unset): Sort index by this specified attribute
            Default: HistoriesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: True.
        search (None | str | Unset): A mix of free text and GitHub-style tags used to filter the
            index operation.

            ## Query Structure

            GitHub-style filter tags (not be confused with Galaxy tags) are tags of the form
            `<tag_name>:<text_no_spaces>` or `<tag_name>:'<text with potential spaces>'`. The tag name
            *generally* (but not exclusively) corresponds to the name of an attribute on the model
            being indexed (i.e. a column in the database).

            If the tag is quoted, the attribute will be filtered exactly. If the tag is unquoted,
            generally a partial match will be used to filter the query (i.e. in terms of the
            implementation
            this means the database operation `ILIKE` will typically be used).

            Once the tagged filters are extracted from the search query, the remaining text is just
            used to search various documented attributes of the object.

            ## GitHub-style Tags Available

            `name`
            : The history's name.

            `annotation`
            : The history's annotation. (The tag `a` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The history's tags. (The tag `t` can be used a short hand alias for this tag to filter
            on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Historys: `title`, `description`, `slug`, `tag`.

        all_ (bool | None | Unset): Whether all histories from other users in this Galaxy should
            be included. Only admins are allowed to query all histories. Default: False.
        deleted (bool | None | Unset): Whether to return only deleted items. Default: False.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        show_archived=show_archived,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
        all_=all_,
        deleted=deleted,
        q=q,
        qv=qv,
        order=order,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    show_archived: bool | None | Unset = UNSET,
    sort_by: HistoriesIndexSortAttribute | Unset = HistoriesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    all_: bool | None | Unset = False,
    deleted: bool | None | Unset = False,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Returns histories available to the current user.

    Args:
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        show_archived (bool | None | Unset): Whether to include archived histories.
        sort_by (HistoriesIndexSortAttribute | Unset): Sort index by this specified attribute
            Default: HistoriesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: True.
        search (None | str | Unset): A mix of free text and GitHub-style tags used to filter the
            index operation.

            ## Query Structure

            GitHub-style filter tags (not be confused with Galaxy tags) are tags of the form
            `<tag_name>:<text_no_spaces>` or `<tag_name>:'<text with potential spaces>'`. The tag name
            *generally* (but not exclusively) corresponds to the name of an attribute on the model
            being indexed (i.e. a column in the database).

            If the tag is quoted, the attribute will be filtered exactly. If the tag is unquoted,
            generally a partial match will be used to filter the query (i.e. in terms of the
            implementation
            this means the database operation `ILIKE` will typically be used).

            Once the tagged filters are extracted from the search query, the remaining text is just
            used to search various documented attributes of the object.

            ## GitHub-style Tags Available

            `name`
            : The history's name.

            `annotation`
            : The history's annotation. (The tag `a` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The history's tags. (The tag `t` can be used a short hand alias for this tag to filter
            on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Historys: `title`, `description`, `slug`, `tag`.

        all_ (bool | None | Unset): Whether all histories from other users in this Galaxy should
            be included. Only admins are allowed to query all histories. Default: False.
        deleted (bool | None | Unset): Whether to return only deleted items. Default: False.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        show_archived=show_archived,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
        all_=all_,
        deleted=deleted,
        q=q,
        qv=qv,
        order=order,
        view=view,
        keys=keys,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    show_archived: bool | None | Unset = UNSET,
    sort_by: HistoriesIndexSortAttribute | Unset = HistoriesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    all_: bool | None | Unset = False,
    deleted: bool | None | Unset = False,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Returns histories available to the current user.

    Args:
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        show_archived (bool | None | Unset): Whether to include archived histories.
        sort_by (HistoriesIndexSortAttribute | Unset): Sort index by this specified attribute
            Default: HistoriesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: True.
        search (None | str | Unset): A mix of free text and GitHub-style tags used to filter the
            index operation.

            ## Query Structure

            GitHub-style filter tags (not be confused with Galaxy tags) are tags of the form
            `<tag_name>:<text_no_spaces>` or `<tag_name>:'<text with potential spaces>'`. The tag name
            *generally* (but not exclusively) corresponds to the name of an attribute on the model
            being indexed (i.e. a column in the database).

            If the tag is quoted, the attribute will be filtered exactly. If the tag is unquoted,
            generally a partial match will be used to filter the query (i.e. in terms of the
            implementation
            this means the database operation `ILIKE` will typically be used).

            Once the tagged filters are extracted from the search query, the remaining text is just
            used to search various documented attributes of the object.

            ## GitHub-style Tags Available

            `name`
            : The history's name.

            `annotation`
            : The history's annotation. (The tag `a` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The history's tags. (The tag `t` can be used a short hand alias for this tag to filter
            on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Historys: `title`, `description`, `slug`, `tag`.

        all_ (bool | None | Unset): Whether all histories from other users in this Galaxy should
            be included. Only admins are allowed to query all histories. Default: False.
        deleted (bool | None | Unset): Whether to return only deleted items. Default: False.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        show_archived=show_archived,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
        all_=all_,
        deleted=deleted,
        q=q,
        qv=qv,
        order=order,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    show_archived: bool | None | Unset = UNSET,
    sort_by: HistoriesIndexSortAttribute | Unset = HistoriesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    all_: bool | None | Unset = False,
    deleted: bool | None | Unset = False,
    q: list[str] | None | Unset = UNSET,
    qv: list[str] | None | Unset = UNSET,
    order: None | str | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Returns histories available to the current user.

    Args:
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        show_archived (bool | None | Unset): Whether to include archived histories.
        sort_by (HistoriesIndexSortAttribute | Unset): Sort index by this specified attribute
            Default: HistoriesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: True.
        search (None | str | Unset): A mix of free text and GitHub-style tags used to filter the
            index operation.

            ## Query Structure

            GitHub-style filter tags (not be confused with Galaxy tags) are tags of the form
            `<tag_name>:<text_no_spaces>` or `<tag_name>:'<text with potential spaces>'`. The tag name
            *generally* (but not exclusively) corresponds to the name of an attribute on the model
            being indexed (i.e. a column in the database).

            If the tag is quoted, the attribute will be filtered exactly. If the tag is unquoted,
            generally a partial match will be used to filter the query (i.e. in terms of the
            implementation
            this means the database operation `ILIKE` will typically be used).

            Once the tagged filters are extracted from the search query, the remaining text is just
            used to search various documented attributes of the object.

            ## GitHub-style Tags Available

            `name`
            : The history's name.

            `annotation`
            : The history's annotation. (The tag `a` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The history's tags. (The tag `t` can be used a short hand alias for this tag to filter
            on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Historys: `title`, `description`, `slug`, `tag`.

        all_ (bool | None | Unset): Whether all histories from other users in this Galaxy should
            be included. Only admins are allowed to query all histories. Default: False.
        deleted (bool | None | Unset): Whether to return only deleted items. Default: False.
        q (list[str] | None | Unset): Generally a property name to filter by followed by an (often
            optional) hyphen and operator string.
        qv (list[str] | None | Unset): The value to filter by.
        order (None | str | Unset): String containing one of the valid ordering attributes
            followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively.
            Orders can be stacked as a comma-separated list of values.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
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
            client=client,
            limit=limit,
            offset=offset,
            show_own=show_own,
            show_published=show_published,
            show_shared=show_shared,
            show_archived=show_archived,
            sort_by=sort_by,
            sort_desc=sort_desc,
            search=search,
            all_=all_,
            deleted=deleted,
            q=q,
            qv=qv,
            order=order,
            view=view,
            keys=keys,
            run_as=run_as,
        )
    ).parsed
