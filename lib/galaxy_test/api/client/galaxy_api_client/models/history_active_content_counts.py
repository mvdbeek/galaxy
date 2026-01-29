from dataclasses import dataclass

__all__ = ["HistoryActiveContentCounts"]


@dataclass
class HistoryActiveContentCounts:
    """
    Contains the number of active, deleted or hidden items in a History.

    Args:
        active (int)             : Number of active datasets.
        deleted (int)            : Number of deleted datasets.
        hidden (int)             : Number of hidden datasets.
    """

    active: int  # Number of active datasets.
    deleted: int  # Number of deleted datasets.
    hidden: int  # Number of hidden datasets.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "deleted": "deleted",
            "hidden": "hidden",
        }
        key_transform_with_dump = {
            "active": "active",
            "deleted": "deleted",
            "hidden": "hidden",
        }
