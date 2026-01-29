from typing import TypeAlias

__all__ = ["Accessible"]

Accessible: TypeAlias = bool | None
"""Alias for Whether this item is accessible to the current user due to permissions."""
