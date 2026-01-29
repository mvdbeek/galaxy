from dataclasses import dataclass
from datetime import datetime

from .content import Content
from .expiration_time import ExpirationTime
from .notification_variant import NotificationVariant
from .personal_notification_category import PersonalNotificationCategory
from .seen_time import SeenTime

__all__ = ["UserNotificationResponse"]


@dataclass
class UserNotificationResponse:
    """
    A notification response specific to the user.

    Args:
        category (PersonalNotificationCategory)
                                 : These notification categories can be opt-out by the user
                                   and will be displayed in the notification preferences.
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        create_time (datetime)   : The time when the notification was created.
        deleted (bool)           : Whether the notification is marked as deleted by the
                                   user. Deleted notifications don't show up in the
                                   notification list.
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
        seen_time (Optional[SeenTime])
                                 : The time when the notification was seen by the user. If
                                   not set, the notification was not seen yet.
    """

    category: PersonalNotificationCategory  # These notification categories can be opt-out by the user and will be displayed in the notification preferences.
    content: (
        Content | None
    )  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    create_time: datetime  # The time when the notification was created.
    deleted: bool  # Whether the notification is marked as deleted by the user. Deleted notifications don't show up in the notification list.
    id_: str  # The encoded ID of the notification.
    publication_time: datetime  # The time when the notification was published. Notifications can be created and then published at a later time.
    source: str  # The source of the notification. Represents the agent that created the notification. E.g. 'galaxy' or 'admin'.
    update_time: datetime  # The time when the notification was last updated.
    variant: NotificationVariant  # The notification variant communicates the intent or relevance of the notification.
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
    seen_time: SeenTime | None = (
        None  # The time when the notification was seen by the user. If not set, the notification was not seen yet.
    )
