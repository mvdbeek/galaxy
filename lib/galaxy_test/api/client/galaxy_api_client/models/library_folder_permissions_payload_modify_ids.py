from typing import TypeAlias

__all__ = ["LibraryFolderPermissionsPayloadModifyIds"]

LibraryFolderPermissionsPayloadModifyIds: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should have modify permission on the library."""
