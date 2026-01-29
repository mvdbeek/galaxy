from typing import TypeAlias

from .library_folder_permission_action import LibraryFolderPermissionAction

__all__ = ["LibraryFolderPermissionsPayloadAction"]

LibraryFolderPermissionsPayloadAction: TypeAlias = LibraryFolderPermissionAction | None
"""Alias for Indicates what action should be performed on the library folder."""
