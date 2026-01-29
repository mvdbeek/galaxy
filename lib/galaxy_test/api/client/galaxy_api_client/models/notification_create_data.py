from dataclasses import dataclass

from .notification_create_data_category import NotificationCreateDataCategory
from .notification_create_data_content import NotificationCreateDataContent
from .notification_create_data_expiration_time import NotificationCreateDataExpirationTime
from .notification_create_data_publication_time import NotificationCreateDataPublicationTime
from .notification_variant import NotificationVariant

__all__ = ["NotificationCreateData"]


@dataclass
class NotificationCreateData:
    """
    Basic common fields for all notification create requests.

    Args:
        category (NotificationCreateDataCategory)
                                 : The category of the notification. Represents the type of
                                   the notification. E.g. 'message' or 'new_shared_item'.
        content (NotificationCreateDataContent)
                                 : The content of the notification. The structure depends on
                                   the category.
        source (str)             : The source of the notification. Represents the agent that
                                   created the notification. E.g. 'galaxy' or 'admin'.
        variant (NotificationVariant)
                                 : The notification variant communicates the intent or
                                   relevance of the notification.
        expiration_time (NotificationCreateDataExpirationTime | None)
                                 : The time when the notification should expire. By default
                                   it will expire after 6 months. Expired notifications will
                                   be permanently deleted.
        publication_time (NotificationCreateDataPublicationTime | None)
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
    """

    category: NotificationCreateDataCategory  # The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'.
    content: NotificationCreateDataContent  # The content of the notification. The structure depends on the category.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: NotificationCreateDataExpirationTime | None = (
        None  # The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted.
    )
    publication_time: NotificationCreateDataPublicationTime | None = (
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
