from dataclasses import dataclass

__all__ = ["DeleteHistoriesPayload"]


@dataclass
class DeleteHistoriesPayload:
    """
    DeleteHistoriesPayload dataclass

    Args:
        ids (List[str])          : List of history IDs to be deleted.
        purge (bool | None)      : Whether to definitely remove this history from disk.
    """

    ids: list[str]  # List of history IDs to be deleted.
    purge: bool | None = False  # Whether to definitely remove this history from disk.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "ids": "ids",
            "purge": "purge",
        }
        key_transform_with_dump = {
            "ids": "ids",
            "purge": "purge",
        }
