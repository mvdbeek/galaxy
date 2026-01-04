from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.parse_fetch_workbook import ParseFetchWorkbook
from ...models.parsed_fetch_workbook_for_collections import ParsedFetchWorkbookForCollections
from ...models.parsed_fetch_workbook_for_datasets import ParsedFetchWorkbookForDatasets
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ParseFetchWorkbook,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tools/fetch/workbook/parse",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ParsedFetchWorkbookForDatasets.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ParsedFetchWorkbookForCollections.from_dict(data)

            return response_200_type_1

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
) -> Response[MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ParseFetchWorkbook,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets]:
    """Generate a template workbook to use with the activity builder UI

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseFetchWorkbook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets]
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
    body: ParseFetchWorkbook,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets | None:
    """Generate a template workbook to use with the activity builder UI

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseFetchWorkbook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets
    """

    return sync_detailed(
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ParseFetchWorkbook,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets]:
    """Generate a template workbook to use with the activity builder UI

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseFetchWorkbook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets]
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
    body: ParseFetchWorkbook,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets | None:
    """Generate a template workbook to use with the activity builder UI

    Args:
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseFetchWorkbook):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ParsedFetchWorkbookForCollections | ParsedFetchWorkbookForDatasets
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
