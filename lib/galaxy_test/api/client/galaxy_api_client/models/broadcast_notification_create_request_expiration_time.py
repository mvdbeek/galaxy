from datetime import datetime
from typing import TypeAlias

__all__ = ["BroadcastNotificationCreateRequestExpirationTime"]

BroadcastNotificationCreateRequestExpirationTime: TypeAlias = datetime | None
"""Alias for The time when the notification should expire. By default it will expire after 6 months. Expired notifications will be permanently deleted."""
