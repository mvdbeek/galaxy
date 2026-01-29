from typing import TypeAlias

from .chat_payload import ChatPayload

__all__ = ["ChatQueryRequestBody"]

ChatQueryRequestBody: TypeAlias = ChatPayload | None
