from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_entry_payload import CreateEntryPayload
from ..models.created_entry_response import CreatedEntryResponse
from ..models.files_source_plugin_list import FilesSourcePluginList
from ..models.remote_files_create_entry_param_run_as import RemoteFilesCreateEntryParamRunAs
from ..models.remote_files_index_200_response_2 import RemoteFilesIndex200Response2
from ..models.remote_files_index_param_disable import RemoteFilesIndexParamDisable
from ..models.remote_files_index_param_format import RemoteFilesIndexParamFormat
from ..models.remote_files_index_param_limit import RemoteFilesIndexParamLimit
from ..models.remote_files_index_param_offset import RemoteFilesIndexParamOffset
from ..models.remote_files_index_param_query import RemoteFilesIndexParamQuery
from ..models.remote_files_index_param_recursive import RemoteFilesIndexParamRecursive
from ..models.remote_files_index_param_run_as import RemoteFilesIndexParamRunAs
from ..models.remote_files_index_param_sort_by import RemoteFilesIndexParamSortBy
from ..models.remote_files_index_param_write_intent import RemoteFilesIndexParamWriteIntent
from ..models.remote_files_index_param_writeable import RemoteFilesIndexParamWriteable
from ..models.remote_files_oidc_tokens_get_token_param_run_as import RemoteFilesOidcTokensGetTokenParamRunAs
from ..models.remote_files_plugins_plugins_param_browsable_only import RemoteFilesPluginsPluginsParamBrowsableOnly
from ..models.remote_files_plugins_plugins_param_exclude_kind import RemoteFilesPluginsPluginsParamExcludeKind
from ..models.remote_files_plugins_plugins_param_include_kind import RemoteFilesPluginsPluginsParamIncludeKind
from ..models.remote_files_plugins_plugins_param_run_as import RemoteFilesPluginsPluginsParamRunAs


