from dataclasses import dataclass
from datetime import datetime

from .broadcast_notification_content import BroadcastNotificationContent
from .broadcast_notification_response_expiration_time import BroadcastNotificationResponseExpirationTime
from .notification_variant import NotificationVariant

__all__ = ["BroadcastNotificationResponse"]


@dataclass
class BroadcastNotificationResponse:
    """
    A notification response specific for broadcasting.

    Args:
        content (BroadcastNotificationContent)
                                 :
        create_time (datetime)   : The time when the notification was created.
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
        category (str | None)    :
        expiration_time (BroadcastNotificationResponseExpirationTime | None)
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
    """

    content: BroadcastNotificationContent
    create_time: datetime  # The time when the notification was created.
    id_: str  # The encoded ID of the notification. (maps from 'id')
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    category: str | None = "broadcast"
    expiration_time: BroadcastNotificationResponseExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "category": "category",
            "content": "content",
            "create_time": "create_time",
            "expiration_time": "expiration_time",
            "id": "id_",
            "publication_time": "publication_time",
            "source": "source",
            "update_time": "update_time",
            "variant": "variant",
        }
        key_transform_with_dump = {
            "category": "category",
            "content": "content",
            "create_time": "create_time",
            "expiration_time": "expiration_time",
            "id_": "id",
            "publication_time": "publication_time",
            "source": "source",
            "update_time": "update_time",
            "variant": "variant",
        }
