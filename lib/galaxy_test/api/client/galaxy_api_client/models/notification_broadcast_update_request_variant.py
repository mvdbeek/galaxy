from typing import TypeAlias

from .notification_variant import NotificationVariant

__all__ = ["NotificationBroadcastUpdateRequestVariant"]

NotificationBroadcastUpdateRequestVariant: TypeAlias = NotificationVariant | None
"""Alias for The variant of the notification. Used to express the importance of the notification."""
