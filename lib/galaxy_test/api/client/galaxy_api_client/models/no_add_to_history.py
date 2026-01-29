from typing import TypeAlias

__all__ = ["NoAddToHistory"]

NoAddToHistory: TypeAlias = bool | None
"""Alias for Indicates if the workflow invocation should not be added to the history."""
