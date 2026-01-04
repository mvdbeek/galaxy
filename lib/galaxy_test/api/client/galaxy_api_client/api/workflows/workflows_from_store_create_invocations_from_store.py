from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_invocations_from_store_payload import CreateInvocationsFromStorePayload
from ...models.message_exception_model import MessageExceptionModel
from ...models.workflow_invocation_collection_view import WorkflowInvocationCollectionView
from ...models.workflow_invocation_element_view import WorkflowInvocationElementView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateInvocationsFromStorePayload,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/invocations/from_store",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    *,
    client: AuthenticatedClient,
    body: CreateInvocationsFromStorePayload,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]:
    """Create Invocations From Store

     Create invocation(s) from a supplied model store.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateInvocationsFromStorePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateInvocationsFromStorePayload,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView] | None:
    """Create Invocations From Store

     Create invocation(s) from a supplied model store.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateInvocationsFromStorePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInvocationsFromStorePayload,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]:
    """Create Invocations From Store

     Create invocation(s) from a supplied model store.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateInvocationsFromStorePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]]
    """

    kwargs = _get_kwargs(
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInvocationsFromStorePayload,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView] | None:
    """Create Invocations From Store

     Create invocation(s) from a supplied model store.

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateInvocationsFromStorePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[WorkflowInvocationCollectionView | WorkflowInvocationElementView]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
