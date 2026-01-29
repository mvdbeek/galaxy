from datetime import datetime
from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.broadcast_notification_create_request import BroadcastNotificationCreateRequest
from ..models.broadcast_notification_list_response import BroadcastNotificationListResponse
from ..models.broadcast_notification_response import BroadcastNotificationResponse
from ..models.notification_broadcast_update_request import NotificationBroadcastUpdateRequest
from ..models.notification_create_request import NotificationCreateRequest
from ..models.notification_created_response import NotificationCreatedResponse
from ..models.notification_status_summary import NotificationStatusSummary
from ..models.notifications_batch_request import NotificationsBatchRequest
from ..models.notifications_batch_update_response import NotificationsBatchUpdateResponse
from ..models.notifications_broadcast_broadcast_notification_param_run_as import (
    NotificationsBroadcastBroadcastNotificationParamRunAs,
)
from ..models.notifications_broadcast_get_all_broadcasted_param_run_as import (
    NotificationsBroadcastGetAllBroadcastedParamRunAs,
)
from ..models.notifications_broadcast_get_broadcasted_param_run_as import NotificationsBroadcastGetBroadcastedParamRunAs
from ..models.notifications_broadcast_update_broadcasted_notification_param_run_as import (
    NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs,
)
from ..models.notifications_delete_user_notification_param_run_as import NotificationsDeleteUserNotificationParamRunAs
from ..models.notifications_delete_user_notifications_param_run_as import NotificationsDeleteUserNotificationsParamRunAs
from ..models.notifications_get_user_notifications_param_limit import NotificationsGetUserNotificationsParamLimit
from ..models.notifications_get_user_notifications_param_offset import NotificationsGetUserNotificationsParamOffset
from ..models.notifications_get_user_notifications_param_run_as import NotificationsGetUserNotificationsParamRunAs
from ..models.notifications_preferences_get_notification_preferences_param_run_as import (
    NotificationsPreferencesGetNotificationPreferencesParamRunAs,
)
from ..models.notifications_preferences_update_notification_preferences_param_run_as import (
    NotificationsPreferencesUpdateNotificationPreferencesParamRunAs,
)
from ..models.notifications_send_notification_200_response import NotificationsSendNotification200Response
from ..models.notifications_send_notification_param_run_as import NotificationsSendNotificationParamRunAs
from ..models.notifications_show_notification_param_run_as import NotificationsShowNotificationParamRunAs
from ..models.notifications_status_get_notifications_status_param_run_as import (
    NotificationsStatusGetNotificationsStatusParamRunAs,
)
from ..models.notifications_update_user_notification_param_run_as import NotificationsUpdateUserNotificationParamRunAs
from ..models.notifications_update_user_notifications_param_run_as import NotificationsUpdateUserNotificationsParamRunAs
from ..models.update_user_notification_preferences_request import UpdateUserNotificationPreferencesRequest
from ..models.user_notification_list_response import UserNotificationListResponse
from ..models.user_notification_preferences import UserNotificationPreferences
from ..models.user_notification_response import UserNotificationResponse
from ..models.user_notification_update_request import UserNotificationUpdateRequest
from ..models.user_notifications_batch_update_request import UserNotificationsBatchUpdateRequest


