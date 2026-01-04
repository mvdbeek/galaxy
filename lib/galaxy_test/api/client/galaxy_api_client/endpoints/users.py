from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_220 import AnonymousArrayItem220
from ..models.anonymous_array_item_222 import AnonymousArrayItem222
from ..models.api_key_model_2 import ApiKeyModel2
from ..models.async_task_result_summary import AsyncTaskResultSummary
from ..models.create_source_credentials_payload import CreateSourceCredentialsPayload
from ..models.created_user_model import CreatedUserModel
from ..models.custom_build_creation_payload import CustomBuildCreationPayload
from ..models.custom_builds_collection import CustomBuildsCollection
from ..models.deleted_custom_build import DeletedCustomBuild
from ..models.detailed_user_model import DetailedUserModel
from ..models.favorite_object import FavoriteObject
from ..models.favorite_object_type import FavoriteObjectType
from ..models.favorite_objects_summary import FavoriteObjectsSummary
from ..models.role_list_response import RoleListResponse
from ..models.select_service_credential_payload import SelectServiceCredentialPayload
from ..models.service_credential_group_payload import ServiceCredentialGroupPayload
from ..models.service_credential_group_response import ServiceCredentialGroupResponse
from ..models.user_beacon_setting import UserBeaconSetting
from ..models.user_objectstore_usage import UserObjectstoreUsage
from ..models.user_quota_usage import UserQuotaUsage
from ..models.user_update_payload import UserUpdatePayload
from ..models.users_api_key_create_api_key_param_run_as import UsersApiKeyCreateApiKeyParamRunAs
from ..models.users_api_key_delete_api_key_param_run_as import UsersApiKeyDeleteApiKeyParamRunAs
from ..models.users_api_key_detailed_get_api_key_param_run_as import UsersApiKeyDetailedGetApiKeyParamRunAs
from ..models.users_api_key_get_or_create_api_key_param_run_as import UsersApiKeyGetOrCreateApiKeyParamRunAs
from ..models.users_beacon_get_beacon_param_run_as import UsersBeaconGetBeaconParamRunAs
from ..models.users_beacon_set_beacon_param_run_as import UsersBeaconSetBeaconParamRunAs
from ..models.users_create_param_run_as import UsersCreateParamRunAs
from ..models.users_create_request_body_2 import UsersCreateRequestBody2
from ..models.users_credentials_delete_service_credentials_param_run_as import (
    UsersCredentialsDeleteServiceCredentialsParamRunAs,
)
from ..models.users_credentials_delete_service_credentials_param_user_id import (
    UsersCredentialsDeleteServiceCredentialsParamUserId,
)
from ..models.users_credentials_groups_delete_credentials_param_run_as import (
    UsersCredentialsGroupsDeleteCredentialsParamRunAs,
)
from ..models.users_credentials_groups_delete_credentials_param_user_id import (
    UsersCredentialsGroupsDeleteCredentialsParamUserId,
)
from ..models.users_credentials_groups_update_user_credentials_param_run_as import (
    UsersCredentialsGroupsUpdateUserCredentialsParamRunAs,
)
from ..models.users_credentials_groups_update_user_credentials_param_user_id import (
    UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
)
from ..models.users_credentials_list_user_credentials_200_response_2 import (
    UsersCredentialsListUserCredentials200Response2,
)
from ..models.users_credentials_list_user_credentials_param_run_as import UsersCredentialsListUserCredentialsParamRunAs
from ..models.users_credentials_list_user_credentials_param_source_id import (
    UsersCredentialsListUserCredentialsParamSourceId,
)
from ..models.users_credentials_list_user_credentials_param_source_type import (
    UsersCredentialsListUserCredentialsParamSourceType,
)
from ..models.users_credentials_list_user_credentials_param_source_version import (
    UsersCredentialsListUserCredentialsParamSourceVersion,
)
from ..models.users_credentials_list_user_credentials_param_user_id import (
    UsersCredentialsListUserCredentialsParamUserId,
)
from ..models.users_credentials_provide_credential_param_run_as import UsersCredentialsProvideCredentialParamRunAs
from ..models.users_credentials_provide_credential_param_user_id import UsersCredentialsProvideCredentialParamUserId
from ..models.users_credentials_update_user_credentials_group_param_run_as import (
    UsersCredentialsUpdateUserCredentialsGroupParamRunAs,
)
from ..models.users_credentials_update_user_credentials_group_param_user_id import (
    UsersCredentialsUpdateUserCredentialsGroupParamUserId,
)
from ..models.users_current_recalculate_disk_usage_recalculate_disk_usage_param_run_as import (
    UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs,
)
from ..models.users_custom_builds_add_custom_builds_param_run_as import UsersCustomBuildsAddCustomBuildsParamRunAs
from ..models.users_custom_builds_delete_custom_builds_param_run_as import UsersCustomBuildsDeleteCustomBuildsParamRunAs
from ..models.users_custom_builds_get_custom_builds_param_run_as import UsersCustomBuildsGetCustomBuildsParamRunAs
from ..models.users_delete_param_run_as import UsersDeleteParamRunAs
from ..models.users_delete_request_body_2 import UsersDeleteRequestBody2
from ..models.users_deleted_index_deleted_param_f_any import UsersDeletedIndexDeletedParamFAny
from ..models.users_deleted_index_deleted_param_f_email import UsersDeletedIndexDeletedParamFEmail
from ..models.users_deleted_index_deleted_param_f_name import UsersDeletedIndexDeletedParamFName
from ..models.users_deleted_index_deleted_param_run_as import UsersDeletedIndexDeletedParamRunAs
from ..models.users_deleted_show_deleted_200_response_2 import UsersDeletedShowDeleted200Response2
from ..models.users_deleted_show_deleted_param_run_as import UsersDeletedShowDeletedParamRunAs
from ..models.users_deleted_undelete_undelete_param_run_as import UsersDeletedUndeleteUndeleteParamRunAs
from ..models.users_favorites_remove_favorite_param_run_as import UsersFavoritesRemoveFavoriteParamRunAs
from ..models.users_favorites_set_favorite_param_run_as import UsersFavoritesSetFavoriteParamRunAs
from ..models.users_index_param_f_any import UsersIndexParamFAny
from ..models.users_index_param_f_email import UsersIndexParamFEmail
from ..models.users_index_param_f_name import UsersIndexParamFName
from ..models.users_index_param_run_as import UsersIndexParamRunAs
from ..models.users_objectstore_usage_objectstore_usage_param_run_as import (
    UsersObjectstoreUsageObjectstoreUsageParamRunAs,
)
from ..models.users_objectstore_usage_objectstore_usage_param_user_id import (
    UsersObjectstoreUsageObjectstoreUsageParamUserId,
)
from ..models.users_recalculate_disk_usage_recalculate_disk_usage_by_user_id_param_run_as import (
    UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs,
)
from ..models.users_recalculate_disk_usage_recalculate_disk_usage_param_run_as import (
    UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs,
)
from ..models.users_roles_get_user_roles_param_run_as import UsersRolesGetUserRolesParamRunAs
from ..models.users_send_activation_email_send_activation_email_param_run_as import (
    UsersSendActivationEmailSendActivationEmailParamRunAs,
)
from ..models.users_show_200_response_2 import UsersShow200Response2
from ..models.users_show_param_deleted import UsersShowParamDeleted
from ..models.users_show_param_run_as import UsersShowParamRunAs
from ..models.users_show_param_user_id import UsersShowParamUserId
from ..models.users_theme_set_theme_param_run_as import UsersThemeSetThemeParamRunAs
from ..models.users_update_param_deleted import UsersUpdateParamDeleted
from ..models.users_update_param_run_as import UsersUpdateParamRunAs
from ..models.users_update_param_user_id import UsersUpdateParamUserId
from ..models.users_usage_usage_for_200_response_2 import UsersUsageUsageFor200Response2
from ..models.users_usage_usage_for_param_run_as import UsersUsageUsageForParamRunAs
from ..models.users_usage_usage_for_param_user_id import UsersUsageUsageForParamUserId
from ..models.users_usage_usage_param_run_as import UsersUsageUsageParamRunAs
from ..models.users_usage_usage_param_user_id import UsersUsageUsageParamUserId


