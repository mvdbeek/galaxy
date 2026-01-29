from typing import TypeAlias

__all__ = ["UpdateQuotaParamsAmount"]

UpdateQuotaParamsAmount: TypeAlias = str | None
"""Alias for Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)"""
