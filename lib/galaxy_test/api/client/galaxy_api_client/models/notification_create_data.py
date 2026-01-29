from dataclasses import dataclass

from .category import Category
from .content import Content
from .expiration_time import ExpirationTime
from .notification_variant import NotificationVariant
from .publication_time import PublicationTime

__all__ = ["NotificationCreateData"]


@dataclass
class NotificationCreateData:
    """
    Basic common fields for all notification create requests.

    Args:
        category (Category)      : The category of the notification. Represents the type of
                                   the notification. E.g. 'message' or 'new_shared_item'.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        source (str)             : The source of the notification. Represents the agent that
                                   created the notification. E.g. 'galaxy' or 'admin'.
        variant (NotificationVariant)
                                 : The notification variant communicates the intent or
                                   relevance of the notification.
        expiration_time (Optional[ExpirationTime])
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
        publication_time (Optional[PublicationTime])
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
    """

    category: Category  # The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'.
    content: (
        Content | None
    )  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
    publication_time: PublicationTime | None = (
        None  # The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.
    )
