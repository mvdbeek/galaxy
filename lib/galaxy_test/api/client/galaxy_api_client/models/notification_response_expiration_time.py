from datetime import datetime
from typing import TypeAlias

__all__ = ["NotificationResponseExpirationTime"]

NotificationResponseExpirationTime: TypeAlias = datetime | None
"""Alias for The time when the notification will expire. If not set, the notification will never expire. Expired notifications will be permanently deleted."""
