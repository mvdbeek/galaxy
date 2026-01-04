from dataclasses import dataclass

from .errors import Errors

__all__ = ["DeleteDatasetBatchResult"]


@dataclass
class DeleteDatasetBatchResult:
    """
    DeleteDatasetBatchResult dataclass.

    Args:
        success_count (int)      : The number of datasets successfully processed.
        errors (Optional[Errors]): Collection of messages indicating that the resource was
                                   not shared with some (or all users) due to an error.
    """

    success_count: int  # The number of datasets successfully processed.
    errors: Errors | None = (
        None  # Collection of messages indicating that the resource was not shared with some (or all users) due to an error.
    )
