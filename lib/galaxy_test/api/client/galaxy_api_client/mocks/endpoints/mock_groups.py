from typing import TYPE_CHECKING, Any

from ...models.group_create_payload import GroupCreatePayload
from ...models.group_list_response import GroupListResponse
from ...models.group_response import GroupResponse
from ...models.group_update_payload import GroupUpdatePayload
from ...models.groups_create_param_run_as import GroupsCreateParamRunAs
from ...models.groups_delete_param_run_as import GroupsDeleteParamRunAs
from ...models.groups_index_param_run_as import GroupsIndexParamRunAs
from ...models.groups_purge_purge_param_run_as import GroupsPurgePurgeParamRunAs
from ...models.groups_show_param_run_as import GroupsShowParamRunAs
from ...models.groups_undelete_undelete_param_run_as import GroupsUndeleteUndeleteParamRunAs
from ...models.groups_update_param_run_as import GroupsUpdateParamRunAs

if TYPE_CHECKING:
    pass


class MockGroupsClient:
    """
    Mock implementation of GroupsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestGroupsClient(MockGroupsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def groups_index(
        self,
        run_as: GroupsIndexParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_index() not implemented. Override this method in your test subclass."
        )

    async def groups_create(
        self,
        body: GroupCreatePayload,
        run_as: GroupsCreateParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_create() not implemented. Override this method in your test subclass."
        )

    async def groups_delete(
        self,
        group_id: str,
        run_as: GroupsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_delete() not implemented. Override this method in your test subclass."
        )

    async def groups_show(
        self,
        group_id: str,
        run_as: GroupsShowParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_show() not implemented. Override this method in your test subclass."
        )

    async def groups_update(
        self,
        group_id: str,
        body: GroupUpdatePayload,
        run_as: GroupsUpdateParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_update() not implemented. Override this method in your test subclass."
        )

    async def groups_purge_purge(
        self,
        group_id: str,
        run_as: GroupsPurgePurgeParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_purge_purge() not implemented. Override this method in your test subclass."
        )

    async def groups_undelete_undelete(
        self,
        group_id: str,
        run_as: GroupsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupsClient.groups_undelete_undelete() not implemented. Override this method in your test subclass."
        )
