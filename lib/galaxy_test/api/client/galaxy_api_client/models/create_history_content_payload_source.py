from typing import TypeAlias

from .history_content_source import HistoryContentSource

__all__ = ["CreateHistoryContentPayloadSource"]

CreateHistoryContentPayloadSource: TypeAlias = HistoryContentSource | None
"""Alias for The source of the content. Can be other history element to be copied or library elements."""
