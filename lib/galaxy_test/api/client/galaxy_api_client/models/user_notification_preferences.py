from dataclasses import dataclass

from .user_notification_preferences_preferences import UserNotificationPreferencesPreferences

__all__ = ["UserNotificationPreferences"]


@dataclass
class UserNotificationPreferences:
    """
    Contains the full notification preferences of a user.

    Args:
        preferences (UserNotificationPreferencesPreferences)
                                 : The notification preferences of the user.
    """

    preferences: UserNotificationPreferencesPreferences  # The notification preferences of the user.
