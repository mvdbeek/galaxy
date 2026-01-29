from typing import TYPE_CHECKING, Any

from ...models.anonymous_array_item_125 import AnonymousArrayItem125
from ...models.anonymous_array_item_127 import AnonymousArrayItem127
from ...models.api_key_model_2 import ApiKeyModel2
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.create_source_credentials_payload import CreateSourceCredentialsPayload
from ...models.created_user_model import CreatedUserModel
from ...models.custom_build_creation_payload import CustomBuildCreationPayload
from ...models.custom_builds_collection import CustomBuildsCollection
from ...models.deleted_custom_build import DeletedCustomBuild
from ...models.detailed_user_model import DetailedUserModel
from ...models.favorite_object import FavoriteObject
from ...models.favorite_object_type import FavoriteObjectType
from ...models.favorite_objects_summary import FavoriteObjectsSummary
from ...models.role_list_response import RoleListResponse
from ...models.select_service_credential_payload import SelectServiceCredentialPayload
from ...models.service_credential_group_payload import ServiceCredentialGroupPayload
from ...models.service_credential_group_response import ServiceCredentialGroupResponse
from ...models.user_beacon_setting import UserBeaconSetting
from ...models.user_objectstore_usage import UserObjectstoreUsage
from ...models.user_quota_usage import UserQuotaUsage
from ...models.user_update_payload import UserUpdatePayload
from ...models.users_api_key_create_api_key_param_run_as import UsersApiKeyCreateApiKeyParamRunAs
from ...models.users_api_key_delete_api_key_param_run_as import UsersApiKeyDeleteApiKeyParamRunAs
from ...models.users_api_key_detailed_get_api_key_param_run_as import UsersApiKeyDetailedGetApiKeyParamRunAs
from ...models.users_api_key_get_or_create_api_key_param_run_as import UsersApiKeyGetOrCreateApiKeyParamRunAs
from ...models.users_beacon_get_beacon_param_run_as import UsersBeaconGetBeaconParamRunAs
from ...models.users_beacon_set_beacon_param_run_as import UsersBeaconSetBeaconParamRunAs
from ...models.users_create_param_run_as import UsersCreateParamRunAs
from ...models.users_create_request_body import UsersCreateRequestBody
from ...models.users_credentials_delete_service_credentials_param_run_as import (
    UsersCredentialsDeleteServiceCredentialsParamRunAs,
)
from ...models.users_credentials_delete_service_credentials_param_user_id import (
    UsersCredentialsDeleteServiceCredentialsParamUserId,
)
from ...models.users_credentials_groups_delete_credentials_param_run_as import (
    UsersCredentialsGroupsDeleteCredentialsParamRunAs,
)
from ...models.users_credentials_groups_delete_credentials_param_user_id import (
    UsersCredentialsGroupsDeleteCredentialsParamUserId,
)
from ...models.users_credentials_groups_update_user_credentials_param_run_as import (
    UsersCredentialsGroupsUpdateUserCredentialsParamRunAs,
)
from ...models.users_credentials_groups_update_user_credentials_param_user_id import (
    UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
)
from ...models.users_credentials_list_user_credentials_200_response import (
    UsersCredentialsListUserCredentials200Response,
)
from ...models.users_credentials_list_user_credentials_param_run_as import UsersCredentialsListUserCredentialsParamRunAs
from ...models.users_credentials_list_user_credentials_param_source_id import (
    UsersCredentialsListUserCredentialsParamSourceId,
)
from ...models.users_credentials_list_user_credentials_param_source_type import (
    UsersCredentialsListUserCredentialsParamSourceType,
)
from ...models.users_credentials_list_user_credentials_param_source_version import (
    UsersCredentialsListUserCredentialsParamSourceVersion,
)
from ...models.users_credentials_list_user_credentials_param_user_id import (
    UsersCredentialsListUserCredentialsParamUserId,
)
from ...models.users_credentials_provide_credential_param_run_as import UsersCredentialsProvideCredentialParamRunAs
from ...models.users_credentials_provide_credential_param_user_id import UsersCredentialsProvideCredentialParamUserId
from ...models.users_credentials_update_user_credentials_group_param_run_as import (
    UsersCredentialsUpdateUserCredentialsGroupParamRunAs,
)
from ...models.users_credentials_update_user_credentials_group_param_user_id import (
    UsersCredentialsUpdateUserCredentialsGroupParamUserId,
)
from ...models.users_current_recalculate_disk_usage_recalculate_disk_usage_param_run_as import (
    UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs,
)
from ...models.users_custom_builds_add_custom_builds_param_run_as import UsersCustomBuildsAddCustomBuildsParamRunAs
from ...models.users_custom_builds_delete_custom_builds_param_run_as import (
    UsersCustomBuildsDeleteCustomBuildsParamRunAs,
)
from ...models.users_custom_builds_get_custom_builds_param_run_as import UsersCustomBuildsGetCustomBuildsParamRunAs
from ...models.users_delete_param_run_as import UsersDeleteParamRunAs
from ...models.users_delete_request_body import UsersDeleteRequestBody
from ...models.users_deleted_index_deleted_param_f_any import UsersDeletedIndexDeletedParamFAny
from ...models.users_deleted_index_deleted_param_f_email import UsersDeletedIndexDeletedParamFEmail
from ...models.users_deleted_index_deleted_param_f_name import UsersDeletedIndexDeletedParamFName
from ...models.users_deleted_index_deleted_param_run_as import UsersDeletedIndexDeletedParamRunAs
from ...models.users_deleted_show_deleted_200_response import UsersDeletedShowDeleted200Response
from ...models.users_deleted_show_deleted_param_run_as import UsersDeletedShowDeletedParamRunAs
from ...models.users_deleted_undelete_undelete_param_run_as import UsersDeletedUndeleteUndeleteParamRunAs
from ...models.users_favorites_remove_favorite_param_run_as import UsersFavoritesRemoveFavoriteParamRunAs
from ...models.users_favorites_set_favorite_param_run_as import UsersFavoritesSetFavoriteParamRunAs
from ...models.users_index_param_f_any import UsersIndexParamFAny
from ...models.users_index_param_f_email import UsersIndexParamFEmail
from ...models.users_index_param_f_name import UsersIndexParamFName
from ...models.users_index_param_run_as import UsersIndexParamRunAs
from ...models.users_objectstore_usage_objectstore_usage_param_run_as import (
    UsersObjectstoreUsageObjectstoreUsageParamRunAs,
)
from ...models.users_objectstore_usage_objectstore_usage_param_user_id import (
    UsersObjectstoreUsageObjectstoreUsageParamUserId,
)
from ...models.users_recalculate_disk_usage_recalculate_disk_usage_by_user_id_param_run_as import (
    UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs,
)
from ...models.users_recalculate_disk_usage_recalculate_disk_usage_param_run_as import (
    UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs,
)
from ...models.users_roles_get_user_roles_param_run_as import UsersRolesGetUserRolesParamRunAs
from ...models.users_send_activation_email_send_activation_email_param_run_as import (
    UsersSendActivationEmailSendActivationEmailParamRunAs,
)
from ...models.users_show_200_response import UsersShow200Response
from ...models.users_show_param_deleted import UsersShowParamDeleted
from ...models.users_show_param_run_as import UsersShowParamRunAs
from ...models.users_show_param_user_id import UsersShowParamUserId
from ...models.users_theme_set_theme_param_run_as import UsersThemeSetThemeParamRunAs
from ...models.users_update_param_deleted import UsersUpdateParamDeleted
from ...models.users_update_param_run_as import UsersUpdateParamRunAs
from ...models.users_update_param_user_id import UsersUpdateParamUserId
from ...models.users_usage_usage_for_200_response import UsersUsageUsageFor200Response
from ...models.users_usage_usage_for_param_run_as import UsersUsageUsageForParamRunAs
from ...models.users_usage_usage_for_param_user_id import UsersUsageUsageForParamUserId
from ...models.users_usage_usage_param_run_as import UsersUsageUsageParamRunAs
from ...models.users_usage_usage_param_user_id import UsersUsageUsageParamUserId

