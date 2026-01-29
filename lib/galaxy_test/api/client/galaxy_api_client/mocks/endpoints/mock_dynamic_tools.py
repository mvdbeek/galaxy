from typing import TYPE_CHECKING, Any

from ...models.dynamic_tools_build_build_param_run_as import DynamicToolsBuildBuildParamRunAs
from ...models.dynamic_tools_create_param_run_as import DynamicToolsCreateParamRunAs
from ...models.dynamic_tools_create_param_run_as_2 import DynamicToolsCreateParamRunAs2
from ...models.dynamic_tools_create_request_body import DynamicToolsCreateRequestBody
from ...models.dynamic_tools_delete_200_response import DynamicToolsDelete200Response
from ...models.dynamic_tools_delete_param_dynamic_tool_id import DynamicToolsDeleteParamDynamicToolId
from ...models.dynamic_tools_delete_param_run_as import DynamicToolsDeleteParamRunAs
from ...models.dynamic_tools_delete_param_run_as_2 import DynamicToolsDeleteParamRunAs2
from ...models.dynamic_tools_index_param_run_as import DynamicToolsIndexParamRunAs
from ...models.dynamic_tools_runtime_model_runtime_model_param_run_as import (
    DynamicToolsRuntimeModelRuntimeModelParamRunAs,
)
from ...models.dynamic_tools_show_param_dynamic_tool_id import DynamicToolsShowParamDynamicToolId
from ...models.dynamic_tools_show_param_run_as import DynamicToolsShowParamRunAs
from ...models.dynamic_unprivileged_tool_create_payload import DynamicUnprivilegedToolCreatePayload
from ...models.unprivileged_tool_response import UnprivilegedToolResponse

if TYPE_CHECKING:
    pass


class MockDynamicToolsClient:
    """
    Mock implementation of DynamicToolsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDynamicToolsClient(MockDynamicToolsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def dynamic_tools_index(
        self,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_index() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_create(
        self,
        body: DynamicToolsCreateRequestBody,
        run_as: DynamicToolsCreateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_create() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_delete(
        self,
        dynamic_tool_id: DynamicToolsDeleteParamDynamicToolId,
        run_as: DynamicToolsDeleteParamRunAs | None = None,
    ) -> DynamicToolsDelete200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_delete() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_show(
        self,
        dynamic_tool_id: DynamicToolsShowParamDynamicToolId,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_show() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_index_2(
        self,
        active: bool | None = None,
        run_as: DynamicToolsIndexParamRunAs | None = None,
    ) -> list[UnprivilegedToolResponse]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_index_2() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_create_2(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsCreateParamRunAs2 | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_create_2() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_build_build(
        self,
        history_id: str,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsBuildBuildParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_build_build() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_runtime_model_runtime_model(
        self,
        body: DynamicUnprivilegedToolCreatePayload,
        run_as: DynamicToolsRuntimeModelRuntimeModelParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_runtime_model_runtime_model() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_delete_2(
        self,
        uuid_: str,
        run_as: DynamicToolsDeleteParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_delete_2() not implemented. Override this method in your test subclass."
        )

    async def dynamic_tools_show_2(
        self,
        uuid_: str,
        run_as: DynamicToolsShowParamRunAs | None = None,
    ) -> UnprivilegedToolResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDynamicToolsClient.dynamic_tools_show_2() not implemented. Override this method in your test subclass."
        )
