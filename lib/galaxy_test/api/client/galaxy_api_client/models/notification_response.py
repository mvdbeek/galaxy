from dataclasses import dataclass
from datetime import datetime

from .notification_response_category import NotificationResponseCategory
from .notification_response_content import NotificationResponseContent
from .notification_response_expiration_time import NotificationResponseExpirationTime
from .notification_variant import NotificationVariant

__all__ = ["NotificationResponse"]


@dataclass
class NotificationResponse:
    """
    Basic common fields for all notification responses.

    Args:
        category (NotificationResponseCategory)
                                 : The category of the notification. Represents the type of
                                   the notification. E.g. 'message' or 'new_shared_item'.
        content (NotificationResponseContent)
                                 : The content of the notification. The structure depends on
                                   the category.
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
        expiration_time (NotificationResponseExpirationTime | None)
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
    """

    category: NotificationResponseCategory  # The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'.
    content: NotificationResponseContent  # The content of the notification. The structure depends on the category.
    create_time: datetime  # The time when the notification was created.
    id_: str  # The encoded ID of the notification. (maps from 'id')
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: NotificationResponseExpirationTime | None = (
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
