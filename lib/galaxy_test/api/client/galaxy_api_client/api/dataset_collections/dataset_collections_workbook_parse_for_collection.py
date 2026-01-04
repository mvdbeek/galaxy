from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.parse_workbook_for_collection_api import ParseWorkbookForCollectionApi
from ...models.parsed_workbook_for_collection import ParsedWorkbookForCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hdca_id: str,
    *,
    body: ParseWorkbookForCollectionApi,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dataset_collections/{hdca_id}/sample_sheet_workbook/parse".format(
            hdca_id=quote(str(hdca_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | ParsedWorkbookForCollection | None:
    if response.status_code == 200:
        response_200 = ParsedWorkbookForCollection.from_dict(response.json())

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
) -> Response[MessageExceptionModel | ParsedWorkbookForCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    body: ParseWorkbookForCollectionApi,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ParsedWorkbookForCollection]:
    """Parse an XLSX workbook for a sample sheet definition and supplied file contents.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseWorkbookForCollectionApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ParsedWorkbookForCollection]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        body=body,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    body: ParseWorkbookForCollectionApi,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ParsedWorkbookForCollection | None:
    """Parse an XLSX workbook for a sample sheet definition and supplied file contents.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseWorkbookForCollectionApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ParsedWorkbookForCollection
    """

    return sync_detailed(
        hdca_id=hdca_id,
        client=client,
        body=body,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    body: ParseWorkbookForCollectionApi,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | ParsedWorkbookForCollection]:
    """Parse an XLSX workbook for a sample sheet definition and supplied file contents.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseWorkbookForCollectionApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | ParsedWorkbookForCollection]
    """

    kwargs = _get_kwargs(
        hdca_id=hdca_id,
        body=body,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hdca_id: str,
    *,
    client: AuthenticatedClient,
    body: ParseWorkbookForCollectionApi,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | ParsedWorkbookForCollection | None:
    """Parse an XLSX workbook for a sample sheet definition and supplied file contents.

    Args:
        hdca_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (ParseWorkbookForCollectionApi):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | ParsedWorkbookForCollection
    """

    return (
        await asyncio_detailed(
            hdca_id=hdca_id,
            client=client,
            body=body,
            run_as=run_as,
        )
    ).parsed
