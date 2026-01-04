from dataclasses import dataclass

from .content import Content
from .expiration_time import ExpirationTime
from .publication_time import PublicationTime
from .source import Source
from .variant import Variant

__all__ = ["NotificationBroadcastUpdateRequest"]


@dataclass
class NotificationBroadcastUpdateRequest:
    """
    A notification update request specific for broadcasting.

    Args:
        content (Optional[Content])
                                 : Text contents of the last page revision with embedded
                                   directives expanded (type dependent on content_format).
        expiration_time (Optional[ExpirationTime])
                                 : The time when the notification will expire. If not set,
                                   the notification will never expire. Expired notifications
                                   will be permanently deleted.
        publication_time (Optional[PublicationTime])
                                 : The time when the notification should be published.
                                   Notifications can be created and then scheduled to be
                                   published at a later time.
        source (Optional[Source]): The source of the notification. Represents the agent that
                                   created the notification.
        variant (Optional[Variant])
                                 : The variant of the notification. Used to express the
                                   importance of the notification.
    """

    content: Content | None = (
        ""  # Text contents of the last page revision with embedded directives expanded (type dependent on content_format).
    )
    expiration_time: ExpirationTime | None = (
        None  # The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted.
    )
    publication_time: PublicationTime | None = (
        None  # The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time.
    )
    source: Source | None = None  # The source of the notification. Represents the agent that created the notification.
    variant: Variant | None = (
        None  # The variant of the notification. Used to express the importance of the notification.
    )
