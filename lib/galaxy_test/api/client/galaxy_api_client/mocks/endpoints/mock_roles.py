from typing import TYPE_CHECKING

from ...models.role_definition_model import RoleDefinitionModel
from ...models.role_list_response import RoleListResponse
from ...models.role_model_response import RoleModelResponse
from ...models.roles_create_param_run_as import RolesCreateParamRunAs
from ...models.roles_delete_param_run_as import RolesDeleteParamRunAs
from ...models.roles_index_param_run_as import RolesIndexParamRunAs
from ...models.roles_purge_purge_param_run_as import RolesPurgePurgeParamRunAs
from ...models.roles_show_param_run_as import RolesShowParamRunAs
from ...models.roles_undelete_undelete_param_run_as import RolesUndeleteUndeleteParamRunAs

if TYPE_CHECKING:
    pass


class MockRolesClient:
    """
    Mock implementation of RolesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestRolesClient(MockRolesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def roles_index(
        self,
        run_as: RolesIndexParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_index() not implemented. Override this method in your test subclass."
        )

    async def roles_create(
        self,
        body: RoleDefinitionModel,
        run_as: RolesCreateParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_create() not implemented. Override this method in your test subclass."
        )

    async def roles_delete(
        self,
        id_: str,
        run_as: RolesDeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_delete() not implemented. Override this method in your test subclass."
        )

    async def roles_show(
        self,
        id_: str,
        run_as: RolesShowParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_show() not implemented. Override this method in your test subclass."
        )

    async def roles_purge_purge(
        self,
        id_: str,
        run_as: RolesPurgePurgeParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_purge_purge() not implemented. Override this method in your test subclass."
        )

    async def roles_undelete_undelete(
        self,
        id_: str,
        run_as: RolesUndeleteUndeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockRolesClient.roles_undelete_undelete() not implemented. Override this method in your test subclass."
        )
