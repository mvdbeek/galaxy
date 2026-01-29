from dataclasses import dataclass

__all__ = ["HistoryContentStats"]


@dataclass
class HistoryContentStats:
    """
    HistoryContentStats dataclass

    Args:
        total_matches (int)      : The total number of items that match the search query
                                   without any pagination
    """

    total_matches: int  # The total number of items that match the search query without any pagination

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "total_matches": "total_matches",
        }
        key_transform_with_dump = {
            "total_matches": "total_matches",
        }
