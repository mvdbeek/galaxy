from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .message_notification_content import MessageNotificationContent
from .new_shared_item_notification_content import NewSharedItemNotificationContent

__all__ = ["UserNotificationResponseContent", "UserNotificationResponseContentDiscriminator"]


@dataclass(frozen=True)
class UserNotificationResponseContentDiscriminator:
    """Discriminator metadata for UserNotificationResponseContent union."""

    property_name: str = "category"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("message", "MessageNotificationContent"),
        ("new_shared_item", "NewSharedItemNotificationContent"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .message_notification_content import MessageNotificationContent
        from .new_shared_item_notification_content import NewSharedItemNotificationContent

        return {
            "message": MessageNotificationContent,
            "new_shared_item": NewSharedItemNotificationContent,
        }


UserNotificationResponseContent: TypeAlias = Annotated[
    MessageNotificationContent | NewSharedItemNotificationContent, UserNotificationResponseContentDiscriminator()
]
"""Alias for The content of the notification. The structure depends on the category."""
