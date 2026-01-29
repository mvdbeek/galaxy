from typing import TypeAlias

__all__ = ["LegacyLibraryPermissionsPayloadLibraryAddIn"]

LegacyLibraryPermissionsPayloadLibraryAddIn: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should have manage permission on the library."""
