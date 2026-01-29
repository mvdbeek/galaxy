from typing import TypeAlias

from .library_current_permissions_access_library_role_list_item import (
    LibraryCurrentPermissionsAccessLibraryRoleListItem,
)

__all__ = ["LibraryCurrentPermissionsAccessLibraryRoleList"]

LibraryCurrentPermissionsAccessLibraryRoleList: TypeAlias = list[LibraryCurrentPermissionsAccessLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which have access to the Library."""