if TYPE_CHECKING:
    pass


class MockUsersClient:
    """
    Mock implementation of UsersClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestUsersClient(MockUsersClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def users_index(
        self,
        deleted: bool | None = None,
        f_email: UsersIndexParamFEmail | None = None,
        f_name: UsersIndexParamFName | None = None,
        f_any: UsersIndexParamFAny | None = None,
        run_as: UsersIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_index() not implemented. Override this method in your test subclass."
        )

    async def users_create(
        self,
        body: UsersCreateRequestBody,
        run_as: UsersCreateParamRunAs | None = None,
    ) -> CreatedUserModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_create() not implemented. Override this method in your test subclass."
        )

    async def users_current_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersCurrentRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_current_recalculate_disk_usage_recalculate_disk_usage() not implemented. Override this method in your test subclass."
        )

    async def users_deleted_index_deleted(
        self,
        f_email: UsersDeletedIndexDeletedParamFEmail | None = None,
        f_name: UsersDeletedIndexDeletedParamFName | None = None,
        f_any: UsersDeletedIndexDeletedParamFAny | None = None,
        run_as: UsersDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_deleted_index_deleted() not implemented. Override this method in your test subclass."
        )

    async def users_deleted_show_deleted(
        self,
        user_id: str,
        run_as: UsersDeletedShowDeletedParamRunAs | None = None,
    ) -> UsersDeletedShowDeleted200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_deleted_show_deleted() not implemented. Override this method in your test subclass."
        )

    async def users_deleted_undelete_undelete(
        self,
        user_id: str,
        run_as: UsersDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_deleted_undelete_undelete() not implemented. Override this method in your test subclass."
        )

    async def users_recalculate_disk_usage_recalculate_disk_usage(
        self,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_recalculate_disk_usage_recalculate_disk_usage() not implemented. Override this method in your test subclass."
        )

    async def users_delete(
        self,
        user_id: str,
        purge: bool | None = None,
        run_as: UsersDeleteParamRunAs | None = None,
        body: UsersDeleteRequestBody | None = None,
    ) -> DetailedUserModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_delete() not implemented. Override this method in your test subclass."
        )

    async def users_show(
        self,
        user_id: UsersShowParamUserId,
        deleted: UsersShowParamDeleted | None = None,
        run_as: UsersShowParamRunAs | None = None,
    ) -> UsersShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_show() not implemented. Override this method in your test subclass."
        )

    async def users_update(
        self,
        user_id: UsersUpdateParamUserId,
        body: UserUpdatePayload,
        deleted: UsersUpdateParamDeleted | None = None,
        run_as: UsersUpdateParamRunAs | None = None,
    ) -> DetailedUserModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_update() not implemented. Override this method in your test subclass."
        )

    async def users_api_key_delete_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDeleteApiKeyParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_api_key_delete_api_key() not implemented. Override this method in your test subclass."
        )

    async def users_api_key_get_or_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyGetOrCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_api_key_get_or_create_api_key() not implemented. Override this method in your test subclass."
        )

    async def users_api_key_create_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyCreateApiKeyParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_api_key_create_api_key() not implemented. Override this method in your test subclass."
        )

    async def users_api_key_detailed_get_api_key(
        self,
        user_id: str,
        run_as: UsersApiKeyDetailedGetApiKeyParamRunAs | None = None,
    ) -> ApiKeyModel2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_api_key_detailed_get_api_key() not implemented. Override this method in your test subclass."
        )

    async def users_beacon_get_beacon(
        self,
        user_id: str,
        run_as: UsersBeaconGetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_beacon_get_beacon() not implemented. Override this method in your test subclass."
        )

    async def users_beacon_set_beacon(
        self,
        user_id: str,
        body: UserBeaconSetting,
        run_as: UsersBeaconSetBeaconParamRunAs | None = None,
    ) -> UserBeaconSetting:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_beacon_set_beacon() not implemented. Override this method in your test subclass."
        )

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
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_list_user_credentials() not implemented. Override this method in your test subclass."
        )

    async def users_credentials_provide_credential(
        self,
        user_id: UsersCredentialsProvideCredentialParamUserId,
        body: CreateSourceCredentialsPayload,
        run_as: UsersCredentialsProvideCredentialParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_provide_credential() not implemented. Override this method in your test subclass."
        )

    async def users_credentials_update_user_credentials_group(
        self,
        user_id: UsersCredentialsUpdateUserCredentialsGroupParamUserId,
        body: SelectServiceCredentialPayload,
        run_as: UsersCredentialsUpdateUserCredentialsGroupParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_update_user_credentials_group() not implemented. Override this method in your test subclass."
        )

    async def users_credentials_delete_service_credentials(
        self,
        user_id: UsersCredentialsDeleteServiceCredentialsParamUserId,
        user_credentials_id: str,
        run_as: UsersCredentialsDeleteServiceCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_delete_service_credentials() not implemented. Override this method in your test subclass."
        )

    async def users_credentials_groups_delete_credentials(
        self,
        user_id: UsersCredentialsGroupsDeleteCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        run_as: UsersCredentialsGroupsDeleteCredentialsParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_groups_delete_credentials() not implemented. Override this method in your test subclass."
        )

    async def users_credentials_groups_update_user_credentials(
        self,
        user_id: UsersCredentialsGroupsUpdateUserCredentialsParamUserId,
        user_credentials_id: str,
        group_id: str,
        body: ServiceCredentialGroupPayload,
        run_as: UsersCredentialsGroupsUpdateUserCredentialsParamRunAs | None = None,
    ) -> ServiceCredentialGroupResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_credentials_groups_update_user_credentials() not implemented. Override this method in your test subclass."
        )

    async def users_custom_builds_get_custom_builds(
        self,
        user_id: str,
        run_as: UsersCustomBuildsGetCustomBuildsParamRunAs | None = None,
    ) -> CustomBuildsCollection:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_custom_builds_get_custom_builds() not implemented. Override this method in your test subclass."
        )

    async def users_custom_builds_delete_custom_builds(
        self,
        user_id: str,
        key: str,
        run_as: UsersCustomBuildsDeleteCustomBuildsParamRunAs | None = None,
    ) -> DeletedCustomBuild:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_custom_builds_delete_custom_builds() not implemented. Override this method in your test subclass."
        )

    async def users_custom_builds_add_custom_builds(
        self,
        user_id: str,
        key: str,
        body: CustomBuildCreationPayload,
        run_as: UsersCustomBuildsAddCustomBuildsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_custom_builds_add_custom_builds() not implemented. Override this method in your test subclass."
        )

    async def users_favorites_set_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        body: FavoriteObject,
        run_as: UsersFavoritesSetFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_favorites_set_favorite() not implemented. Override this method in your test subclass."
        )

    async def users_favorites_remove_favorite(
        self,
        user_id: str,
        object_type: FavoriteObjectType,
        object_id: str,
        run_as: UsersFavoritesRemoveFavoriteParamRunAs | None = None,
    ) -> FavoriteObjectsSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_favorites_remove_favorite() not implemented. Override this method in your test subclass."
        )

    async def users_objectstore_usage_objectstore_usage(
        self,
        user_id: UsersObjectstoreUsageObjectstoreUsageParamUserId,
        run_as: UsersObjectstoreUsageObjectstoreUsageParamRunAs | None = None,
    ) -> list[UserObjectstoreUsage]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_objectstore_usage_objectstore_usage() not implemented. Override this method in your test subclass."
        )

    async def users_recalculate_disk_usage_recalculate_disk_usage_by_user_id(
        self,
        user_id: str,
        run_as: UsersRecalculateDiskUsageRecalculateDiskUsageByUserIdParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_recalculate_disk_usage_recalculate_disk_usage_by_user_id() not implemented. Override this method in your test subclass."
        )

    async def users_roles_get_user_roles(
        self,
        user_id: str,
        run_as: UsersRolesGetUserRolesParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_roles_get_user_roles() not implemented. Override this method in your test subclass."
        )

    async def users_send_activation_email_send_activation_email(
        self,
        user_id: str,
        run_as: UsersSendActivationEmailSendActivationEmailParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_send_activation_email_send_activation_email() not implemented. Override this method in your test subclass."
        )

    async def users_theme_set_theme(
        self,
        user_id: str,
        theme: str,
        run_as: UsersThemeSetThemeParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_theme_set_theme() not implemented. Override this method in your test subclass."
        )

    async def users_usage_usage(
        self,
        user_id: UsersUsageUsageParamUserId,
        run_as: UsersUsageUsageParamRunAs | None = None,
    ) -> list[UserQuotaUsage]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_usage_usage() not implemented. Override this method in your test subclass."
        )

    async def users_usage_usage_for(
        self,
        user_id: UsersUsageUsageForParamUserId,
        label: str,
        run_as: UsersUsageUsageForParamRunAs | None = None,
    ) -> UsersUsageUsageFor200Response | None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockUsersClient.users_usage_usage_for() not implemented. Override this method in your test subclass."
        )
