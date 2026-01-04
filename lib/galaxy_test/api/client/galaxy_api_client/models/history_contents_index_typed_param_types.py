from typing import TypeAlias

from .anonymous_array_item_190 import AnonymousArrayItem190

__all__ = ["HistoryContentsIndexTypedParamTypes"]

HistoryContentsIndexTypedParamTypes: TypeAlias = list[AnonymousArrayItem190] | None
"""Alias for A list or comma-separated list of kinds of contents to return (currently just `dataset` and `dataset_collection` are available). If unset, all types will be returned."""
