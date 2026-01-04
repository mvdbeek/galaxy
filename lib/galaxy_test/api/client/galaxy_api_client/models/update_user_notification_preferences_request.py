from dataclasses import dataclass

from .update_user_notification_preferences_request_preferences import (
    UpdateUserNotificationPreferencesRequestPreferences,
)

__all__ = ["UpdateUserNotificationPreferencesRequest"]


@dataclass
class UpdateUserNotificationPreferencesRequest:
    """
    Contains the new notification preferences of a user.

    Args:
        preferences (UpdateUserNotificationPreferencesRequestPreferences)
                                 : The new notification preferences of the user.
    """

    preferences: UpdateUserNotificationPreferencesRequestPreferences  # The new notification preferences of the user.
