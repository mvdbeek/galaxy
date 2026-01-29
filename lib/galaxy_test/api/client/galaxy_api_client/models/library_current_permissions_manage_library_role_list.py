from typing import TypeAlias

from .library_current_permissions_manage_library_role_list_item import (
    LibraryCurrentPermissionsManageLibraryRoleListItem,
)

__all__ = ["LibraryCurrentPermissionsManageLibraryRoleList"]

LibraryCurrentPermissionsManageLibraryRoleList: TypeAlias = list[LibraryCurrentPermissionsManageLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can manage the Library."""
