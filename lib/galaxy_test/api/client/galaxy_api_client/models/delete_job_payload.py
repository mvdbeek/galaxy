from dataclasses import dataclass

from .delete_job_payload_message import DeleteJobPayloadMessage

__all__ = ["DeleteJobPayload"]


@dataclass
class DeleteJobPayload:
    """
    DeleteJobPayload dataclass

    Args:
        message (DeleteJobPayloadMessage | None)
                                 : Stop message
    """

    message: DeleteJobPayloadMessage | None = None  # Stop message

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
        }
        key_transform_with_dump = {
            "message": "message",
        }
