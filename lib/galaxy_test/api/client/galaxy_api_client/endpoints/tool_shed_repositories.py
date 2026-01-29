from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

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


@runtime_checkable
class ToolShedRepositoriesClientProtocol(Protocol):
    """Protocol defining the interface of ToolShedRepositoriesClient for dependency injection."""

    async def tool_shed_repositories_index(
        self,
        name: ToolShedRepositoriesIndexParamName | None = None,
        owner: ToolShedRepositoriesIndexParamOwner | None = None,
        changeset: ToolShedRepositoriesIndexParamChangeset | None = None,
        deleted: ToolShedRepositoriesIndexParamDeleted | None = None,
        uninstalled: ToolShedRepositoriesIndexParamUninstalled | None = None,
    ) -> list[InstalledToolShedRepository]: ...

    async def tool_shed_repositories_index(
        self,
        name: ToolShedRepositoriesIndexParamName | None = None,
        owner: ToolShedRepositoriesIndexParamOwner | None = None,
        changeset: ToolShedRepositoriesIndexParamChangeset | None = None,
        deleted: ToolShedRepositoriesIndexParamDeleted | None = None,
        uninstalled: ToolShedRepositoriesIndexParamUninstalled | None = None,
    ) -> list[InstalledToolShedRepository]: ...

    async def tool_shed_repositories_check_for_updates_check_for_updates(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse: ...

    async def tool_shed_repositories_check_for_updates_check_for_updates(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse: ...

    async def tool_shed_repositories_show(
        self,
        id_: str,
    ) -> InstalledToolShedRepository: ...

    async def tool_shed_repositories_show(
        self,
        id_: str,
    ) -> InstalledToolShedRepository: ...


class ToolShedRepositoriesClient(ToolShedRepositoriesClientProtocol):
    """Client for tool_shed_repositories endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tool_shed_repositories_index(
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
            name (ToolShedRepositoriesIndexParamName | None)
                                     : Filter by repository name.
            owner (ToolShedRepositoriesIndexParamOwner | None)
                                     : Filter by repository owner.
            changeset (ToolShedRepositoriesIndexParamChangeset | None)
                                     : Filter by changeset revision.
            deleted (ToolShedRepositoriesIndexParamDeleted | None)
                                     : Filter by whether the repository has been deleted.
            uninstalled (ToolShedRepositoriesIndexParamUninstalled | None)
                                     : Filter by whether the repository has been uninstalled.

        Returns:
            List[InstalledToolShedRepository]: A list of installed tool shed repository objects.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories"

        params: dict[str, Any] = {
            **({"name": DataclassSerializer.serialize(name)} if name is not None else {}),
            **({"owner": DataclassSerializer.serialize(owner)} if owner is not None else {}),
            **({"changeset": DataclassSerializer.serialize(changeset)} if changeset is not None else {}),
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"uninstalled": DataclassSerializer.serialize(uninstalled)} if uninstalled is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[InstalledToolShedRepository])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_shed_repositories_index(
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
            name (ToolShedRepositoriesIndexParamName | None)
                                     : Filter by repository name.
            owner (ToolShedRepositoriesIndexParamOwner | None)
                                     : Filter by repository owner.
            changeset (ToolShedRepositoriesIndexParamChangeset | None)
                                     : Filter by changeset revision.
            deleted (ToolShedRepositoriesIndexParamDeleted | None)
                                     : Filter by whether the repository has been deleted.
            uninstalled (ToolShedRepositoriesIndexParamUninstalled | None)
                                     : Filter by whether the repository has been uninstalled.

        Returns:
            List[InstalledToolShedRepository]: A list of installed tool shed repository objects.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tool_shed_repositories"

        params: dict[str, Any] = {
            **({"name": DataclassSerializer.serialize(name)} if name is not None else {}),
            **({"owner": DataclassSerializer.serialize(owner)} if owner is not None else {}),
            **({"changeset": DataclassSerializer.serialize(changeset)} if changeset is not None else {}),
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"uninstalled": DataclassSerializer.serialize(uninstalled)} if uninstalled is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[InstalledToolShedRepository])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_shed_repositories_check_for_updates_check_for_updates(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse:
        """
        Check for updates to the specified repository, or all installed repositories.

        Args:
            id (ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None)
                                     :
            run-as (ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None)
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
            **({"id": DataclassSerializer.serialize(id_)} if id_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CheckForUpdatesResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_shed_repositories_check_for_updates_check_for_updates(
        self,
        id_: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None = None,
        run_as: ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None = None,
    ) -> CheckForUpdatesResponse:
        """
        Check for updates to the specified repository, or all installed repositories.

        Args:
            id (ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamId | None)
                                     :
            run-as (ToolShedRepositoriesCheckForUpdatesCheckForUpdatesParamRunAs | None)
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
            **({"id": DataclassSerializer.serialize(id_)} if id_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CheckForUpdatesResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_shed_repositories_show(
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
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/tool_shed_repositories/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), InstalledToolShedRepository)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tool_shed_repositories_show(
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
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/tool_shed_repositories/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), InstalledToolShedRepository)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
