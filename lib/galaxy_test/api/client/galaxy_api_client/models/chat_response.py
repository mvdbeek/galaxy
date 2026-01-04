from dataclasses import dataclass

from .error_code import ErrorCode
from .error_message import ErrorMessage

__all__ = ["ChatResponse"]


@dataclass
class ChatResponse:
    """
    ChatResponse dataclass.

    Args:
        error_code (Optional[ErrorCode])
                                 : The error code, if any, for the chat query.
        error_message (Optional[ErrorMessage])
                                 : The error message, if any, for the chat query.
        response (str)           : The response to the chat query.
    """

    error_code: ErrorCode | None  # The error code, if any, for the chat query.
    error_message: ErrorMessage | None  # The error message, if any, for the chat query.
    response: str  # The response to the chat query.
