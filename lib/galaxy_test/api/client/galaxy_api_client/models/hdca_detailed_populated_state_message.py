from typing import TypeAlias

__all__ = ["HdcaDetailedPopulatedStateMessage"]

HdcaDetailedPopulatedStateMessage: TypeAlias = str | None
"""Alias for Optional message with further information in case the population of the dataset collection failed."""
