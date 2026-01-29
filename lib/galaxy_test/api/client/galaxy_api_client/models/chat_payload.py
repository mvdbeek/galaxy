from dataclasses import dataclass

from .context import Context
from .exchange_id import ExchangeId

__all__ = ["ChatPayload"]


@dataclass
class ChatPayload:
    """
    ChatPayload dataclass.

    Args:
        query (str)              : The query to be sent to the chatbot.
        context (Optional[Context])
                                 : The context for the chatbot.
        exchange_id (Optional[ExchangeId])
                                 : The ID of an existing chat exchange to continue.
    """

    query: str  # The query to be sent to the chatbot.
    context: Context | None = ""  # The context for the chatbot.
    exchange_id: ExchangeId | None = None  # The ID of an existing chat exchange to continue.
