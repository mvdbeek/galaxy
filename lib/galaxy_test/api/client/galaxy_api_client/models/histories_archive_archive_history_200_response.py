from typing import TypeAlias

from .archived_history_detailed import ArchivedHistoryDetailed
from .archived_history_summary import ArchivedHistorySummary
from .custom_archived_history_view import CustomArchivedHistoryView

__all__ = ["HistoriesArchiveArchiveHistory200Response"]

HistoriesArchiveArchiveHistory200Response: TypeAlias = (
    CustomArchivedHistoryView | ArchivedHistoryDetailed | ArchivedHistorySummary
)
