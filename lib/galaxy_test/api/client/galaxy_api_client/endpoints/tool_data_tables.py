from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
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


@runtime_checkable
class ToolDataTablesClientProtocol(Protocol):
    """Protocol defining the interface of ToolDataTablesClient for dependency injection."""

    async def tool_data_tables_index(
        self,
    ) -> ToolDataEntryList: ...

    async def tool_data_tables_index(
        self,
    ) -> ToolDataEntryList: ...

    async def tool_data_tables_create(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def tool_data_tables_create(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def tool_data_tables_delete(
        self,
        table_name: str,
        body: ToolDataItem,
        run_as: ToolDataTablesDeleteParamRunAs | None = None,
    ) -> ToolDataDetails: ...

    async def tool_data_tables_delete(
        self,
        table_name: str,
        body: ToolDataItem,
        run_as: ToolDataTablesDeleteParamRunAs | None = None,
    ) -> ToolDataDetails: ...

    async def tool_data_tables_show(
        self,
        table_name: str,
        run_as: ToolDataTablesShowParamRunAs | None = None,
    ) -> ToolDataDetails: ...

    async def tool_data_tables_show(
        self,
        table_name: str,
        run_as: ToolDataTablesShowParamRunAs | None = None,
    ) -> ToolDataDetails: ...

    async def tool_data_tables_fields_show_field(
        self,
        table_name: str,
        field_name: str,
        run_as: ToolDataTablesFieldsShowFieldParamRunAs | None = None,
    ) -> ToolDataField: ...

    async def tool_data_tables_fields_show_field(
        self,
        table_name: str,
        field_name: str,
        run_as: ToolDataTablesFieldsShowFieldParamRunAs | None = None,
    ) -> ToolDataField: ...

    async def tool_data_tables_fields_files_download_field_file(
        self,
        table_name: str,
        field_name: str,
        file_name: str,
        run_as: ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None = None,
    ) -> None: ...

    async def tool_data_tables_fields_files_download_field_file(
        self,
        table_name: str,
        field_name: str,
        file_name: str,
        run_as: ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None = None,
    ) -> None: ...

    async def tool_data_tables_reload_reload(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails: ...

    async def tool_data_tables_reload_reload(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails: ...


class ToolDataTablesClient(ToolDataTablesClientProtocol):
    """Client for tool data tables endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tool_data_tables_index(
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
                return structure_from_dict(response.json(), ToolDataEntryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_index(
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
                return structure_from_dict(response.json(), ToolDataEntryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_create(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Import a data manager bundle

        Args:
            tool_data_file_path (ToolDataTablesCreateParamToolDataFilePath | None)
                                     :
            run-as (ToolDataTablesCreateParamRunAs | None)
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
            **(
                {"tool_data_file_path": DataclassSerializer.serialize(tool_data_file_path)}
                if tool_data_file_path is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ImportToolDataBundle = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_create(
        self,
        body: ImportToolDataBundle,
        tool_data_file_path: ToolDataTablesCreateParamToolDataFilePath | None = None,
        run_as: ToolDataTablesCreateParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Import a data manager bundle

        Args:
            tool_data_file_path (ToolDataTablesCreateParamToolDataFilePath | None)
                                     :
            run-as (ToolDataTablesCreateParamRunAs | None)
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
            **(
                {"tool_data_file_path": DataclassSerializer.serialize(tool_data_file_path)}
                if tool_data_file_path is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ImportToolDataBundle = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_delete(
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
            run-as (ToolDataTablesDeleteParamRunAs | None)
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
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ToolDataItem = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_delete(
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
            run-as (ToolDataTablesDeleteParamRunAs | None)
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
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ToolDataItem = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_show(
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
            run-as (ToolDataTablesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the given data table and its content.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_show(
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
            run-as (ToolDataTablesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the given data table and its content.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_fields_show_field(
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
            run-as (ToolDataTablesFieldsShowFieldParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataField: Information about a data table field

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)
        field_name = DataclassSerializer.serialize(field_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataField)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_fields_show_field(
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
            run-as (ToolDataTablesFieldsShowFieldParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataField: Information about a data table field

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)
        field_name = DataclassSerializer.serialize(field_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataField)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_fields_files_download_field_file(
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
            run-as (ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)
        field_name = DataclassSerializer.serialize(field_name)
        file_name = DataclassSerializer.serialize(file_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}/files/{file_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_fields_files_download_field_file(
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
            run-as (ToolDataTablesFieldsFilesDownloadFieldFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)
        field_name = DataclassSerializer.serialize(field_name)
        file_name = DataclassSerializer.serialize(file_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/fields/{field_name}/files/{file_name}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_reload_reload(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Reloads a tool data table

        Reloads a data table and return its details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (ToolDataTablesReloadReloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the reloaded data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/reload"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_data_tables_reload_reload(
        self,
        table_name: str,
        run_as: ToolDataTablesReloadReloadParamRunAs | None = None,
    ) -> ToolDataDetails:
        """
        Reloads a tool data table

        Reloads a data table and return its details.

        Args:
            table_name (str)         : The name of the tool data table
            run-as (ToolDataTablesReloadReloadParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolDataDetails: A description of the reloaded data table and its content

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        table_name = DataclassSerializer.serialize(table_name)

        url = f"{self.base_url}/api/tool_data/{table_name}/reload"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolDataDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
