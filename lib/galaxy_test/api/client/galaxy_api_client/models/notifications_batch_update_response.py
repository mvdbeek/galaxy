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
