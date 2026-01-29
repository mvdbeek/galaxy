from dataclasses import dataclass

__all__ = ["NotificationsBatchUpdateResponse"]


@dataclass
class NotificationsBatchUpdateResponse:
    """
    The response of a batch update request.

    Args:
        updated_count (int)      : The number of notifications that were updated.
    """

    updated_count: int  # The number of notifications that were updated.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "updated_count": "updated_count",
        }
        key_transform_with_dump = {
            "updated_count": "updated_count",
        }
