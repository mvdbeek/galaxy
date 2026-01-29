from typing import TypeAlias

__all__ = ["UserNotificationUpdateRequestDeleted"]

UserNotificationUpdateRequestDeleted: TypeAlias = bool | None
"""Alias for Whether the notification should be marked as deleted by the user. If not set, the notification will not be changed."""
