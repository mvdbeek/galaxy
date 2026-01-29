from typing import TypeAlias

from .library_current_permissions_modify_library_role_list_item import (
    LibraryCurrentPermissionsModifyLibraryRoleListItem,
)

__all__ = ["LibraryCurrentPermissionsModifyLibraryRoleList"]

LibraryCurrentPermissionsModifyLibraryRoleList: TypeAlias = list[LibraryCurrentPermissionsModifyLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can modify the Library."""
