from dataclasses import dataclass

from .history_content_type import HistoryContentType

__all__ = ["HistoryContentItem"]


@dataclass
class HistoryContentItem:
    """
    HistoryContentItem dataclass

    Args:
        history_content_type (HistoryContentType)
                                 : Available types of History contents.
        id_ (str)                : Maps from 'id'
    """

    history_content_type: HistoryContentType  # Available types of History contents.
    id_: str  # Maps from 'id'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_content_type": "history_content_type",
            "id": "id_",
        }
        key_transform_with_dump = {
            "history_content_type": "history_content_type",
            "id_": "id",
        }
