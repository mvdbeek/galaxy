from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.datatypes_combined_map import DatatypesCombinedMap
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    extension_only: bool | None | Unset = True,
    upload_only: bool | None | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_extension_only: bool | None | Unset
    if isinstance(extension_only, Unset):
        json_extension_only = UNSET
    else:
        json_extension_only = extension_only
    params["extension_only"] = json_extension_only

    json_upload_only: bool | None | Unset
    if isinstance(upload_only, Unset):
        json_upload_only = UNSET
    else:
        json_upload_only = upload_only
    params["upload_only"] = json_upload_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datatypes/types_and_mapping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatatypesCombinedMap | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = DatatypesCombinedMap.from_dict(response.json())

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
) -> Response[DatatypesCombinedMap | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    extension_only: bool | None | Unset = True,
    upload_only: bool | None | Unset = True,
) -> Response[DatatypesCombinedMap | MessageExceptionModel]:
    """Returns all the data types extensions and their mappings

     Combines the datatype information from (/api/datatypes) and the
    mapping information from (/api/datatypes/mapping) into a single
    response.

    Args:
        extension_only (bool | None | Unset): Whether to return only the datatype's extension
            rather than the datatype's details Default: True.
        upload_only (bool | None | Unset): Whether to return only datatypes which can be uploaded
            Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatatypesCombinedMap | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        extension_only=extension_only,
        upload_only=upload_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    extension_only: bool | None | Unset = True,
    upload_only: bool | None | Unset = True,
) -> DatatypesCombinedMap | MessageExceptionModel | None:
    """Returns all the data types extensions and their mappings

     Combines the datatype information from (/api/datatypes) and the
    mapping information from (/api/datatypes/mapping) into a single
    response.

    Args:
        extension_only (bool | None | Unset): Whether to return only the datatype's extension
            rather than the datatype's details Default: True.
        upload_only (bool | None | Unset): Whether to return only datatypes which can be uploaded
            Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatatypesCombinedMap | MessageExceptionModel
    """

    return sync_detailed(
        client=client,
        extension_only=extension_only,
        upload_only=upload_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    extension_only: bool | None | Unset = True,
    upload_only: bool | None | Unset = True,
) -> Response[DatatypesCombinedMap | MessageExceptionModel]:
    """Returns all the data types extensions and their mappings

     Combines the datatype information from (/api/datatypes) and the
    mapping information from (/api/datatypes/mapping) into a single
    response.

    Args:
        extension_only (bool | None | Unset): Whether to return only the datatype's extension
            rather than the datatype's details Default: True.
        upload_only (bool | None | Unset): Whether to return only datatypes which can be uploaded
            Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatatypesCombinedMap | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        extension_only=extension_only,
        upload_only=upload_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    extension_only: bool | None | Unset = True,
    upload_only: bool | None | Unset = True,
) -> DatatypesCombinedMap | MessageExceptionModel | None:
    """Returns all the data types extensions and their mappings

     Combines the datatype information from (/api/datatypes) and the
    mapping information from (/api/datatypes/mapping) into a single
    response.

    Args:
        extension_only (bool | None | Unset): Whether to return only the datatype's extension
            rather than the datatype's details Default: True.
        upload_only (bool | None | Unset): Whether to return only datatypes which can be uploaded
            Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatatypesCombinedMap | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            client=client,
            extension_only=extension_only,
            upload_only=upload_only,
        )
    ).parsed
