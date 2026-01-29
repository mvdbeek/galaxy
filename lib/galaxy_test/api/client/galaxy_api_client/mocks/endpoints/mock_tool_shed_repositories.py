from typing import TYPE_CHECKING

from ...models.check_for_updates_response import CheckForUpdatesResponse
from ...models.installed_tool_shed_repository import InstalledToolShedRepository
from ...models.tool_shed_repositories_check_for_updates_check_for_updates_param_id import (
    ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId,
)
from ...models.tool_shed_repositories_check_for_updates_check_for_updates_param_run_as import (
    ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs,
)
from ...models.tool_shed_repositories_index_param_changeset import ToolShedRepositoriesIndexParamChangeset
from ...models.tool_shed_repositories_index_param_deleted import ToolShedRepositoriesIndexParamDeleted
from ...models.tool_shed_repositories_index_param_name import ToolShedRepositoriesIndexParamName
from ...models.tool_shed_repositories_index_param_owner import ToolShedRepositoriesIndexParamOwner
from ...models.tool_shed_repositories_index_param_uninstalled import ToolShedRepositoriesIndexParamUninstalled

if TYPE_CHECKING:
    pass


class MockToolShedRepositoriesClient:
    """
    Mock implementation of ToolShedRepositoriesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestToolShedRepositoriesClient(MockToolShedRepositoriesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def tool_shed_repositories_index(
        self,
        name: ToolShedRepositoriesIndexParamName | None = None,
        owner: ToolShedRepositoriesIndexParamOwner | None = None,
        changeset: ToolShedRepositoriesIndexParamChangeset | None = None,
        deleted: ToolShedRepositoriesIndexParamDeleted | None = None,
        uninstalled: ToolShedRepositoriesIndexParamUninstalled | None = None,
    ) -> list[InstalledToolShedRepository]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolShedRepositoriesClient.tool_shed_repositories_index() not implemented. Override this method in your test subclass."
        )

    async def tool_shed_repositories_check_for_updates_check_for_updates(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolShedRepositoriesClient.tool_shed_repositories_check_for_updates_check_for_updates() not implemented. Override this method in your test subclass."
        )

    async def tool_shed_repositories_show(
        self,
        id_: str,
    ) -> InstalledToolShedRepository:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockToolShedRepositoriesClient.tool_shed_repositories_show() not implemented. Override this method in your test subclass."
        )
