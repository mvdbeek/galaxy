from dataclasses import dataclass

from .history_content_type import HistoryContentType

__all__ = ["HistoryContentItem"]


@dataclass
class HistoryContentItem:
    """
    HistoryContentItem dataclass.

    Args:
        history_content_type (HistoryContentType)
                                 : This is always `dataset_collection` for dataset
                                   collections.
        id_ (str)                :
    """

    history_content_type: HistoryContentType  # This is always `dataset_collection` for dataset collections.
    id_: str
