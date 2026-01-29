from typing import TypeAlias

from .dce_type import DceType

__all__ = ["DceSummaryElementType"]

DceSummaryElementType: TypeAlias = DceType | None
"""Alias for The type of the element. Used to interpret the `object` field."""
