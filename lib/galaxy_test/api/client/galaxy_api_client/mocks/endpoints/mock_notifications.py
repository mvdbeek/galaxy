from datetime import datetime
from typing import TYPE_CHECKING

from ...models.broadcast_notification_create_request import BroadcastNotificationCreateRequest
from ...models.broadcast_notification_list_response import BroadcastNotificationListResponse
from ...models.broadcast_notification_response import BroadcastNotificationResponse
from ...models.notification_broadcast_update_request import NotificationBroadcastUpdateRequest
from ...models.notification_create_request import NotificationCreateRequest
from ...models.notification_created_response import NotificationCreatedResponse
from ...models.notification_status_summary import NotificationStatusSummary
from ...models.notifications_batch_request import NotificationsBatchRequest
from ...models.notifications_batch_update_response import NotificationsBatchUpdateResponse
from ...models.notifications_broadcast_broadcast_notification_param_run_as import (
    NotificationsBroadcastBroadcastNotificationParamRunAs,
)
from ...models.notifications_broadcast_get_all_broadcasted_param_run_as import (
    NotificationsBroadcastGetAllBroadcastedParamRunAs,
)
from ...models.notifications_broadcast_get_broadcasted_param_run_as import (
    NotificationsBroadcastGetBroadcastedParamRunAs,
)
from ...models.notifications_broadcast_update_broadcasted_notification_param_run_as import (
    NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs,
)
from ...models.notifications_delete_user_notification_param_run_as import NotificationsDeleteUserNotificationParamRunAs
from ...models.notifications_delete_user_notifications_param_run_as import (
    NotificationsDeleteUserNotificationsParamRunAs,
)
from ...models.notifications_get_user_notifications_param_limit import NotificationsGetUserNotificationsParamLimit
from ...models.notifications_get_user_notifications_param_offset import NotificationsGetUserNotificationsParamOffset
from ...models.notifications_get_user_notifications_param_run_as import NotificationsGetUserNotificationsParamRunAs
from ...models.notifications_preferences_get_notification_preferences_param_run_as import (
    NotificationsPreferencesGetNotificationPreferencesParamRunAs,
)
from ...models.notifications_preferences_update_notification_preferences_param_run_as import (
    NotificationsPreferencesUpdateNotificationPreferencesParamRunAs,
)
from ...models.notifications_send_notification_200_response import NotificationsSendNotification200Response
from ...models.notifications_send_notification_param_run_as import NotificationsSendNotificationParamRunAs
from ...models.notifications_show_notification_param_run_as import NotificationsShowNotificationParamRunAs
from ...models.notifications_status_get_notifications_status_param_run_as import (
    NotificationsStatusGetNotificationsStatusParamRunAs,
)
from ...models.notifications_update_user_notification_param_run_as import NotificationsUpdateUserNotificationParamRunAs
from ...models.notifications_update_user_notifications_param_run_as import (
    NotificationsUpdateUserNotificationsParamRunAs,
)
from ...models.update_user_notification_preferences_request import UpdateUserNotificationPreferencesRequest
from ...models.user_notification_list_response import UserNotificationListResponse
from ...models.user_notification_preferences import UserNotificationPreferences
from ...models.user_notification_response import UserNotificationResponse
from ...models.user_notification_update_request import UserNotificationUpdateRequest
from ...models.user_notifications_batch_update_request import UserNotificationsBatchUpdateRequest

if TYPE_CHECKING:
    pass


class MockNotificationsClient:
    """
    Mock implementation of NotificationsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestNotificationsClient(MockNotificationsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def notifications_delete_user_notifications(
        self,
        body: NotificationsBatchRequest,
        run_as: NotificationsDeleteUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_delete_user_notifications() not implemented. Override this method in your test subclass."
        )

    async def notifications_get_user_notifications(
        self,
        limit: NotificationsGetUserNotificationsParamLimit | None = None,
        offset: NotificationsGetUserNotificationsParamOffset | None = None,
        run_as: NotificationsGetUserNotificationsParamRunAs | None = None,
    ) -> UserNotificationListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_get_user_notifications() not implemented. Override this method in your test subclass."
        )

    async def notifications_send_notification(
        self,
        body: NotificationCreateRequest,
        run_as: NotificationsSendNotificationParamRunAs | None = None,
    ) -> NotificationsSendNotification200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_send_notification() not implemented. Override this method in your test subclass."
        )

    async def notifications_update_user_notifications(
        self,
        body: UserNotificationsBatchUpdateRequest,
        run_as: NotificationsUpdateUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_update_user_notifications() not implemented. Override this method in your test subclass."
        )

    async def notifications_broadcast_get_all_broadcasted(
        self,
        run_as: NotificationsBroadcastGetAllBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_broadcast_get_all_broadcasted() not implemented. Override this method in your test subclass."
        )

    async def notifications_broadcast_broadcast_notification(
        self,
        body: BroadcastNotificationCreateRequest,
        run_as: NotificationsBroadcastBroadcastNotificationParamRunAs | None = None,
    ) -> NotificationCreatedResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_broadcast_broadcast_notification() not implemented. Override this method in your test subclass."
        )

    async def notifications_broadcast_get_broadcasted(
        self,
        notification_id: str,
        run_as: NotificationsBroadcastGetBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_broadcast_get_broadcasted() not implemented. Override this method in your test subclass."
        )

    async def notifications_broadcast_update_broadcasted_notification(
        self,
        notification_id: str,
        body: NotificationBroadcastUpdateRequest,
        run_as: NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_broadcast_update_broadcasted_notification() not implemented. Override this method in your test subclass."
        )

    async def notifications_preferences_get_notification_preferences(
        self,
        run_as: NotificationsPreferencesGetNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_preferences_get_notification_preferences() not implemented. Override this method in your test subclass."
        )

    async def notifications_preferences_update_notification_preferences(
        self,
        body: UpdateUserNotificationPreferencesRequest,
        run_as: NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_preferences_update_notification_preferences() not implemented. Override this method in your test subclass."
        )

    async def notifications_status_get_notifications_status(
        self,
        since: datetime,
        run_as: NotificationsStatusGetNotificationsStatusParamRunAs | None = None,
    ) -> NotificationStatusSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_status_get_notifications_status() not implemented. Override this method in your test subclass."
        )

    async def notifications_delete_user_notification(
        self,
        notification_id: str,
        run_as: NotificationsDeleteUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_delete_user_notification() not implemented. Override this method in your test subclass."
        )

    async def notifications_show_notification(
        self,
        notification_id: str,
        run_as: NotificationsShowNotificationParamRunAs | None = None,
    ) -> UserNotificationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_show_notification() not implemented. Override this method in your test subclass."
        )

    async def notifications_update_user_notification(
        self,
        notification_id: str,
        body: UserNotificationUpdateRequest,
        run_as: NotificationsUpdateUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockNotificationsClient.notifications_update_user_notification() not implemented. Override this method in your test subclass."
        )
