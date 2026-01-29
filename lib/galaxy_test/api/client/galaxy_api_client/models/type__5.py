from typing import TypeAlias

from .history_content_type import HistoryContentType

__all__ = ["Type5"]

Type5: TypeAlias = HistoryContentType | None
"""Alias for The type of content to be created in the history."""
