from typing import TypeAlias

from .delete_history_payload import DeleteHistoryPayload

__all__ = ["HistoriesDeleteRequestBody"]

HistoriesDeleteRequestBody: TypeAlias = DeleteHistoryPayload | None
