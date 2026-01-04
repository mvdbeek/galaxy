from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.refactor_request import RefactorRequest
from ...models.refactor_response import RefactorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    body: RefactorRequest,
    instance: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_instance: bool | None | Unset
    if isinstance(instance, Unset):
        json_instance = UNSET
    else:
        json_instance = instance
    params["instance"] = json_instance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/workflows/{workflow_id}/refactor".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | RefactorResponse | None:
    if response.status_code == 200:
        response_200 = RefactorResponse.from_dict(response.json())

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
) -> Response[MessageExceptionModel | RefactorResponse]:
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
    body: RefactorRequest,
    instance: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | RefactorResponse]:
    """Updates the workflow stored with the given ID.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        instance (bool | None | Unset):  Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RefactorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | RefactorResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
        instance=instance,
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
    body: RefactorRequest,
    instance: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | RefactorResponse | None:
    """Updates the workflow stored with the given ID.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        instance (bool | None | Unset):  Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RefactorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | RefactorResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
        instance=instance,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: RefactorRequest,
    instance: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | RefactorResponse]:
    """Updates the workflow stored with the given ID.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        instance (bool | None | Unset):  Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RefactorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | RefactorResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
        instance=instance,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: RefactorRequest,
    instance: bool | None | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | RefactorResponse | None:
    """Updates the workflow stored with the given ID.

    Args:
        workflow_id (str):  Example: 0123456789ABCDEF.
        instance (bool | None | Unset):  Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (RefactorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | RefactorResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
            instance=instance,
            run_as=run_as,
        )
    ).parsed
