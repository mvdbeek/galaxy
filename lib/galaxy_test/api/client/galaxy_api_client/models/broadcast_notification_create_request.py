from dataclasses import dataclass

from .broadcast_notification_content import BroadcastNotificationContent
from .broadcast_notification_create_request_expiration_time import BroadcastNotificationCreateRequestExpirationTime
from .broadcast_notification_create_request_publication_time import BroadcastNotificationCreateRequestPublicationTime
from .notification_variant import NotificationVariant

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
        category (str | None)    :
        expiration_time (BroadcastNotificationCreateRequestExpirationTime | None)
                                 : The time when the notification should expire. By default
                                   it will expire after 6 months. Expired notifications will
                                   be permanently deleted.
        publication_time (BroadcastNotificationCreateRequestPublicationTime | None)
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
    """

    content: BroadcastNotificationContent
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    category: str | None = "broadcast"
    expiration_time: BroadcastNotificationCreateRequestExpirationTime | None = (
        None  # The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.
    )
    publication_time: BroadcastNotificationCreateRequestPublicationTime | None = (
        None  # The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "category": "category",
            "content": "content",
            "expiration_time": "expiration_time",
            "publication_time": "publication_time",
            "source": "source",
            "variant": "variant",
        }
        key_transform_with_dump = {
            "category": "category",
            "content": "content",
            "expiration_time": "expiration_time",
            "publication_time": "publication_time",
            "source": "source",
            "variant": "variant",
        }
