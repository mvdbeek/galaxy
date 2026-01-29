from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.group_create_payload import GroupCreatePayload
from ..models.group_list_response import GroupListResponse
from ..models.group_response import GroupResponse
from ..models.group_update_payload import GroupUpdatePayload
from ..models.groups_create_param_run_as import GroupsCreateParamRunAs
from ..models.groups_delete_param_run_as import GroupsDeleteParamRunAs
from ..models.groups_index_param_run_as import GroupsIndexParamRunAs
from ..models.groups_purge_purge_param_run_as import GroupsPurgePurgeParamRunAs
from ..models.groups_show_param_run_as import GroupsShowParamRunAs
from ..models.groups_undelete_undelete_param_run_as import GroupsUndeleteUndeleteParamRunAs
from ..models.groups_update_param_run_as import GroupsUpdateParamRunAs


@runtime_checkable
class GroupsClientProtocol(Protocol):
    """Protocol defining the interface of GroupsClient for dependency injection."""

    async def groups_index(
        self,
        run_as: GroupsIndexParamRunAs | None = None,
    ) -> GroupListResponse: ...

    async def groups_index(
        self,
        run_as: GroupsIndexParamRunAs | None = None,
    ) -> GroupListResponse: ...

    async def groups_create(
        self,
        body: GroupCreatePayload,
        run_as: GroupsCreateParamRunAs | None = None,
    ) -> GroupListResponse: ...

    async def groups_create(
        self,
        body: GroupCreatePayload,
        run_as: GroupsCreateParamRunAs | None = None,
    ) -> GroupListResponse: ...

    async def groups_delete(
        self,
        group_id: str,
        run_as: GroupsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def groups_delete(
        self,
        group_id: str,
        run_as: GroupsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def groups_show(
        self,
        group_id: str,
        run_as: GroupsShowParamRunAs | None = None,
    ) -> GroupResponse: ...

    async def groups_show(
        self,
        group_id: str,
        run_as: GroupsShowParamRunAs | None = None,
    ) -> GroupResponse: ...

    async def groups_update(
        self,
        group_id: str,
        body: GroupUpdatePayload,
        run_as: GroupsUpdateParamRunAs | None = None,
    ) -> GroupResponse: ...

    async def groups_update(
        self,
        group_id: str,
        body: GroupUpdatePayload,
        run_as: GroupsUpdateParamRunAs | None = None,
    ) -> GroupResponse: ...

    async def groups_purge_purge(
        self,
        group_id: str,
        run_as: GroupsPurgePurgeParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def groups_purge_purge(
        self,
        group_id: str,
        run_as: GroupsPurgePurgeParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def groups_undelete_undelete(
        self,
        group_id: str,
        run_as: GroupsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def groups_undelete_undelete(
        self,
        group_id: str,
        run_as: GroupsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class GroupsClient(GroupsClientProtocol):
    """Client for groups endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def groups_index(
        self,
        run_as: GroupsIndexParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Displays a collection (list) of groups.

        Args:
            run-as (GroupsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_index(
        self,
        run_as: GroupsIndexParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Displays a collection (list) of groups.

        Args:
            run-as (GroupsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_create(
        self,
        body: GroupCreatePayload,
        run_as: GroupsCreateParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Creates a new group.

        Args:
            run-as (GroupsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (GroupCreatePayload): Request body. (json)

        Returns:
            GroupListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: GroupCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_create(
        self,
        body: GroupCreatePayload,
        run_as: GroupsCreateParamRunAs | None = None,
    ) -> GroupListResponse:
        """
        Creates a new group.

        Args:
            run-as (GroupsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (GroupCreatePayload): Request body. (json)

        Returns:
            GroupListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: GroupCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_delete(
        self,
        group_id: str,
        run_as: GroupsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_delete(
        self,
        group_id: str,
        run_as: GroupsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_show(
        self,
        group_id: str,
        run_as: GroupsShowParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Displays information about a group.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_show(
        self,
        group_id: str,
        run_as: GroupsShowParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Displays information about a group.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_update(
        self,
        group_id: str,
        body: GroupUpdatePayload,
        run_as: GroupsUpdateParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Modifies a group.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (GroupUpdatePayload): Request body. (json)

        Returns:
            GroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: GroupUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_update(
        self,
        group_id: str,
        body: GroupUpdatePayload,
        run_as: GroupsUpdateParamRunAs | None = None,
    ) -> GroupResponse:
        """
        Modifies a group.

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (GroupUpdatePayload): Request body. (json)

        Returns:
            GroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: GroupUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_purge_purge(
        self,
        group_id: str,
        run_as: GroupsPurgePurgeParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Purge

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsPurgePurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/purge"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_purge_purge(
        self,
        group_id: str,
        run_as: GroupsPurgePurgeParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Purge

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsPurgePurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/purge"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_undelete_undelete(
        self,
        group_id: str,
        run_as: GroupsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Undelete

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def groups_undelete_undelete(
        self,
        group_id: str,
        run_as: GroupsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Undelete

        Args:
            group_id (str)           : The ID of the group.
            run-as (GroupsUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/groups/{group_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
