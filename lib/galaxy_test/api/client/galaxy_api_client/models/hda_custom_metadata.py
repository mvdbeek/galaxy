from typing import Any, TypeAlias

__all__ = ["HdaCustomMetadata"]

HdaCustomMetadata: TypeAlias = dict[str, Any] | None
"""Alias for The metadata associated with this dataset."""
