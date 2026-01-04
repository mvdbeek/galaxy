from dataclasses import dataclass

from .message import Message
from .source import Source
from .type_ import Type_

__all__ = ["BadgeDict"]


@dataclass
class BadgeDict:
    """
    BadgeDict dataclass.

    Args:
        message (Optional[Message])
                                 : The optional message sent with the error report.
        source (Source)          : The source of the notification. Represents the agent that
                                   created the notification.
        type_ (Type_)            : The type of content to be created in the history.
    """

    message: Message | None  # The optional message sent with the error report.
    source: Source  # The source of the notification. Represents the agent that created the notification.
    type_: Type_  # The type of content to be created in the history.
