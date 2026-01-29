from dataclasses import dataclass

from .delete_dataset_batch_result_errors import DeleteDatasetBatchResultErrors

__all__ = ["DeleteDatasetBatchResult"]


@dataclass
class DeleteDatasetBatchResult:
    """
    DeleteDatasetBatchResult dataclass

    Args:
        success_count (int)      : The number of datasets successfully processed.
        errors (DeleteDatasetBatchResultErrors | None)
                                 : A list of dataset IDs and the corresponding error message
                                   if something went wrong while processing the dataset.
    """

    success_count: int  # The number of datasets successfully processed.
    errors: DeleteDatasetBatchResultErrors | None = (
        None  # A list of dataset IDs and the corresponding error message if something went wrong while processing the dataset.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "errors": "errors",
            "success_count": "success_count",
        }
        key_transform_with_dump = {
            "errors": "errors",
            "success_count": "success_count",
        }
