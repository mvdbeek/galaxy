from typing import Any, TypeAlias

__all__ = ["Config3"]

Config3: TypeAlias = dict[str, Any] | bytes | None
"""Alias for The config of the visualization."""
