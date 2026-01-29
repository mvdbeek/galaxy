from typing import IO, Any, cast
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core import Error304, Error404
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_218 import AnonymousArrayItem218
from ..models.create_data_landing_payload import CreateDataLandingPayload
from ..models.create_file_landing_payload import CreateFileLandingPayload
from ..models.create_tool_landing_request_payload import CreateToolLandingRequestPayload
from ..models.parse_fetch_workbook import ParseFetchWorkbook
from ..models.tool_landing_request import ToolLandingRequest
from ..models.tool_request_detailed_model import ToolRequestDetailedModel
from ..models.tools_claim_claim_landing_param_run_as import ToolsClaimClaimLandingParamRunAs
from ..models.tools_claim_claim_landing_request_body_2 import ToolsClaimClaimLandingRequestBody2
from ..models.tools_create_data_landing_param_run_as import ToolsCreateDataLandingParamRunAs
from ..models.tools_create_file_landing_param_run_as import ToolsCreateFileLandingParamRunAs
from ..models.tools_create_landing_param_run_as import ToolsCreateLandingParamRunAs
from ..models.tools_fetch_fetch_form_param_run_as import ToolsFetchFetchFormParamRunAs
from ..models.tools_fetch_workbook_download_param_filename import ToolsFetchWorkbookDownloadParamFilename
from ..models.tools_fetch_workbook_download_param_run_as import ToolsFetchWorkbookDownloadParamRunAs
from ..models.tools_fetch_workbook_parse_200_response_2 import ToolsFetchWorkbookParse200Response2
from ..models.tools_fetch_workbook_parse_param_run_as import ToolsFetchWorkbookParseParamRunAs
from ..models.tools_get_landing_param_run_as import ToolsGetLandingParamRunAs
from ..models.tools_get_tool_request_param_run_as import ToolsGetToolRequestParamRunAs
from ..models.tools_icon_get_icon_param_run_as import ToolsIconGetIconParamRunAs
from ..models.tools_inputs_tool_inputs_param_run_as import ToolsInputsToolInputsParamRunAs
from ..models.tools_inputs_tool_inputs_param_tool_version import ToolsInputsToolInputsParamToolVersion
from ..models.tools_parameter_landing_request_schema_param_run_as import ToolsParameterLandingRequestSchemaParamRunAs
from ..models.tools_parameter_landing_request_schema_param_tool_version import (
    ToolsParameterLandingRequestSchemaParamToolVersion,
)
from ..models.tools_parameter_request_schema_param_run_as import ToolsParameterRequestSchemaParamRunAs
from ..models.tools_parameter_request_schema_param_tool_version import ToolsParameterRequestSchemaParamToolVersion
from ..models.tools_parameter_test_case_xml_schema_param_run_as import ToolsParameterTestCaseXmlSchemaParamRunAs
from ..models.tools_parameter_test_case_xml_schema_param_tool_version import (
    ToolsParameterTestCaseXmlSchemaParamToolVersion,
)
from ..models.tools_state_tool_request_state_param_run_as import ToolsStateToolRequestStateParamRunAs


