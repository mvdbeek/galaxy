from typing import TypeAlias

__all__ = ["LegacyLibraryPermissionsPayloadLibraryModifyIn"]

LegacyLibraryPermissionsPayloadLibraryModifyIn: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should be able to add items to the library."""
