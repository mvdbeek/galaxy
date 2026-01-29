from typing import Any, TypeAlias

__all__ = ["DsMap"]

DsMap: TypeAlias = dict[str, Any] | None
"""Alias for An older alternative to specifying inputs using database IDs, do not use this and use inputs instead"""
