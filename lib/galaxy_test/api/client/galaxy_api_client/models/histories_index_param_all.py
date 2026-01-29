from typing import TypeAlias

__all__ = ["HistoriesIndexParamAll"]

HistoriesIndexParamAll: TypeAlias = bool | None
"""Alias for Whether all histories from other users in this Galaxy should be included. Only admins are allowed to query all histories."""
