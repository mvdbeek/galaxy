from datetime import datetime
from typing import TypeAlias

__all__ = ["UserNotificationResponseSeenTime"]

UserNotificationResponseSeenTime: TypeAlias = datetime | None
"""Alias for The time when the notification was seen by the user. If not set, the notification was not seen yet."""
