from dataclasses import dataclass

from .ids import Ids

__all__ = ["DeleteHistoriesPayload"]


@dataclass
class DeleteHistoriesPayload:
    """
    DeleteHistoriesPayload dataclass.

    Args:
        ids (Ids)                : List of history IDs to be deleted.
        purge (Optional[bool])   : Whether to definitely remove this history from disk.
    """

    ids: Ids  # List of history IDs to be deleted.
    purge: bool | None = False  # Whether to definitely remove this history from disk.
