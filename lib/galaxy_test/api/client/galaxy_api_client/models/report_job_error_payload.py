from dataclasses import dataclass

from .email_ import Email_
from .message import Message

__all__ = ["ReportJobErrorPayload"]


@dataclass
class ReportJobErrorPayload:
    """
    ReportJobErrorPayload dataclass.

    Args:
        dataset_id (str)         : The History Dataset Association ID related to the error.
        email_ (Optional[Email_]): Email address for communication with the user. Only
                                   required for anonymous users.
        message (Optional[Message])
                                 : The optional message sent with the error report.
    """

    dataset_id: str  # The History Dataset Association ID related to the error.
    email_: Email_ | None = None  # Email address for communication with the user. Only required for anonymous users.
    message: Message | None = None  # The optional message sent with the error report.
