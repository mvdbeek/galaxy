from typing import TypeAlias

from .custom_history_view import CustomHistoryView
from .history_detailed import HistoryDetailed
from .history_summary import HistorySummary

__all__ = ["HistoriesArchiveRestoreRestoreArchivedHistory200Response2"]

HistoriesArchiveRestoreRestoreArchivedHistory200Response2: TypeAlias = (
    CustomHistoryView | HistoryDetailed | HistorySummary
)
