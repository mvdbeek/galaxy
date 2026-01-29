from typing import TypeAlias

from .custom_history_view import CustomHistoryView
from .history_detailed import HistoryDetailed
from .history_summary import HistorySummary
from .job_import_history_response import JobImportHistoryResponse

__all__ = ["HistoriesCreate200Response2"]

HistoriesCreate200Response2: TypeAlias = CustomHistoryView | HistoryDetailed | HistorySummary | JobImportHistoryResponse
