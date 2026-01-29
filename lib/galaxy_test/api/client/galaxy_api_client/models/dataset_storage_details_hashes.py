from typing import TypeAlias

from .dataset_storage_details_hashes_item import DatasetStorageDetailsHashesItem

__all__ = ["DatasetStorageDetailsHashes"]

DatasetStorageDetailsHashes: TypeAlias = list[DatasetStorageDetailsHashesItem]
"""Alias for The file contents hashes associated with the supplied dataset instance."""
