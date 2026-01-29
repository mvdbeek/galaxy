from dataclasses import dataclass

from .notification_channel_settings import NotificationChannelSettings

__all__ = ["NotificationCategorySettings"]


@dataclass
class NotificationCategorySettings:
    """
    The settings for a notification category.

    Args:
        channels (NotificationChannelSettings | None)
                                 : The settings for each channel of a notification category.
        enabled (bool | None)    : Whether the user wants to receive notifications for this
                                   category.
    """

    channels: NotificationChannelSettings | None = None  # The settings for each channel of a notification category.
    enabled: bool | None = True  # Whether the user wants to receive notifications for this category.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "channels": "channels",
            "enabled": "enabled",
        }
        key_transform_with_dump = {
            "channels": "channels",
            "enabled": "enabled",
        }
