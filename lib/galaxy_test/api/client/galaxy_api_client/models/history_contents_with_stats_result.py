from dataclasses import dataclass

from .history_content_stats import HistoryContentStats
from .history_contents_with_stats_result_contents import HistoryContentsWithStatsResultContents

__all__ = ["HistoryContentsWithStatsResult"]


@dataclass
class HistoryContentsWithStatsResult:
    """
    Includes stats with items counting

    Args:
        contents (HistoryContentsWithStatsResultContents)
                                 : The items matching the search query. Only the items
                                   fitting in the current page limit will be returned.
        stats (HistoryContentStats)
                                 :
    """

    contents: HistoryContentsWithStatsResultContents  # The items matching the search query. Only the items fitting in the current page limit will be returned.
    stats: HistoryContentStats

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "contents": "contents",
            "stats": "stats",
        }
        key_transform_with_dump = {
            "contents": "contents",
            "stats": "stats",
        }
