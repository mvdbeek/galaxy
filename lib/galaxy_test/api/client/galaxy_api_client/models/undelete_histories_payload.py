from dataclasses import dataclass

from .ids import Ids

__all__ = ["UndeleteHistoriesPayload"]


@dataclass
class UndeleteHistoriesPayload:
    """
    UndeleteHistoriesPayload dataclass.

    Args:
        ids (Ids)                : List of history IDs to be undeleted.
    """

    ids: Ids  # List of history IDs to be undeleted.
