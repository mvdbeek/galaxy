from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.check_for_updates_response import CheckForUpdatesResponse
from ..models.installed_tool_shed_repository import InstalledToolShedRepository
from ..models.tool_shed_repositories_check_for_updates_check_for_updates_param_id import (
    ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId,
)
from ..models.tool_shed_repositories_check_for_updates_check_for_updates_param_run_as import (
    ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs,
)
from ..models.tool_shed_repositories_index_param_changeset import ToolShedRepositoriesIndexParamChangeset
from ..models.tool_shed_repositories_index_param_deleted import ToolShedRepositoriesIndexParamDeleted
from ..models.tool_shed_repositories_index_param_name import ToolShedRepositoriesIndexParamName
from ..models.tool_shed_repositories_index_param_owner import ToolShedRepositoriesIndexParamOwner
from ..models.tool_shed_repositories_index_param_uninstalled import ToolShedRepositoriesIndexParamUninstalled


class ToolShedRepositoriesClient:
    """Client for tool_shed_repositories endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tool_shed_repositories_index_2_2(
        self,
        name: ToolShedRepositoriesIndexParamName | None = None,
        owner: ToolShedRepositoriesIndexParamOwner | None = None,
        changeset: ToolShedRepositoriesIndexParamChangeset | None = None,
        deleted: ToolShedRepositoriesIndexParamDeleted | None = None,
        uninstalled: ToolShedRepositoriesIndexParamUninstalled | None = None,
    ) -> list[InstalledToolShedRepository]:
        """
        Lists installed tool shed repositories.

        Args:
            name (Optional[ToolShedRepositoriesIndexParamName])
                                     : Filter by repository name.
            owner (Optional[ToolShedRepositoriesIndexParamOwner])
                                     : Filter by repository owner.
            changeset (Optional[ToolShedRepositoriesIndexParamChangeset])
                                     : Filter by changeset revision.
            deleted (Optional[ToolShedRepositoriesIndexParamDeleted])
                                     : Filter by whether the repository has been deleted.
            uninstalled (Optional[ToolShedRepositoriesIndexParamUninstalled])
                                     : Filter by whether the repository has been uninstalled.

        Returns:
            List[InstalledToolShedRepository]: A list of installed tool shed repository objects.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories"

        params: dict[str, Any] = {
            **({"name": name} if name is not None else {}),
            **({"owner": owner} if owner is not None else {}),
            **({"changeset": changeset} if changeset is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"uninstalled": uninstalled} if uninstalled is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[InstalledToolShedRepository], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_shed_repositories_index_2_2(
        self,
        name: ToolShedRepositoriesIndexParamName | None = None,
        owner: ToolShedRepositoriesIndexParamOwner | None = None,
        changeset: ToolShedRepositoriesIndexParamChangeset | None = None,
        deleted: ToolShedRepositoriesIndexParamDeleted | None = None,
        uninstalled: ToolShedRepositoriesIndexParamUninstalled | None = None,
    ) -> list[InstalledToolShedRepository]:
        """
        Lists installed tool shed repositories.

        Args:
            name (Optional[ToolShedRepositoriesIndexParamName])
                                     : Filter by repository name.
            owner (Optional[ToolShedRepositoriesIndexParamOwner])
                                     : Filter by repository owner.
            changeset (Optional[ToolShedRepositoriesIndexParamChangeset])
                                     : Filter by changeset revision.
            deleted (Optional[ToolShedRepositoriesIndexParamDeleted])
                                     : Filter by whether the repository has been deleted.
            uninstalled (Optional[ToolShedRepositoriesIndexParamUninstalled])
                                     : Filter by whether the repository has been uninstalled.

        Returns:
            List[InstalledToolShedRepository]: A list of installed tool shed repository objects.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories"

        params: dict[str, Any] = {
            **({"name": name} if name is not None else {}),
            **({"owner": owner} if owner is not None else {}),
            **({"changeset": changeset} if changeset is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"uninstalled": uninstalled} if uninstalled is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[InstalledToolShedRepository], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_shed_repositories_check_for_updates_check_for_updates_2_2(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse:
        """
        Check for updates to the specified repository, or all installed repositories.

        Args:
            id (Optional[ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId])
                                     :
            run-as (Optional[ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CheckForUpdatesResponse: A description of the state and updates message.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories/check_for_updates"

        params: dict[str, Any] = {
            **({"id": id_} if id_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CheckForUpdatesResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_shed_repositories_check_for_updates_check_for_updates_2_2(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse:
        """
        Check for updates to the specified repository, or all installed repositories.

        Args:
            id (Optional[ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId])
                                     :
            run-as (Optional[ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CheckForUpdatesResponse: A description of the state and updates message.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories/check_for_updates"

        params: dict[str, Any] = {
            **({"id": id_} if id_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CheckForUpdatesResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_shed_repositories_show_2_2(
        self,
        id_: str,
    ) -> InstalledToolShedRepository:
        """
        Show installed tool shed repository.

        Args:
            id (str)                 : The encoded database identifier of the installed Tool
                                       Shed Repository.

        Returns:
            InstalledToolShedRepository: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InstalledToolShedRepository, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def tool_shed_repositories_show_2_2(
        self,
        id_: str,
    ) -> InstalledToolShedRepository:
        """
        Show installed tool shed repository.

        Args:
            id (str)                 : The encoded database identifier of the installed Tool
                                       Shed Repository.

        Returns:
            InstalledToolShedRepository: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InstalledToolShedRepository, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
