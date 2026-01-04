from dataclasses import dataclass

from .broadcast_notification_content import BroadcastNotificationContent
from .expiration_time import ExpirationTime
from .notification_variant import NotificationVariant
from .publication_time import PublicationTime

__all__ = ["BroadcastNotificationCreateRequest"]


@dataclass
class BroadcastNotificationCreateRequest:
    """
    A notification create request specific for broadcasting.

    Args:
        content (BroadcastNotificationContent)
                                 :
        source (str)             : The source of the notification. Represents the agent that
                                   created the notification. E.g. 'galaxy' or 'admin'.
        variant (NotificationVariant)
                                 : The notification variant communicates the intent or
                                   relevance of the notification.
        category (Optional[str]) :
        expiration_time (Optional[ExpirationTime])
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
        publication_time (Optional[PublicationTime])
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
    """

    content: BroadcastNotificationContent
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    category: str | None = "broadcast"
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
    publication_time: PublicationTime | None = (
        None  # The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.
    )
