from typing import TypeAlias

from .history_active_content_counts import HistoryActiveContentCounts

__all__ = ["CustomArchivedHistoryViewContentsActive"]

CustomArchivedHistoryViewContentsActive: TypeAlias = HistoryActiveContentCounts | None
"""Alias for Contains the number of active, deleted or hidden items in a History."""
