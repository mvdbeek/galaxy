from typing import Any, TypeAlias

__all__ = ["SourceMetadata"]

SourceMetadata: TypeAlias = dict[str, Any] | None
"""Alias for The source metadata of the workflow."""
