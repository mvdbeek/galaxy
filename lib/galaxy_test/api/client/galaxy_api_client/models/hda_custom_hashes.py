from typing import TypeAlias

from .dataset_hash import DatasetHash

__all__ = ["HdaCustomHashes"]

HdaCustomHashes: TypeAlias = list[DatasetHash] | None
"""Alias for The list of hashes associated with this dataset."""
