from dataclasses import dataclass

from .check_for_updates_response_status import CheckForUpdatesResponseStatus

__all__ = ["CheckForUpdatesResponse"]


@dataclass
class CheckForUpdatesResponse:
    """
    CheckForUpdatesResponse dataclass

    Args:
        message (str)            : Unstructured description of tool shed updates discovered
                                   or failure
        status (CheckForUpdatesResponseStatus)
                                 : 'ok' or 'error'
    """

    message: str  # Unstructured description of tool shed updates discovered or failure
    status: CheckForUpdatesResponseStatus  # 'ok' or 'error'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
            "status": "status",
        }
        key_transform_with_dump = {
            "message": "message",
            "status": "status",
        }
