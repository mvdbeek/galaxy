from dataclasses import dataclass

from .chat_payload_context import ChatPayloadContext
from .chat_payload_exchange_id import ChatPayloadExchangeId

__all__ = ["ChatPayload"]


@dataclass
class ChatPayload:
    """
    ChatPayload dataclass

    Args:
        query (str)              : The query to be sent to the chatbot.
        context (ChatPayloadContext | None)
                                 : The context for the chatbot.
        exchange_id (ChatPayloadExchangeId | None)
                                 : The ID of an existing chat exchange to continue.
    """

    query: str  # The query to be sent to the chatbot.
    context: ChatPayloadContext | None = ""  # The context for the chatbot.
    exchange_id: ChatPayloadExchangeId | None = None  # The ID of an existing chat exchange to continue.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "context": "context",
            "exchange_id": "exchange_id",
            "query": "query",
        }
        key_transform_with_dump = {
            "context": "context",
            "exchange_id": "exchange_id",
            "query": "query",
        }
