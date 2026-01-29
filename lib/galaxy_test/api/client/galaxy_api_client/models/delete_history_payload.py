from dataclasses import dataclass

__all__ = ["DeleteHistoryPayload"]


@dataclass
class DeleteHistoryPayload:
    """
    DeleteHistoryPayload dataclass

    Args:
        purge (bool | None)      : Whether to definitely remove this history from disk.
    """

    purge: bool | None = False  # Whether to definitely remove this history from disk.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "purge": "purge",
        }
        key_transform_with_dump = {
            "purge": "purge",
        }
