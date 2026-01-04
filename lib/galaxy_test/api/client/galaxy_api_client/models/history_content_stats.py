from dataclasses import dataclass

__all__ = ["HistoryContentStats"]


@dataclass
class HistoryContentStats:
    """
    HistoryContentStats dataclass.

    Args:
        total_matches (int)      : The total number of items that match the search query
                                   without any pagination
    """

    total_matches: int  # The total number of items that match the search query without any pagination
