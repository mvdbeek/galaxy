from typing import TypeAlias

__all__ = ["HistoryContentsIndexParamTypes"]

HistoryContentsIndexParamTypes: TypeAlias = list[str] | None
"""Alias for A list or comma-separated list of kinds of contents to return (currently just `dataset` and `dataset_collection` are available). If unset, all types will be returned."""
