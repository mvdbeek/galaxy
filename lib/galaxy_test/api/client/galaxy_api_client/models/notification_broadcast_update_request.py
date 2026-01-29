from dataclasses import dataclass

from .notification_broadcast_update_request_content import NotificationBroadcastUpdateRequestContent
from .notification_broadcast_update_request_expiration_time import NotificationBroadcastUpdateRequestExpirationTime
from .notification_broadcast_update_request_publication_time import NotificationBroadcastUpdateRequestPublicationTime
from .notification_broadcast_update_request_source import NotificationBroadcastUpdateRequestSource
from .notification_broadcast_update_request_variant import NotificationBroadcastUpdateRequestVariant

__all__ = ["NotificationBroadcastUpdateRequest"]


@dataclass
class NotificationBroadcastUpdateRequest:
    """
    A notification update request specific for broadcasting.

    Args:
        content (NotificationBroadcastUpdateRequestContent | None)
                                 : The content of the broadcast notification. Broadcast
                                   notifications are displayed prominently to all users and
                                   can contain action links to redirect the user to a
                                   specific page.
        expiration_time (NotificationBroadcastUpdateRequestExpirationTime | None)
                                 : The time when the notification should expire. By default
                                   it will expire after 6 months. Expired notifications will
                                   be permanently deleted.
        publication_time (NotificationBroadcastUpdateRequestPublicationTime | None)
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
        source (NotificationBroadcastUpdateRequestSource | None)
                                 : The source of the notification. Represents the agent that
                                   created the notification.
        variant (NotificationBroadcastUpdateRequestVariant | None)
                                 : The variant of the notification. Used to express the
                                   importance of the notification.
    """

    content: NotificationBroadcastUpdateRequestContent | None = (
        None  # The content of the broadcast notification. Broadcast notifications are displayed prominently to all users and can contain action links to redirect the user to a specific page.
    )
    expiration_time: NotificationBroadcastUpdateRequestExpirationTime | None = (
        None  # The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.
    )
    publication_time: NotificationBroadcastUpdateRequestPublicationTime | None = (
        None  # The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.
    )
    source: NotificationBroadcastUpdateRequestSource | None = (
        None  # The source of the notification. Represents the agent that created the notification.
    )
    variant: NotificationBroadcastUpdateRequestVariant | None = (
        None  # The variant of the notification. Used to express the importance of the notification.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "expiration_time": "expiration_time",
            "publication_time": "publication_time",
            "source": "source",
            "variant": "variant",
        }
        key_transform_with_dump = {
            "content": "content",
            "expiration_time": "expiration_time",
            "publication_time": "publication_time",
            "source": "source",
            "variant": "variant",
        }