class ToolsClient:
    """Client for tools endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tools_create_data_landing_2_2(
        self,
        body: CreateDataLandingPayload,
        run_as: ToolsCreateDataLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create Data Landing

        Args:
            run-as (Optional[ToolsCreateDataLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateDataLandingPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/data_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateDataLandingPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_create_data_landing_2_2(
        self,
        body: CreateDataLandingPayload,
        run_as: ToolsCreateDataLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create Data Landing

        Args:
            run-as (Optional[ToolsCreateDataLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateDataLandingPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/data_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateDataLandingPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_create_file_landing_2_2(
        self,
        body: CreateFileLandingPayload,
        run_as: ToolsCreateFileLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create File Landing

        Args:
            run-as (Optional[ToolsCreateFileLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateFileLandingPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateFileLandingPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_create_file_landing_2_2(
        self,
        body: CreateFileLandingPayload,
        run_as: ToolsCreateFileLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create File Landing

        Args:
            run-as (Optional[ToolsCreateFileLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateFileLandingPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/file_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateFileLandingPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_create_landing_2_2(
        self,
        body: CreateToolLandingRequestPayload,
        run_as: ToolsCreateLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create Landing

        Args:
            run-as (Optional[ToolsCreateLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateToolLandingRequestPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateToolLandingRequestPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_create_landing_2_2(
        self,
        body: CreateToolLandingRequestPayload,
        run_as: ToolsCreateLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Create Landing

        Args:
            run-as (Optional[ToolsCreateLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateToolLandingRequestPayload)
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateToolLandingRequestPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_get_landing_2_2(
        self,
        uuid_: UUID,
        run_as: ToolsGetLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Get Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[ToolsGetLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_get_landing_2_2(
        self,
        uuid_: UUID,
        run_as: ToolsGetLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Get Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[ToolsGetLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_claim_claim_landing_2_2(
        self,
        uuid_: UUID,
        body: ToolsClaimClaimLandingRequestBody2 | None,
        run_as: ToolsClaimClaimLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Claim Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[ToolsClaimClaimLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[ToolsClaimClaimLandingRequestBody2])
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings/{uuid_}/claim"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ToolsClaimClaimLandingRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_claim_claim_landing_2_2(
        self,
        uuid_: UUID,
        body: ToolsClaimClaimLandingRequestBody2 | None,
        run_as: ToolsClaimClaimLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Claim Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[ToolsClaimClaimLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[ToolsClaimClaimLandingRequestBody2])
                                     : Request body. (json)

        Returns:
            ToolLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_landings/{uuid_}/claim"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ToolsClaimClaimLandingRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_get_tool_request_2_2(
        self,
        id_: str,
        run_as: ToolsGetToolRequestParamRunAs | None = None,
    ) -> ToolRequestDetailedModel:
        """
        Get tool request state.

        Args:
            id (str)                 :
            run-as (Optional[ToolsGetToolRequestParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolRequestDetailedModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_requests/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolRequestDetailedModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_get_tool_request_2_2(
        self,
        id_: str,
        run_as: ToolsGetToolRequestParamRunAs | None = None,
    ) -> ToolRequestDetailedModel:
        """
        Get tool request state.

        Args:
            id (str)                 :
            run-as (Optional[ToolsGetToolRequestParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolRequestDetailedModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_requests/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolRequestDetailedModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_state_tool_request_state_2_2(
        self,
        id_: str,
        run_as: ToolsStateToolRequestStateParamRunAs | None = None,
    ) -> str:
        """
        Get tool request state.

        Args:
            id (str)                 :
            run-as (Optional[ToolsStateToolRequestStateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_requests/{id_}/state"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_state_tool_request_state_2_2(
        self,
        id_: str,
        run_as: ToolsStateToolRequestStateParamRunAs | None = None,
    ) -> str:
        """
        Get tool request state.

        Args:
            id (str)                 :
            run-as (Optional[ToolsStateToolRequestStateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_requests/{id_}/state"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_fetch_form_2_2(
        self,
        files: dict[str, IO[Any]],
        run_as: ToolsFetchFetchFormParamRunAs | None = None,
    ) -> Any:
        """
        Upload files to Galaxy

        Args:
            run-as (Optional[ToolsFetchFetchFormParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (Dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_fetch_form_2_2(
        self,
        files: dict[str, IO[Any]],
        run_as: ToolsFetchFetchFormParamRunAs | None = None,
    ) -> Any:
        """
        Upload files to Galaxy

        Args:
            run-as (Optional[ToolsFetchFetchFormParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (Dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_workbook_download_2_2(
        self,
        type_: str | None = "datasets",
        collection_type: str | None = "list",
        filename: ToolsFetchWorkbookDownloadParamFilename | None = None,
        run_as: ToolsFetchWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Generate a template workbook to use with the activity builder UI

        Args:
            type (Optional[str])     : Generate a workbook for simple datasets or a collection.
            collection_type (Optional[str])
                                     : Generate workbook for specified collection type (not all
                                       collection types are supported)
            filename (Optional[ToolsFetchWorkbookDownloadParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[ToolsFetchWorkbookDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch/workbook"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"collection_type": collection_type} if collection_type is not None else {}),
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_workbook_download_2_2(
        self,
        type_: str | None = "datasets",
        collection_type: str | None = "list",
        filename: ToolsFetchWorkbookDownloadParamFilename | None = None,
        run_as: ToolsFetchWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Generate a template workbook to use with the activity builder UI

        Args:
            type (Optional[str])     : Generate a workbook for simple datasets or a collection.
            collection_type (Optional[str])
                                     : Generate workbook for specified collection type (not all
                                       collection types are supported)
            filename (Optional[ToolsFetchWorkbookDownloadParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[ToolsFetchWorkbookDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch/workbook"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"collection_type": collection_type} if collection_type is not None else {}),
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_workbook_parse_2_2(
        self,
        body: ParseFetchWorkbook,
        run_as: ToolsFetchWorkbookParseParamRunAs | None = None,
    ) -> ToolsFetchWorkbookParse200Response2:
        """
        Generate a template workbook to use with the activity builder UI

        Args:
            run-as (Optional[ToolsFetchWorkbookParseParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseFetchWorkbook): Request body. (json)

        Returns:
            ToolsFetchWorkbookParse200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch/workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseFetchWorkbook = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolsFetchWorkbookParse200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_fetch_workbook_parse_2_2(
        self,
        body: ParseFetchWorkbook,
        run_as: ToolsFetchWorkbookParseParamRunAs | None = None,
    ) -> ToolsFetchWorkbookParse200Response2:
        """
        Generate a template workbook to use with the activity builder UI

        Args:
            run-as (Optional[ToolsFetchWorkbookParseParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseFetchWorkbook): Request body. (json)

        Returns:
            ToolsFetchWorkbookParse200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/fetch/workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseFetchWorkbook = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolsFetchWorkbookParse200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_icon_get_icon_2_2(
        self,
        tool_id: str,
        run_as: ToolsIconGetIconParamRunAs | None = None,
    ) -> str:
        """
        Get the icon image associated with a tool

        Returns the icon image associated with a tool.  The icon image is served with caching
        headers to allow for efficient client-side caching. The icon image is expected to be in
        PNG format.

        Args:
            tool_id (str)            :
            run-as (Optional[ToolsIconGetIconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Tool icon image in PNG format

        Raises:
            HttpError:
                HTTPError: 404: Tool icon file not found or not provided by the tool
        """
        url = f"{self.base_url}/api/tools/{tool_id}/icon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case 304:
                raise Error304(response=response)
            case 404:
                raise Error404(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_icon_get_icon_2_2(
        self,
        tool_id: str,
        run_as: ToolsIconGetIconParamRunAs | None = None,
    ) -> str:
        """
        Get the icon image associated with a tool

        Returns the icon image associated with a tool.  The icon image is served with caching
        headers to allow for efficient client-side caching. The icon image is expected to be in
        PNG format.

        Args:
            tool_id (str)            :
            run-as (Optional[ToolsIconGetIconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Tool icon image in PNG format

        Raises:
            HttpError:
                HTTPError: 404: Tool icon file not found or not provided by the tool
        """
        url = f"{self.base_url}/api/tools/{tool_id}/icon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case 304:
                raise Error304(response=response)
            case 404:
                raise Error404(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_inputs_tool_inputs_2_2(
        self,
        tool_id: str,
        tool_version: ToolsInputsToolInputsParamToolVersion | None = None,
        run_as: ToolsInputsToolInputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem218]:
        """
        Get tool inputs.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsInputsToolInputsParamToolVersion])
                                     :
            run-as (Optional[ToolsInputsToolInputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem218]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/inputs"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem218], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_inputs_tool_inputs_2_2(
        self,
        tool_id: str,
        tool_version: ToolsInputsToolInputsParamToolVersion | None = None,
        run_as: ToolsInputsToolInputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem218]:
        """
        Get tool inputs.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsInputsToolInputsParamToolVersion])
                                     :
            run-as (Optional[ToolsInputsToolInputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem218]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/inputs"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem218], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_landing_request_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterLandingRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterLandingRequestSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for the tool landing request API.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterLandingRequestSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterLandingRequestSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_landing_request_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_landing_request_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterLandingRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterLandingRequestSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for the tool landing request API.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterLandingRequestSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterLandingRequestSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_landing_request_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_request_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterRequestSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for the tool request API that will
        be added to Galaxy at some point

        The tool request schema includes validation of map/reduce concepts that can be consumed
        by the tool execution API and not just the request for a single execution.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterRequestSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterRequestSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_request_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_request_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterRequestSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for the tool request API that will
        be added to Galaxy at some point

        The tool request schema includes validation of map/reduce concepts that can be consumed
        by the tool execution API and not just the request for a single execution.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterRequestSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterRequestSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_request_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_test_case_xml_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterTestCaseXmlSchemaParamToolVersion | None = None,
        run_as: ToolsParameterTestCaseXmlSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for test case construction.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterTestCaseXmlSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterTestCaseXmlSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_test_case_xml_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tools_parameter_test_case_xml_schema_2_2(
        self,
        tool_id: str,
        tool_version: ToolsParameterTestCaseXmlSchemaParamToolVersion | None = None,
        run_as: ToolsParameterTestCaseXmlSchemaParamRunAs | None = None,
    ) -> Any:
        """
        Return a JSON schema description of the tool's inputs for test case construction.

        Args:
            tool_id (str)            : The tool ID for the lineage stored in Galaxy's toolbox.
            tool_version (Optional[ToolsParameterTestCaseXmlSchemaParamToolVersion])
                                     :
            run-as (Optional[ToolsParameterTestCaseXmlSchemaParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tools/{tool_id}/parameter_test_case_xml_schema"

        params: dict[str, Any] = {
            **({"tool_version": tool_version} if tool_version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
