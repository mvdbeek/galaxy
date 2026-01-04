from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.browsable_files_source_plugin import BrowsableFilesSourcePlugin
from ...models.files_source_plugin import FilesSourcePlugin
from ...models.message_exception_model import MessageExceptionModel
from ...models.plugin_kind import PluginKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    browsable_only: bool | None | Unset = True,
    include_kind: list[PluginKind] | None | Unset = UNSET,
    exclude_kind: list[PluginKind] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_browsable_only: bool | None | Unset
    if isinstance(browsable_only, Unset):
        json_browsable_only = UNSET
    else:
        json_browsable_only = browsable_only
    params["browsable_only"] = json_browsable_only

    json_include_kind: list[str] | None | Unset
    if isinstance(include_kind, Unset):
        json_include_kind = UNSET
    elif isinstance(include_kind, list):
        json_include_kind = []
        for include_kind_type_0_item_data in include_kind:
            include_kind_type_0_item = include_kind_type_0_item_data.value
            json_include_kind.append(include_kind_type_0_item)

    else:
        json_include_kind = include_kind
    params["include_kind"] = json_include_kind

    json_exclude_kind: list[str] | None | Unset
    if isinstance(exclude_kind, Unset):
        json_exclude_kind = UNSET
    elif isinstance(exclude_kind, list):
        json_exclude_kind = []
        for exclude_kind_type_0_item_data in exclude_kind:
            exclude_kind_type_0_item = exclude_kind_type_0_item_data.value
            json_exclude_kind.append(exclude_kind_type_0_item)

    else:
        json_exclude_kind = exclude_kind
    params["exclude_kind"] = json_exclude_kind

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/remote_files/plugins",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_files_source_plugin_list_item_data in _response_200:

            def _parse_componentsschemas_files_source_plugin_list_item(
                data: object,
            ) -> BrowsableFilesSourcePlugin | FilesSourcePlugin:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_files_source_plugin_list_item_type_0 = BrowsableFilesSourcePlugin.from_dict(data)

                    return componentsschemas_files_source_plugin_list_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_files_source_plugin_list_item_type_1 = FilesSourcePlugin.from_dict(data)

                return componentsschemas_files_source_plugin_list_item_type_1

            componentsschemas_files_source_plugin_list_item = _parse_componentsschemas_files_source_plugin_list_item(
                componentsschemas_files_source_plugin_list_item_data
            )

            response_200.append(componentsschemas_files_source_plugin_list_item)

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
) -> Response[MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    browsable_only: bool | None | Unset = True,
    include_kind: list[PluginKind] | None | Unset = UNSET,
    exclude_kind: list[PluginKind] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]]:
    """Display plugin information for each of the gxfiles:// URI targets available.

     Display plugin information for each of the gxfiles:// URI targets available.

    Args:
        browsable_only (bool | None | Unset): Whether to return browsable filesources only. The
            default is `True`, which will omit filesourceslike `http` and `base64` that do not
            implement a list method. Default: True.
        include_kind (list[PluginKind] | None | Unset): Whether to return **only** filesources of
            the specified kind. The default is `None`, which will return all filesources. Multiple
            values can be specified by repeating the parameter.
        exclude_kind (list[PluginKind] | None | Unset): Whether to exclude filesources of the
            specified kind from the list. The default is `None`, which will return all filesources.
            Multiple values can be specified by repeating the parameter.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]]
    """

    kwargs = _get_kwargs(
        browsable_only=browsable_only,
        include_kind=include_kind,
        exclude_kind=exclude_kind,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    browsable_only: bool | None | Unset = True,
    include_kind: list[PluginKind] | None | Unset = UNSET,
    exclude_kind: list[PluginKind] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin] | None:
    """Display plugin information for each of the gxfiles:// URI targets available.

     Display plugin information for each of the gxfiles:// URI targets available.

    Args:
        browsable_only (bool | None | Unset): Whether to return browsable filesources only. The
            default is `True`, which will omit filesourceslike `http` and `base64` that do not
            implement a list method. Default: True.
        include_kind (list[PluginKind] | None | Unset): Whether to return **only** filesources of
            the specified kind. The default is `None`, which will return all filesources. Multiple
            values can be specified by repeating the parameter.
        exclude_kind (list[PluginKind] | None | Unset): Whether to exclude filesources of the
            specified kind from the list. The default is `None`, which will return all filesources.
            Multiple values can be specified by repeating the parameter.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]
    """

    return sync_detailed(
        client=client,
        browsable_only=browsable_only,
        include_kind=include_kind,
        exclude_kind=exclude_kind,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    browsable_only: bool | None | Unset = True,
    include_kind: list[PluginKind] | None | Unset = UNSET,
    exclude_kind: list[PluginKind] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]]:
    """Display plugin information for each of the gxfiles:// URI targets available.

     Display plugin information for each of the gxfiles:// URI targets available.

    Args:
        browsable_only (bool | None | Unset): Whether to return browsable filesources only. The
            default is `True`, which will omit filesourceslike `http` and `base64` that do not
            implement a list method. Default: True.
        include_kind (list[PluginKind] | None | Unset): Whether to return **only** filesources of
            the specified kind. The default is `None`, which will return all filesources. Multiple
            values can be specified by repeating the parameter.
        exclude_kind (list[PluginKind] | None | Unset): Whether to exclude filesources of the
            specified kind from the list. The default is `None`, which will return all filesources.
            Multiple values can be specified by repeating the parameter.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]]
    """

    kwargs = _get_kwargs(
        browsable_only=browsable_only,
        include_kind=include_kind,
        exclude_kind=exclude_kind,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    browsable_only: bool | None | Unset = True,
    include_kind: list[PluginKind] | None | Unset = UNSET,
    exclude_kind: list[PluginKind] | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin] | None:
    """Display plugin information for each of the gxfiles:// URI targets available.

     Display plugin information for each of the gxfiles:// URI targets available.

    Args:
        browsable_only (bool | None | Unset): Whether to return browsable filesources only. The
            default is `True`, which will omit filesourceslike `http` and `base64` that do not
            implement a list method. Default: True.
        include_kind (list[PluginKind] | None | Unset): Whether to return **only** filesources of
            the specified kind. The default is `None`, which will return all filesources. Multiple
            values can be specified by repeating the parameter.
        exclude_kind (list[PluginKind] | None | Unset): Whether to exclude filesources of the
            specified kind from the list. The default is `None`, which will return all filesources.
            Multiple values can be specified by repeating the parameter.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[BrowsableFilesSourcePlugin | FilesSourcePlugin]
    """

    return (
        await asyncio_detailed(
            client=client,
            browsable_only=browsable_only,
            include_kind=include_kind,
            exclude_kind=exclude_kind,
            run_as=run_as,
        )
    ).parsed
