from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_125 import AnonymousArrayItem125
from ..models.anonymous_array_item_127 import AnonymousArrayItem127
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
from ..models.users_create_request_body import UsersCreateRequestBody
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
from ..models.users_credentials_list_user_credentials_200_response import UsersCredentialsListUserCredentials200Response
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
from ..models.users_delete_request_body import UsersDeleteRequestBody
from ..models.users_deleted_index_deleted_param_f_any import UsersDeletedIndexDeletedParamFAny
from ..models.users_deleted_index_deleted_param_f_email import UsersDeletedIndexDeletedParamFEmail
from ..models.users_deleted_index_deleted_param_f_name import UsersDeletedIndexDeletedParamFName
from ..models.users_deleted_index_deleted_param_run_as import UsersDeletedIndexDeletedParamRunAs
from ..models.users_deleted_show_deleted_200_response import UsersDeletedShowDeleted200Response
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
from ..models.users_show_200_response import UsersShow200Response
from ..models.users_show_param_deleted import UsersShowParamDeleted
from ..models.users_show_param_run_as import UsersShowParamRunAs
from ..models.users_show_param_user_id import UsersShowParamUserId
from ..models.users_theme_set_theme_param_run_as import UsersThemeSetThemeParamRunAs
from ..models.users_update_param_deleted import UsersUpdateParamDeleted
from ..models.users_update_param_run_as import UsersUpdateParamRunAs
from ..models.users_update_param_user_id import UsersUpdateParamUserId
from ..models.users_usage_usage_for_200_response import UsersUsageUsageFor200Response
from ..models.users_usage_usage_for_param_run_as import UsersUsageUsageForParamRunAs
from ..models.users_usage_usage_for_param_user_id import UsersUsageUsageForParamUserId
from ..models.users_usage_usage_param_run_as import UsersUsageUsageParamRunAs
from ..models.users_usage_usage_param_user_id import UsersUsageUsageParamUserId


