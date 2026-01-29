from typing import TYPE_CHECKING

from ...models.group_role_list_response import GroupRoleListResponse
from ...models.group_role_response import GroupRoleResponse
from ...models.group_roles_roles_delete_param_run_as import GroupRolesRolesDeleteParamRunAs
from ...models.group_roles_roles_index_param_run_as import GroupRolesRolesIndexParamRunAs
from ...models.group_roles_roles_show_param_run_as import GroupRolesRolesShowParamRunAs
from ...models.group_roles_roles_update_param_run_as import GroupRolesRolesUpdateParamRunAs

if TYPE_CHECKING:
    pass


class MockGroupRolesClient:
    """
    Mock implementation of GroupRolesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestGroupRolesClient(MockGroupRolesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def group_roles_roles_index(
        self,
        group_id: str,
        run_as: GroupRolesRolesIndexParamRunAs | None = None,
    ) -> GroupRoleListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupRolesClient.group_roles_roles_index() not implemented. Override this method in your test subclass."
        )

    async def group_roles_roles_delete(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesDeleteParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupRolesClient.group_roles_roles_delete() not implemented. Override this method in your test subclass."
        )

    async def group_roles_roles_show(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesShowParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupRolesClient.group_roles_roles_show() not implemented. Override this method in your test subclass."
        )

    async def group_roles_roles_update(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesUpdateParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupRolesClient.group_roles_roles_update() not implemented. Override this method in your test subclass."
        )
