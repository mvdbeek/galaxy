from dataclasses import dataclass

from .history_content_type import HistoryContentType

__all__ = ["UpdateContentItem"]


@dataclass
class UpdateContentItem:
    """
    Used for updating a particular history item. All fields are optional.

    Args:
        history_content_type (HistoryContentType)
                                 : This is always `dataset_collection` for dataset
                                   collections.
        id_ (str)                :
    """

    history_content_type: HistoryContentType  # This is always `dataset_collection` for dataset collections.
    id_: str
