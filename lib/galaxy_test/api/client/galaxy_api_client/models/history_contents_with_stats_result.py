from dataclasses import dataclass

from .contents import Contents
from .history_content_stats import HistoryContentStats

__all__ = ["HistoryContentsWithStatsResult"]


@dataclass
class HistoryContentsWithStatsResult:
    """
    Includes stats with items counting

    Args:
        contents (Optional[Contents])
                                 : The items matching the search query. Only the items
                                   fitting in the current page limit will be returned.
        stats (HistoryContentStats)
                                 :
    """

    contents: (
        Contents | None
    )  # The items matching the search query. Only the items fitting in the current page limit will be returned.
    stats: HistoryContentStats
