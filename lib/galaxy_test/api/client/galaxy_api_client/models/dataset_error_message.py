from dataclasses import dataclass

from .encoded_dataset_source_id import EncodedDatasetSourceId

__all__ = ["DatasetErrorMessage"]


@dataclass
class DatasetErrorMessage:
    """
    DatasetErrorMessage dataclass

    Args:
        dataset (EncodedDatasetSourceId)
                                 :
        error_message (str)      : The error message returned while processing this dataset.
    """

    dataset: EncodedDatasetSourceId
    error_message: str  # The error message returned while processing this dataset.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dataset": "dataset",
            "error_message": "error_message",
        }
        key_transform_with_dump = {
            "dataset": "dataset",
            "error_message": "error_message",
        }
