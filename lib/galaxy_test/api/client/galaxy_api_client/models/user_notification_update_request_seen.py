from typing import TypeAlias

__all__ = ["UserNotificationUpdateRequestSeen"]

UserNotificationUpdateRequestSeen: TypeAlias = bool | None
"""Alias for Whether the notification should be marked as seen by the user. If not set, the notification will not be changed."""
