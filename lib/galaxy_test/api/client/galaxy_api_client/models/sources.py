from typing import TypeAlias

from .sources_item import SourcesItem

__all__ = ["Sources"]

Sources: TypeAlias = list[SourcesItem]
"""Alias for The file sources associated with the supplied dataset instance."""
