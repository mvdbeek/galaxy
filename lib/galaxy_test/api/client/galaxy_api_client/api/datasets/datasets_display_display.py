from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_content_id: str,
    *,
    preview: bool | Unset = False,
    filename: None | str | Unset = UNSET,
    to_ext: None | str | Unset = UNSET,
    raw: bool | Unset = False,
    offset: int | None | Unset = UNSET,
    ck_size: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    params["preview"] = preview

    json_filename: None | str | Unset
    if isinstance(filename, Unset):
        json_filename = UNSET
    else:
        json_filename = filename
    params["filename"] = json_filename

    json_to_ext: None | str | Unset
    if isinstance(to_ext, Unset):
        json_to_ext = UNSET
    else:
        json_to_ext = to_ext
    params["to_ext"] = json_to_ext

    params["raw"] = raw

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_ck_size: int | None | Unset
    if isinstance(ck_size, Unset):
        json_ck_size = UNSET
    else:
        json_ck_size = ck_size
    params["ck_size"] = json_ck_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": "/api/datasets/{history_content_id}/display".format(
            history_content_id=quote(str(history_content_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_content_id: str,
    *,
    client: AuthenticatedClient,
    preview: bool | Unset = False,
    filename: None | str | Unset = UNSET,
    to_ext: None | str | Unset = UNSET,
    raw: bool | Unset = False,
    offset: int | None | Unset = UNSET,
    ck_size: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Check if dataset content can be previewed or downloaded.

     Streams the dataset for download or the contents preview to be displayed in a browser.

    Args:
        history_content_id (str):  Example: 0123456789ABCDEF.
        preview (bool | Unset): Whether to get preview contents to be directly displayed on the
            web. If preview is False (default) the contents will be downloaded instead. Default:
            False.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        to_ext (None | str | Unset): The file extension when downloading the display data. Use the
            value `data` to let the server infer it from the data type.
        raw (bool | Unset): The query parameter 'raw' should be considered experimental and may be
            dropped at some point in the future without warning. Generally, data should be processed
            by its datatype prior to display. Default: False.
        offset (int | None | Unset): Set this for datatypes that allow chunked display through the
            display_data method to enable chunking. This specifies a byte offset into the target
            dataset's display.
        ck_size (int | None | Unset): If offset is set, this recommends 'how large' the next chunk
            should be. This is not respected or interpreted uniformly and should be interpreted as a
            very loose recommendation. Different datatypes interpret 'largeness' differently - for bam
            datasets this is a number of lines whereas for tabular datatypes this is interpreted as a
            number of bytes.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_content_id=history_content_id,
        preview=preview,
        filename=filename,
        to_ext=to_ext,
        raw=raw,
        offset=offset,
        ck_size=ck_size,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_content_id: str,
    *,
    client: AuthenticatedClient,
    preview: bool | Unset = False,
    filename: None | str | Unset = UNSET,
    to_ext: None | str | Unset = UNSET,
    raw: bool | Unset = False,
    offset: int | None | Unset = UNSET,
    ck_size: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Check if dataset content can be previewed or downloaded.

     Streams the dataset for download or the contents preview to be displayed in a browser.

    Args:
        history_content_id (str):  Example: 0123456789ABCDEF.
        preview (bool | Unset): Whether to get preview contents to be directly displayed on the
            web. If preview is False (default) the contents will be downloaded instead. Default:
            False.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        to_ext (None | str | Unset): The file extension when downloading the display data. Use the
            value `data` to let the server infer it from the data type.
        raw (bool | Unset): The query parameter 'raw' should be considered experimental and may be
            dropped at some point in the future without warning. Generally, data should be processed
            by its datatype prior to display. Default: False.
        offset (int | None | Unset): Set this for datatypes that allow chunked display through the
            display_data method to enable chunking. This specifies a byte offset into the target
            dataset's display.
        ck_size (int | None | Unset): If offset is set, this recommends 'how large' the next chunk
            should be. This is not respected or interpreted uniformly and should be interpreted as a
            very loose recommendation. Different datatypes interpret 'largeness' differently - for bam
            datasets this is a number of lines whereas for tabular datatypes this is interpreted as a
            number of bytes.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return sync_detailed(
        history_content_id=history_content_id,
        client=client,
        preview=preview,
        filename=filename,
        to_ext=to_ext,
        raw=raw,
        offset=offset,
        ck_size=ck_size,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_content_id: str,
    *,
    client: AuthenticatedClient,
    preview: bool | Unset = False,
    filename: None | str | Unset = UNSET,
    to_ext: None | str | Unset = UNSET,
    raw: bool | Unset = False,
    offset: int | None | Unset = UNSET,
    ck_size: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[Any | MessageExceptionModel]:
    """Check if dataset content can be previewed or downloaded.

     Streams the dataset for download or the contents preview to be displayed in a browser.

    Args:
        history_content_id (str):  Example: 0123456789ABCDEF.
        preview (bool | Unset): Whether to get preview contents to be directly displayed on the
            web. If preview is False (default) the contents will be downloaded instead. Default:
            False.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        to_ext (None | str | Unset): The file extension when downloading the display data. Use the
            value `data` to let the server infer it from the data type.
        raw (bool | Unset): The query parameter 'raw' should be considered experimental and may be
            dropped at some point in the future without warning. Generally, data should be processed
            by its datatype prior to display. Default: False.
        offset (int | None | Unset): Set this for datatypes that allow chunked display through the
            display_data method to enable chunking. This specifies a byte offset into the target
            dataset's display.
        ck_size (int | None | Unset): If offset is set, this recommends 'how large' the next chunk
            should be. This is not respected or interpreted uniformly and should be interpreted as a
            very loose recommendation. Different datatypes interpret 'largeness' differently - for bam
            datasets this is a number of lines whereas for tabular datatypes this is interpreted as a
            number of bytes.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_content_id=history_content_id,
        preview=preview,
        filename=filename,
        to_ext=to_ext,
        raw=raw,
        offset=offset,
        ck_size=ck_size,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_content_id: str,
    *,
    client: AuthenticatedClient,
    preview: bool | Unset = False,
    filename: None | str | Unset = UNSET,
    to_ext: None | str | Unset = UNSET,
    raw: bool | Unset = False,
    offset: int | None | Unset = UNSET,
    ck_size: int | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Any | MessageExceptionModel | None:
    """Check if dataset content can be previewed or downloaded.

     Streams the dataset for download or the contents preview to be displayed in a browser.

    Args:
        history_content_id (str):  Example: 0123456789ABCDEF.
        preview (bool | Unset): Whether to get preview contents to be directly displayed on the
            web. If preview is False (default) the contents will be downloaded instead. Default:
            False.
        filename (None | str | Unset): If non-null, get the specified filename from the extra
            files for this dataset.
        to_ext (None | str | Unset): The file extension when downloading the display data. Use the
            value `data` to let the server infer it from the data type.
        raw (bool | Unset): The query parameter 'raw' should be considered experimental and may be
            dropped at some point in the future without warning. Generally, data should be processed
            by its datatype prior to display. Default: False.
        offset (int | None | Unset): Set this for datatypes that allow chunked display through the
            display_data method to enable chunking. This specifies a byte offset into the target
            dataset's display.
        ck_size (int | None | Unset): If offset is set, this recommends 'how large' the next chunk
            should be. This is not respected or interpreted uniformly and should be interpreted as a
            very loose recommendation. Different datatypes interpret 'largeness' differently - for bam
            datasets this is a number of lines whereas for tabular datatypes this is interpreted as a
            number of bytes.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_content_id=history_content_id,
            client=client,
            preview=preview,
            filename=filename,
            to_ext=to_ext,
            raw=raw,
            offset=offset,
            ck_size=ck_size,
            run_as=run_as,
        )
    ).parsed
