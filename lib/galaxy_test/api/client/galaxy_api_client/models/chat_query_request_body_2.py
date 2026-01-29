from typing import TypeAlias

from .chat_payload import ChatPayload

__all__ = ["ChatQueryRequestBody2"]

ChatQueryRequestBody2: TypeAlias = ChatPayload | None
