from typing import TypeAlias

__all__ = ["DatatypeExt"]

DatatypeExt: TypeAlias = str | None
"""Alias for If action is 'datatype_groom', this is the datatype that was used to find and run the grooming code as part of the transform action."""
