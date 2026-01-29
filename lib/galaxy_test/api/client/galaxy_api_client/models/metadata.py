from typing import Any, TypeAlias

__all__ = ["Metadata"]

Metadata: TypeAlias = dict[str, Any] | None
"""Alias for The metadata associated with this dataset."""
