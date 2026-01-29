from typing import TYPE_CHECKING
from uuid import UUID

from ...models.anonymous_array_item_121 import AnonymousArrayItem121
from ...models.concrete_object_store_model import ConcreteObjectStoreModel
from ...models.create_instance_payload import CreateInstancePayload
from ...models.object_store_template_summaries import ObjectStoreTemplateSummaries
from ...models.object_stores_create_instance_param_run_as import ObjectStoresCreateInstanceParamRunAs
from ...models.object_stores_index_param_run_as import ObjectStoresIndexParamRunAs
from ...models.object_stores_instances_get_param_run_as import ObjectStoresInstancesGetParamRunAs
from ...models.object_stores_instances_index_param_run_as import ObjectStoresInstancesIndexParamRunAs
from ...models.object_stores_instances_purge_param_run_as import ObjectStoresInstancesPurgeParamRunAs
from ...models.object_stores_instances_test_instance_param_run_as import ObjectStoresInstancesTestInstanceParamRunAs
from ...models.object_stores_instances_update_param_run_as import ObjectStoresInstancesUpdateParamRunAs
from ...models.object_stores_instances_update_request_body import ObjectStoresInstancesUpdateRequestBody
from ...models.object_stores_show_info_param_run_as import ObjectStoresShowInfoParamRunAs
from ...models.object_stores_templates_index_param_run_as import ObjectStoresTemplatesIndexParamRunAs
from ...models.object_stores_test_instances_update_param_run_as import ObjectStoresTestInstancesUpdateParamRunAs
from ...models.object_stores_test_instances_update_request_body import ObjectStoresTestInstancesUpdateRequestBody
from ...models.object_stores_test_new_instance_configuration_param_run_as import (
    ObjectStoresTestNewInstanceConfigurationParamRunAs,
)
from ...models.plugin_status import PluginStatus
from ...models.user_concrete_object_store_model import UserConcreteObjectStoreModel

if TYPE_CHECKING:
    pass


class MockObjectStoresClient:
    """
    Mock implementation of ObjectStoresClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestObjectStoresClient(MockObjectStoresClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def object_stores_instances_index(
        self,
        run_as: ObjectStoresInstancesIndexParamRunAs | None = None,
    ) -> list[UserConcreteObjectStoreModel]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_instances_index() not implemented. Override this method in your test subclass."
        )

    async def object_stores_create_instance(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresCreateInstanceParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_create_instance() not implemented. Override this method in your test subclass."
        )

    async def object_stores_test_new_instance_configuration(
        self,
        body: CreateInstancePayload,
        run_as: ObjectStoresTestNewInstanceConfigurationParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_test_new_instance_configuration() not implemented. Override this method in your test subclass."
        )

    async def object_stores_instances_purge(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesPurgeParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_instances_purge() not implemented. Override this method in your test subclass."
        )

    async def object_stores_instances_get(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesGetParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_instances_get() not implemented. Override this method in your test subclass."
        )

    async def object_stores_instances_update(
        self,
        uuid_: UUID,
        body: ObjectStoresInstancesUpdateRequestBody,
        run_as: ObjectStoresInstancesUpdateParamRunAs | None = None,
    ) -> UserConcreteObjectStoreModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_instances_update() not implemented. Override this method in your test subclass."
        )

    async def object_stores_instances_test_instance(
        self,
        uuid_: UUID,
        run_as: ObjectStoresInstancesTestInstanceParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_instances_test_instance() not implemented. Override this method in your test subclass."
        )

    async def object_stores_test_instances_update(
        self,
        uuid_: UUID,
        body: ObjectStoresTestInstancesUpdateRequestBody,
        run_as: ObjectStoresTestInstancesUpdateParamRunAs | None = None,
    ) -> PluginStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_test_instances_update() not implemented. Override this method in your test subclass."
        )

    async def object_stores_templates_index(
        self,
        run_as: ObjectStoresTemplatesIndexParamRunAs | None = None,
    ) -> ObjectStoreTemplateSummaries:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_templates_index() not implemented. Override this method in your test subclass."
        )

    async def object_stores_index(
        self,
        selectable: bool | None = None,
        run_as: ObjectStoresIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem121]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_index() not implemented. Override this method in your test subclass."
        )

    async def object_stores_show_info(
        self,
        object_store_id: str,
        run_as: ObjectStoresShowInfoParamRunAs | None = None,
    ) -> ConcreteObjectStoreModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockObjectStoresClient.object_stores_show_info() not implemented. Override this method in your test subclass."
        )
