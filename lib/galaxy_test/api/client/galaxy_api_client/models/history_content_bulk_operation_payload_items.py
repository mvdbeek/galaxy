from typing import TypeAlias

from .history_content_item import HistoryContentItem

__all__ = ["HistoryContentBulkOperationPayloadItems"]

HistoryContentBulkOperationPayloadItems: TypeAlias = list[HistoryContentItem] | None