class UsersClient:
    """Client for users endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def users_index_2_2(
        self,
        deleted: bool | None = False,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem220]:
        """
        Get Users

        Return a collection of users. Filters will only work if enabled in config or user is
        admin.

        Args:
            deleted (Optional[bool]) : Indicates if the collection will be about deleted users
            f_email (Optional[UsersIndexParamFEmail])
                                     : An email address to filter on
            f_name (Optional[UsersIndexParamFName])
                                     : An username address to filter on
            f_any (Optional[UsersIndexParamFAny])
                                     : Filter on username OR email
            run-as (Optional[UsersIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem220]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
            **({"f_email": f_email} if f_email is not None else {}),
            **({"f_name": f_name} if f_name is not None else {}),
            **({"f_any": f_any} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem220], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_index_2_2(
        self,
        deleted: bool | None = False,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem220]:
        """
        Get Users

        Return a collection of users. Filters will only work if enabled in config or user is
        admin.

        Args:
            deleted (Optional[bool]) : Indicates if the collection will be about deleted users
            f_email (Optional[UsersIndexParamFEmail])
                                     : An email address to filter on
            f_name (Optional[UsersIndexParamFName])
                                     : An username address to filter on
            f_any (Optional[UsersIndexParamFAny])
                                     : Filter on username OR email
            run-as (Optional[UsersIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem220]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
            **({"f_email": f_email} if f_email is not None else {}),
            **({"f_name": f_name} if f_name is not None else {}),
            **({"f_any": f_any} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem220], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_create_2_2(
        self,
        body: UsersCreateRequestBody2,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel:
        """
        Create a new Galaxy user. Only admins can create users for now.

        Args:
            run-as (Optional[UsersCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersCreateRequestBody2)
                                     : Request body. (json)

        Returns:
            CreatedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UsersCreateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreatedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_create_2_2(
        self,
        body: UsersCreateRequestBody2,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel:
        """
        Create a new Galaxy user. Only admins can create users for now.

        Args:
            run-as (Optional[UsersCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersCreateRequestBody2)
                                     : Request body. (json)

        Returns:
            CreatedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UsersCreateRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreatedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_current_recalculate_disk_usage_recalculate_disk_usage_2_2(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (Optional[UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/current/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_current_recalculate_disk_usage_recalculate_disk_usage_2_2(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (Optional[UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/current/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_index_deleted_2_2(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem222]:
        """
        Get Deleted Users

        Return a collection of deleted users. Only admins can see deleted users.

        Args:
            f_email (Optional[UsersDeletedIndexDeletedParamFEmail])
                                     : An email address to filter on
            f_name (Optional[UsersDeletedIndexDeletedParamFName])
                                     : An username address to filter on
            f_any (Optional[UsersDeletedIndexDeletedParamFAny])
                                     : Filter on username OR email
            run-as (Optional[UsersDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem222]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted"

        params: dict[str, Any] = {
            **({"f_email": f_email} if f_email is not None else {}),
            **({"f_name": f_name} if f_name is not None else {}),
            **({"f_any": f_any} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem222], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_index_deleted_2_2(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem222]:
        """
        Get Deleted Users

        Return a collection of deleted users. Only admins can see deleted users.

        Args:
            f_email (Optional[UsersDeletedIndexDeletedParamFEmail])
                                     : An email address to filter on
            f_name (Optional[UsersDeletedIndexDeletedParamFName])
                                     : An username address to filter on
            f_any (Optional[UsersDeletedIndexDeletedParamFAny])
                                     : Filter on username OR email
            run-as (Optional[UsersDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem222]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted"

        params: dict[str, Any] = {
            **({"f_email": f_email} if f_email is not None else {}),
            **({"f_name": f_name} if f_name is not None else {}),
            **({"f_any": f_any} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem222], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_show_deleted_2_2(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response2:
        """
        Return information about a deleted user. Only admins can see deleted users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersDeletedShowDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersDeletedShowDeleted200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersDeletedShowDeleted200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_show_deleted_2_2(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response2:
        """
        Return information about a deleted user. Only admins can see deleted users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersDeletedShowDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersDeletedShowDeleted200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersDeletedShowDeleted200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_undelete_undelete_2_2(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Restore a deleted user. Only admins can restore users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted/{user_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_deleted_undelete_undelete_2_2(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Restore a deleted user. Only admins can restore users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted/{user_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_2_2(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (Optional[UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_2_2(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (Optional[UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_delete_2_2(
        self,
        user_id: str,
        purge: bool | None = False,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody2 | None = None,
    ) -> DetailedUserModel:
        """
        Delete a user. Only admins can delete others or purge users.

        Args:
            user_id (str)            : The ID of the user.
            purge (Optional[bool])   : Whether to definitely remove this user. Only deleted
                                       users can be purged.
            run-as (Optional[UsersDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[UsersDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UsersDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_delete_2_2(
        self,
        user_id: str,
        purge: bool | None = False,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody2 | None = None,
    ) -> DetailedUserModel:
        """
        Delete a user. Only admins can delete others or purge users.

        Args:
            user_id (str)            : The ID of the user.
            purge (Optional[bool])   : Whether to definitely remove this user. Only deleted
                                       users can be purged.
            run-as (Optional[UsersDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[UsersDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UsersDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_show_2_2(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response2:
        """
        Return information about a specified or the current user. Only admin can see deleted or
        other users

        Args:
            user_id (UsersShowParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (Optional[UsersShowParamDeleted])
                                     : Indicates if the user is deleted
            run-as (Optional[UsersShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_show_2_2(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response2:
        """
        Return information about a specified or the current user. Only admin can see deleted or
        other users

        Args:
            user_id (UsersShowParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (Optional[UsersShowParamDeleted])
                                     : Indicates if the user is deleted
            run-as (Optional[UsersShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_update_2_2(
        self,
        user_id: UsersUpdateParamUserId,
        body: UserUpdatePayload,
        deleted: UsersUpdateParamDeleted | None = None,
        run_as: UsersUpdateParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Update the values of a user. Only admin can update others.

        Args:
            user_id (UsersUpdateParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (Optional[UsersUpdateParamDeleted])
                                     : Indicates if the user is deleted
            run-as (Optional[UsersUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserUpdatePayload) : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UserUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_update_2_2(
        self,
        user_id: UsersUpdateParamUserId,
        body: UserUpdatePayload,
        deleted: UsersUpdateParamDeleted | None = None,
        run_as: UsersUpdateParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Update the values of a user. Only admin can update others.

        Args:
            user_id (UsersUpdateParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (Optional[UsersUpdateParamDeleted])
                                     : Indicates if the user is deleted
            run-as (Optional[UsersUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserUpdatePayload) : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UserUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DetailedUserModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_delete_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None:
        """
        Delete the current API key of the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyDeleteApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_delete_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None:
        """
        Delete the current API key of the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyDeleteApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_get_or_create_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Return the user's API key

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyGetOrCreateApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_get_or_create_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Return the user's API key

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyGetOrCreateApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_create_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Create a new API key for the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyCreateApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_create_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Create a new API key for the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyCreateApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_detailed_get_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2:
        """
        Return the user's API key with extra information.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyDetailedGetApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ApiKeyModel2: The API key of the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key/detailed"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ApiKeyModel2, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_api_key_detailed_get_api_key_2_2(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2:
        """
        Return the user's API key with extra information.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersApiKeyDetailedGetApiKeyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ApiKeyModel2: The API key of the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/api_key/detailed"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ApiKeyModel2, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_beacon_get_beacon_2_2(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Return information about beacon share settings

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersBeaconGetBeaconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserBeaconSetting, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_beacon_get_beacon_2_2(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Return information about beacon share settings

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersBeaconGetBeaconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserBeaconSetting, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_beacon_set_beacon_2_2(
        self,
        user_id: str,
        body: UserBeaconSetting,
        run_as: UsersBeaconSetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Change beacon setting

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersBeaconSetBeaconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserBeaconSetting) : Request body. (json)

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UserBeaconSetting = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserBeaconSetting, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_beacon_set_beacon_2_2(
        self,
        user_id: str,
        body: UserBeaconSetting,
        run_as: UsersBeaconSetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Change beacon setting

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersBeaconSetBeaconParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserBeaconSetting) : Request body. (json)

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UserBeaconSetting = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UserBeaconSetting, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_list_user_credentials_2_2(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = False,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response2:
        """
        Lists all credentials the user has provided

        Args:
            user_id (UsersCredentialsListUserCredentialsParamUserId)
                                     :
            source_type (Optional[UsersCredentialsListUserCredentialsParamSourceType])
                                     : The type of source to filter by.
            source_id (Optional[UsersCredentialsListUserCredentialsParamSourceId])
                                     : The ID of the source to filter by.
            source_version (Optional[UsersCredentialsListUserCredentialsParamSourceVersion])
                                     : The version of the source to filter by. By default it is
                                       the latest version.
            include_definition (Optional[bool])
                                     : Whether to include extended credential definition
                                       information.
            run-as (Optional[UsersCredentialsListUserCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersCredentialsListUserCredentials200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        params: dict[str, Any] = {
            **({"source_type": source_type} if source_type is not None else {}),
            **({"source_id": source_id} if source_id is not None else {}),
            **({"source_version": source_version} if source_version is not None else {}),
            **({"include_definition": include_definition} if include_definition is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersCredentialsListUserCredentials200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_list_user_credentials_2_2(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = False,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response2:
        """
        Lists all credentials the user has provided

        Args:
            user_id (UsersCredentialsListUserCredentialsParamUserId)
                                     :
            source_type (Optional[UsersCredentialsListUserCredentialsParamSourceType])
                                     : The type of source to filter by.
            source_id (Optional[UsersCredentialsListUserCredentialsParamSourceId])
                                     : The ID of the source to filter by.
            source_version (Optional[UsersCredentialsListUserCredentialsParamSourceVersion])
                                     : The version of the source to filter by. By default it is
                                       the latest version.
            include_definition (Optional[bool])
                                     : Whether to include extended credential definition
                                       information.
            run-as (Optional[UsersCredentialsListUserCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersCredentialsListUserCredentials200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        params: dict[str, Any] = {
            **({"source_type": source_type} if source_type is not None else {}),
            **({"source_id": source_id} if source_id is not None else {}),
            **({"source_version": source_version} if source_version is not None else {}),
            **({"include_definition": include_definition} if include_definition is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersCredentialsListUserCredentials200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_provide_credential_2_2(
        self,
        user_id: UsersCredentialsProvideCredentialParamUserId,
        body: CreateSourceCredentialsPayload,
        run_as: UsersCredentialsProvideCredentialParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Allows users to provide credentials for a secret/variable

        Args:
            user_id (UsersCredentialsProvideCredentialParamUserId)
                                     :
            run-as (Optional[UsersCredentialsProvideCredentialParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateSourceCredentialsPayload)
                                     : Request body. (json)

        Returns:
            ServiceCredentialGroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateSourceCredentialsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ServiceCredentialGroupResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_provide_credential_2_2(
        self,
        user_id: UsersCredentialsProvideCredentialParamUserId,
        body: CreateSourceCredentialsPayload,
        run_as: UsersCredentialsProvideCredentialParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Allows users to provide credentials for a secret/variable

        Args:
            user_id (UsersCredentialsProvideCredentialParamUserId)
                                     :
            run-as (Optional[UsersCredentialsProvideCredentialParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateSourceCredentialsPayload)
                                     : Request body. (json)

        Returns:
            ServiceCredentialGroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateSourceCredentialsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ServiceCredentialGroupResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_update_user_credentials_group_2_2(
        self,
        user_id: UsersCredentialsUpdateUserCredentialsGroupParamUserId,
        body: SelectServiceCredentialPayload,
        run_as: UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None = None,
    ) -> None:
        """
        Updates the current credentials group

        Args:
            user_id (UsersCredentialsUpdateUserCredentialsGroupParamUserId)
                                     :
            run-as (Optional[UsersCredentialsUpdateUserCredentialsGroupParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SelectServiceCredentialPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SelectServiceCredentialPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_update_user_credentials_group_2_2(
        self,
        user_id: UsersCredentialsUpdateUserCredentialsGroupParamUserId,
        body: SelectServiceCredentialPayload,
        run_as: UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None = None,
    ) -> None:
        """
        Updates the current credentials group

        Args:
            user_id (UsersCredentialsUpdateUserCredentialsGroupParamUserId)
                                     :
            run-as (Optional[UsersCredentialsUpdateUserCredentialsGroupParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SelectServiceCredentialPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SelectServiceCredentialPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_delete_service_credentials_2_2(
        self,
        user_id: UsersCredentialsDeleteServiceCredentialsParamUserId,
        user_credentials_id: str,
        run_as: UsersCredentialsDeleteServiceCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Deletes all credentials for a specific service

        Args:
            user_id (UsersCredentialsDeleteServiceCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            run-as (Optional[UsersCredentialsDeleteServiceCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_delete_service_credentials_2_2(
        self,
        user_id: UsersCredentialsDeleteServiceCredentialsParamUserId,
        user_credentials_id: str,
        run_as: UsersCredentialsDeleteServiceCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Deletes all credentials for a specific service

        Args:
            user_id (UsersCredentialsDeleteServiceCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            run-as (Optional[UsersCredentialsDeleteServiceCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_groups_delete_credentials_2_2(
        self,
        user_id: UsersCredentialsGroupsDeleteCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        run_as: UsersCredentialsGroupsDeleteCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Deletes a specific credential group

        Args:
            user_id (UsersCredentialsGroupsDeleteCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            group_id (str)           :
            run-as (Optional[UsersCredentialsGroupsDeleteCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_groups_delete_credentials_2_2(
        self,
        user_id: UsersCredentialsGroupsDeleteCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        run_as: UsersCredentialsGroupsDeleteCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Deletes a specific credential group

        Args:
            user_id (UsersCredentialsGroupsDeleteCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            group_id (str)           :
            run-as (Optional[UsersCredentialsGroupsDeleteCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_groups_update_user_credentials_2_2(
        self,
        user_id: UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        body: ServiceCredentialGroupPayload,
        run_as: UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Updates user credentials

        Args:
            user_id (UsersCredentialsGroupsUpdateUserCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            group_id (str)           :
            run-as (Optional[UsersCredentialsGroupsUpdateUserCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ServiceCredentialGroupPayload)
                                     : Request body. (json)

        Returns:
            ServiceCredentialGroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ServiceCredentialGroupPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ServiceCredentialGroupResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_credentials_groups_update_user_credentials_2_2(
        self,
        user_id: UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        body: ServiceCredentialGroupPayload,
        run_as: UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Updates user credentials

        Args:
            user_id (UsersCredentialsGroupsUpdateUserCredentialsParamUserId)
                                     :
            user_credentials_id (str):
            group_id (str)           :
            run-as (Optional[UsersCredentialsGroupsUpdateUserCredentialsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ServiceCredentialGroupPayload)
                                     : Request body. (json)

        Returns:
            ServiceCredentialGroupResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ServiceCredentialGroupPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ServiceCredentialGroupResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_get_custom_builds_2_2(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection:
        """
         Returns collection of custom builds.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersCustomBuildsGetCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CustomBuildsCollection, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_get_custom_builds_2_2(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection:
        """
         Returns collection of custom builds.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersCustomBuildsGetCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CustomBuildsCollection, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_delete_custom_builds_2_2(
        self,
        user_id: str,
        key: str,
        run_as: UsersCustomBuildsDeleteCustomBuildsParamRunAs | None = None,
    ) -> DeletedCustomBuild:
        """
        Delete a custom build

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (Optional[UsersCustomBuildsDeleteCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DeletedCustomBuild: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DeletedCustomBuild, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_delete_custom_builds_2_2(
        self,
        user_id: str,
        key: str,
        run_as: UsersCustomBuildsDeleteCustomBuildsParamRunAs | None = None,
    ) -> DeletedCustomBuild:
        """
        Delete a custom build

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (Optional[UsersCustomBuildsDeleteCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DeletedCustomBuild: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DeletedCustomBuild, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_add_custom_builds_2_2(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> Any:
        """
        Add new custom build.

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (Optional[UsersCustomBuildsAddCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CustomBuildCreationPayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CustomBuildCreationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_custom_builds_add_custom_builds_2_2(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> Any:
        """
        Add new custom build.

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (Optional[UsersCustomBuildsAddCustomBuildsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CustomBuildCreationPayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CustomBuildCreationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_favorites_set_favorite_2_2(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        body: FavoriteObject,
        run_as: UsersFavoritesSetFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Add the object to user's favorites

        Args:
            user_id (str)            : The ID of the user.
            object_type (FavoriteObjectType)
                                     : The object type the user wants to favorite
            run-as (Optional[UsersFavoritesSetFavoriteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FavoriteObject)    : Request body. (json)

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FavoriteObject = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FavoriteObjectsSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_favorites_set_favorite_2_2(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        body: FavoriteObject,
        run_as: UsersFavoritesSetFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Add the object to user's favorites

        Args:
            user_id (str)            : The ID of the user.
            object_type (FavoriteObjectType)
                                     : The object type the user wants to favorite
            run-as (Optional[UsersFavoritesSetFavoriteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (FavoriteObject)    : Request body. (json)

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: FavoriteObject = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FavoriteObjectsSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_favorites_remove_favorite_2_2(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        object_id: str,
        run_as: UsersFavoritesRemoveFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Remove the object from user's favorites

        Args:
            user_id (str)            : The ID of the user.
            object_type (FavoriteObjectType)
                                     : The object type the user wants to favorite
            object_id (str)          : The ID of an object the user wants to remove from
                                       favorites
            run-as (Optional[UsersFavoritesRemoveFavoriteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FavoriteObjectsSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_favorites_remove_favorite_2_2(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        object_id: str,
        run_as: UsersFavoritesRemoveFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Remove the object from user's favorites

        Args:
            user_id (str)            : The ID of the user.
            object_type (FavoriteObjectType)
                                     : The object type the user wants to favorite
            object_id (str)          : The ID of an object the user wants to remove from
                                       favorites
            run-as (Optional[UsersFavoritesRemoveFavoriteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(FavoriteObjectsSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_objectstore_usage_objectstore_usage_2_2(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]:
        """
        Return the user's object store usage summary broken down by object store ID

        Args:
            user_id (UsersObjectstoreUsageObjectstoreUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (Optional[UsersObjectstoreUsageObjectstoreUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserObjectstoreUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/objectstore_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserObjectstoreUsage], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_objectstore_usage_objectstore_usage_2_2(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]:
        """
        Return the user's object store usage summary broken down by object store ID

        Args:
            user_id (UsersObjectstoreUsageObjectstoreUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (Optional[UsersObjectstoreUsageObjectstoreUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserObjectstoreUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/objectstore_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserObjectstoreUsage], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id_2_2(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id_2_2(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_roles_get_user_roles_2_2(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Get User Roles

        Return a list of roles associated with this user. Only admins can see user roles.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersRolesGetUserRolesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RoleListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_roles_get_user_roles_2_2(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Get User Roles

        Return a list of roles associated with this user. Only admins can see user roles.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersRolesGetUserRolesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RoleListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_send_activation_email_send_activation_email_2_2(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> Any:
        """
        Sends activation email to user.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersSendActivationEmailSendActivationEmailParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/send_activation_email"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_send_activation_email_send_activation_email_2_2(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> Any:
        """
        Sends activation email to user.

        Args:
            user_id (str)            : The ID of the user.
            run-as (Optional[UsersSendActivationEmailSendActivationEmailParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/send_activation_email"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_theme_set_theme_2_2(
        self,
        user_id: str,
        theme: str,
        run_as: UsersThemeSetThemeParamRunAs | None = None,
    ) -> str:
        """
        Set the user's theme choice

        Args:
            user_id (str)            : The ID of the user.
            theme (str)              : The theme of the GUI
            run-as (Optional[UsersThemeSetThemeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/theme/{theme}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_theme_set_theme_2_2(
        self,
        user_id: str,
        theme: str,
        run_as: UsersThemeSetThemeParamRunAs | None = None,
    ) -> str:
        """
        Set the user's theme choice

        Args:
            user_id (str)            : The ID of the user.
            theme (str)              : The theme of the GUI
            run-as (Optional[UsersThemeSetThemeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/theme/{theme}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_usage_usage_2_2(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]:
        """
        Return the user's quota usage summary broken down by quota source

        Args:
            user_id (UsersUsageUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (Optional[UsersUsageUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserQuotaUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserQuotaUsage], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_usage_usage_2_2(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]:
        """
        Return the user's quota usage summary broken down by quota source

        Args:
            user_id (UsersUsageUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (Optional[UsersUsageUsageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserQuotaUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[UserQuotaUsage], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_usage_usage_for_2_2(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response2:
        """
        Return the user's quota usage summary for a given quota source label

        Args:
            user_id (UsersUsageUsageForParamUserId)
                                     : The ID of the user to get or 'current'.
            label (str)              : The label corresponding to the quota source to fetch
                                       usage information about.
            run-as (Optional[UsersUsageUsageForParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersUsageUsageFor200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/usage/{label}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersUsageUsageFor200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def users_usage_usage_for_2_2(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response2:
        """
        Return the user's quota usage summary for a given quota source label

        Args:
            user_id (UsersUsageUsageForParamUserId)
                                     : The ID of the user to get or 'current'.
            label (str)              : The label corresponding to the quota source to fetch
                                       usage information about.
            run-as (Optional[UsersUsageUsageForParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersUsageUsageFor200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/{user_id}/usage/{label}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(UsersUsageUsageFor200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
