from typing import TypeAlias

from .library_permission_action import LibraryPermissionAction

__all__ = ["LibrariesPermissionsSetPermissionsParamAction"]

LibrariesPermissionsSetPermissionsParamAction: TypeAlias = LibraryPermissionAction | None
"""Alias for Indicates what action should be performed on the Library."""
