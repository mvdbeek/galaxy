from dataclasses import dataclass

from .history_ids import HistoryIds

__all__ = ["CopyDatasetsResponse"]


@dataclass
class CopyDatasetsResponse:
    """
    CopyDatasetsResponse dataclass.

    Args:
        history_ids (HistoryIds) :
    """

    history_ids: HistoryIds
