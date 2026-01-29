from typing import TYPE_CHECKING
from uuid import UUID

from ...models.create_instance_payload import CreateInstancePayload
from ...models.file_source_template_summaries import FileSourceTemplateSummaries
from ...models.file_sources_create_instance_param_run_as import FileSourcesCreateInstanceParamRunAs
from ...models.file_sources_instances_get_param_run_as import FileSourcesInstancesGetParamRunAs
from ...models.file_sources_instances_index_param_run_as import FileSourcesInstancesIndexParamRunAs
from ...models.file_sources_instances_purge_param_run_as import FileSourcesInstancesPurgeParamRunAs
from ...models.file_sources_instances_test_instance_param_run_as import FileSourcesInstancesTestInstanceParamRunAs
from ...models.file_sources_instances_update_param_run_as import FileSourcesInstancesUpdateParamRunAs
from ...models.file_sources_instances_update_request_body import FileSourcesInstancesUpdateRequestBody
from ...models.file_sources_template_oauth_2_param_run_as import FileSourcesTemplateOauth2ParamRunAs
from ...models.file_sources_templates_index_param_run_as import FileSourcesTemplatesIndexParamRunAs
from ...models.file_sources_test_instances_update_param_run_as import FileSourcesTestInstancesUpdateParamRunAs
from ...models.file_sources_test_instances_update_request_body import FileSourcesTestInstancesUpdateRequestBody
from ...models.file_sources_test_new_instance_configuration_param_run_as import (
    FileSourcesTestNewInstanceConfigurationParamRunAs,
)
from ...models.o_auth_2_info import OAuth2Info
from ...models.plugin_status import PluginStatus
from ...models.user_file_source_model import UserFileSourceModel

if TYPE_CHECKING:
    pass


class MockFileSourcesClient:
    """
    Mock implementation of FileSourcesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestFileSourcesClient(MockFileSourcesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def file_sources_instances_index(
        self,
        run_as: FileSourcesInstancesIndexParamRunAs | None = None,
    ) -> list[UserFileSourceModel]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_instances_index() not implemented. Override this method in your test subclass."
        )

    async def file_sources_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesCreateInstanceParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_create_instance() not implemented. Override this method in your test subclass."
        )

    async def file_sources_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: FileSourcesTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_test_new_instance_configuration() not implemented. Override this method in your test subclass."
        )

    async def file_sources_instances_purge(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_instances_purge() not implemented. Override this method in your test subclass."
        )

    async def file_sources_instances_get(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesGetParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_instances_get() not implemented. Override this method in your test subclass."
        )

    async def file_sources_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesInstancesUpdateRequestBody,
        run_as: FileSourcesInstancesUpdateParamRunAs | None = None,
    ) -> UserFileSourceModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_instances_update() not implemented. Override this method in your test subclass."
        )

    async def file_sources_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: FileSourcesInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_instances_test_instance() not implemented. Override this method in your test subclass."
        )

    async def file_sources_test_instances_update(
        self,
        uuid_: UUID,
        body: FileSourcesTestInstancesUpdateRequestBody,
        run_as: FileSourcesTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_test_instances_update() not implemented. Override this method in your test subclass."
        )

    async def file_sources_templates_index(
        self,
        run_as: FileSourcesTemplatesIndexParamRunAs | None = None,
    ) -> FileSourceTemplateSummaries:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_templates_index() not implemented. Override this method in your test subclass."
        )

    async def file_sources_template_oauth2(
        self,
        template_id: str,
        template_version: int,
        run_as: FileSourcesTemplateOauth2ParamRunAs | None = None,
    ) -> OAuth2Info:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockFileSourcesClient.file_sources_template_oauth2() not implemented. Override this method in your test subclass."
        )
