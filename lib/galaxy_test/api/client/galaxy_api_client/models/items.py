from typing import TypeAlias

from .history_content_item import HistoryContentItem

__all__ = ["Items"]

Items: TypeAlias = list[HistoryContentItem] | None
