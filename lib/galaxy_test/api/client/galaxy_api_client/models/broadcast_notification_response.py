from dataclasses import dataclass
from datetime import datetime

from .broadcast_notification_content import BroadcastNotificationContent
from .expiration_time import ExpirationTime
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
        id_ (str)                : The encoded ID of the notification.
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
        category (Optional[str]) :
        expiration_time (Optional[ExpirationTime])
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
    """

    content: BroadcastNotificationContent
    create_time: datetime  # The time when the notification was created.
    id_: str  # The encoded ID of the notification.
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    category: str | None = "broadcast"
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
