from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.page_summary import PageSummary
from ...models.pages_index_sort_attribute import PagesIndexSortAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    deleted: bool | Unset = False,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    search: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: PagesIndexSortAttribute | Unset = PagesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["deleted"] = deleted

    params["limit"] = limit

    params["offset"] = offset

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["show_own"] = show_own

    params["show_published"] = show_published

    params["show_shared"] = show_shared

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["sort_desc"] = sort_desc

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/pages",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[PageSummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_page_summary_list_item_data in _response_200:
            componentsschemas_page_summary_list_item = PageSummary.from_dict(
                componentsschemas_page_summary_list_item_data
            )

            response_200.append(componentsschemas_page_summary_list_item)

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
) -> Response[MessageExceptionModel | list[PageSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    search: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: PagesIndexSortAttribute | Unset = PagesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[PageSummary]]:
    """Lists all Pages viewable by the user.

     Get a list with summary information of all Pages available to the user.

    Args:
        deleted (bool | Unset): Whether to include deleted pages in the result. Default: False.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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

            `title`
            : The page's title.

            `slug`
            : The page's slug. (The tag `s` can be used a short hand alias for this tag to filter on
            this attribute.)

            `tag`
            : The page's tags. (The tag `t` can be used a short hand alias for this tag to filter on
            this attribute.)

            `user`
            : The page's owner's username. (The tag `u` can be used a short hand alias for this tag to
            filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Pages: `title`, `slug`, `tag`, `user`.

        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (PagesIndexSortAttribute | Unset): Sort page index by this specified attribute on
            the page model Default: PagesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        user_id (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[PageSummary]]
    """

    kwargs = _get_kwargs(
        deleted=deleted,
        limit=limit,
        offset=offset,
        search=search,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        user_id=user_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    search: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: PagesIndexSortAttribute | Unset = PagesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[PageSummary] | None:
    """Lists all Pages viewable by the user.

     Get a list with summary information of all Pages available to the user.

    Args:
        deleted (bool | Unset): Whether to include deleted pages in the result. Default: False.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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

            `title`
            : The page's title.

            `slug`
            : The page's slug. (The tag `s` can be used a short hand alias for this tag to filter on
            this attribute.)

            `tag`
            : The page's tags. (The tag `t` can be used a short hand alias for this tag to filter on
            this attribute.)

            `user`
            : The page's owner's username. (The tag `u` can be used a short hand alias for this tag to
            filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Pages: `title`, `slug`, `tag`, `user`.

        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (PagesIndexSortAttribute | Unset): Sort page index by this specified attribute on
            the page model Default: PagesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        user_id (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[PageSummary]
    """

    return sync_detailed(
        client=client,
        deleted=deleted,
        limit=limit,
        offset=offset,
        search=search,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        user_id=user_id,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    search: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: PagesIndexSortAttribute | Unset = PagesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[PageSummary]]:
    """Lists all Pages viewable by the user.

     Get a list with summary information of all Pages available to the user.

    Args:
        deleted (bool | Unset): Whether to include deleted pages in the result. Default: False.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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

            `title`
            : The page's title.

            `slug`
            : The page's slug. (The tag `s` can be used a short hand alias for this tag to filter on
            this attribute.)

            `tag`
            : The page's tags. (The tag `t` can be used a short hand alias for this tag to filter on
            this attribute.)

            `user`
            : The page's owner's username. (The tag `u` can be used a short hand alias for this tag to
            filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Pages: `title`, `slug`, `tag`, `user`.

        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (PagesIndexSortAttribute | Unset): Sort page index by this specified attribute on
            the page model Default: PagesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        user_id (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[PageSummary]]
    """

    kwargs = _get_kwargs(
        deleted=deleted,
        limit=limit,
        offset=offset,
        search=search,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        user_id=user_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    search: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: PagesIndexSortAttribute | Unset = PagesIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[PageSummary] | None:
    """Lists all Pages viewable by the user.

     Get a list with summary information of all Pages available to the user.

    Args:
        deleted (bool | Unset): Whether to include deleted pages in the result. Default: False.
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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

            `title`
            : The page's title.

            `slug`
            : The page's slug. (The tag `s` can be used a short hand alias for this tag to filter on
            this attribute.)

            `tag`
            : The page's tags. (The tag `t` can be used a short hand alias for this tag to filter on
            this attribute.)

            `user`
            : The page's owner's username. (The tag `u` can be used a short hand alias for this tag to
            filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Pages: `title`, `slug`, `tag`, `user`.

        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (PagesIndexSortAttribute | Unset): Sort page index by this specified attribute on
            the page model Default: PagesIndexSortAttribute.UPDATE_TIME.
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        user_id (None | str | Unset):
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[PageSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            deleted=deleted,
            limit=limit,
            offset=offset,
            search=search,
            show_own=show_own,
            show_published=show_published,
            show_shared=show_shared,
            sort_by=sort_by,
            sort_desc=sort_desc,
            user_id=user_id,
            run_as=run_as,
        )
    ).parsed