@runtime_checkable
class UsersClientProtocol(Protocol):
    """Protocol defining the interface of UsersClient for dependency injection."""

    async def users_index(
        self,
        deleted: bool | None = None,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]: ...

    async def users_index(
        self,
        deleted: bool | None = None,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]: ...

    async def users_create(
        self,
        body: UsersCreateRequestBody,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel: ...

    async def users_create(
        self,
        body: UsersCreateRequestBody,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel: ...

    async def users_current_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_current_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_deleted_index_deleted(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]: ...

    async def users_deleted_index_deleted(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]: ...

    async def users_deleted_show_deleted(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response: ...

    async def users_deleted_show_deleted(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response: ...

    async def users_deleted_undelete_undelete(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel: ...

    async def users_deleted_undelete_undelete(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel: ...

    async def users_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_delete(
        self,
        user_id: str,
        purge: bool | None = None,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody | None = None,
    ) -> DetailedUserModel: ...

    async def users_delete(
        self,
        user_id: str,
        purge: bool | None = None,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody | None = None,
    ) -> DetailedUserModel: ...

    async def users_show(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response: ...

    async def users_show(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response: ...

    async def users_update(
        self,
        user_id: UsersUpdateParamUserId,
        body: UserUpdatePayload,
        deleted: UsersUpdateParamDeleted | None = None,
        run_as: UsersUpdateParamRunAs | None = None,
    ) -> DetailedUserModel: ...

    async def users_update(
        self,
        user_id: UsersUpdateParamUserId,
        body: UserUpdatePayload,
        deleted: UsersUpdateParamDeleted | None = None,
        run_as: UsersUpdateParamRunAs | None = None,
    ) -> DetailedUserModel: ...

    async def users_api_key_delete_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None: ...

    async def users_api_key_delete_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None: ...

    async def users_api_key_get_or_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str: ...

    async def users_api_key_get_or_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str: ...

    async def users_api_key_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str: ...

    async def users_api_key_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str: ...

    async def users_api_key_detailed_get_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2: ...

    async def users_api_key_detailed_get_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2: ...

    async def users_beacon_get_beacon(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting: ...

    async def users_beacon_get_beacon(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting: ...

    async def users_beacon_set_beacon(
        self,
        user_id: str,
        body: UserBeaconSetting,
        run_as: UsersBeaconSetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting: ...

    async def users_beacon_set_beacon(
        self,
        user_id: str,
        body: UserBeaconSetting,
        run_as: UsersBeaconSetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting: ...

    async def users_credentials_list_user_credentials(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = None,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response: ...

    async def users_credentials_list_user_credentials(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = None,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response: ...

    async def users_credentials_provide_credential(
        self,
        user_id: UsersCredentialsProvideCredentialParamUserId,
        body: CreateSourceCredentialsPayload,
        run_as: UsersCredentialsProvideCredentialParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse: ...

    async def users_credentials_provide_credential(
        self,
        user_id: UsersCredentialsProvideCredentialParamUserId,
        body: CreateSourceCredentialsPayload,
        run_as: UsersCredentialsProvideCredentialParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse: ...

    async def users_credentials_update_user_credentials_group(
        self,
        user_id: UsersCredentialsUpdateUserCredentialsGroupParamUserId,
        body: SelectServiceCredentialPayload,
        run_as: UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_update_user_credentials_group(
        self,
        user_id: UsersCredentialsUpdateUserCredentialsGroupParamUserId,
        body: SelectServiceCredentialPayload,
        run_as: UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_delete_service_credentials(
        self,
        user_id: UsersCredentialsDeleteServiceCredentialsParamUserId,
        user_credentials_id: str,
        run_as: UsersCredentialsDeleteServiceCredentialsParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_delete_service_credentials(
        self,
        user_id: UsersCredentialsDeleteServiceCredentialsParamUserId,
        user_credentials_id: str,
        run_as: UsersCredentialsDeleteServiceCredentialsParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_groups_delete_credentials(
        self,
        user_id: UsersCredentialsGroupsDeleteCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        run_as: UsersCredentialsGroupsDeleteCredentialsParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_groups_delete_credentials(
        self,
        user_id: UsersCredentialsGroupsDeleteCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        run_as: UsersCredentialsGroupsDeleteCredentialsParamRunAs | None = None,
    ) -> None: ...

    async def users_credentials_groups_update_user_credentials(
        self,
        user_id: UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        body: ServiceCredentialGroupPayload,
        run_as: UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse: ...

    async def users_credentials_groups_update_user_credentials(
        self,
        user_id: UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        body: ServiceCredentialGroupPayload,
        run_as: UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse: ...

    async def users_custom_builds_get_custom_builds(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection: ...

    async def users_custom_builds_get_custom_builds(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection: ...

    async def users_custom_builds_delete_custom_builds(
        self,
        user_id: str,
        key: str,
        run_as: UsersCustomBuildsDeleteCustomBuildsParamRunAs | None = None,
    ) -> DeletedCustomBuild: ...

    async def users_custom_builds_delete_custom_builds(
        self,
        user_id: str,
        key: str,
        run_as: UsersCustomBuildsDeleteCustomBuildsParamRunAs | None = None,
    ) -> DeletedCustomBuild: ...

    async def users_custom_builds_add_custom_builds(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def users_custom_builds_add_custom_builds(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def users_favorites_set_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        body: FavoriteObject,
        run_as: UsersFavoritesSetFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary: ...

    async def users_favorites_set_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        body: FavoriteObject,
        run_as: UsersFavoritesSetFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary: ...

    async def users_favorites_remove_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        object_id: str,
        run_as: UsersFavoritesRemoveFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary: ...

    async def users_favorites_remove_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        object_id: str,
        run_as: UsersFavoritesRemoveFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary: ...

    async def users_objectstore_usage_objectstore_usage(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]: ...

    async def users_objectstore_usage_objectstore_usage(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]: ...

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def users_roles_get_user_roles(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse: ...

    async def users_roles_get_user_roles(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse: ...

    async def users_send_activation_email_send_activation_email(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def users_send_activation_email_send_activation_email(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def users_theme_set_theme(
        self,
        user_id: str,
        theme: str,
        run_as: UsersThemeSetThemeParamRunAs | None = None,
    ) -> str: ...

    async def users_theme_set_theme(
        self,
        user_id: str,
        theme: str,
        run_as: UsersThemeSetThemeParamRunAs | None = None,
    ) -> str: ...

    async def users_usage_usage(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]: ...

    async def users_usage_usage(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]: ...

    async def users_usage_usage_for(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response | None: ...

    async def users_usage_usage_for(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response | None: ...


class UsersClient(UsersClientProtocol):
    """Client for users endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def users_index(
        self,
        deleted: bool | None = None,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]:
        """
        Get Users

        Return a collection of users. Filters will only work if enabled in config or user is
        admin.

        Args:
            deleted (bool | None)    : Indicates if the collection will be about deleted users
            f_email (UsersIndexParamFEmail | None)
                                     : An email address to filter on
            f_name (UsersIndexParamFName | None)
                                     : An username address to filter on
            f_any (UsersIndexParamFAny | None)
                                     : Filter on username OR email
            run-as (UsersIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem125]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"f_email": DataclassSerializer.serialize(f_email)} if f_email is not None else {}),
            **({"f_name": DataclassSerializer.serialize(f_name)} if f_name is not None else {}),
            **({"f_any": DataclassSerializer.serialize(f_any)} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem125])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_index(
        self,
        deleted: bool | None = None,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]:
        """
        Get Users

        Return a collection of users. Filters will only work if enabled in config or user is
        admin.

        Args:
            deleted (bool | None)    : Indicates if the collection will be about deleted users
            f_email (UsersIndexParamFEmail | None)
                                     : An email address to filter on
            f_name (UsersIndexParamFName | None)
                                     : An username address to filter on
            f_any (UsersIndexParamFAny | None)
                                     : Filter on username OR email
            run-as (UsersIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem125]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
            **({"f_email": DataclassSerializer.serialize(f_email)} if f_email is not None else {}),
            **({"f_name": DataclassSerializer.serialize(f_name)} if f_name is not None else {}),
            **({"f_any": DataclassSerializer.serialize(f_any)} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem125])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_create(
        self,
        body: UsersCreateRequestBody,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel:
        """
        Create a new Galaxy user. Only admins can create users for now.

        Args:
            run-as (UsersCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersCreateRequestBody)
                                     : Request body. (json)

        Returns:
            CreatedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UsersCreateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CreatedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_create(
        self,
        body: UsersCreateRequestBody,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel:
        """
        Create a new Galaxy user. Only admins can create users for now.

        Args:
            run-as (UsersCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersCreateRequestBody)
                                     : Request body. (json)

        Returns:
            CreatedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UsersCreateRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CreatedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_current_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None)
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
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_current_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None)
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
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_index_deleted(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]:
        """
        Get Deleted Users

        Return a collection of deleted users. Only admins can see deleted users.

        Args:
            f_email (UsersDeletedIndexDeletedParamFEmail | None)
                                     : An email address to filter on
            f_name (UsersDeletedIndexDeletedParamFName | None)
                                     : An username address to filter on
            f_any (UsersDeletedIndexDeletedParamFAny | None)
                                     : Filter on username OR email
            run-as (UsersDeletedIndexDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem127]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted"

        params: dict[str, Any] = {
            **({"f_email": DataclassSerializer.serialize(f_email)} if f_email is not None else {}),
            **({"f_name": DataclassSerializer.serialize(f_name)} if f_name is not None else {}),
            **({"f_any": DataclassSerializer.serialize(f_any)} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem127])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_index_deleted(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]:
        """
        Get Deleted Users

        Return a collection of deleted users. Only admins can see deleted users.

        Args:
            f_email (UsersDeletedIndexDeletedParamFEmail | None)
                                     : An email address to filter on
            f_name (UsersDeletedIndexDeletedParamFName | None)
                                     : An username address to filter on
            f_any (UsersDeletedIndexDeletedParamFAny | None)
                                     : Filter on username OR email
            run-as (UsersDeletedIndexDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem127]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/users/deleted"

        params: dict[str, Any] = {
            **({"f_email": DataclassSerializer.serialize(f_email)} if f_email is not None else {}),
            **({"f_name": DataclassSerializer.serialize(f_name)} if f_name is not None else {}),
            **({"f_any": DataclassSerializer.serialize(f_any)} if f_any is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem127])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_show_deleted(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response:
        """
        Return information about a deleted user. Only admins can see deleted users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersDeletedShowDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersDeletedShowDeleted200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/deleted/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersDeletedShowDeleted200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_show_deleted(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response:
        """
        Return information about a deleted user. Only admins can see deleted users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersDeletedShowDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersDeletedShowDeleted200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/deleted/{user_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersDeletedShowDeleted200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_undelete_undelete(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Restore a deleted user. Only admins can restore users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersDeletedUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/deleted/{user_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_deleted_undelete_undelete(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Restore a deleted user. Only admins can restore users.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersDeletedUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/deleted/{user_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None)
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
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.  Please use
        `/api/users/current/recalculate_disk_usage` instead.

        Args:
            run-as (UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None)
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
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_delete(
        self,
        user_id: str,
        purge: bool | None = None,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody | None = None,
    ) -> DetailedUserModel:
        """
        Delete a user. Only admins can delete others or purge users.

        Args:
            user_id (str)            : The ID of the user.
            purge (bool | None)      : Whether to definitely remove this user. Only deleted
                                       users can be purged.
            run-as (UsersDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"purge": DataclassSerializer.serialize(purge)} if purge is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UsersDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_delete(
        self,
        user_id: str,
        purge: bool | None = None,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody | None = None,
    ) -> DetailedUserModel:
        """
        Delete a user. Only admins can delete others or purge users.

        Args:
            user_id (str)            : The ID of the user.
            purge (bool | None)      : Whether to definitely remove this user. Only deleted
                                       users can be purged.
            run-as (UsersDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UsersDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            DetailedUserModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"purge": DataclassSerializer.serialize(purge)} if purge is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UsersDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_show(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response:
        """
        Return information about a specified or the current user. Only admin can see deleted or
        other users

        Args:
            user_id (UsersShowParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (UsersShowParamDeleted | None)
                                     : Indicates if the user is deleted
            run-as (UsersShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_show(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response:
        """
        Return information about a specified or the current user. Only admin can see deleted or
        other users

        Args:
            user_id (UsersShowParamUserId)
                                     : The ID of the user to get or 'current'.
            deleted (UsersShowParamDeleted | None)
                                     : Indicates if the user is deleted
            run-as (UsersShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_update(
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
            deleted (UsersUpdateParamDeleted | None)
                                     : Indicates if the user is deleted
            run-as (UsersUpdateParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_update(
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
            deleted (UsersUpdateParamDeleted | None)
                                     : Indicates if the user is deleted
            run-as (UsersUpdateParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DetailedUserModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_delete_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None:
        """
        Delete the current API key of the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyDeleteApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_delete_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None:
        """
        Delete the current API key of the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyDeleteApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_get_or_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Return the user's API key

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyGetOrCreateApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_get_or_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Return the user's API key

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyGetOrCreateApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Create a new API key for the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyCreateApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Create a new API key for the user

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyCreateApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_detailed_get_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2:
        """
        Return the user's API key with extra information.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyDetailedGetApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ApiKeyModel2: The API key of the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key/detailed"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ApiKeyModel2)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_api_key_detailed_get_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2:
        """
        Return the user's API key with extra information.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersApiKeyDetailedGetApiKeyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ApiKeyModel2: The API key of the user.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/api_key/detailed"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ApiKeyModel2)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_beacon_get_beacon(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Return information about beacon share settings

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersBeaconGetBeaconParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserBeaconSetting)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_beacon_get_beacon(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Return information about beacon share settings

        **Warning**: This API is unstable and may change without notice.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersBeaconGetBeaconParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserBeaconSetting: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserBeaconSetting)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_beacon_set_beacon(
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
            run-as (UsersBeaconSetBeaconParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserBeaconSetting = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserBeaconSetting)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_beacon_set_beacon(
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
            run-as (UsersBeaconSetBeaconParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/beacon"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserBeaconSetting = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserBeaconSetting)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_list_user_credentials(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = None,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response:
        """
        Lists all credentials the user has provided

        Args:
            user_id (UsersCredentialsListUserCredentialsParamUserId)
                                     :
            source_type (UsersCredentialsListUserCredentialsParamSourceType | None)
                                     : The type of source to filter by.
            source_id (UsersCredentialsListUserCredentialsParamSourceId | None)
                                     : The ID of the source to filter by.
            source_version (UsersCredentialsListUserCredentialsParamSourceVersion | None)
                                     : The version of the source to filter by. By default it is
                                       the latest version.
            include_definition (bool | None)
                                     : Whether to include extended credential definition
                                       information.
            run-as (UsersCredentialsListUserCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersCredentialsListUserCredentials200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        params: dict[str, Any] = {
            **({"source_type": DataclassSerializer.serialize(source_type)} if source_type is not None else {}),
            **({"source_id": DataclassSerializer.serialize(source_id)} if source_id is not None else {}),
            **({"source_version": DataclassSerializer.serialize(source_version)} if source_version is not None else {}),
            **(
                {"include_definition": DataclassSerializer.serialize(include_definition)}
                if include_definition is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersCredentialsListUserCredentials200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_list_user_credentials(
        self,
        user_id: UsersCredentialsListUserCredentialsParamUserId,
        source_type: UsersCredentialsListUserCredentialsParamSourceType | None = None,
        source_id: UsersCredentialsListUserCredentialsParamSourceId | None = None,
        source_version: UsersCredentialsListUserCredentialsParamSourceVersion | None = None,
        include_definition: bool | None = None,
        run_as: UsersCredentialsListUserCredentialsParamRunAs | None = None,
    ) -> UsersCredentialsListUserCredentials200Response:
        """
        Lists all credentials the user has provided

        Args:
            user_id (UsersCredentialsListUserCredentialsParamUserId)
                                     :
            source_type (UsersCredentialsListUserCredentialsParamSourceType | None)
                                     : The type of source to filter by.
            source_id (UsersCredentialsListUserCredentialsParamSourceId | None)
                                     : The ID of the source to filter by.
            source_version (UsersCredentialsListUserCredentialsParamSourceVersion | None)
                                     : The version of the source to filter by. By default it is
                                       the latest version.
            include_definition (bool | None)
                                     : Whether to include extended credential definition
                                       information.
            run-as (UsersCredentialsListUserCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersCredentialsListUserCredentials200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        params: dict[str, Any] = {
            **({"source_type": DataclassSerializer.serialize(source_type)} if source_type is not None else {}),
            **({"source_id": DataclassSerializer.serialize(source_id)} if source_id is not None else {}),
            **({"source_version": DataclassSerializer.serialize(source_version)} if source_version is not None else {}),
            **(
                {"include_definition": DataclassSerializer.serialize(include_definition)}
                if include_definition is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UsersCredentialsListUserCredentials200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_provide_credential(
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
            run-as (UsersCredentialsProvideCredentialParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateSourceCredentialsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ServiceCredentialGroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_provide_credential(
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
            run-as (UsersCredentialsProvideCredentialParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateSourceCredentialsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ServiceCredentialGroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_update_user_credentials_group(
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
            run-as (UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SelectServiceCredentialPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
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
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_update_user_credentials_group(
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
            run-as (UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SelectServiceCredentialPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
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
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_delete_service_credentials(
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
            run-as (UsersCredentialsDeleteServiceCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_delete_service_credentials(
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
            run-as (UsersCredentialsDeleteServiceCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_groups_delete_credentials(
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
            run-as (UsersCredentialsGroupsDeleteCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_groups_delete_credentials(
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
            run-as (UsersCredentialsGroupsDeleteCredentialsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_groups_update_user_credentials(
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
            run-as (UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ServiceCredentialGroupPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ServiceCredentialGroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_credentials_groups_update_user_credentials(
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
            run-as (UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)
        user_credentials_id = DataclassSerializer.serialize(user_credentials_id)
        group_id = DataclassSerializer.serialize(group_id)

        url = f"{self.base_url}/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ServiceCredentialGroupPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ServiceCredentialGroupResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_get_custom_builds(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection:
        """
         Returns collection of custom builds.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersCustomBuildsGetCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CustomBuildsCollection)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_get_custom_builds(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection:
        """
         Returns collection of custom builds.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersCustomBuildsGetCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CustomBuildsCollection)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_delete_custom_builds(
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
            run-as (UsersCustomBuildsDeleteCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DeletedCustomBuild: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        key = DataclassSerializer.serialize(key)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DeletedCustomBuild)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_delete_custom_builds(
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
            run-as (UsersCustomBuildsDeleteCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DeletedCustomBuild: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        key = DataclassSerializer.serialize(key)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DeletedCustomBuild)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_add_custom_builds(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Add new custom build.

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (UsersCustomBuildsAddCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CustomBuildCreationPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        key = DataclassSerializer.serialize(key)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CustomBuildCreationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_custom_builds_add_custom_builds(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Add new custom build.

        Args:
            user_id (str)            : The ID of the user.
            key (str)                : The key of the custom build to be deleted.
            run-as (UsersCustomBuildsAddCustomBuildsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CustomBuildCreationPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        key = DataclassSerializer.serialize(key)

        url = f"{self.base_url}/api/users/{user_id}/custom_builds/{key}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CustomBuildCreationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_favorites_set_favorite(
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
            run-as (UsersFavoritesSetFavoriteParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)
        object_type = DataclassSerializer.serialize(object_type)

        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FavoriteObject = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FavoriteObjectsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_favorites_set_favorite(
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
            run-as (UsersFavoritesSetFavoriteParamRunAs | None)
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
        user_id = DataclassSerializer.serialize(user_id)
        object_type = DataclassSerializer.serialize(object_type)

        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: FavoriteObject = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FavoriteObjectsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_favorites_remove_favorite(
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
            run-as (UsersFavoritesRemoveFavoriteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        object_type = DataclassSerializer.serialize(object_type)
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FavoriteObjectsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_favorites_remove_favorite(
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
            run-as (UsersFavoritesRemoveFavoriteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            FavoriteObjectsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        object_type = DataclassSerializer.serialize(object_type)
        object_id = DataclassSerializer.serialize(object_id)

        url = f"{self.base_url}/api/users/{user_id}/favorites/{object_type}/{object_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), FavoriteObjectsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_objectstore_usage_objectstore_usage(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]:
        """
        Return the user's object store usage summary broken down by object store ID

        Args:
            user_id (UsersObjectstoreUsageObjectstoreUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (UsersObjectstoreUsageObjectstoreUsageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserObjectstoreUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/objectstore_usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserObjectstoreUsage])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_objectstore_usage_objectstore_usage(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]:
        """
        Return the user's object store usage summary broken down by object store ID

        Args:
            user_id (UsersObjectstoreUsageObjectstoreUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (UsersObjectstoreUsageObjectstoreUsageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserObjectstoreUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/objectstore_usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserObjectstoreUsage])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Triggers a recalculation of the current user disk usage.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: The asynchronous task summary to track the task state.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/recalculate_disk_usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_roles_get_user_roles(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Get User Roles

        Return a list of roles associated with this user. Only admins can see user roles.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersRolesGetUserRolesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_roles_get_user_roles(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Get User Roles

        Return a list of roles associated with this user. Only admins can see user roles.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersRolesGetUserRolesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_send_activation_email_send_activation_email(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Sends activation email to user.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersSendActivationEmailSendActivationEmailParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/send_activation_email"

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

    async def users_send_activation_email_send_activation_email(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Sends activation email to user.

        Args:
            user_id (str)            : The ID of the user.
            run-as (UsersSendActivationEmailSendActivationEmailParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/send_activation_email"

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

    async def users_theme_set_theme(
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
            run-as (UsersThemeSetThemeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        theme = DataclassSerializer.serialize(theme)

        url = f"{self.base_url}/api/users/{user_id}/theme/{theme}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_theme_set_theme(
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
            run-as (UsersThemeSetThemeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        theme = DataclassSerializer.serialize(theme)

        url = f"{self.base_url}/api/users/{user_id}/theme/{theme}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_usage_usage(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]:
        """
        Return the user's quota usage summary broken down by quota source

        Args:
            user_id (UsersUsageUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (UsersUsageUsageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserQuotaUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserQuotaUsage])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_usage_usage(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]:
        """
        Return the user's quota usage summary broken down by quota source

        Args:
            user_id (UsersUsageUsageParamUserId)
                                     : The ID of the user to get or 'current'.
            run-as (UsersUsageUsageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[UserQuotaUsage]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)

        url = f"{self.base_url}/api/users/{user_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[UserQuotaUsage])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_usage_usage_for(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response | None:
        """
        Return the user's quota usage summary for a given quota source label

        Args:
            user_id (UsersUsageUsageForParamUserId)
                                     : The ID of the user to get or 'current'.
            label (str)              : The label corresponding to the quota source to fetch
                                       usage information about.
            run-as (UsersUsageUsageForParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersUsageUsageFor200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        label = DataclassSerializer.serialize(label)

        url = f"{self.base_url}/api/users/{user_id}/usage/{label}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), UsersUsageUsageFor200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def users_usage_usage_for(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response | None:
        """
        Return the user's quota usage summary for a given quota source label

        Args:
            user_id (UsersUsageUsageForParamUserId)
                                     : The ID of the user to get or 'current'.
            label (str)              : The label corresponding to the quota source to fetch
                                       usage information about.
            run-as (UsersUsageUsageForParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UsersUsageUsageFor200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        user_id = DataclassSerializer.serialize(user_id)
        label = DataclassSerializer.serialize(label)

        url = f"{self.base_url}/api/users/{user_id}/usage/{label}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), UsersUsageUsageFor200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
