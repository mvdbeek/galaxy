from dataclasses import dataclass

__all__ = ["CleanableItemsSummary"]


@dataclass
class CleanableItemsSummary:
    """
    CleanableItemsSummary dataclass.

    Args:
        total_items (int)        : The total number of items that could be purged.
        total_size (int)         : The total size in bytes that can be recovered by purging
                                   all the items.
    """

    total_items: int  # The total number of items that could be purged.
    total_size: int  # The total size in bytes that can be recovered by purging all the items.
