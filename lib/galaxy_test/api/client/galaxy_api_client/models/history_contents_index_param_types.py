from typing import TypeAlias

from .anonymous_array_item_170 import AnonymousArrayItem170

__all__ = ["HistoryContentsIndexParamTypes"]

HistoryContentsIndexParamTypes: TypeAlias = list[AnonymousArrayItem170] | None
"""Alias for A list or comma-separated list of kinds of contents to return (currently just `dataset` and `dataset_collection` are available). If unset, all types will be returned."""
