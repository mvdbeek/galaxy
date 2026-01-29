from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.group_role_list_response import GroupRoleListResponse
from ..models.group_role_response import GroupRoleResponse
from ..models.group_roles_roles_delete_param_run_as import GroupRolesRolesDeleteParamRunAs
from ..models.group_roles_roles_index_param_run_as import GroupRolesRolesIndexParamRunAs
from ..models.group_roles_roles_show_param_run_as import GroupRolesRolesShowParamRunAs
from ..models.group_roles_roles_update_param_run_as import GroupRolesRolesUpdateParamRunAs


@runtime_checkable
class GroupRolesClientProtocol(Protocol):
    """Protocol defining the interface of GroupRolesClient for dependency injection."""

    async def group_roles_roles_index(
        self,
        group_id: str,
        run_as: GroupRolesRolesIndexParamRunAs | None = None,
    ) -> GroupRoleListResponse: ...

    async def group_roles_roles_index(
        self,
        group_id: str,
        run_as: GroupRolesRolesIndexParamRunAs | None = None,
    ) -> GroupRoleListResponse: ...

    async def group_roles_roles_delete(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesDeleteParamRunAs | None = None,
    ) -> GroupRoleResponse: ...

    async def group_roles_roles_delete(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesDeleteParamRunAs | None = None,
    ) -> GroupRoleResponse: ...

    async def group_roles_roles_show(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesShowParamRunAs | None = None,
    ) -> GroupRoleResponse: ...

    async def group_roles_roles_show(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesShowParamRunAs | None = None,
    ) -> GroupRoleResponse: ...

    async def group_roles_roles_update(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesUpdateParamRunAs | None = None,
    ) -> GroupRoleResponse: ...

    async def group_roles_roles_update(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesUpdateParamRunAs | None = None,
    ) -> GroupRoleResponse: ...


class GroupRolesClient(GroupRolesClientProtocol):
    """Client for group_roles endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def group_roles_roles_index(
        self,
        group_id: str,
        run_as: GroupRolesRolesIndexParamRunAs | None = None,
    ) -> GroupRoleListResponse:
        """
        Displays a collection (list) of groups.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupRolesRolesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_index(
        self,
        group_id: str,
        run_as: GroupRolesRolesIndexParamRunAs | None = None,
    ) -> GroupRoleListResponse:
        """
        Displays a collection (list) of groups.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupRolesRolesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_delete(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesDeleteParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Removes a role from a group

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_delete(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesDeleteParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Removes a role from a group

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_show(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesShowParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Displays information about a group role.

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_show(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesShowParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Displays information about a group role.

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_update(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesUpdateParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Adds a role to a group

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def group_roles_roles_update(
        self,
        group_id: str,
        role_id: str,
        run_as: GroupRolesRolesUpdateParamRunAs | None = None,
    ) -> GroupRoleResponse:
        """
        Adds a role to a group

        Args:
            group_id (str)           : The ID of the group.
            role_id (str)            : The ID of the role.
            run-as (GroupRolesRolesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupRoleResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)
        role_id = DataclassSerializer.serialize(role_id)

        url = f"{self.base_url}/api/groups/{group_id}/roles/{role_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupRoleResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
