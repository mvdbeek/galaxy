from dataclasses import dataclass

from .chat_response_error_code import ChatResponseErrorCode
from .chat_response_error_message import ChatResponseErrorMessage

__all__ = ["ChatResponse"]


@dataclass
class ChatResponse:
    """
    ChatResponse dataclass

    Args:
        error_code (ChatResponseErrorCode)
                                 : The error code, if any, for the chat query.
        error_message (ChatResponseErrorMessage)
                                 : The error message, if any, for the chat query.
        response (str)           : The response to the chat query.
    """

    error_code: ChatResponseErrorCode  # The error code, if any, for the chat query.
    error_message: ChatResponseErrorMessage  # The error message, if any, for the chat query.
    response: str  # The response to the chat query.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "error_code": "error_code",
            "error_message": "error_message",
            "response": "response",
        }
        key_transform_with_dump = {
            "error_code": "error_code",
            "error_message": "error_message",
            "response": "response",
        }
