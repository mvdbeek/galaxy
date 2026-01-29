from dataclasses import dataclass
from datetime import datetime

from .notification_variant import NotificationVariant
from .personal_notification_category import PersonalNotificationCategory
from .user_notification_response_content import UserNotificationResponseContent
from .user_notification_response_expiration_time import UserNotificationResponseExpirationTime
from .user_notification_response_seen_time import UserNotificationResponseSeenTime

__all__ = ["UserNotificationResponse"]


@dataclass
class UserNotificationResponse:
    """
    A notification response specific to the user.

    Args:
        category (PersonalNotificationCategory)
                                 : These notification categories can be opt-out by the user
                                   and will be displayed in the notification preferences.
        content (UserNotificationResponseContent)
                                 : The content of the notification. The structure depends on
                                   the category.
        create_time (datetime)   : The time when the notification was created.
        deleted (bool)           : Whether the notification is marked as deleted by the
                                   user. Deleted notifications don't show up in the
                                   notification list.
        id_ (str)                : The encoded ID of the notification. (maps from 'id')
        publication_time (datetime)
                                 : The time when the notification was published.
                                   Notifications can be created and then published at a
                                   later time.
        source (str)             : The source of the notification. Represents the agent that
                                   created the notification. E.g. 'galaxy' or 'admin'.
        update_time (datetime)   : The time when the notification was last updated.
        variant (NotificationVariant)
                                 : The notification variant communicates the intent or
                                   relevance of the notification.
        expiration_time (UserNotificationResponseExpirationTime | None)
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
        seen_time (UserNotificationResponseSeenTime | None)
                                 : The time when the notification was seen by the user. If
                                   not set, the notification was not seen yet.
    """

    category: PersonalNotificationCategory  # These notification categories can be opt-out by the user and will be displayed in the notification preferences.
    content: UserNotificationResponseContent  # The content of the notification. The structure depends on the category.
    create_time: datetime  # The time when the notification was created.
    deleted: bool  # Whether the notification is marked as deleted by the user. Deleted notifications don't show up in the notification list.
    id_: str  # The encoded ID of the notification. (maps from 'id')
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: UserNotificationResponseExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
    seen_time: UserNotificationResponseSeenTime | None = (
        None  # The time when the notification was seen by the user. If not set, the notification was not seen yet.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "category": "category",
            "content": "content",
            "create_time": "create_time",
            "deleted": "deleted",
            "expiration_time": "expiration_time",
            "id": "id_",
            "publication_time": "publication_time",
            "seen_time": "seen_time",
            "source": "source",
            "update_time": "update_time",
            "variant": "variant",
        }
        key_transform_with_dump = {
            "category": "category",
            "content": "content",
            "create_time": "create_time",
            "deleted": "deleted",
            "expiration_time": "expiration_time",
            "id_": "id",
            "publication_time": "publication_time",
            "seen_time": "seen_time",
            "source": "source",
            "update_time": "update_time",
            "variant": "variant",
        }
