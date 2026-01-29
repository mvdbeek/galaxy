from typing import TYPE_CHECKING

from ...models.create_entry_payload import CreateEntryPayload
from ...models.created_entry_response import CreatedEntryResponse
from ...models.files_source_plugin_list import FilesSourcePluginList
from ...models.remote_files_create_entry_param_run_as import RemoteFilesCreateEntryParamRunAs
from ...models.remote_files_index_200_response import RemoteFilesIndex200Response
from ...models.remote_files_index_200_response_2 import RemoteFilesIndex200Response2
from ...models.remote_files_index_param_disable import RemoteFilesIndexParamDisable
from ...models.remote_files_index_param_disable_2 import RemoteFilesIndexParamDisable2
from ...models.remote_files_index_param_format import RemoteFilesIndexParamFormat
from ...models.remote_files_index_param_format_2 import RemoteFilesIndexParamFormat2
from ...models.remote_files_index_param_limit import RemoteFilesIndexParamLimit
from ...models.remote_files_index_param_limit_2 import RemoteFilesIndexParamLimit2
from ...models.remote_files_index_param_offset import RemoteFilesIndexParamOffset
from ...models.remote_files_index_param_offset_2 import RemoteFilesIndexParamOffset2
from ...models.remote_files_index_param_query import RemoteFilesIndexParamQuery
from ...models.remote_files_index_param_query_2 import RemoteFilesIndexParamQuery2
from ...models.remote_files_index_param_recursive import RemoteFilesIndexParamRecursive
from ...models.remote_files_index_param_recursive_2 import RemoteFilesIndexParamRecursive2
from ...models.remote_files_index_param_run_as import RemoteFilesIndexParamRunAs
from ...models.remote_files_index_param_run_as_2 import RemoteFilesIndexParamRunAs2
from ...models.remote_files_index_param_sort_by import RemoteFilesIndexParamSortBy
from ...models.remote_files_index_param_sort_by_2 import RemoteFilesIndexParamSortBy2
from ...models.remote_files_index_param_write_intent import RemoteFilesIndexParamWriteIntent
from ...models.remote_files_index_param_write_intent_2 import RemoteFilesIndexParamWriteIntent2
from ...models.remote_files_index_param_writeable import RemoteFilesIndexParamWriteable
from ...models.remote_files_index_param_writeable_2 import RemoteFilesIndexParamWriteable2
from ...models.remote_files_oidc_tokens_get_token_param_run_as import RemoteFilesOidcTokensGetTokenParamRunAs
from ...models.remote_files_plugins_plugins_param_browsable_only import RemoteFilesPluginsPluginsParamBrowsableOnly
from ...models.remote_files_plugins_plugins_param_exclude_kind import RemoteFilesPluginsPluginsParamExcludeKind
from ...models.remote_files_plugins_plugins_param_include_kind import RemoteFilesPluginsPluginsParamIncludeKind
from ...models.remote_files_plugins_plugins_param_run_as import RemoteFilesPluginsPluginsParamRunAs

if TYPE_CHECKING:
    pass


class MockRemoteFilesClient:
    """
    Mock implementation of RemoteFilesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestRemoteFilesClient(MockRemoteFilesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def remote_files_index(
        self,
        target: str | None = None,
        format_: RemoteFilesIndexParamFormat | None = None,
        recursive: RemoteFilesIndexParamRecursive | None = None,
        disable: RemoteFilesIndexParamDisable | None = None,
        writeable: RemoteFilesIndexParamWriteable | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent | None = None,
        limit: RemoteFilesIndexParamLimit | None = None,
        offset: RemoteFilesIndexParamOffset | None = None,
        query: RemoteFilesIndexParamQuery | None = None,
        sort_by: RemoteFilesIndexParamSortBy | None = None,
        run_as: RemoteFilesIndexParamRunAs | None = None,
    ) -> RemoteFilesIndex200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRemoteFilesClient.remote_files_index() not implemented. Override this method in your test subclass."
        )

    async def remote_files_oidc_tokens_get_token(
        self,
        job_id: str,
        job_key: str,
        provider: str,
        run_as: RemoteFilesOidcTokensGetTokenParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRemoteFilesClient.remote_files_oidc_tokens_get_token() not implemented. Override this method in your test subclass."
        )

    async def remote_files_index_2(
        self,
        target: str | None = None,
        format_: RemoteFilesIndexParamFormat2 | None = None,
        recursive: RemoteFilesIndexParamRecursive2 | None = None,
        disable: RemoteFilesIndexParamDisable2 | None = None,
        writeable: RemoteFilesIndexParamWriteable2 | None = None,
        write_intent: RemoteFilesIndexParamWriteIntent2 | None = None,
        limit: RemoteFilesIndexParamLimit2 | None = None,
        offset: RemoteFilesIndexParamOffset2 | None = None,
        query: RemoteFilesIndexParamQuery2 | None = None,
        sort_by: RemoteFilesIndexParamSortBy2 | None = None,
        run_as: RemoteFilesIndexParamRunAs2 | None = None,
    ) -> RemoteFilesIndex200Response2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRemoteFilesClient.remote_files_index_2() not implemented. Override this method in your test subclass."
        )

    async def remote_files_create_entry(
        self,
        body: CreateEntryPayload,
        run_as: RemoteFilesCreateEntryParamRunAs | None = None,
    ) -> CreatedEntryResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRemoteFilesClient.remote_files_create_entry() not implemented. Override this method in your test subclass."
        )

    async def remote_files_plugins_plugins(
        self,
        browsable_only: RemoteFilesPluginsPluginsParamBrowsableOnly | None = None,
        include_kind: RemoteFilesPluginsPluginsParamIncludeKind | None = None,
        exclude_kind: RemoteFilesPluginsPluginsParamExcludeKind | None = None,
        run_as: RemoteFilesPluginsPluginsParamRunAs | None = None,
    ) -> FilesSourcePluginList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRemoteFilesClient.remote_files_plugins_plugins() not implemented. Override this method in your test subclass."
        )
