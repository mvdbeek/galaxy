from typing import Any, TypeAlias

__all__ = ["Context"]

Context: TypeAlias = dict[str, Any] | None
"""Alias for The context for the chatbot."""
