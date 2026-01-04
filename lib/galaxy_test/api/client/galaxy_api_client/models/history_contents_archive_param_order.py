from typing import TypeAlias

__all__ = ["HistoryContentsArchiveParamOrder"]

HistoryContentsArchiveParamOrder: TypeAlias = str | None
"""Alias for String containing one of the valid ordering attributes followed (optionally) by '-asc' or '-dsc' for ascending and descending order respectively. Orders can be stacked as a comma-separated list of values."""
