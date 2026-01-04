from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_text_content_details import DatasetTextContentDetails
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    *,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_filename: None | str | Unset
    if isinstance(filename, Unset):
        json_filename = UNSET
    else:
        json_filename = filename
    params["filename"] = json_filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasets/{dataset_id}/get_content_as_text".format(
            dataset_id=quote(str(dataset_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetTextContentDetails | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DatasetTextContentDetails.from_dict(response.json())

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
) -> Response[DatasetTextContentDetails | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetTextContentDetails | MessageExceptionModel]:
    """Returns dataset content as Text.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetTextContentDetails | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        filename=filename,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> DatasetTextContentDetails | MessageExceptionModel | None:
    """Returns dataset content as Text.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetTextContentDetails | MessageExceptionModel
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        filename=filename,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[DatasetTextContentDetails | MessageExceptionModel]:
    """Returns dataset content as Text.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetTextContentDetails | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        filename=filename,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    filename: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> DatasetTextContentDetails | MessageExceptionModel | None:
    """Returns dataset content as Text.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetTextContentDetails | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            filename=filename,
            run_as=run_as,
        )
    ).parsed
