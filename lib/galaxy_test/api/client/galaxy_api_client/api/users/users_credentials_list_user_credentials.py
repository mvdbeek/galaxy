from http import HTTPStatus
from typing import Any, Literal
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...models.user_service_credentials_response import UserServiceCredentialsResponse
from ...models.user_service_credentials_with_definition_response import UserServiceCredentialsWithDefinitionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: Literal["current"] | str,
    *,
    source_type: Literal["tool"] | None | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    source_version: None | str | Unset = UNSET,
    include_definition: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_source_type: Literal["tool"] | None | Unset
    if isinstance(source_type, Unset):
        json_source_type = UNSET
    else:
        json_source_type = source_type
    params["source_type"] = json_source_type

    json_source_id: None | str | Unset
    if isinstance(source_id, Unset):
        json_source_id = UNSET
    else:
        json_source_id = source_id
    params["source_id"] = json_source_id

    json_source_version: None | str | Unset
    if isinstance(source_version, Unset):
        json_source_version = UNSET
    else:
        json_source_version = source_version
    params["source_version"] = json_source_version

    params["include_definition"] = include_definition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/{user_id}/credentials".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    MessageExceptionModel
    | list[UserServiceCredentialsResponse]
    | list[UserServiceCredentialsWithDefinitionResponse]
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for componentsschemas_user_service_credentials_list_response_item_data in _response_200_type_0:
                    componentsschemas_user_service_credentials_list_response_item = (
                        UserServiceCredentialsResponse.from_dict(
                            componentsschemas_user_service_credentials_list_response_item_data
                        )
                    )

                    response_200_type_0.append(componentsschemas_user_service_credentials_list_response_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = []
            _response_200_type_1 = data
            for componentsschemas_extended_user_credentials_list_response_item_data in _response_200_type_1:
                componentsschemas_extended_user_credentials_list_response_item = (
                    UserServiceCredentialsWithDefinitionResponse.from_dict(
                        componentsschemas_extended_user_credentials_list_response_item_data
                    )
                )

                response_200_type_1.append(componentsschemas_extended_user_credentials_list_response_item)

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
) -> Response[
    MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: Literal["current"] | str,
    *,
    client: AuthenticatedClient,
    source_type: Literal["tool"] | None | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    source_version: None | str | Unset = UNSET,
    include_definition: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]
]:
    """Lists all credentials the user has provided

    Args:
        user_id (Literal['current'] | str):
        source_type (Literal['tool'] | None | Unset): The type of source to filter by.
        source_id (None | str | Unset): The ID of the source to filter by.
        source_version (None | str | Unset): The version of the source to filter by. By default it
            is the latest version.
        include_definition (bool | Unset): Whether to include extended credential definition
            information. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        source_type=source_type,
        source_id=source_id,
        source_version=source_version,
        include_definition=include_definition,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: Literal["current"] | str,
    *,
    client: AuthenticatedClient,
    source_type: Literal["tool"] | None | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    source_version: None | str | Unset = UNSET,
    include_definition: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> (
    MessageExceptionModel
    | list[UserServiceCredentialsResponse]
    | list[UserServiceCredentialsWithDefinitionResponse]
    | None
):
    """Lists all credentials the user has provided

    Args:
        user_id (Literal['current'] | str):
        source_type (Literal['tool'] | None | Unset): The type of source to filter by.
        source_id (None | str | Unset): The ID of the source to filter by.
        source_version (None | str | Unset): The version of the source to filter by. By default it
            is the latest version.
        include_definition (bool | Unset): Whether to include extended credential definition
            information. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        source_type=source_type,
        source_id=source_id,
        source_version=source_version,
        include_definition=include_definition,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    user_id: Literal["current"] | str,
    *,
    client: AuthenticatedClient,
    source_type: Literal["tool"] | None | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    source_version: None | str | Unset = UNSET,
    include_definition: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> Response[
    MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]
]:
    """Lists all credentials the user has provided

    Args:
        user_id (Literal['current'] | str):
        source_type (Literal['tool'] | None | Unset): The type of source to filter by.
        source_id (None | str | Unset): The ID of the source to filter by.
        source_version (None | str | Unset): The version of the source to filter by. By default it
            is the latest version.
        include_definition (bool | Unset): Whether to include extended credential definition
            information. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        source_type=source_type,
        source_id=source_id,
        source_version=source_version,
        include_definition=include_definition,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: Literal["current"] | str,
    *,
    client: AuthenticatedClient,
    source_type: Literal["tool"] | None | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    source_version: None | str | Unset = UNSET,
    include_definition: bool | Unset = False,
    run_as: None | str | Unset = UNSET,
) -> (
    MessageExceptionModel
    | list[UserServiceCredentialsResponse]
    | list[UserServiceCredentialsWithDefinitionResponse]
    | None
):
    """Lists all credentials the user has provided

    Args:
        user_id (Literal['current'] | str):
        source_type (Literal['tool'] | None | Unset): The type of source to filter by.
        source_id (None | str | Unset): The ID of the source to filter by.
        source_version (None | str | Unset): The version of the source to filter by. By default it
            is the latest version.
        include_definition (bool | Unset): Whether to include extended credential definition
            information. Default: False.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[UserServiceCredentialsResponse] | list[UserServiceCredentialsWithDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            source_type=source_type,
            source_id=source_id,
            source_version=source_version,
            include_definition=include_definition,
            run_as=run_as,
        )
    ).parsed
