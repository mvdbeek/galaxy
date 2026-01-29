from dataclasses import dataclass

from .action_links import ActionLinks

__all__ = ["BroadcastNotificationContent"]


@dataclass
class BroadcastNotificationContent:
    """
    BroadcastNotificationContent dataclass.

    Args:
        message (str)            : The message of the notification (supports Markdown).
        subject (str)            : The subject of the notification.
        action_links (Optional[ActionLinks])
                                 : The optional action links (buttons) to be displayed in
                                   the notification.
        category (Optional[str]) :
    """

    message: str  # The message of the notification (supports Markdown).
    subject: str  # The subject of the notification.
    action_links: ActionLinks | None = None  # The optional action links (buttons) to be displayed in the notification.
    category: str | None = "broadcast"
