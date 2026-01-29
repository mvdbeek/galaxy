from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .broadcast_notification_content import BroadcastNotificationContent
from .message_notification_content import MessageNotificationContent
from .new_shared_item_notification_content import NewSharedItemNotificationContent

__all__ = ["NotificationResponseContent", "NotificationResponseContentDiscriminator"]


@dataclass(frozen=True)
class NotificationResponseContentDiscriminator:
    """Discriminator metadata for NotificationResponseContent union."""

    property_name: str = "category"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("broadcast", "BroadcastNotificationContent"),
        ("message", "MessageNotificationContent"),
        ("new_shared_item", "NewSharedItemNotificationContent"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .broadcast_notification_content import BroadcastNotificationContent
        from .message_notification_content import MessageNotificationContent
        from .new_shared_item_notification_content import NewSharedItemNotificationContent

        return {
            "broadcast": BroadcastNotificationContent,
            "message": MessageNotificationContent,
            "new_shared_item": NewSharedItemNotificationContent,
        }


NotificationResponseContent: TypeAlias = Annotated[
    MessageNotificationContent | NewSharedItemNotificationContent | BroadcastNotificationContent,
    NotificationResponseContentDiscriminator(),
]
"""Alias for The content of the notification. The structure depends on the category."""
