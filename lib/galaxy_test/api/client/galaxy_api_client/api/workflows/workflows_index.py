from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.workflows_index_response_200_item import WorkflowsIndexResponse200Item
from ...models.workflows_index_sort_by_type_0 import WorkflowsIndexSortByType0
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_deleted: bool | Unset = False,
    show_hidden: bool | Unset = False,
    missing_tools: bool | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    sort_by: None | Unset | WorkflowsIndexSortByType0 = UNSET,
    sort_desc: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    search: None | str | Unset = UNSET,
    skip_step_counts: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["show_deleted"] = show_deleted

    params["show_hidden"] = show_hidden

    params["missing_tools"] = missing_tools

    json_show_published: bool | None | Unset
    if isinstance(show_published, Unset):
        json_show_published = UNSET
    else:
        json_show_published = show_published
    params["show_published"] = json_show_published

    json_show_shared: bool | None | Unset
    if isinstance(show_shared, Unset):
        json_show_shared = UNSET
    else:
        json_show_shared = show_shared
    params["show_shared"] = json_show_shared

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, WorkflowsIndexSortByType0):
        json_sort_by = sort_by.value
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    json_sort_desc: bool | None | Unset
    if isinstance(sort_desc, Unset):
        json_sort_desc = UNSET
    else:
        json_sort_desc = sort_desc
    params["sort_desc"] = json_sort_desc

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

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["skip_step_counts"] = skip_step_counts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/workflows",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[WorkflowsIndexResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WorkflowsIndexResponse200Item.from_dict(response_200_item_data)

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
) -> Response[MessageExceptionModel | list[WorkflowsIndexResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | Unset = False,
    show_hidden: bool | Unset = False,
    missing_tools: bool | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    sort_by: None | Unset | WorkflowsIndexSortByType0 = UNSET,
    sort_desc: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    search: None | str | Unset = UNSET,
    skip_step_counts: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowsIndexResponse200Item]]:
    """Lists stored workflows viewable by the user.

     Lists stored workflows viewable by the user.

    Args:
        show_deleted (bool | Unset): Whether to restrict result to deleted workflows. Default:
            False.
        show_hidden (bool | Unset): Whether to restrict result to hidden workflows. Default:
            False.
        missing_tools (bool | Unset): Whether to include a list of missing tools per workflow
            entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        sort_by (None | Unset | WorkflowsIndexSortByType0): In unspecified, default ordering
            depends on other parameters but generally the user's own workflows appear first based on
            update time
        sort_desc (bool | None | Unset): Sort in descending order?
        limit (int | None | Unset):
        offset (int | None | Unset):  Default: 0.
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
            : The stored workflow's name. (The tag `n` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The workflow's tag, if the tag contains a colon an approach will be made to match the
            key and value of the tag separately. (The tag `t` can be used a short hand alias for this
            tag to filter on this attribute.)

            `user`
            : The stored workflow's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            `is:published`
            : Include only published workflows in the final result. Be sure the query parameter
            `show_published` is set to `true` if to include all published workflows and not just the
            requesting user's.

            `is:importable`
            : Include only importable workflows in the final result.

            `is:deleted`
            : Include only deleted workflows in the final result.

            `is:shared_with_me`
            : Include only workflows shared with the requesting user.  Be sure the query parameter
            `show_shared` is set to `true` if to include shared workflows.

            `is:bookmarked`
            : Include only workflows bookmarked by the requesting user.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Stored Workflows: `name`, `tag`, `user`.

        skip_step_counts (bool | Unset): Set this to true to skip joining workflow step counts and
            optimize the resulting index query. Response objects will not contain step counts.
            Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowsIndexResponse200Item]]
    """

    kwargs = _get_kwargs(
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        limit=limit,
        offset=offset,
        search=search,
        skip_step_counts=skip_step_counts,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | Unset = False,
    show_hidden: bool | Unset = False,
    missing_tools: bool | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    sort_by: None | Unset | WorkflowsIndexSortByType0 = UNSET,
    sort_desc: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    search: None | str | Unset = UNSET,
    skip_step_counts: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowsIndexResponse200Item] | None:
    """Lists stored workflows viewable by the user.

     Lists stored workflows viewable by the user.

    Args:
        show_deleted (bool | Unset): Whether to restrict result to deleted workflows. Default:
            False.
        show_hidden (bool | Unset): Whether to restrict result to hidden workflows. Default:
            False.
        missing_tools (bool | Unset): Whether to include a list of missing tools per workflow
            entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        sort_by (None | Unset | WorkflowsIndexSortByType0): In unspecified, default ordering
            depends on other parameters but generally the user's own workflows appear first based on
            update time
        sort_desc (bool | None | Unset): Sort in descending order?
        limit (int | None | Unset):
        offset (int | None | Unset):  Default: 0.
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
            : The stored workflow's name. (The tag `n` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The workflow's tag, if the tag contains a colon an approach will be made to match the
            key and value of the tag separately. (The tag `t` can be used a short hand alias for this
            tag to filter on this attribute.)

            `user`
            : The stored workflow's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            `is:published`
            : Include only published workflows in the final result. Be sure the query parameter
            `show_published` is set to `true` if to include all published workflows and not just the
            requesting user's.

            `is:importable`
            : Include only importable workflows in the final result.

            `is:deleted`
            : Include only deleted workflows in the final result.

            `is:shared_with_me`
            : Include only workflows shared with the requesting user.  Be sure the query parameter
            `show_shared` is set to `true` if to include shared workflows.

            `is:bookmarked`
            : Include only workflows bookmarked by the requesting user.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Stored Workflows: `name`, `tag`, `user`.

        skip_step_counts (bool | Unset): Set this to true to skip joining workflow step counts and
            optimize the resulting index query. Response objects will not contain step counts.
            Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowsIndexResponse200Item]
    """

    return sync_detailed(
        client=client,
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        limit=limit,
        offset=offset,
        search=search,
        skip_step_counts=skip_step_counts,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | Unset = False,
    show_hidden: bool | Unset = False,
    missing_tools: bool | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    sort_by: None | Unset | WorkflowsIndexSortByType0 = UNSET,
    sort_desc: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    search: None | str | Unset = UNSET,
    skip_step_counts: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowsIndexResponse200Item]]:
    """Lists stored workflows viewable by the user.

     Lists stored workflows viewable by the user.

    Args:
        show_deleted (bool | Unset): Whether to restrict result to deleted workflows. Default:
            False.
        show_hidden (bool | Unset): Whether to restrict result to hidden workflows. Default:
            False.
        missing_tools (bool | Unset): Whether to include a list of missing tools per workflow
            entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        sort_by (None | Unset | WorkflowsIndexSortByType0): In unspecified, default ordering
            depends on other parameters but generally the user's own workflows appear first based on
            update time
        sort_desc (bool | None | Unset): Sort in descending order?
        limit (int | None | Unset):
        offset (int | None | Unset):  Default: 0.
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
            : The stored workflow's name. (The tag `n` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The workflow's tag, if the tag contains a colon an approach will be made to match the
            key and value of the tag separately. (The tag `t` can be used a short hand alias for this
            tag to filter on this attribute.)

            `user`
            : The stored workflow's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            `is:published`
            : Include only published workflows in the final result. Be sure the query parameter
            `show_published` is set to `true` if to include all published workflows and not just the
            requesting user's.

            `is:importable`
            : Include only importable workflows in the final result.

            `is:deleted`
            : Include only deleted workflows in the final result.

            `is:shared_with_me`
            : Include only workflows shared with the requesting user.  Be sure the query parameter
            `show_shared` is set to `true` if to include shared workflows.

            `is:bookmarked`
            : Include only workflows bookmarked by the requesting user.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Stored Workflows: `name`, `tag`, `user`.

        skip_step_counts (bool | Unset): Set this to true to skip joining workflow step counts and
            optimize the resulting index query. Response objects will not contain step counts.
            Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowsIndexResponse200Item]]
    """

    kwargs = _get_kwargs(
        show_deleted=show_deleted,
        show_hidden=show_hidden,
        missing_tools=missing_tools,
        show_published=show_published,
        show_shared=show_shared,
        sort_by=sort_by,
        sort_desc=sort_desc,
        limit=limit,
        offset=offset,
        search=search,
        skip_step_counts=skip_step_counts,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    show_deleted: bool | Unset = False,
    show_hidden: bool | Unset = False,
    missing_tools: bool | Unset = False,
    show_published: bool | None | Unset = UNSET,
    show_shared: bool | None | Unset = UNSET,
    sort_by: None | Unset | WorkflowsIndexSortByType0 = UNSET,
    sort_desc: bool | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = 0,
    search: None | str | Unset = UNSET,
    skip_step_counts: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowsIndexResponse200Item] | None:
    """Lists stored workflows viewable by the user.

     Lists stored workflows viewable by the user.

    Args:
        show_deleted (bool | Unset): Whether to restrict result to deleted workflows. Default:
            False.
        show_hidden (bool | Unset): Whether to restrict result to hidden workflows. Default:
            False.
        missing_tools (bool | Unset): Whether to include a list of missing tools per workflow
            entry Default: False.
        show_published (bool | None | Unset):
        show_shared (bool | None | Unset):
        sort_by (None | Unset | WorkflowsIndexSortByType0): In unspecified, default ordering
            depends on other parameters but generally the user's own workflows appear first based on
            update time
        sort_desc (bool | None | Unset): Sort in descending order?
        limit (int | None | Unset):
        offset (int | None | Unset):  Default: 0.
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
            : The stored workflow's name. (The tag `n` can be used a short hand alias for this tag to
            filter on this attribute.)

            `tag`
            : The workflow's tag, if the tag contains a colon an approach will be made to match the
            key and value of the tag separately. (The tag `t` can be used a short hand alias for this
            tag to filter on this attribute.)

            `user`
            : The stored workflow's owner's username. (The tag `u` can be used a short hand alias for
            this tag to filter on this attribute.)

            `is:published`
            : Include only published workflows in the final result. Be sure the query parameter
            `show_published` is set to `true` if to include all published workflows and not just the
            requesting user's.

            `is:importable`
            : Include only importable workflows in the final result.

            `is:deleted`
            : Include only deleted workflows in the final result.

            `is:shared_with_me`
            : Include only workflows shared with the requesting user.  Be sure the query parameter
            `show_shared` is set to `true` if to include shared workflows.

            `is:bookmarked`
            : Include only workflows bookmarked by the requesting user.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Stored Workflows: `name`, `tag`, `user`.

        skip_step_counts (bool | Unset): Set this to true to skip joining workflow step counts and
            optimize the resulting index query. Response objects will not contain step counts.
            Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowsIndexResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            show_deleted=show_deleted,
            show_hidden=show_hidden,
            missing_tools=missing_tools,
            show_published=show_published,
            show_shared=show_shared,
            sort_by=sort_by,
            sort_desc=sort_desc,
            limit=limit,
            offset=offset,
            search=search,
            skip_step_counts=skip_step_counts,
            run_as=run_as,
        )
    ).parsed
