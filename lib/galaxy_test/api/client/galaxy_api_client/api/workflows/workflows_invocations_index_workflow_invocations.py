from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invocation_sort_by_enum import InvocationSortByEnum
from ...models.message_exception_model import MessageExceptionModel
from ...models.workflow_invocation_collection_view import WorkflowInvocationCollectionView
from ...models.workflow_invocation_element_view import WorkflowInvocationElementView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    history_id: None | str | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    sort_by: InvocationSortByEnum | None | Unset = UNSET,
    sort_desc: bool | Unset = False,
    include_terminal: bool | None | Unset = True,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    instance: bool | None | Unset = False,
    view: None | str | Unset = UNSET,
    step_details: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_history_id: None | str | Unset
    if isinstance(history_id, Unset):
        json_history_id = UNSET
    else:
        json_history_id = history_id
    params["history_id"] = json_history_id

    json_job_id: None | str | Unset
    if isinstance(job_id, Unset):
        json_job_id = UNSET
    else:
        json_job_id = job_id
    params["job_id"] = json_job_id

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    elif isinstance(sort_by, InvocationSortByEnum):
        json_sort_by = sort_by.value
    else:
        json_sort_by = sort_by
    params["sort_by"] = json_sort_by

    params["sort_desc"] = sort_desc

    json_include_terminal: bool | None | Unset
    if isinstance(include_terminal, Unset):
        json_include_terminal = UNSET
    else:
        json_include_terminal = include_terminal
    params["include_terminal"] = json_include_terminal

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

    json_instance: bool | None | Unset
    if isinstance(instance, Unset):
        json_instance = UNSET
    else:
        json_instance = instance
    params["instance"] = json_instance

    json_view: None | str | Unset
    if isinstance(view, Unset):
        json_view = UNSET
    else:
        json_view = view
    params["view"] = json_view

    params["step_details"] = step_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/workflows/{workflow_id}/invocations".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> WorkflowInvocationCollectionView | WorkflowInvocationElementView:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_workflow_invocation_response_type_0 = WorkflowInvocationElementView.from_dict(
                        data
                    )

                    return componentsschemas_workflow_invocation_response_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_invocation_response_type_1 = WorkflowInvocationCollectionView.from_dict(data)

                return componentsschemas_workflow_invocation_response_type_1

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
) -> Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    history_id: None | str | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    sort_by: InvocationSortByEnum | None | Unset = UNSET,
    sort_desc: bool | Unset = False,
    include_terminal: bool | None | Unset = True,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    instance: bool | None | Unset = False,
    view: None | str | Unset = UNSET,
    step_details: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]:
    """Get the list of a user's workflow invocations.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        history_id (None | str | Unset): Return only invocations for this History ID
        job_id (None | str | Unset): Return only invocations for this Job ID
        user_id (None | str | Unset): Return invocations for this User ID.
        sort_by (InvocationSortByEnum | None | Unset): Sort Workflow Invocations by this attribute
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        include_terminal (bool | None | Unset): Set to false to only include terminal Invocations.
            Default: True.
        limit (int | None | Unset): Limit the number of invocations to return. Default: 20.
        offset (int | None | Unset): Number of invocations to skip.
        instance (bool | None | Unset): Is provided workflow id for Workflow instead of
            StoredWorkflow? Default: False.
        view (None | str | Unset): View to be passed to the serializer
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        history_id=history_id,
        job_id=job_id,
        user_id=user_id,
        sort_by=sort_by,
        sort_desc=sort_desc,
        include_terminal=include_terminal,
        limit=limit,
        offset=offset,
        instance=instance,
        view=view,
        step_details=step_details,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    history_id: None | str | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    sort_by: InvocationSortByEnum | None | Unset = UNSET,
    sort_desc: bool | Unset = False,
    include_terminal: bool | None | Unset = True,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    instance: bool | None | Unset = False,
    view: None | str | Unset = UNSET,
    step_details: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView] | None:
    """Get the list of a user's workflow invocations.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        history_id (None | str | Unset): Return only invocations for this History ID
        job_id (None | str | Unset): Return only invocations for this Job ID
        user_id (None | str | Unset): Return invocations for this User ID.
        sort_by (InvocationSortByEnum | None | Unset): Sort Workflow Invocations by this attribute
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        include_terminal (bool | None | Unset): Set to false to only include terminal Invocations.
            Default: True.
        limit (int | None | Unset): Limit the number of invocations to return. Default: 20.
        offset (int | None | Unset): Number of invocations to skip.
        instance (bool | None | Unset): Is provided workflow id for Workflow instead of
            StoredWorkflow? Default: False.
        view (None | str | Unset): View to be passed to the serializer
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        history_id=history_id,
        job_id=job_id,
        user_id=user_id,
        sort_by=sort_by,
        sort_desc=sort_desc,
        include_terminal=include_terminal,
        limit=limit,
        offset=offset,
        instance=instance,
        view=view,
        step_details=step_details,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    history_id: None | str | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    sort_by: InvocationSortByEnum | None | Unset = UNSET,
    sort_desc: bool | Unset = False,
    include_terminal: bool | None | Unset = True,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    instance: bool | None | Unset = False,
    view: None | str | Unset = UNSET,
    step_details: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]:
    """Get the list of a user's workflow invocations.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        history_id (None | str | Unset): Return only invocations for this History ID
        job_id (None | str | Unset): Return only invocations for this Job ID
        user_id (None | str | Unset): Return invocations for this User ID.
        sort_by (InvocationSortByEnum | None | Unset): Sort Workflow Invocations by this attribute
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        include_terminal (bool | None | Unset): Set to false to only include terminal Invocations.
            Default: True.
        limit (int | None | Unset): Limit the number of invocations to return. Default: 20.
        offset (int | None | Unset): Number of invocations to skip.
        instance (bool | None | Unset): Is provided workflow id for Workflow instead of
            StoredWorkflow? Default: False.
        view (None | str | Unset): View to be passed to the serializer
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        history_id=history_id,
        job_id=job_id,
        user_id=user_id,
        sort_by=sort_by,
        sort_desc=sort_desc,
        include_terminal=include_terminal,
        limit=limit,
        offset=offset,
        instance=instance,
        view=view,
        step_details=step_details,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    history_id: None | str | Unset = UNSET,
    job_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    sort_by: InvocationSortByEnum | None | Unset = UNSET,
    sort_desc: bool | Unset = False,
    include_terminal: bool | None | Unset = True,
    limit: int | None | Unset = 20,
    offset: int | None | Unset = UNSET,
    instance: bool | None | Unset = False,
    view: None | str | Unset = UNSET,
    step_details: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView] | None:
    """Get the list of a user's workflow invocations.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        history_id (None | str | Unset): Return only invocations for this History ID
        job_id (None | str | Unset): Return only invocations for this Job ID
        user_id (None | str | Unset): Return invocations for this User ID.
        sort_by (InvocationSortByEnum | None | Unset): Sort Workflow Invocations by this attribute
        sort_desc (bool | Unset): Sort in descending order? Default: False.
        include_terminal (bool | None | Unset): Set to false to only include terminal Invocations.
            Default: True.
        limit (int | None | Unset): Limit the number of invocations to return. Default: 20.
        offset (int | None | Unset): Number of invocations to skip.
        instance (bool | None | Unset): Is provided workflow id for Workflow instead of
            StoredWorkflow? Default: False.
        view (None | str | Unset): View to be passed to the serializer
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            history_id=history_id,
            job_id=job_id,
            user_id=user_id,
            sort_by=sort_by,
            sort_desc=sort_desc,
            include_terminal=include_terminal,
            limit=limit,
            offset=offset,
            instance=instance,
            view=view,
            step_details=step_details,
            run_as=run_as,
        )
    ).parsed
