from typing import TypeAlias

__all__ = ["LibraryFolderPermissionsPayloadManageIds"]

LibraryFolderPermissionsPayloadManageIds: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should have manage permission on the library."""
