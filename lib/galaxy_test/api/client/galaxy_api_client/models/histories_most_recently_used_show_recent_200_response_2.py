from typing import TypeAlias

from .custom_history_view import CustomHistoryView
from .history_detailed import HistoryDetailed
from .history_summary import HistorySummary

__all__ = ["HistoriesMostRecentlyUsedShowRecent200Response2"]

HistoriesMostRecentlyUsedShowRecent200Response2: TypeAlias = CustomHistoryView | HistoryDetailed | HistorySummary
