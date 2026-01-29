from typing import TypeAlias

from .user_notification_response import UserNotificationResponse

__all__ = ["UserNotificationListResponse"]

UserNotificationListResponse: TypeAlias = list[UserNotificationResponse]
"""Alias for A list of user notifications."""
