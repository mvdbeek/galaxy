from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.visualization_summary import VisualizationSummary
from ...models.visualizations_index_sort_attribute import VisualizationsIndexSortAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    deleted: bool | Unset = False,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    user_id: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: VisualizationsIndexSortAttribute | Unset = VisualizationsIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["deleted"] = deleted

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

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    params["show_own"] = show_own

    params["show_published"] = show_published

    params["show_shared"] = show_shared

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/visualizations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[VisualizationSummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_visualization_summary_list_item_data in _response_200:
            componentsschemas_visualization_summary_list_item = VisualizationSummary.from_dict(
                componentsschemas_visualization_summary_list_item_data
            )

            response_200.append(componentsschemas_visualization_summary_list_item)

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
) -> Response[MessageExceptionModel | list[VisualizationSummary]]:
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
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    user_id: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: VisualizationsIndexSortAttribute | Unset = VisualizationsIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[VisualizationSummary]]:
    """Returns visualizations for the current user.

    Args:
        deleted (bool | Unset): Whether to include deleted visualizations in the result. Default:
            False.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        user_id (None | str | Unset):
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (VisualizationsIndexSortAttribute | Unset): Sort visualization index by this
            specified attribute on the visualization model Default:
            VisualizationsIndexSortAttribute.UPDATE_TIME.
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

            `title`
            : The visualization's title.

            `slug`
            : The visualization's slug. (The tag `s` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The visualization's tags. (The tag `t` can be used a short hand alias for this tag to
            filter on this attribute.)

            `user`
            : The visualization's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Visualizations: `title`, `slug`, `tag`, `type`.

        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[VisualizationSummary]]
    """

    kwargs = _get_kwargs(
        deleted=deleted,
        limit=limit,
        offset=offset,
        user_id=user_id,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
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
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    user_id: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: VisualizationsIndexSortAttribute | Unset = VisualizationsIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[VisualizationSummary] | None:
    """Returns visualizations for the current user.

    Args:
        deleted (bool | Unset): Whether to include deleted visualizations in the result. Default:
            False.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        user_id (None | str | Unset):
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (VisualizationsIndexSortAttribute | Unset): Sort visualization index by this
            specified attribute on the visualization model Default:
            VisualizationsIndexSortAttribute.UPDATE_TIME.
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

            `title`
            : The visualization's title.

            `slug`
            : The visualization's slug. (The tag `s` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The visualization's tags. (The tag `t` can be used a short hand alias for this tag to
            filter on this attribute.)

            `user`
            : The visualization's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Visualizations: `title`, `slug`, `tag`, `type`.

        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[VisualizationSummary]
    """

    return sync_detailed(
        client=client,
        deleted=deleted,
        limit=limit,
        offset=offset,
        user_id=user_id,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    user_id: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: VisualizationsIndexSortAttribute | Unset = VisualizationsIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[VisualizationSummary]]:
    """Returns visualizations for the current user.

    Args:
        deleted (bool | Unset): Whether to include deleted visualizations in the result. Default:
            False.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        user_id (None | str | Unset):
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (VisualizationsIndexSortAttribute | Unset): Sort visualization index by this
            specified attribute on the visualization model Default:
            VisualizationsIndexSortAttribute.UPDATE_TIME.
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

            `title`
            : The visualization's title.

            `slug`
            : The visualization's slug. (The tag `s` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The visualization's tags. (The tag `t` can be used a short hand alias for this tag to
            filter on this attribute.)

            `user`
            : The visualization's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Visualizations: `title`, `slug`, `tag`, `type`.

        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[VisualizationSummary]]
    """

    kwargs = _get_kwargs(
        deleted=deleted,
        limit=limit,
        offset=offset,
        user_id=user_id,
        show_own=show_own,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        search=search,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    deleted: bool | Unset = False,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    user_id: None | str | Unset = UNSET,
    show_own: bool | Unset = True,
    show_published: bool | Unset = True,
    show_shared: bool | Unset = False,
    sort_by: VisualizationsIndexSortAttribute | Unset = VisualizationsIndexSortAttribute.UPDATE_TIME,
    sort_desc: bool | Unset = True,
    search: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[VisualizationSummary] | None:
    """Returns visualizations for the current user.

    Args:
        deleted (bool | Unset): Whether to include deleted visualizations in the result. Default:
            False.
        limit (int | None | Unset): The maximum number of items to return.
        offset (int | None | Unset): Starts at the beginning skip the first ( offset - 1 ) items
            and begin returning at the Nth item Default: 0.
        user_id (None | str | Unset):
        show_own (bool | Unset):  Default: True.
        show_published (bool | Unset):  Default: True.
        show_shared (bool | Unset):  Default: False.
        sort_by (VisualizationsIndexSortAttribute | Unset): Sort visualization index by this
            specified attribute on the visualization model Default:
            VisualizationsIndexSortAttribute.UPDATE_TIME.
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

            `title`
            : The visualization's title.

            `slug`
            : The visualization's slug. (The tag `s` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The visualization's tags. (The tag `t` can be used a short hand alias for this tag to
            filter on this attribute.)

            `user`
            : The visualization's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Visualizations: `title`, `slug`, `tag`, `type`.

        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[VisualizationSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            deleted=deleted,
            limit=limit,
            offset=offset,
            user_id=user_id,
            show_own=show_own,
            show_published=show_published,
            show_shared=show_shared,
            sort_by=sort_by,
            sort_desc=sort_desc,
            search=search,
            run_as=run_as,
        )
    ).parsed
