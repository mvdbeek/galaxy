from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.group_user_list_response import GroupUserListResponse
from ..models.group_user_response import GroupUserResponse
from ..models.group_users_user_delete_param_run_as import GroupUsersUserDeleteParamRunAs
from ..models.group_users_user_show_param_run_as import GroupUsersUserShowParamRunAs
from ..models.group_users_user_update_param_run_as import GroupUsersUserUpdateParamRunAs
from ..models.group_users_users_delete_param_run_as import GroupUsersUsersDeleteParamRunAs
from ..models.group_users_users_index_param_run_as import GroupUsersUsersIndexParamRunAs
from ..models.group_users_users_show_param_run_as import GroupUsersUsersShowParamRunAs
from ..models.group_users_users_update_param_run_as import GroupUsersUsersUpdateParamRunAs


class GroupUsersClient:
    """Client for group_users endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def group_users_user_delete_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id} Removes a user from a
        group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_user_delete_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id} Removes a user from a
        group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_user_show_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Displays information about a group user.

        Displays information about a group user.

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_user_show_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Displays information about a group user.

        Displays information about a group user.

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_user_update_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id} Adds a user to a group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_user_update_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUserUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id} Adds a user to a group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUserUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/user/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_index_2_2(
        self,
        group_id: str,
        run_as: GroupUsersUsersIndexParamRunAs | None = None,
    ) -> GroupUserListResponse:
        """
        Displays a collection (list) of groups.

        GET /api/groups/{encoded_group_id}/users Displays a collection (list) of groups.

        Args:
            group_id (str)           : The ID of the group.
            run-as (Optional[GroupUsersUsersIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_index_2_2(
        self,
        group_id: str,
        run_as: GroupUsersUsersIndexParamRunAs | None = None,
    ) -> GroupUserListResponse:
        """
        Displays a collection (list) of groups.

        GET /api/groups/{encoded_group_id}/users Displays a collection (list) of groups.

        Args:
            group_id (str)           : The ID of the group.
            run-as (Optional[GroupUsersUsersIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_delete_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id} Removes a user from a
        group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_delete_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersDeleteParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id} Removes a user from a
        group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_show_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Displays information about a group user.

        Displays information about a group user.

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_show_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersShowParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Displays information about a group user.

        Displays information about a group user.

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_update_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id} Adds a user to a group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def group_users_users_update_2_2(
        self,
        group_id: str,
        user_id: str,
        run_as: GroupUsersUsersUpdateParamRunAs | None = None,
    ) -> GroupUserResponse:
        """
        Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id} Adds a user to a group

        Args:
            group_id (str)           : The ID of the group.
            user_id (str)            : The ID of the user.
            run-as (Optional[GroupUsersUsersUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GroupUserResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/groups/{group_id}/users/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(GroupUserResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
