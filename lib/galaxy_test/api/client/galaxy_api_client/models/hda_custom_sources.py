from typing import TypeAlias

from .dataset_source import DatasetSource

__all__ = ["HdaCustomSources"]

HdaCustomSources: TypeAlias = list[DatasetSource] | None
"""Alias for The list of sources associated with this dataset."""
