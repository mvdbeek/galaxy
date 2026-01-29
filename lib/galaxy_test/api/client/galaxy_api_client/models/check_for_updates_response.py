from dataclasses import dataclass

from .status import Status

__all__ = ["CheckForUpdatesResponse"]


@dataclass
class CheckForUpdatesResponse:
    """
    CheckForUpdatesResponse dataclass.

    Args:
        message (str)            : Unstructured description of tool shed updates discovered
                                   or failure
        status (Status)          : 'ok' or 'error'
    """

    message: str  # Unstructured description of tool shed updates discovered or failure
    status: Status  # 'ok' or 'error'
