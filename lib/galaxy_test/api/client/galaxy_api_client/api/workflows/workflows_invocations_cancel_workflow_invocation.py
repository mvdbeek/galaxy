from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.workflow_invocation_collection_view import WorkflowInvocationCollectionView
from ...models.workflow_invocation_element_view import WorkflowInvocationElementView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    invocation_id: str,
    *,
    step_details: bool | Unset = False,
    legacy_job_state: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["step_details"] = step_details

    params["legacy_job_state"] = legacy_job_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/workflows/{workflow_id}/invocations/{invocation_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
            invocation_id=quote(str(invocation_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> WorkflowInvocationCollectionView | WorkflowInvocationElementView:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_invocation_response_type_0 = WorkflowInvocationElementView.from_dict(data)

                return componentsschemas_workflow_invocation_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_workflow_invocation_response_type_1 = WorkflowInvocationCollectionView.from_dict(data)

            return componentsschemas_workflow_invocation_response_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    step_details: bool | Unset = False,
    legacy_job_state: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView]:
    """Cancel the specified workflow invocation.

     An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        invocation_id (str):  Example: 0123456789ABCDEF.
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        legacy_job_state (bool | Unset): Populate the invocation step state with the job state
            instead of the invocation step state.
                    This will also produce one step per job in mapping jobs to mimic the older
            behavior with respect to collections.
                    Partially scheduled steps may provide incomplete information and the listed steps
            outputs
                    are not the mapped over step outputs but the individual job outputs. Default:
            False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        step_details=step_details,
        legacy_job_state=legacy_job_state,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    step_details: bool | Unset = False,
    legacy_job_state: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView | None:
    """Cancel the specified workflow invocation.

     An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        invocation_id (str):  Example: 0123456789ABCDEF.
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        legacy_job_state (bool | Unset): Populate the invocation step state with the job state
            instead of the invocation step state.
                    This will also produce one step per job in mapping jobs to mimic the older
            behavior with respect to collections.
                    Partially scheduled steps may provide incomplete information and the listed steps
            outputs
                    are not the mapped over step outputs but the individual job outputs. Default:
            False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView
    """

    return sync_detailed(
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        client=client,
        step_details=step_details,
        legacy_job_state=legacy_job_state,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    step_details: bool | Unset = False,
    legacy_job_state: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView]:
    """Cancel the specified workflow invocation.

     An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        invocation_id (str):  Example: 0123456789ABCDEF.
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        legacy_job_state (bool | Unset): Populate the invocation step state with the job state
            instead of the invocation step state.
                    This will also produce one step per job in mapping jobs to mimic the older
            behavior with respect to collections.
                    Partially scheduled steps may provide incomplete information and the listed steps
            outputs
                    are not the mapped over step outputs but the individual job outputs. Default:
            False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        invocation_id=invocation_id,
        step_details=step_details,
        legacy_job_state=legacy_job_state,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    invocation_id: str,
    *,
    client: AuthenticatedClient,
    step_details: bool | Unset = False,
    legacy_job_state: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView | None:
    """Cancel the specified workflow invocation.

     An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        invocation_id (str):  Example: 0123456789ABCDEF.
        step_details (bool | Unset): Include details for individual invocation steps and populate
            a steps attribute in the resulting dictionary. Default: False.
        legacy_job_state (bool | Unset): Populate the invocation step state with the job state
            instead of the invocation step state.
                    This will also produce one step per job in mapping jobs to mimic the older
            behavior with respect to collections.
                    Partially scheduled steps may provide incomplete information and the listed steps
            outputs
                    are not the mapped over step outputs but the individual job outputs. Default:
            False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | WorkflowInvocationCollectionView | WorkflowInvocationElementView
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            invocation_id=invocation_id,
            client=client,
            step_details=step_details,
            legacy_job_state=legacy_job_state,
            run_as=run_as,
        )
    ).parsed
