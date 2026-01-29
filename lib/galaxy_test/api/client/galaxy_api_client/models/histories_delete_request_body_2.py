from typing import TypeAlias

from .delete_history_payload import DeleteHistoryPayload

__all__ = ["HistoriesDeleteRequestBody2"]

HistoriesDeleteRequestBody2: TypeAlias = DeleteHistoryPayload | None
