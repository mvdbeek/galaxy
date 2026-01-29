from typing import TypeAlias

__all__ = ["Purge"]

Purge: TypeAlias = bool | None
"""Alias for Whether to permanently delete from disk the specified datasets. *Warning*: this is a destructive operation."""
