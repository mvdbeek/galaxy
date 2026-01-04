import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_index_sort_by_enum import JobIndexSortByEnum
from ...models.job_index_view_enum import JobIndexViewEnum
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_details: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    view: JobIndexViewEnum | Unset = UNSET,
    date_range_min: datetime.date | datetime.datetime | None | Unset = UNSET,
    date_range_max: datetime.date | datetime.datetime | None | Unset = UNSET,
    history_id: None | str | Unset = UNSET,
    workflow_id: None | str | Unset = UNSET,
    invocation_id: None | str | Unset = UNSET,
    implicit_collection_jobs_id: None | str | Unset = UNSET,
    tool_request_id: None | str | Unset = UNSET,
    order_by: JobIndexSortByEnum | Unset = UNSET,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    state: list[str] | None | Unset = UNSET,
    tool_id: list[str] | None | Unset = UNSET,
    tool_id_like: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["user_details"] = user_details

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_date_range_min: None | str | Unset
    if isinstance(date_range_min, Unset):
        json_date_range_min = UNSET
    elif isinstance(date_range_min, datetime.datetime):
        json_date_range_min = date_range_min.isoformat()
    elif isinstance(date_range_min, datetime.date):
        json_date_range_min = date_range_min.isoformat()
    else:
        json_date_range_min = date_range_min
    params["date_range_min"] = json_date_range_min

    json_date_range_max: None | str | Unset
    if isinstance(date_range_max, Unset):
        json_date_range_max = UNSET
    elif isinstance(date_range_max, datetime.datetime):
        json_date_range_max = date_range_max.isoformat()
    elif isinstance(date_range_max, datetime.date):
        json_date_range_max = date_range_max.isoformat()
    else:
        json_date_range_max = date_range_max
    params["date_range_max"] = json_date_range_max

    json_history_id: None | str | Unset
    if isinstance(history_id, Unset):
        json_history_id = UNSET
    else:
        json_history_id = history_id
    params["history_id"] = json_history_id

    json_workflow_id: None | str | Unset
    if isinstance(workflow_id, Unset):
        json_workflow_id = UNSET
    else:
        json_workflow_id = workflow_id
    params["workflow_id"] = json_workflow_id

    json_invocation_id: None | str | Unset
    if isinstance(invocation_id, Unset):
        json_invocation_id = UNSET
    else:
        json_invocation_id = invocation_id
    params["invocation_id"] = json_invocation_id

    json_implicit_collection_jobs_id: None | str | Unset
    if isinstance(implicit_collection_jobs_id, Unset):
        json_implicit_collection_jobs_id = UNSET
    else:
        json_implicit_collection_jobs_id = implicit_collection_jobs_id
    params["implicit_collection_jobs_id"] = json_implicit_collection_jobs_id

    json_tool_request_id: None | str | Unset
    if isinstance(tool_request_id, Unset):
        json_tool_request_id = UNSET
    else:
        json_tool_request_id = tool_request_id
    params["tool_request_id"] = json_tool_request_id

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["limit"] = limit

    params["offset"] = offset

    json_state: list[str] | None | Unset
    if isinstance(state, Unset):
        json_state = UNSET
    elif isinstance(state, list):
        json_state = state

    else:
        json_state = state
    params["state"] = json_state

    json_tool_id: list[str] | None | Unset
    if isinstance(tool_id, Unset):
        json_tool_id = UNSET
    elif isinstance(tool_id, list):
        json_tool_id = tool_id

    else:
        json_tool_id = tool_id
    params["tool_id"] = json_tool_id

    json_tool_id_like: list[str] | None | Unset
    if isinstance(tool_id_like, Unset):
        json_tool_id_like = UNSET
    elif isinstance(tool_id_like, list):
        json_tool_id_like = tool_id_like

    else:
        json_tool_id_like = tool_id_like
    params["tool_id_like"] = json_tool_id_like

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs",
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
    user_details: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    view: JobIndexViewEnum | Unset = UNSET,
    date_range_min: datetime.date | datetime.datetime | None | Unset = UNSET,
    date_range_max: datetime.date | datetime.datetime | None | Unset = UNSET,
    history_id: None | str | Unset = UNSET,
    workflow_id: None | str | Unset = UNSET,
    invocation_id: None | str | Unset = UNSET,
    implicit_collection_jobs_id: None | str | Unset = UNSET,
    tool_request_id: None | str | Unset = UNSET,
    order_by: JobIndexSortByEnum | Unset = UNSET,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    state: list[str] | None | Unset = UNSET,
    tool_id: list[str] | None | Unset = UNSET,
    tool_id_like: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Index

    Args:
        user_details (bool | Unset): If true, and requester is an admin, will return external job
            id and user email. This is only available to admins. Default: False.
        user_id (None | str | Unset): an encoded user id to restrict query to, must be own id if
            not admin user
        view (JobIndexViewEnum | Unset):
        date_range_min (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated after specified date (e.g. '2014-01-01')
        date_range_max (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated before specified date (e.g. '2014-01-01')
        history_id (None | str | Unset): Limit listing of jobs to those that match the history_id.
            If none, jobs from any history may be returned.
        workflow_id (None | str | Unset): Limit listing of jobs to those that match the specified
            workflow ID. If none, jobs from any workflow (or from no workflows) may be returned.
        invocation_id (None | str | Unset): Limit listing of jobs to those that match the
            specified workflow invocation ID. If none, jobs from any workflow invocation (or from no
            workflows) may be returned.
        implicit_collection_jobs_id (None | str | Unset): Limit listing of jobs to those that
            match the specified implicit collection job ID. If none, jobs from any implicit collection
            execution (or from no implicit collection execution) may be returned.
        tool_request_id (None | str | Unset): Limit listing of jobs to those that were created
            from the supplied tool request ID. If none, jobs from any tool request (or from no
            workflows) may be returned.
        order_by (JobIndexSortByEnum | Unset):
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

            `user`
            : The user email of the user that executed the Job. (The tag `u` can be used a short hand
            alias for this tag to filter on this attribute.)

            `tool_id`
            : The tool ID corresponding to the job. (The tag `t` can be used a short hand alias for
            this tag to filter on this attribute.)

            `runner`
            : The job runner name used to execute the job. (The tag `r` can be used a short hand alias
            for this tag to filter on this attribute.) This tag is only available for requests using
            admin keys and/or sessions.

            `handler`
            : The job handler name used to execute the job. (The tag `h` can be used a short hand
            alias for this tag to filter on this attribute.) This tag is only available for requests
            using admin keys and/or sessions.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Jobs: `user`, `tool`, `handler`, `runner`.

        limit (int | Unset): Maximum number of jobs to return. Default: 500.
        offset (int | Unset): Return jobs starting from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, jobs 200-299 will be returned. Default: 0.
        state (list[str] | None | Unset): A list or comma-separated list of states to filter job
            query on. If unspecified, jobs of any state may be returned.
        tool_id (list[str] | None | Unset): Limit listing of jobs to those that match one of the
            included tool_ids. If none, all are returned
        tool_id_like (list[str] | None | Unset): Limit listing of jobs to those that match one of
            the included tool ID sql-like patterns. If none, all are returned
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_details=user_details,
        user_id=user_id,
        view=view,
        date_range_min=date_range_min,
        date_range_max=date_range_max,
        history_id=history_id,
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        implicit_collection_jobs_id=implicit_collection_jobs_id,
        tool_request_id=tool_request_id,
        order_by=order_by,
        search=search,
        limit=limit,
        offset=offset,
        state=state,
        tool_id=tool_id,
        tool_id_like=tool_id_like,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_details: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    view: JobIndexViewEnum | Unset = UNSET,
    date_range_min: datetime.date | datetime.datetime | None | Unset = UNSET,
    date_range_max: datetime.date | datetime.datetime | None | Unset = UNSET,
    history_id: None | str | Unset = UNSET,
    workflow_id: None | str | Unset = UNSET,
    invocation_id: None | str | Unset = UNSET,
    implicit_collection_jobs_id: None | str | Unset = UNSET,
    tool_request_id: None | str | Unset = UNSET,
    order_by: JobIndexSortByEnum | Unset = UNSET,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    state: list[str] | None | Unset = UNSET,
    tool_id: list[str] | None | Unset = UNSET,
    tool_id_like: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Index

    Args:
        user_details (bool | Unset): If true, and requester is an admin, will return external job
            id and user email. This is only available to admins. Default: False.
        user_id (None | str | Unset): an encoded user id to restrict query to, must be own id if
            not admin user
        view (JobIndexViewEnum | Unset):
        date_range_min (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated after specified date (e.g. '2014-01-01')
        date_range_max (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated before specified date (e.g. '2014-01-01')
        history_id (None | str | Unset): Limit listing of jobs to those that match the history_id.
            If none, jobs from any history may be returned.
        workflow_id (None | str | Unset): Limit listing of jobs to those that match the specified
            workflow ID. If none, jobs from any workflow (or from no workflows) may be returned.
        invocation_id (None | str | Unset): Limit listing of jobs to those that match the
            specified workflow invocation ID. If none, jobs from any workflow invocation (or from no
            workflows) may be returned.
        implicit_collection_jobs_id (None | str | Unset): Limit listing of jobs to those that
            match the specified implicit collection job ID. If none, jobs from any implicit collection
            execution (or from no implicit collection execution) may be returned.
        tool_request_id (None | str | Unset): Limit listing of jobs to those that were created
            from the supplied tool request ID. If none, jobs from any tool request (or from no
            workflows) may be returned.
        order_by (JobIndexSortByEnum | Unset):
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

            `user`
            : The user email of the user that executed the Job. (The tag `u` can be used a short hand
            alias for this tag to filter on this attribute.)

            `tool_id`
            : The tool ID corresponding to the job. (The tag `t` can be used a short hand alias for
            this tag to filter on this attribute.)

            `runner`
            : The job runner name used to execute the job. (The tag `r` can be used a short hand alias
            for this tag to filter on this attribute.) This tag is only available for requests using
            admin keys and/or sessions.

            `handler`
            : The job handler name used to execute the job. (The tag `h` can be used a short hand
            alias for this tag to filter on this attribute.) This tag is only available for requests
            using admin keys and/or sessions.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Jobs: `user`, `tool`, `handler`, `runner`.

        limit (int | Unset): Maximum number of jobs to return. Default: 500.
        offset (int | Unset): Return jobs starting from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, jobs 200-299 will be returned. Default: 0.
        state (list[str] | None | Unset): A list or comma-separated list of states to filter job
            query on. If unspecified, jobs of any state may be returned.
        tool_id (list[str] | None | Unset): Limit listing of jobs to those that match one of the
            included tool_ids. If none, all are returned
        tool_id_like (list[str] | None | Unset): Limit listing of jobs to those that match one of
            the included tool ID sql-like patterns. If none, all are returned
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
        user_details=user_details,
        user_id=user_id,
        view=view,
        date_range_min=date_range_min,
        date_range_max=date_range_max,
        history_id=history_id,
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        implicit_collection_jobs_id=implicit_collection_jobs_id,
        tool_request_id=tool_request_id,
        order_by=order_by,
        search=search,
        limit=limit,
        offset=offset,
        state=state,
        tool_id=tool_id,
        tool_id_like=tool_id_like,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_details: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    view: JobIndexViewEnum | Unset = UNSET,
    date_range_min: datetime.date | datetime.datetime | None | Unset = UNSET,
    date_range_max: datetime.date | datetime.datetime | None | Unset = UNSET,
    history_id: None | str | Unset = UNSET,
    workflow_id: None | str | Unset = UNSET,
    invocation_id: None | str | Unset = UNSET,
    implicit_collection_jobs_id: None | str | Unset = UNSET,
    tool_request_id: None | str | Unset = UNSET,
    order_by: JobIndexSortByEnum | Unset = UNSET,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    state: list[str] | None | Unset = UNSET,
    tool_id: list[str] | None | Unset = UNSET,
    tool_id_like: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Index

    Args:
        user_details (bool | Unset): If true, and requester is an admin, will return external job
            id and user email. This is only available to admins. Default: False.
        user_id (None | str | Unset): an encoded user id to restrict query to, must be own id if
            not admin user
        view (JobIndexViewEnum | Unset):
        date_range_min (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated after specified date (e.g. '2014-01-01')
        date_range_max (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated before specified date (e.g. '2014-01-01')
        history_id (None | str | Unset): Limit listing of jobs to those that match the history_id.
            If none, jobs from any history may be returned.
        workflow_id (None | str | Unset): Limit listing of jobs to those that match the specified
            workflow ID. If none, jobs from any workflow (or from no workflows) may be returned.
        invocation_id (None | str | Unset): Limit listing of jobs to those that match the
            specified workflow invocation ID. If none, jobs from any workflow invocation (or from no
            workflows) may be returned.
        implicit_collection_jobs_id (None | str | Unset): Limit listing of jobs to those that
            match the specified implicit collection job ID. If none, jobs from any implicit collection
            execution (or from no implicit collection execution) may be returned.
        tool_request_id (None | str | Unset): Limit listing of jobs to those that were created
            from the supplied tool request ID. If none, jobs from any tool request (or from no
            workflows) may be returned.
        order_by (JobIndexSortByEnum | Unset):
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

            `user`
            : The user email of the user that executed the Job. (The tag `u` can be used a short hand
            alias for this tag to filter on this attribute.)

            `tool_id`
            : The tool ID corresponding to the job. (The tag `t` can be used a short hand alias for
            this tag to filter on this attribute.)

            `runner`
            : The job runner name used to execute the job. (The tag `r` can be used a short hand alias
            for this tag to filter on this attribute.) This tag is only available for requests using
            admin keys and/or sessions.

            `handler`
            : The job handler name used to execute the job. (The tag `h` can be used a short hand
            alias for this tag to filter on this attribute.) This tag is only available for requests
            using admin keys and/or sessions.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Jobs: `user`, `tool`, `handler`, `runner`.

        limit (int | Unset): Maximum number of jobs to return. Default: 500.
        offset (int | Unset): Return jobs starting from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, jobs 200-299 will be returned. Default: 0.
        state (list[str] | None | Unset): A list or comma-separated list of states to filter job
            query on. If unspecified, jobs of any state may be returned.
        tool_id (list[str] | None | Unset): Limit listing of jobs to those that match one of the
            included tool_ids. If none, all are returned
        tool_id_like (list[str] | None | Unset): Limit listing of jobs to those that match one of
            the included tool ID sql-like patterns. If none, all are returned
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        user_details=user_details,
        user_id=user_id,
        view=view,
        date_range_min=date_range_min,
        date_range_max=date_range_max,
        history_id=history_id,
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        implicit_collection_jobs_id=implicit_collection_jobs_id,
        tool_request_id=tool_request_id,
        order_by=order_by,
        search=search,
        limit=limit,
        offset=offset,
        state=state,
        tool_id=tool_id,
        tool_id_like=tool_id_like,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_details: bool | Unset = False,
    user_id: None | str | Unset = UNSET,
    view: JobIndexViewEnum | Unset = UNSET,
    date_range_min: datetime.date | datetime.datetime | None | Unset = UNSET,
    date_range_max: datetime.date | datetime.datetime | None | Unset = UNSET,
    history_id: None | str | Unset = UNSET,
    workflow_id: None | str | Unset = UNSET,
    invocation_id: None | str | Unset = UNSET,
    implicit_collection_jobs_id: None | str | Unset = UNSET,
    tool_request_id: None | str | Unset = UNSET,
    order_by: JobIndexSortByEnum | Unset = UNSET,
    search: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
    state: list[str] | None | Unset = UNSET,
    tool_id: list[str] | None | Unset = UNSET,
    tool_id_like: list[str] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Index

    Args:
        user_details (bool | Unset): If true, and requester is an admin, will return external job
            id and user email. This is only available to admins. Default: False.
        user_id (None | str | Unset): an encoded user id to restrict query to, must be own id if
            not admin user
        view (JobIndexViewEnum | Unset):
        date_range_min (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated after specified date (e.g. '2014-01-01')
        date_range_max (datetime.date | datetime.datetime | None | Unset): Limit listing of jobs
            to those that are updated before specified date (e.g. '2014-01-01')
        history_id (None | str | Unset): Limit listing of jobs to those that match the history_id.
            If none, jobs from any history may be returned.
        workflow_id (None | str | Unset): Limit listing of jobs to those that match the specified
            workflow ID. If none, jobs from any workflow (or from no workflows) may be returned.
        invocation_id (None | str | Unset): Limit listing of jobs to those that match the
            specified workflow invocation ID. If none, jobs from any workflow invocation (or from no
            workflows) may be returned.
        implicit_collection_jobs_id (None | str | Unset): Limit listing of jobs to those that
            match the specified implicit collection job ID. If none, jobs from any implicit collection
            execution (or from no implicit collection execution) may be returned.
        tool_request_id (None | str | Unset): Limit listing of jobs to those that were created
            from the supplied tool request ID. If none, jobs from any tool request (or from no
            workflows) may be returned.
        order_by (JobIndexSortByEnum | Unset):
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

            `user`
            : The user email of the user that executed the Job. (The tag `u` can be used a short hand
            alias for this tag to filter on this attribute.)

            `tool_id`
            : The tool ID corresponding to the job. (The tag `t` can be used a short hand alias for
            this tag to filter on this attribute.)

            `runner`
            : The job runner name used to execute the job. (The tag `r` can be used a short hand alias
            for this tag to filter on this attribute.) This tag is only available for requests using
            admin keys and/or sessions.

            `handler`
            : The job handler name used to execute the job. (The tag `h` can be used a short hand
            alias for this tag to filter on this attribute.) This tag is only available for requests
            using admin keys and/or sessions.

            ## Free Text

            Free text search terms will be searched against the following attributes of the
            Jobs: `user`, `tool`, `handler`, `runner`.

        limit (int | Unset): Maximum number of jobs to return. Default: 500.
        offset (int | Unset): Return jobs starting from this specified position. For example, if
            ``limit`` is set to 100 and ``offset`` to 200, jobs 200-299 will be returned. Default: 0.
        state (list[str] | None | Unset): A list or comma-separated list of states to filter job
            query on. If unspecified, jobs of any state may be returned.
        tool_id (list[str] | None | Unset): Limit listing of jobs to those that match one of the
            included tool_ids. If none, all are returned
        tool_id_like (list[str] | None | Unset): Limit listing of jobs to those that match one of
            the included tool ID sql-like patterns. If none, all are returned
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
            user_details=user_details,
            user_id=user_id,
            view=view,
            date_range_min=date_range_min,
            date_range_max=date_range_max,
            history_id=history_id,
            workflow_id=workflow_id,
            invocation_id=invocation_id,
            implicit_collection_jobs_id=implicit_collection_jobs_id,
            tool_request_id=tool_request_id,
            order_by=order_by,
            search=search,
            limit=limit,
            offset=offset,
            state=state,
            tool_id=tool_id,
            tool_id_like=tool_id_like,
            run_as=run_as,
        )
    ).parsed
