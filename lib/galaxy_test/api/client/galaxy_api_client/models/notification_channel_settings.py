from dataclasses import dataclass

__all__ = ["NotificationChannelSettings"]


@dataclass
class NotificationChannelSettings:
    """
    The settings for each channel of a notification category.

    Args:
        email_ (bool | None)     : Whether the user wants to receive email notifications for
                                   this category. This setting will be ignored unless the
                                   server supports asynchronous tasks. (maps from 'email')
        push (bool | None)       : Whether the user wants to receive push notifications in
                                   the browser for this category.
    """

    email_: bool | None = (
        True  # Whether the user wants to receive email notifications for this category. This setting will be ignored unless the server supports asynchronous tasks. (maps from 'email')
    )
    push: bool | None = True  # Whether the user wants to receive push notifications in the browser for this category.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "push": "push",
        }
        key_transform_with_dump = {
            "email_": "email",
            "push": "push",
        }
