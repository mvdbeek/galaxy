from dataclasses import dataclass

from .email__3 import Email3
from .report_invocation_error_payload_message import ReportInvocationErrorPayloadMessage

__all__ = ["ReportInvocationErrorPayload"]


@dataclass
class ReportInvocationErrorPayload:
    """
    ReportInvocationErrorPayload dataclass

    Args:
        invocation_id (str)      : The ID of the invocation related to the error.
        email_ (Email3 | None)   : Email address for communication with the user. Only
                                   required for anonymous users. (maps from 'email')
        message (ReportInvocationErrorPayloadMessage | None)
                                 : The optional message sent with the error report.
    """

    invocation_id: str  # The ID of the invocation related to the error.
    email_: Email3 | None = (
        None  # Email address for communication with the user. Only required for anonymous users. (maps from 'email')
    )
    message: ReportInvocationErrorPayloadMessage | None = None  # The optional message sent with the error report.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "email": "email_",
            "invocation_id": "invocation_id",
            "message": "message",
        }
        key_transform_with_dump = {
            "email_": "email",
            "invocation_id": "invocation_id",
            "message": "message",
        }
