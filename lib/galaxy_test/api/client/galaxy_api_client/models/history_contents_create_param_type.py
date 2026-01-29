from typing import TypeAlias

from .history_content_type import HistoryContentType

__all__ = ["HistoryContentsCreateParamType"]

HistoryContentsCreateParamType: TypeAlias = HistoryContentType | None
"""Alias for The type of the target history element."""
