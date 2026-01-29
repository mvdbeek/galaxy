from typing import TypeAlias

__all__ = ["CreateQuotaParamsInGroups"]

CreateQuotaParamsInGroups: TypeAlias = list[str] | None
"""Alias for A list of group IDs or names to associate with this quota."""
