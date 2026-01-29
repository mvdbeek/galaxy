from typing import TypeAlias

from .library_permission_scope import LibraryPermissionScope

__all__ = ["DataLibrariesFoldersPermissionsGetPermissionsParamScope"]

DataLibrariesFoldersPermissionsGetPermissionsParamScope: TypeAlias = LibraryPermissionScope | None
"""Alias for The scope of the permissions to retrieve. Either the `current` permissions or the `available`."""
