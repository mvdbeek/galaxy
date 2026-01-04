from dataclasses import dataclass
from datetime import datetime

from .category import Category
from .content import Content
from .expiration_time import ExpirationTime
from .notification_variant import NotificationVariant

__all__ = ["NotificationResponse"]


@dataclass
class NotificationResponse:
    """
    Basic common fields for all notification responses.

    Args:
        category (Category)      : The category of the notification. Represents the type of
                                   the notification. E.g. 'message' or 'new_shared_item'.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
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
        expiration_time (Optional[ExpirationTime])
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
    """

    category: Category  # The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'.
    content: (
        Content | None
    )  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    create_time: datetime  # The time when the notification was created.
    id_: str  # The encoded ID of the notification.
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
