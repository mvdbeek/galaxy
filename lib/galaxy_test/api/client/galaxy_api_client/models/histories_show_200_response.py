from typing import TypeAlias

from .custom_history_view import CustomHistoryView
from .history_detailed import HistoryDetailed
from .history_summary import HistorySummary

__all__ = ["HistoriesShow200Response"]

HistoriesShow200Response: TypeAlias = CustomHistoryView | HistoryDetailed | HistorySummary
