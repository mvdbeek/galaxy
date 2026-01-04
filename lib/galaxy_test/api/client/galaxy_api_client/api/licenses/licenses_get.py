from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_metadata_model import LicenseMetadataModel
from ...models.message_exception_model import MessageExceptionModel
from ...types import Response


def _get_kwargs(
    id: Any,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/licenses/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LicenseMetadataModel | MessageExceptionModel | None:
    if response.status_code == 200:
        response_200 = LicenseMetadataModel.from_dict(response.json())

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
) -> Response[LicenseMetadataModel | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LicenseMetadataModel | MessageExceptionModel]:
    """Gets the SPDX license metadata associated with the short identifier

     Returns the license metadata associated with the given
    [SPDX license short ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

    Args:
        id (Any): The [SPDX license short identifier](https://spdx.github.io/spdx-spec/appendix-I-
            SPDX-license-list/)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LicenseMetadataModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: Any,
    *,
    client: AuthenticatedClient | Client,
) -> LicenseMetadataModel | MessageExceptionModel | None:
    """Gets the SPDX license metadata associated with the short identifier

     Returns the license metadata associated with the given
    [SPDX license short ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

    Args:
        id (Any): The [SPDX license short identifier](https://spdx.github.io/spdx-spec/appendix-I-
            SPDX-license-list/)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LicenseMetadataModel | MessageExceptionModel
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[LicenseMetadataModel | MessageExceptionModel]:
    """Gets the SPDX license metadata associated with the short identifier

     Returns the license metadata associated with the given
    [SPDX license short ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

    Args:
        id (Any): The [SPDX license short identifier](https://spdx.github.io/spdx-spec/appendix-I-
            SPDX-license-list/)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LicenseMetadataModel | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: Any,
    *,
    client: AuthenticatedClient | Client,
) -> LicenseMetadataModel | MessageExceptionModel | None:
    """Gets the SPDX license metadata associated with the short identifier

     Returns the license metadata associated with the given
    [SPDX license short ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

    Args:
        id (Any): The [SPDX license short identifier](https://spdx.github.io/spdx-spec/appendix-I-
            SPDX-license-list/)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LicenseMetadataModel | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
