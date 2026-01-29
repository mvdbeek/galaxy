from typing import TYPE_CHECKING

from ...models.group_user_list_response import GroupUserListResponse
from ...models.group_user_response import GroupUserResponse
from ...models.group_users_user_delete_param_run_as import GroupUsersUserDeleteParamRunAs
from ...models.group_users_user_show_param_run_as import GroupUsersUserShowParamRunAs
from ...models.group_users_user_update_param_run_as import GroupUsersUserUpdateParamRunAs
from ...models.group_users_users_delete_param_run_as import GroupUsersUsersDeleteParamRunAs
from ...models.group_users_users_index_param_run_as import GroupUsersUsersIndexParamRunAs
from ...models.group_users_users_show_param_run_as import GroupUsersUsersShowParamRunAs
from ...models.group_users_users_update_param_run_as import GroupUsersUsersUpdateParamRunAs

if TYPE_CHECKING:
    pass


class MockGroupUsersClient:
    """
    Mock implementation of GroupUsersClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestGroupUsersClient(MockGroupUsersClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def group_users_user_delete(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_user_delete() not implemented. Override this method in your test subclass."
        )

    async def group_users_user_show(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_user_show() not implemented. Override this method in your test subclass."
        )

    async def group_users_user_update(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_user_update() not implemented. Override this method in your test subclass."
        )

    async def group_users_users_index(
        self,
        group_id: str,
        run_as: GroupUsersUsersIndexParamRunAs | None = None,
    ) -> GroupUserListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_users_index() not implemented. Override this method in your test subclass."
        )

    async def group_users_users_delete(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_users_delete() not implemented. Override this method in your test subclass."
        )

    async def group_users_users_show(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_users_show() not implemented. Override this method in your test subclass."
        )

    async def group_users_users_update(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGroupUsersClient.group_users_users_update() not implemented. Override this method in your test subclass."
        )
