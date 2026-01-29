from dataclasses import dataclass

from .notification_channel_settings import NotificationChannelSettings

__all__ = ["NotificationCategorySettings"]


@dataclass
class NotificationCategorySettings:
    """
    The settings for a notification category.

    Args:
        channels (Optional[NotificationChannelSettings])
                                 : The settings for each channel of a notification category.
        enabled (Optional[bool]) : Whether the user wants to receive notifications for this
                                   category.
    """

    channels: NotificationChannelSettings | None = None  # The settings for each channel of a notification category.
    enabled: bool | None = True  # Whether the user wants to receive notifications for this category.
