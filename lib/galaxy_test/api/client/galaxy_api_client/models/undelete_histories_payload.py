from dataclasses import dataclass

__all__ = ["UndeleteHistoriesPayload"]


@dataclass
class UndeleteHistoriesPayload:
    """
    UndeleteHistoriesPayload dataclass

    Args:
        ids (List[str])          : List of history IDs to be undeleted.
    """

    ids: list[str]  # List of history IDs to be undeleted.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "ids": "ids",
        }
        key_transform_with_dump = {
            "ids": "ids",
        }