class RemoteFilesClient:
    """Client for remote files endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def remote_files_index_2_2(
        self,
        target: str | None = "ftpdir",
        format_: RemoteFilesIndexParamFormat | None = "uri",
        recursive: RemoteFilesIndexParamRecursive | None = None,
        disable: RemoteFilesIndexParamDisable | None = None,
        writeable: RemoteFilesIndexParamWriteable | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent | None = None,
        limit: RemoteFilesIndexParamLimit | None = None,
        offset: RemoteFilesIndexParamOffset | None = None,
        query: RemoteFilesIndexParamQuery | None = None,
        sort_by: RemoteFilesIndexParamSortBy | None = None,
        run_as: RemoteFilesIndexParamRunAs | None = None,
    ) -> RemoteFilesIndex200Response2:
        """
        Displays remote files available to the user. Please use /api/remote_files instead.

        Lists all remote files available to the user from different sources.  The total count of
        files and directories is returned in the 'total_matches' header.

        Args:
            target (Optional[str])   : The source to load datasets from. Possible values:
                                       ftpdir, userdir, importdir
            format (Optional[RemoteFilesIndexParamFormat])
                                     : The requested format of returned data. Either `flat` to
                                       simply list all the files, `jstree` to get a tree
                                       representation of the files, or the default `uri` to list
                                       files and directories by their URI.
            recursive (Optional[RemoteFilesIndexParamRecursive])
                                     : Whether to recursively lists all sub-directories. This
                                       will be `True` by default depending on the `target`.
            disable (Optional[RemoteFilesIndexParamDisable])
                                     : (This only applies when `format` is `jstree`) The value
                                       can be either `folders` or `files` and it will disable
                                       the corresponding nodes of the tree.
            writeable (Optional[RemoteFilesIndexParamWriteable])
                                     : Deprecated, please use `write_intent` instead.
            write_intent (Optional[RemoteFilesIndexParamWriteIntent])
                                     : Whether the query is made with the intention of writing
                                       to the source. If set to True, only entries that can be
                                       written to will be returned.
            limit (Optional[RemoteFilesIndexParamLimit])
                                     : Maximum number of entries to return.
            offset (Optional[RemoteFilesIndexParamOffset])
                                     : Number of entries to skip.
            query (Optional[RemoteFilesIndexParamQuery])
                                     : Search query to filter entries by. The syntax could be
                                       different depending on the target source.
            sort_by (Optional[RemoteFilesIndexParamSortBy])
                                     : Sort the entries by the specified field.
            run-as (Optional[RemoteFilesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RemoteFilesIndex200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ftp_files"

        params: dict[str, Any] = {
            **({"target": target} if target is not None else {}),
            **({"format": format_} if format_ is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"disable": disable} if disable is not None else {}),
            **({"writeable": writeable} if writeable is not None else {}),
            **({"write_intent": write_intent} if write_intent is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RemoteFilesIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_index_2_2(
        self,
        target: str | None = "ftpdir",
        format_: RemoteFilesIndexParamFormat | None = "uri",
        recursive: RemoteFilesIndexParamRecursive | None = None,
        disable: RemoteFilesIndexParamDisable | None = None,
        writeable: RemoteFilesIndexParamWriteable | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent | None = None,
        limit: RemoteFilesIndexParamLimit | None = None,
        offset: RemoteFilesIndexParamOffset | None = None,
        query: RemoteFilesIndexParamQuery | None = None,
        sort_by: RemoteFilesIndexParamSortBy | None = None,
        run_as: RemoteFilesIndexParamRunAs | None = None,
    ) -> RemoteFilesIndex200Response2:
        """
        Displays remote files available to the user. Please use /api/remote_files instead.

        Lists all remote files available to the user from different sources.  The total count of
        files and directories is returned in the 'total_matches' header.

        Args:
            target (Optional[str])   : The source to load datasets from. Possible values:
                                       ftpdir, userdir, importdir
            format (Optional[RemoteFilesIndexParamFormat])
                                     : The requested format of returned data. Either `flat` to
                                       simply list all the files, `jstree` to get a tree
                                       representation of the files, or the default `uri` to list
                                       files and directories by their URI.
            recursive (Optional[RemoteFilesIndexParamRecursive])
                                     : Whether to recursively lists all sub-directories. This
                                       will be `True` by default depending on the `target`.
            disable (Optional[RemoteFilesIndexParamDisable])
                                     : (This only applies when `format` is `jstree`) The value
                                       can be either `folders` or `files` and it will disable
                                       the corresponding nodes of the tree.
            writeable (Optional[RemoteFilesIndexParamWriteable])
                                     : Deprecated, please use `write_intent` instead.
            write_intent (Optional[RemoteFilesIndexParamWriteIntent])
                                     : Whether the query is made with the intention of writing
                                       to the source. If set to True, only entries that can be
                                       written to will be returned.
            limit (Optional[RemoteFilesIndexParamLimit])
                                     : Maximum number of entries to return.
            offset (Optional[RemoteFilesIndexParamOffset])
                                     : Number of entries to skip.
            query (Optional[RemoteFilesIndexParamQuery])
                                     : Search query to filter entries by. The syntax could be
                                       different depending on the target source.
            sort_by (Optional[RemoteFilesIndexParamSortBy])
                                     : Sort the entries by the specified field.
            run-as (Optional[RemoteFilesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RemoteFilesIndex200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ftp_files"

        params: dict[str, Any] = {
            **({"target": target} if target is not None else {}),
            **({"format": format_} if format_ is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"disable": disable} if disable is not None else {}),
            **({"writeable": writeable} if writeable is not None else {}),
            **({"write_intent": write_intent} if write_intent is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RemoteFilesIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_oidc_tokens_get_token_2_2(
        self,
        job_id: str,
        job_key: str,
        provider: str,
        run_as: RemoteFilesOidcTokensGetTokenParamRunAs | None = None,
    ) -> str:
        """
        Get a fresh OIDC token

        Allows remote job running mechanisms to get a fresh OIDC token that can be used on
        remote side to authorize user. It is not meant to represent part of Galaxy's stable,
        user facing API

        Args:
            job_id (str)             :
            job_key (str)            : A key used to authenticate this request as acting on
                                       behalf or a job runner for the specified job
            provider (str)           : OIDC provider name
            run-as (Optional[RemoteFilesOidcTokensGetTokenParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/oidc-tokens"

        params: dict[str, Any] = {
            "job_key": job_key,
            "provider": provider,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_oidc_tokens_get_token_2_2(
        self,
        job_id: str,
        job_key: str,
        provider: str,
        run_as: RemoteFilesOidcTokensGetTokenParamRunAs | None = None,
    ) -> str:
        """
        Get a fresh OIDC token

        Allows remote job running mechanisms to get a fresh OIDC token that can be used on
        remote side to authorize user. It is not meant to represent part of Galaxy's stable,
        user facing API

        Args:
            job_id (str)             :
            job_key (str)            : A key used to authenticate this request as acting on
                                       behalf or a job runner for the specified job
            provider (str)           : OIDC provider name
            run-as (Optional[RemoteFilesOidcTokensGetTokenParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/oidc-tokens"

        params: dict[str, Any] = {
            "job_key": job_key,
            "provider": provider,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_index_3_2(
        self,
        target: str | None = "ftpdir",
        format_: RemoteFilesIndexParamFormat | None = "uri",
        recursive: RemoteFilesIndexParamRecursive | None = None,
        disable: RemoteFilesIndexParamDisable | None = None,
        writeable: RemoteFilesIndexParamWriteable | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent | None = None,
        limit: RemoteFilesIndexParamLimit | None = None,
        offset: RemoteFilesIndexParamOffset | None = None,
        query: RemoteFilesIndexParamQuery | None = None,
        sort_by: RemoteFilesIndexParamSortBy | None = None,
        run_as: RemoteFilesIndexParamRunAs | None = None,
    ) -> RemoteFilesIndex200Response2:
        """
        Displays remote files available to the user.

        Lists all remote files available to the user from different sources.  The total count of
        files and directories is returned in the 'total_matches' header.

        Args:
            target (Optional[str])   : The source to load datasets from. Possible values:
                                       ftpdir, userdir, importdir
            format (Optional[RemoteFilesIndexParamFormat])
                                     : The requested format of returned data. Either `flat` to
                                       simply list all the files, `jstree` to get a tree
                                       representation of the files, or the default `uri` to list
                                       files and directories by their URI.
            recursive (Optional[RemoteFilesIndexParamRecursive])
                                     : Whether to recursively lists all sub-directories. This
                                       will be `True` by default depending on the `target`.
            disable (Optional[RemoteFilesIndexParamDisable])
                                     : (This only applies when `format` is `jstree`) The value
                                       can be either `folders` or `files` and it will disable
                                       the corresponding nodes of the tree.
            writeable (Optional[RemoteFilesIndexParamWriteable])
                                     : Deprecated, please use `write_intent` instead.
            write_intent (Optional[RemoteFilesIndexParamWriteIntent])
                                     : Whether the query is made with the intention of writing
                                       to the source. If set to True, only entries that can be
                                       written to will be returned.
            limit (Optional[RemoteFilesIndexParamLimit])
                                     : Maximum number of entries to return.
            offset (Optional[RemoteFilesIndexParamOffset])
                                     : Number of entries to skip.
            query (Optional[RemoteFilesIndexParamQuery])
                                     : Search query to filter entries by. The syntax could be
                                       different depending on the target source.
            sort_by (Optional[RemoteFilesIndexParamSortBy])
                                     : Sort the entries by the specified field.
            run-as (Optional[RemoteFilesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RemoteFilesIndex200Response2: A list with details about the remote files available
                                          to the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files"

        params: dict[str, Any] = {
            **({"target": target} if target is not None else {}),
            **({"format": format_} if format_ is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"disable": disable} if disable is not None else {}),
            **({"writeable": writeable} if writeable is not None else {}),
            **({"write_intent": write_intent} if write_intent is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RemoteFilesIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_index_3_2(
        self,
        target: str | None = "ftpdir",
        format_: RemoteFilesIndexParamFormat | None = "uri",
        recursive: RemoteFilesIndexParamRecursive | None = None,
        disable: RemoteFilesIndexParamDisable | None = None,
        writeable: RemoteFilesIndexParamWriteable | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent | None = None,
        limit: RemoteFilesIndexParamLimit | None = None,
        offset: RemoteFilesIndexParamOffset | None = None,
        query: RemoteFilesIndexParamQuery | None = None,
        sort_by: RemoteFilesIndexParamSortBy | None = None,
        run_as: RemoteFilesIndexParamRunAs | None = None,
    ) -> RemoteFilesIndex200Response2:
        """
        Displays remote files available to the user.

        Lists all remote files available to the user from different sources.  The total count of
        files and directories is returned in the 'total_matches' header.

        Args:
            target (Optional[str])   : The source to load datasets from. Possible values:
                                       ftpdir, userdir, importdir
            format (Optional[RemoteFilesIndexParamFormat])
                                     : The requested format of returned data. Either `flat` to
                                       simply list all the files, `jstree` to get a tree
                                       representation of the files, or the default `uri` to list
                                       files and directories by their URI.
            recursive (Optional[RemoteFilesIndexParamRecursive])
                                     : Whether to recursively lists all sub-directories. This
                                       will be `True` by default depending on the `target`.
            disable (Optional[RemoteFilesIndexParamDisable])
                                     : (This only applies when `format` is `jstree`) The value
                                       can be either `folders` or `files` and it will disable
                                       the corresponding nodes of the tree.
            writeable (Optional[RemoteFilesIndexParamWriteable])
                                     : Deprecated, please use `write_intent` instead.
            write_intent (Optional[RemoteFilesIndexParamWriteIntent])
                                     : Whether the query is made with the intention of writing
                                       to the source. If set to True, only entries that can be
                                       written to will be returned.
            limit (Optional[RemoteFilesIndexParamLimit])
                                     : Maximum number of entries to return.
            offset (Optional[RemoteFilesIndexParamOffset])
                                     : Number of entries to skip.
            query (Optional[RemoteFilesIndexParamQuery])
                                     : Search query to filter entries by. The syntax could be
                                       different depending on the target source.
            sort_by (Optional[RemoteFilesIndexParamSortBy])
                                     : Sort the entries by the specified field.
            run-as (Optional[RemoteFilesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RemoteFilesIndex200Response2: A list with details about the remote files available
                                          to the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files"

        params: dict[str, Any] = {
            **({"target": target} if target is not None else {}),
            **({"format": format_} if format_ is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"disable": disable} if disable is not None else {}),
            **({"writeable": writeable} if writeable is not None else {}),
            **({"write_intent": write_intent} if write_intent is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RemoteFilesIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_create_entry_2_2(
        self,
        body: CreateEntryPayload,
        run_as: RemoteFilesCreateEntryParamRunAs | None = None,
    ) -> CreatedEntryResponse:
        """
        Creates a new entry (directory/record) on the remote files source.

        Creates a new entry on the remote files source.

        Args:
            run-as (Optional[RemoteFilesCreateEntryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateEntryPayload): Request body. (json)

        Returns:
            CreatedEntryResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateEntryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreatedEntryResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_create_entry_2_2(
        self,
        body: CreateEntryPayload,
        run_as: RemoteFilesCreateEntryParamRunAs | None = None,
    ) -> CreatedEntryResponse:
        """
        Creates a new entry (directory/record) on the remote files source.

        Creates a new entry on the remote files source.

        Args:
            run-as (Optional[RemoteFilesCreateEntryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateEntryPayload): Request body. (json)

        Returns:
            CreatedEntryResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateEntryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreatedEntryResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_plugins_plugins_2_2(
        self,
        browsable_only: RemoteFilesPluginsPluginsParamBrowsableOnly | None = True,
        include_kind: RemoteFilesPluginsPluginsParamIncludeKind | None = None,
        exclude_kind: RemoteFilesPluginsPluginsParamExcludeKind | None = None,
        run_as: RemoteFilesPluginsPluginsParamRunAs | None = None,
    ) -> FilesSourcePluginList:
        """
        Display plugin information for each of the gxfiles:// URI targets available.

        Display plugin information for each of the gxfiles:// URI targets available.

        Args:
            browsable_only (Optional[RemoteFilesPluginsPluginsParamBrowsableOnly])
                                     : Whether to return browsable filesources only. The default
                                       is `True`, which will omit filesourceslike `http` and
                                       `base64` that do not implement a list method.
            include_kind (Optional[RemoteFilesPluginsPluginsParamIncludeKind])
                                     : Whether to return **only** filesources of the specified
                                       kind. The default is `None`, which will return all
                                       filesources. Multiple values can be specified by
                                       repeating the parameter.
            exclude_kind (Optional[RemoteFilesPluginsPluginsParamExcludeKind])
                                     : Whether to exclude filesources of the specified kind from
                                       the list. The default is `None`, which will return all
                                       filesources. Multiple values can be specified by
                                       repeating the parameter.
            run-as (Optional[RemoteFilesPluginsPluginsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FilesSourcePluginList: A list with details about each plugin.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files/plugins"

        params: dict[str, Any] = {
            **({"browsable_only": browsable_only} if browsable_only is not None else {}),
            **({"include_kind": include_kind} if include_kind is not None else {}),
            **({"exclude_kind": exclude_kind} if exclude_kind is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FilesSourcePluginList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def remote_files_plugins_plugins_2_2(
        self,
        browsable_only: RemoteFilesPluginsPluginsParamBrowsableOnly | None = True,
        include_kind: RemoteFilesPluginsPluginsParamIncludeKind | None = None,
        exclude_kind: RemoteFilesPluginsPluginsParamExcludeKind | None = None,
        run_as: RemoteFilesPluginsPluginsParamRunAs | None = None,
    ) -> FilesSourcePluginList:
        """
        Display plugin information for each of the gxfiles:// URI targets available.

        Display plugin information for each of the gxfiles:// URI targets available.

        Args:
            browsable_only (Optional[RemoteFilesPluginsPluginsParamBrowsableOnly])
                                     : Whether to return browsable filesources only. The default
                                       is `True`, which will omit filesourceslike `http` and
                                       `base64` that do not implement a list method.
            include_kind (Optional[RemoteFilesPluginsPluginsParamIncludeKind])
                                     : Whether to return **only** filesources of the specified
                                       kind. The default is `None`, which will return all
                                       filesources. Multiple values can be specified by
                                       repeating the parameter.
            exclude_kind (Optional[RemoteFilesPluginsPluginsParamExcludeKind])
                                     : Whether to exclude filesources of the specified kind from
                                       the list. The default is `None`, which will return all
                                       filesources. Multiple values can be specified by
                                       repeating the parameter.
            run-as (Optional[RemoteFilesPluginsPluginsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FilesSourcePluginList: A list with details about each plugin.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/remote_files/plugins"

        params: dict[str, Any] = {
            **({"browsable_only": browsable_only} if browsable_only is not None else {}),
            **({"include_kind": include_kind} if include_kind is not None else {}),
            **({"exclude_kind": exclude_kind} if exclude_kind is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FilesSourcePluginList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
