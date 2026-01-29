from typing import TypeAlias

from .dataset_error_message import DatasetErrorMessage

__all__ = ["DeleteDatasetBatchResultErrors"]

DeleteDatasetBatchResultErrors: TypeAlias = list[DatasetErrorMessage] | None
"""Alias for A list of dataset IDs and the corresponding error message if something went wrong while processing the dataset."""