@runtime_checkable
class NotificationsClientProtocol(Protocol):
    """Protocol defining the interface of NotificationsClient for dependency injection."""

    async def notifications_delete_user_notifications(
        self,
        body: NotificationsBatchRequest,
        run_as: NotificationsDeleteUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse: ...

    async def notifications_delete_user_notifications(
        self,
        body: NotificationsBatchRequest,
        run_as: NotificationsDeleteUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse: ...

    async def notifications_get_user_notifications(
        self,
        limit: NotificationsGetUserNotificationsParamLimit | None = None,
        offset: NotificationsGetUserNotificationsParamOffset | None = None,
        run_as: NotificationsGetUserNotificationsParamRunAs | None = None,
    ) -> UserNotificationListResponse: ...

    async def notifications_get_user_notifications(
        self,
        limit: NotificationsGetUserNotificationsParamLimit | None = None,
        offset: NotificationsGetUserNotificationsParamOffset | None = None,
        run_as: NotificationsGetUserNotificationsParamRunAs | None = None,
    ) -> UserNotificationListResponse: ...

    async def notifications_send_notification(
        self,
        body: NotificationCreateRequest,
        run_as: NotificationsSendNotificationParamRunAs | None = None,
    ) -> NotificationsSendNotification200Response: ...

    async def notifications_send_notification(
        self,
        body: NotificationCreateRequest,
        run_as: NotificationsSendNotificationParamRunAs | None = None,
    ) -> NotificationsSendNotification200Response: ...

    async def notifications_update_user_notifications(
        self,
        body: UserNotificationsBatchUpdateRequest,
        run_as: NotificationsUpdateUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse: ...

    async def notifications_update_user_notifications(
        self,
        body: UserNotificationsBatchUpdateRequest,
        run_as: NotificationsUpdateUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse: ...

    async def notifications_broadcast_get_all_broadcasted(
        self,
        run_as: NotificationsBroadcastGetAllBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationListResponse: ...

    async def notifications_broadcast_get_all_broadcasted(
        self,
        run_as: NotificationsBroadcastGetAllBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationListResponse: ...

    async def notifications_broadcast_broadcast_notification(
        self,
        body: BroadcastNotificationCreateRequest,
        run_as: NotificationsBroadcastBroadcastNotificationParamRunAs | None = None,
    ) -> NotificationCreatedResponse: ...

    async def notifications_broadcast_broadcast_notification(
        self,
        body: BroadcastNotificationCreateRequest,
        run_as: NotificationsBroadcastBroadcastNotificationParamRunAs | None = None,
    ) -> NotificationCreatedResponse: ...

    async def notifications_broadcast_get_broadcasted(
        self,
        notification_id: str,
        run_as: NotificationsBroadcastGetBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationResponse: ...

    async def notifications_broadcast_get_broadcasted(
        self,
        notification_id: str,
        run_as: NotificationsBroadcastGetBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationResponse: ...

    async def notifications_broadcast_update_broadcasted_notification(
        self,
        notification_id: str,
        body: NotificationBroadcastUpdateRequest,
        run_as: NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None = None,
    ) -> None: ...

    async def notifications_broadcast_update_broadcasted_notification(
        self,
        notification_id: str,
        body: NotificationBroadcastUpdateRequest,
        run_as: NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None = None,
    ) -> None: ...

    async def notifications_preferences_get_notification_preferences(
        self,
        run_as: NotificationsPreferencesGetNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences: ...

    async def notifications_preferences_get_notification_preferences(
        self,
        run_as: NotificationsPreferencesGetNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences: ...

    async def notifications_preferences_update_notification_preferences(
        self,
        body: UpdateUserNotificationPreferencesRequest,
        run_as: NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences: ...

    async def notifications_preferences_update_notification_preferences(
        self,
        body: UpdateUserNotificationPreferencesRequest,
        run_as: NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences: ...

    async def notifications_status_get_notifications_status(
        self,
        since: datetime,
        run_as: NotificationsStatusGetNotificationsStatusParamRunAs | None = None,
    ) -> NotificationStatusSummary: ...

    async def notifications_status_get_notifications_status(
        self,
        since: datetime,
        run_as: NotificationsStatusGetNotificationsStatusParamRunAs | None = None,
    ) -> NotificationStatusSummary: ...

    async def notifications_delete_user_notification(
        self,
        notification_id: str,
        run_as: NotificationsDeleteUserNotificationParamRunAs | None = None,
    ) -> None: ...

    async def notifications_delete_user_notification(
        self,
        notification_id: str,
        run_as: NotificationsDeleteUserNotificationParamRunAs | None = None,
    ) -> None: ...

    async def notifications_show_notification(
        self,
        notification_id: str,
        run_as: NotificationsShowNotificationParamRunAs | None = None,
    ) -> UserNotificationResponse: ...

    async def notifications_show_notification(
        self,
        notification_id: str,
        run_as: NotificationsShowNotificationParamRunAs | None = None,
    ) -> UserNotificationResponse: ...

    async def notifications_update_user_notification(
        self,
        notification_id: str,
        body: UserNotificationUpdateRequest,
        run_as: NotificationsUpdateUserNotificationParamRunAs | None = None,
    ) -> None: ...

    async def notifications_update_user_notification(
        self,
        notification_id: str,
        body: UserNotificationUpdateRequest,
        run_as: NotificationsUpdateUserNotificationParamRunAs | None = None,
    ) -> None: ...


class NotificationsClient(NotificationsClientProtocol):
    """Client for notifications endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def notifications_delete_user_notifications(
        self,
        body: NotificationsBatchRequest,
        run_as: NotificationsDeleteUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Deletes a list of notifications received by the user in a single request.

        Args:
            run-as (NotificationsDeleteUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationsBatchRequest)
                                     : Request body. (json)

        Returns:
            NotificationsBatchUpdateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationsBatchRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsBatchUpdateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_delete_user_notifications(
        self,
        body: NotificationsBatchRequest,
        run_as: NotificationsDeleteUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Deletes a list of notifications received by the user in a single request.

        Args:
            run-as (NotificationsDeleteUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationsBatchRequest)
                                     : Request body. (json)

        Returns:
            NotificationsBatchUpdateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationsBatchRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsBatchUpdateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_get_user_notifications(
        self,
        limit: NotificationsGetUserNotificationsParamLimit | None = None,
        offset: NotificationsGetUserNotificationsParamOffset | None = None,
        run_as: NotificationsGetUserNotificationsParamRunAs | None = None,
    ) -> UserNotificationListResponse:
        """
        Returns the list of notifications associated with the user.

        Anonymous users cannot receive personal notifications, only broadcasted notifications.
        You can use the `limit` and `offset` parameters to paginate through the notifications.

        Args:
            limit (NotificationsGetUserNotificationsParamLimit | None)
                                     :
            offset (NotificationsGetUserNotificationsParamOffset | None)
                                     :
            run-as (NotificationsGetUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_get_user_notifications(
        self,
        limit: NotificationsGetUserNotificationsParamLimit | None = None,
        offset: NotificationsGetUserNotificationsParamOffset | None = None,
        run_as: NotificationsGetUserNotificationsParamRunAs | None = None,
    ) -> UserNotificationListResponse:
        """
        Returns the list of notifications associated with the user.

        Anonymous users cannot receive personal notifications, only broadcasted notifications.
        You can use the `limit` and `offset` parameters to paginate through the notifications.

        Args:
            limit (NotificationsGetUserNotificationsParamLimit | None)
                                     :
            offset (NotificationsGetUserNotificationsParamOffset | None)
                                     :
            run-as (NotificationsGetUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_send_notification(
        self,
        body: NotificationCreateRequest,
        run_as: NotificationsSendNotificationParamRunAs | None = None,
    ) -> NotificationsSendNotification200Response:
        """
        Sends a notification to a list of recipients (users, groups or roles).

        Sends a notification to a list of recipients (users, groups or roles).

        Args:
            run-as (NotificationsSendNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationCreateRequest)
                                     : Request body. (json)

        Returns:
            NotificationsSendNotification200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationCreateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsSendNotification200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_send_notification(
        self,
        body: NotificationCreateRequest,
        run_as: NotificationsSendNotificationParamRunAs | None = None,
    ) -> NotificationsSendNotification200Response:
        """
        Sends a notification to a list of recipients (users, groups or roles).

        Sends a notification to a list of recipients (users, groups or roles).

        Args:
            run-as (NotificationsSendNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationCreateRequest)
                                     : Request body. (json)

        Returns:
            NotificationsSendNotification200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationCreateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsSendNotification200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_update_user_notifications(
        self,
        body: UserNotificationsBatchUpdateRequest,
        run_as: NotificationsUpdateUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Updates a list of notifications with the requested values in a single request.

        Args:
            run-as (NotificationsUpdateUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserNotificationsBatchUpdateRequest)
                                     : Request body. (json)

        Returns:
            NotificationsBatchUpdateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserNotificationsBatchUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsBatchUpdateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_update_user_notifications(
        self,
        body: UserNotificationsBatchUpdateRequest,
        run_as: NotificationsUpdateUserNotificationsParamRunAs | None = None,
    ) -> NotificationsBatchUpdateResponse:
        """
        Updates a list of notifications with the requested values in a single request.

        Args:
            run-as (NotificationsUpdateUserNotificationsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserNotificationsBatchUpdateRequest)
                                     : Request body. (json)

        Returns:
            NotificationsBatchUpdateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserNotificationsBatchUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationsBatchUpdateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_get_all_broadcasted(
        self,
        run_as: NotificationsBroadcastGetAllBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationListResponse:
        """
        Returns all currently active broadcasted notifications.

        Only Admin users can access inactive notifications (scheduled or recently expired).

        Args:
            run-as (NotificationsBroadcastGetAllBroadcastedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            BroadcastNotificationListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/broadcast"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), BroadcastNotificationListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_get_all_broadcasted(
        self,
        run_as: NotificationsBroadcastGetAllBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationListResponse:
        """
        Returns all currently active broadcasted notifications.

        Only Admin users can access inactive notifications (scheduled or recently expired).

        Args:
            run-as (NotificationsBroadcastGetAllBroadcastedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            BroadcastNotificationListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/broadcast"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), BroadcastNotificationListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_broadcast_notification(
        self,
        body: BroadcastNotificationCreateRequest,
        run_as: NotificationsBroadcastBroadcastNotificationParamRunAs | None = None,
    ) -> NotificationCreatedResponse:
        """
        Broadcasts a notification to every user in the system.

        Broadcasted notifications are a special kind of notification that are always accessible
        to all users, including anonymous users. They are typically used to display important
        information such as maintenance windows or new features. These notifications are
        displayed differently from regular notifications, usually in a banner at the top or
        bottom of the page.  Broadcasted notifications can include action links that are
        displayed as buttons. This allows users to easily perform tasks such as filling out
        surveys, accepting legal agreements, or accessing new tutorials.  Some key features of
        broadcasted notifications include: - They are not associated with a specific user, so
        they cannot be deleted or marked as read. - They can be scheduled to be displayed in the
        future or to expire after a certain time. - By default, broadcasted notifications are
        published immediately and expire six months after publication. - Only admins can create,
        edit, reschedule, or expire broadcasted notifications as needed.

        Args:
            run-as (NotificationsBroadcastBroadcastNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BroadcastNotificationCreateRequest)
                                     : Request body. (json)

        Returns:
            NotificationCreatedResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/broadcast"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BroadcastNotificationCreateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationCreatedResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_broadcast_notification(
        self,
        body: BroadcastNotificationCreateRequest,
        run_as: NotificationsBroadcastBroadcastNotificationParamRunAs | None = None,
    ) -> NotificationCreatedResponse:
        """
        Broadcasts a notification to every user in the system.

        Broadcasted notifications are a special kind of notification that are always accessible
        to all users, including anonymous users. They are typically used to display important
        information such as maintenance windows or new features. These notifications are
        displayed differently from regular notifications, usually in a banner at the top or
        bottom of the page.  Broadcasted notifications can include action links that are
        displayed as buttons. This allows users to easily perform tasks such as filling out
        surveys, accepting legal agreements, or accessing new tutorials.  Some key features of
        broadcasted notifications include: - They are not associated with a specific user, so
        they cannot be deleted or marked as read. - They can be scheduled to be displayed in the
        future or to expire after a certain time. - By default, broadcasted notifications are
        published immediately and expire six months after publication. - Only admins can create,
        edit, reschedule, or expire broadcasted notifications as needed.

        Args:
            run-as (NotificationsBroadcastBroadcastNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BroadcastNotificationCreateRequest)
                                     : Request body. (json)

        Returns:
            NotificationCreatedResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/broadcast"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BroadcastNotificationCreateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationCreatedResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_get_broadcasted(
        self,
        notification_id: str,
        run_as: NotificationsBroadcastGetBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationResponse:
        """
        Returns the information of a specific broadcasted notification.

        Only Admin users can access inactive notifications (scheduled or recently expired).

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsBroadcastGetBroadcastedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            BroadcastNotificationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/broadcast/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), BroadcastNotificationResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_get_broadcasted(
        self,
        notification_id: str,
        run_as: NotificationsBroadcastGetBroadcastedParamRunAs | None = None,
    ) -> BroadcastNotificationResponse:
        """
        Returns the information of a specific broadcasted notification.

        Only Admin users can access inactive notifications (scheduled or recently expired).

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsBroadcastGetBroadcastedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            BroadcastNotificationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/broadcast/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), BroadcastNotificationResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_update_broadcasted_notification(
        self,
        notification_id: str,
        body: NotificationBroadcastUpdateRequest,
        run_as: NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None = None,
    ) -> None:
        """
        Updates the state of a broadcasted notification.

        Only Admins can update broadcasted notifications. This is useful to reschedule, edit or
        expire broadcasted notifications.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationBroadcastUpdateRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/broadcast/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationBroadcastUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_broadcast_update_broadcasted_notification(
        self,
        notification_id: str,
        body: NotificationBroadcastUpdateRequest,
        run_as: NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None = None,
    ) -> None:
        """
        Updates the state of a broadcasted notification.

        Only Admins can update broadcasted notifications. This is useful to reschedule, edit or
        expire broadcasted notifications.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsBroadcastUpdateBroadcastedNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (NotificationBroadcastUpdateRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/broadcast/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: NotificationBroadcastUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_preferences_get_notification_preferences(
        self,
        run_as: NotificationsPreferencesGetNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Returns the current user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted
        notifications.  - The settings will contain all possible channels, but the client should
        only show the ones that are really supported by the server.   The supported channels are
        returned in the `supported-channels` header.

        Args:
            run-as (NotificationsPreferencesGetNotificationPreferencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationPreferences: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/preferences"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationPreferences)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_preferences_get_notification_preferences(
        self,
        run_as: NotificationsPreferencesGetNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Returns the current user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted
        notifications.  - The settings will contain all possible channels, but the client should
        only show the ones that are really supported by the server.   The supported channels are
        returned in the `supported-channels` header.

        Args:
            run-as (NotificationsPreferencesGetNotificationPreferencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationPreferences: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/preferences"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationPreferences)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_preferences_update_notification_preferences(
        self,
        body: UpdateUserNotificationPreferencesRequest,
        run_as: NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Updates the user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted
        notifications.  - Can be used to completely enable/disable notifications for a
        particular type (category) or to enable/disable a particular channel on each category.

        Args:
            run-as (NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateUserNotificationPreferencesRequest)
                                     : Request body. (json)

        Returns:
            UserNotificationPreferences: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/preferences"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateUserNotificationPreferencesRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationPreferences)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_preferences_update_notification_preferences(
        self,
        body: UpdateUserNotificationPreferencesRequest,
        run_as: NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None = None,
    ) -> UserNotificationPreferences:
        """
        Updates the user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted
        notifications.  - Can be used to completely enable/disable notifications for a
        particular type (category) or to enable/disable a particular channel on each category.

        Args:
            run-as (NotificationsPreferencesUpdateNotificationPreferencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateUserNotificationPreferencesRequest)
                                     : Request body. (json)

        Returns:
            UserNotificationPreferences: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/preferences"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateUserNotificationPreferencesRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationPreferences)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_status_get_notifications_status(
        self,
        since: datetime,
        run_as: NotificationsStatusGetNotificationsStatusParamRunAs | None = None,
    ) -> NotificationStatusSummary:
        """
        Returns the current status summary of the user's notifications since a particular date.

        Anonymous users cannot receive personal notifications, only broadcasted notifications.

        Args:
            since (datetime)         :
            run-as (NotificationsStatusGetNotificationsStatusParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            NotificationStatusSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/status"

        params: dict[str, Any] = {
            "since": DataclassSerializer.serialize(since),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationStatusSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_status_get_notifications_status(
        self,
        since: datetime,
        run_as: NotificationsStatusGetNotificationsStatusParamRunAs | None = None,
    ) -> NotificationStatusSummary:
        """
        Returns the current status summary of the user's notifications since a particular date.

        Anonymous users cannot receive personal notifications, only broadcasted notifications.

        Args:
            since (datetime)         :
            run-as (NotificationsStatusGetNotificationsStatusParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            NotificationStatusSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/notifications/status"

        params: dict[str, Any] = {
            "since": DataclassSerializer.serialize(since),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), NotificationStatusSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_delete_user_notification(
        self,
        notification_id: str,
        run_as: NotificationsDeleteUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Deletes a notification received by the user.

        When a notification is deleted, it is not immediately removed from the database, but
        marked as deleted.  - It will not be returned in the list of notifications, but admins
        can still access it as long as it is not expired. - It will be eventually removed from
        the database by a background task after the expiration time. - Deleted notifications
        will be permanently deleted when the expiration time is reached.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsDeleteUserNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

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

    async def notifications_delete_user_notification(
        self,
        notification_id: str,
        run_as: NotificationsDeleteUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Deletes a notification received by the user.

        When a notification is deleted, it is not immediately removed from the database, but
        marked as deleted.  - It will not be returned in the list of notifications, but admins
        can still access it as long as it is not expired. - It will be eventually removed from
        the database by a background task after the expiration time. - Deleted notifications
        will be permanently deleted when the expiration time is reached.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsDeleteUserNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

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

    async def notifications_show_notification(
        self,
        notification_id: str,
        run_as: NotificationsShowNotificationParamRunAs | None = None,
    ) -> UserNotificationResponse:
        """
        Displays information about a notification received by the user.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsShowNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_show_notification(
        self,
        notification_id: str,
        run_as: NotificationsShowNotificationParamRunAs | None = None,
    ) -> UserNotificationResponse:
        """
        Displays information about a notification received by the user.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsShowNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            UserNotificationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), UserNotificationResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_update_user_notification(
        self,
        notification_id: str,
        body: UserNotificationUpdateRequest,
        run_as: NotificationsUpdateUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Updates the state of a notification received by the user.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsUpdateUserNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserNotificationUpdateRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserNotificationUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def notifications_update_user_notification(
        self,
        notification_id: str,
        body: UserNotificationUpdateRequest,
        run_as: NotificationsUpdateUserNotificationParamRunAs | None = None,
    ) -> None:
        """
        Updates the state of a notification received by the user.

        Args:
            notification_id (str)    : The ID of the Notification.
            run-as (NotificationsUpdateUserNotificationParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UserNotificationUpdateRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        notification_id = DataclassSerializer.serialize(notification_id)

        url = f"{self.base_url}/api/notifications/{notification_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UserNotificationUpdateRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
