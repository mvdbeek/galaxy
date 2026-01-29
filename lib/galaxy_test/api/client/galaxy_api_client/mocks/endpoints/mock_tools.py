from typing import IO, TYPE_CHECKING, Any
from uuid import UUID

from ...models.anonymous_array_item_123 import AnonymousArrayItem123
from ...models.create_data_landing_payload import CreateDataLandingPayload
from ...models.create_file_landing_payload import CreateFileLandingPayload
from ...models.create_tool_landing_request_payload import CreateToolLandingRequestPayload
from ...models.parse_fetch_workbook import ParseFetchWorkbook
from ...models.tool_landing_request import ToolLandingRequest
from ...models.tool_request_detailed_model import ToolRequestDetailedModel
from ...models.tools_claim_claim_landing_param_run_as import ToolsClaimClaimLandingParamRunAs
from ...models.tools_claim_claim_landing_request_body import ToolsClaimClaimLandingRequestBody
from ...models.tools_create_data_landing_param_run_as import ToolsCreateDataLandingParamRunAs
from ...models.tools_create_file_landing_param_run_as import ToolsCreateFileLandingParamRunAs
from ...models.tools_create_landing_param_run_as import ToolsCreateLandingParamRunAs
from ...models.tools_fetch_fetch_form_param_run_as import ToolsFetchFetchFormParamRunAs
from ...models.tools_fetch_workbook_download_param_filename import ToolsFetchWorkbookDownloadParamFilename
from ...models.tools_fetch_workbook_download_param_run_as import ToolsFetchWorkbookDownloadParamRunAs
from ...models.tools_fetch_workbook_parse_200_response import ToolsFetchWorkbookParse200Response
from ...models.tools_fetch_workbook_parse_param_run_as import ToolsFetchWorkbookParseParamRunAs
from ...models.tools_get_landing_param_run_as import ToolsGetLandingParamRunAs
from ...models.tools_get_tool_request_param_run_as import ToolsGetToolRequestParamRunAs
from ...models.tools_icon_get_icon_param_run_as import ToolsIconGetIconParamRunAs
from ...models.tools_inputs_tool_inputs_param_run_as import ToolsInputsToolInputsParamRunAs
from ...models.tools_inputs_tool_inputs_param_tool_version import ToolsInputsToolInputsParamToolVersion
from ...models.tools_parameter_landing_request_schema_param_run_as import ToolsParameterLandingRequestSchemaParamRunAs
from ...models.tools_parameter_landing_request_schema_param_tool_version import (
    ToolsParameterLandingRequestSchemaParamToolVersion,
)
from ...models.tools_parameter_request_schema_param_run_as import ToolsParameterRequestSchemaParamRunAs
from ...models.tools_parameter_request_schema_param_tool_version import ToolsParameterRequestSchemaParamToolVersion
from ...models.tools_parameter_test_case_xml_schema_param_run_as import ToolsParameterTestCaseXmlSchemaParamRunAs
from ...models.tools_parameter_test_case_xml_schema_param_tool_version import (
    ToolsParameterTestCaseXmlSchemaParamToolVersion,
)
from ...models.tools_state_tool_request_state_param_run_as import ToolsStateToolRequestStateParamRunAs

if TYPE_CHECKING:
    pass


class MockToolsClient:
    """
    Mock implementation of ToolsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestToolsClient(MockToolsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tools_create_data_landing(
        self,
        body: CreateDataLandingPayload,
        run_as: ToolsCreateDataLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_create_data_landing() not implemented. Override this method in your test subclass."
        )

    async def tools_create_file_landing(
        self,
        body: CreateFileLandingPayload,
        run_as: ToolsCreateFileLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_create_file_landing() not implemented. Override this method in your test subclass."
        )

    async def tools_create_landing(
        self,
        body: CreateToolLandingRequestPayload,
        run_as: ToolsCreateLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_create_landing() not implemented. Override this method in your test subclass."
        )

    async def tools_get_landing(
        self,
        uuid_: UUID,
        run_as: ToolsGetLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_get_landing() not implemented. Override this method in your test subclass."
        )

    async def tools_claim_claim_landing(
        self,
        uuid_: UUID,
        body: ToolsClaimClaimLandingRequestBody | None,
        run_as: ToolsClaimClaimLandingParamRunAs | None = None,
    ) -> ToolLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_claim_claim_landing() not implemented. Override this method in your test subclass."
        )

    async def tools_get_tool_request(
        self,
        id_: str,
        run_as: ToolsGetToolRequestParamRunAs | None = None,
    ) -> ToolRequestDetailedModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_get_tool_request() not implemented. Override this method in your test subclass."
        )

    async def tools_state_tool_request_state(
        self,
        id_: str,
        run_as: ToolsStateToolRequestStateParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_state_tool_request_state() not implemented. Override this method in your test subclass."
        )

    async def tools_fetch_fetch_form(
        self,
        files: dict[str, IO[Any]],
        run_as: ToolsFetchFetchFormParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_fetch_fetch_form() not implemented. Override this method in your test subclass."
        )

    async def tools_fetch_workbook_download(
        self,
        type_: str | None = None,
        collection_type: str | None = None,
        filename: ToolsFetchWorkbookDownloadParamFilename | None = None,
        run_as: ToolsFetchWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_fetch_workbook_download() not implemented. Override this method in your test subclass."
        )

    async def tools_fetch_workbook_parse(
        self,
        body: ParseFetchWorkbook,
        run_as: ToolsFetchWorkbookParseParamRunAs | None = None,
    ) -> ToolsFetchWorkbookParse200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_fetch_workbook_parse() not implemented. Override this method in your test subclass."
        )

    async def tools_icon_get_icon(
        self,
        tool_id: str,
        run_as: ToolsIconGetIconParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_icon_get_icon() not implemented. Override this method in your test subclass."
        )

    async def tools_inputs_tool_inputs(
        self,
        tool_id: str,
        tool_version: ToolsInputsToolInputsParamToolVersion | None = None,
        run_as: ToolsInputsToolInputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem123]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_inputs_tool_inputs() not implemented. Override this method in your test subclass."
        )

    async def tools_parameter_landing_request_schema(
        self,
        tool_id: str,
        tool_version: ToolsParameterLandingRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterLandingRequestSchemaParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_parameter_landing_request_schema() not implemented. Override this method in your test subclass."
        )

    async def tools_parameter_request_schema(
        self,
        tool_id: str,
        tool_version: ToolsParameterRequestSchemaParamToolVersion | None = None,
        run_as: ToolsParameterRequestSchemaParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_parameter_request_schema() not implemented. Override this method in your test subclass."
        )

    async def tools_parameter_test_case_xml_schema(
        self,
        tool_id: str,
        tool_version: ToolsParameterTestCaseXmlSchemaParamToolVersion | None = None,
        run_as: ToolsParameterTestCaseXmlSchemaParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolsClient.tools_parameter_test_case_xml_schema() not implemented. Override this method in your test subclass."
        )
