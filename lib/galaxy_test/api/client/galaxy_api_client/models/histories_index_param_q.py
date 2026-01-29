from typing import TypeAlias

__all__ = ["HistoriesIndexParamQ"]

HistoriesIndexParamQ: TypeAlias = list[str] | None
"""Alias for Generally a property name to filter by followed by an (often optional) hyphen and operator string."""
