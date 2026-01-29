from typing import TypeAlias

from .dataset_storage_details_sources_item import DatasetStorageDetailsSourcesItem

__all__ = ["DatasetStorageDetailsSources"]

DatasetStorageDetailsSources: TypeAlias = list[DatasetStorageDetailsSourcesItem]
"""Alias for The file sources associated with the supplied dataset instance."""
