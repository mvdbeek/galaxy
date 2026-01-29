from typing import TYPE_CHECKING

from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.import_tool_data_bundle import ImportToolDataBundle
from ...models.tool_data_details import ToolDataDetails
from ...models.tool_data_entry_list import ToolDataEntryList
from ...models.tool_data_field import ToolDataField
from ...models.tool_data_item import ToolDataItem
from ...models.tool_data_tables_create_param_run_as import ToolDataTablesCreateParamRunAs
from ...models.tool_data_tables_create_param_tool_data_file_path import ToolDataTablesCreateParamToolDataFilePath
from ...models.tool_data_tables_delete_param_run_as import ToolDataTablesDeleteParamRunAs
from ...models.tool_data_tables_fields_files_download_field_file_param_run_as import (
    ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs,
)
from ...models.tool_data_tables_fields_show_field_param_run_as import ToolDataTablesFieldsShowFieldParamRunAs
from ...models.tool_data_tables_reload_reload_param_run_as import ToolDataTablesReloadReloadParamRunAs
from ...models.tool_data_tables_show_param_run_as import ToolDataTablesShowParamRunAs

if TYPE_CHECKING:
    pass


class MockToolDataTablesClient:
    """
    Mock implementation of ToolDataTablesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestToolDataTablesClient(MockToolDataTablesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tool_data_tables_index(
        self,
    ) -> ToolDataEntryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_index() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_create(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_create() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_delete(
        self,
        table_name: str,
        body: ToolDataItem,
        run_as: ToolDataTablesDeleteParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_delete() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_show(
        self,
        table_name: str,
        run_as: ToolDataTablesShowParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_show() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_fields_show_field(
        self,
        table_name: str,
        field_name: str,
        run_as: ToolDataTablesFieldsShowFieldParamRunAs | None = None,
    ) -> ToolDataField:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_fields_show_field() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_fields_files_download_field_file(
        self,
        table_name: str,
        field_name: str,
        file_name: str,
        run_as: ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_fields_files_download_field_file() not implemented. Override this method in your test subclass."
        )

    async def tool_data_tables_reload_reload(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolDataTablesClient.tool_data_tables_reload_reload() not implemented. Override this method in your test subclass."
        )
