from typing import TypeAlias

from .broadcast_notification_response import BroadcastNotificationResponse

__all__ = ["BroadcastNotificationListResponse"]

BroadcastNotificationListResponse: TypeAlias = list[BroadcastNotificationResponse]
"""Alias for A list of broadcast notifications."""
