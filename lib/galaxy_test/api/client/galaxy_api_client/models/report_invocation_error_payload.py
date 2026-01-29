from dataclasses import dataclass

from .email_ import Email_
from .message import Message

__all__ = ["ReportInvocationErrorPayload"]


@dataclass
class ReportInvocationErrorPayload:
    """
    ReportInvocationErrorPayload dataclass.

    Args:
        invocation_id (str)      : The ID of the invocation related to the error.
        email_ (Optional[Email_]): Email address for communication with the user. Only
                                   required for anonymous users.
        message (Optional[Message])
                                 : The optional message sent with the error report.
    """

    invocation_id: str  # The ID of the invocation related to the error.
    email_: Email_ | None = None  # Email address for communication with the user. Only required for anonymous users.
    message: Message | None = None  # The optional message sent with the error report.
