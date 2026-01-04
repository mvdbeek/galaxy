from dataclasses import dataclass

from .message import Message

__all__ = ["DeleteJobPayload"]


@dataclass
class DeleteJobPayload:
    """
    DeleteJobPayload dataclass.

    Args:
        message (Optional[Message])
                                 : The optional message sent with the error report.
    """

    message: Message | None = None  # The optional message sent with the error report.
