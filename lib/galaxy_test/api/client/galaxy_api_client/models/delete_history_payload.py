from dataclasses import dataclass

__all__ = ["DeleteHistoryPayload"]


@dataclass
class DeleteHistoryPayload:
    """
    DeleteHistoryPayload dataclass.

    Args:
        purge (Optional[bool])   : Whether to definitely remove this history from disk.
    """

    purge: bool | None = False  # Whether to definitely remove this history from disk.
