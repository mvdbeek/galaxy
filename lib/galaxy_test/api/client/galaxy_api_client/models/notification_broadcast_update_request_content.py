from typing import TypeAlias

from .broadcast_notification_content import BroadcastNotificationContent

__all__ = ["NotificationBroadcastUpdateRequestContent"]

NotificationBroadcastUpdateRequestContent: TypeAlias = BroadcastNotificationContent | None
"""Alias for The content of the broadcast notification. Broadcast notifications are displayed prominently to all users and can contain action links to redirect the user to a specific page."""
