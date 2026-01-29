from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.async_task_result_summary import AsyncTaskResultSummary
from ..models.import_tool_data_bundle import ImportToolDataBundle
from ..models.tool_data_details import ToolDataDetails
from ..models.tool_data_entry_list import ToolDataEntryList
from ..models.tool_data_field import ToolDataField
from ..models.tool_data_item import ToolDataItem
from ..models.tool_data_tables_create_param_run_as import ToolDataTablesCreateParamRunAs
from ..models.tool_data_tables_create_param_tool_data_file_path import ToolDataTablesCreateParamToolDataFilePath
from ..models.tool_data_tables_delete_param_run_as import ToolDataTablesDeleteParamRunAs
from ..models.tool_data_tables_fields_files_download_field_file_param_run_as import (
    ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs,
)
from ..models.tool_data_tables_fields_show_field_param_run_as import ToolDataTablesFieldsShowFieldParamRunAs
from ..models.tool_data_tables_reload_reload_param_run_as import ToolDataTablesReloadReloadParamRunAs
from ..models.tool_data_tables_show_param_run_as import ToolDataTablesShowParamRunAs


class ToolDataTablesClient:
    """Client for tool data tables endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tool_data_tables_index_2_2(
        self,
    ) -> ToolDataEntryList:
        """
        Lists all available data tables

        Get the list of all available data tables.

        Returns:
            ToolDataEntryList: A list with details on individual data tables.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataEntryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_index_2_2(
        self,
    ) -> ToolDataEntryList:
        """
        Lists all available data tables

        Get the list of all available data tables.

        Returns:
            ToolDataEntryList: A list with details on individual data tables.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataEntryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_create_2_2(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Import a data manager bundle

        Args:
            tool_data_file_path (Optional[ToolDataTablesCreateParamToolDataFilePath])
                                     :
            run-as (Optional[ToolDataTablesCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ImportToolDataBundle)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data"

        params: dict[str, Any] = {
            **({"tool_data_file_path": tool_data_file_path} if tool_data_file_path is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ImportToolDataBundle = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_create_2_2(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Import a data manager bundle

        Args:
            tool_data_file_path (Optional[ToolDataTablesCreateParamToolDataFilePath])
                                     :
            run-as (Optional[ToolDataTablesCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ImportToolDataBundle)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data"

        params: dict[str, Any] = {
            **({"tool_data_file_path": tool_data_file_path} if tool_data_file_path is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ImportToolDataBundle = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_delete_2_2(
        self,
        table_name: str,
        body: ToolDataItem,
        run_as: ToolDataTablesDeleteParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Removes an item from a data table

        Removes an item from a data table and reloads it to return its updated details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ToolDataItem)      : Request body. (json)

        Returns:
            ToolDataDetails: A description of the affected data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ToolDataItem = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_delete_2_2(
        self,
        table_name: str,
        body: ToolDataItem,
        run_as: ToolDataTablesDeleteParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Removes an item from a data table

        Removes an item from a data table and reloads it to return its updated details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ToolDataItem)      : Request body. (json)

        Returns:
            ToolDataDetails: A description of the affected data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ToolDataItem = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_show_2_2(
        self,
        table_name: str,
        run_as: ToolDataTablesShowParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Get details of a data table. For non-administrators, base directories in the path column
        are stripped, leaving only the basename.

        Get details of a given tool data table.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the given data table and its content.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_show_2_2(
        self,
        table_name: str,
        run_as: ToolDataTablesShowParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Get details of a data table. For non-administrators, base directories in the path column
        are stripped, leaving only the basename.

        Get details of a given tool data table.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the given data table and its content.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_fields_show_field_2_2(
        self,
        table_name: str,
        field_name: str,
        run_as: ToolDataTablesFieldsShowFieldParamRunAs | None = None,
    ) -> ToolDataField:
        """
        Get information about a particular field in a tool data table

        Displays information about a data table field.

        Args:
            table_name (str)         : The name of the tool data table
            field_name (str)         : The name of the tool data table field
            run-as (Optional[ToolDataTablesFieldsShowFieldParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataField: Information about a data table field

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataField, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_fields_show_field_2_2(
        self,
        table_name: str,
        field_name: str,
        run_as: ToolDataTablesFieldsShowFieldParamRunAs | None = None,
    ) -> ToolDataField:
        """
        Get information about a particular field in a tool data table

        Displays information about a data table field.

        Args:
            table_name (str)         : The name of the tool data table
            field_name (str)         : The name of the tool data table field
            run-as (Optional[ToolDataTablesFieldsShowFieldParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataField: Information about a data table field

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataField, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_fields_files_download_field_file_2_2(
        self,
        table_name: str,
        field_name: str,
        file_name: str,
        run_as: ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None = None,
    ) -> None:
        """
        Get files associated with a particular field in a tool data table

        Download a file associated with the data table field.

        Args:
            table_name (str)         : The name of the tool data table
            field_name (str)         : The name of the tool data table field
            file_name (str)          : The name of a file associated with this data table field
            run-as (Optional[ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}/files/{file_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_fields_files_download_field_file_2_2(
        self,
        table_name: str,
        field_name: str,
        file_name: str,
        run_as: ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None = None,
    ) -> None:
        """
        Get files associated with a particular field in a tool data table

        Download a file associated with the data table field.

        Args:
            table_name (str)         : The name of the tool data table
            field_name (str)         : The name of the tool data table field
            file_name (str)          : The name of a file associated with this data table field
            run-as (Optional[ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}/files/{file_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_reload_reload_2_2(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Reloads a tool data table

        Reloads a data table and return its details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesReloadReloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the reloaded data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/reload"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_data_tables_reload_reload_2_2(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Reloads a tool data table

        Reloads a data table and return its details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (Optional[ToolDataTablesReloadReloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the reloaded data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_data/{table_name}/reload"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolDataDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
