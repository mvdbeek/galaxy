from dataclasses import dataclass

__all__ = ["MessageNotificationContent"]


@dataclass
class MessageNotificationContent:
    """
    MessageNotificationContent dataclass.

    Args:
        message (str)            : The message of the notification (supports Markdown).
        subject (str)            : The subject of the notification.
        category (Optional[str]) :
    """

    message: str  # The message of the notification (supports Markdown).
    subject: str  # The subject of the notification.
    category: str | None = "message"
