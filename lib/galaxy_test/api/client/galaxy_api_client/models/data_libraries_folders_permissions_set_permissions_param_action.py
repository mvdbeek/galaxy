from typing import TypeAlias

from .library_folder_permission_action import LibraryFolderPermissionAction

__all__ = ["DataLibrariesFoldersPermissionsSetPermissionsParamAction"]

DataLibrariesFoldersPermissionsSetPermissionsParamAction: TypeAlias = LibraryFolderPermissionAction | None
"""Alias for Indicates what action should be performed on the Library. Currently only `set_permissions` is supported."""
