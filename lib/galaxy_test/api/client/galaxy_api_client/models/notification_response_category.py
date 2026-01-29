from typing import TypeAlias

from .mandatory_notification_category import MandatoryNotificationCategory
from .personal_notification_category import PersonalNotificationCategory

__all__ = ["NotificationResponseCategory"]

NotificationResponseCategory: TypeAlias = MandatoryNotificationCategory | PersonalNotificationCategory
"""Alias for The category of the notification. Represents the type of the notification. E.g. 'message' or 'new_shared_item'."""
