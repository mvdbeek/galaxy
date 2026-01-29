from typing import TypeAlias

__all__ = ["DrsObjectAliases"]

DrsObjectAliases: TypeAlias = list[str] | None
"""Alias for A list of strings that can be used to find other metadata about this `DrsObject` from external metadata sources. These aliases can be used to represent secondary accession numbers or external GUIDs."""
