from dataclasses import dataclass

__all__ = ["UserObjectstoreUsage"]


@dataclass
class UserObjectstoreUsage:
    """
    UserObjectstoreUsage dataclass.

    Args:
        object_store_id (str)    :
        total_disk_usage (float) :
    """

    object_store_id: str
    total_disk_usage: float
