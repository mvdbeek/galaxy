from dataclasses import dataclass

__all__ = ["NotificationChannelSettings"]


@dataclass
class NotificationChannelSettings:
    """
    The settings for each channel of a notification category.

    Args:
        email_ (Optional[bool])  : Whether the user wants to receive email notifications for
                                   this category. This setting will be ignored unless the
                                   server supports asynchronous tasks.
        push (Optional[bool])    : Whether the user wants to receive push notifications in
                                   the browser for this category.
    """

    email_: bool | None = (
        True  # Whether the user wants to receive email notifications for this category. This setting will be ignored unless the server supports asynchronous tasks.
    )
    push: bool | None = True  # Whether the user wants to receive push notifications in the browser for this category.
