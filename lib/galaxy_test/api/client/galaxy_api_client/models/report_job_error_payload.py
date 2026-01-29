from dataclasses import dataclass

from .email__4 import Email4
from .report_job_error_payload_message import ReportJobErrorPayloadMessage

__all__ = ["ReportJobErrorPayload"]


@dataclass
class ReportJobErrorPayload:
    """
    ReportJobErrorPayload dataclass

    Args:
        dataset_id (str)         : The History Dataset Association ID related to the error.
        email_ (Email4 | None)   : Email address for communication with the user. Only
                                   required for anonymous users. (maps from 'email')
        message (ReportJobErrorPayloadMessage | None)
                                 : The optional message sent with the error report.
    """

    dataset_id: str  # The History Dataset Association ID related to the error.
    email_: Email4 | None = (
        None  # Email address for communication with the user. Only required for anonymous users. (maps from 'email')
    )
    message: ReportJobErrorPayloadMessage | None = None  # The optional message sent with the error report.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dataset_id": "dataset_id",
            "email": "email_",
            "message": "message",
        }
        key_transform_with_dump = {
            "dataset_id": "dataset_id",
            "email_": "email",
            "message": "message",
        }
