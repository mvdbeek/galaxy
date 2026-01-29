from typing import TypeAlias

from .library_current_permissions_add_library_item_role_list_item import (
    LibraryCurrentPermissionsAddLibraryItemRoleListItem,
)

__all__ = ["LibraryCurrentPermissionsAddLibraryItemRoleList"]

LibraryCurrentPermissionsAddLibraryItemRoleList: TypeAlias = list[LibraryCurrentPermissionsAddLibraryItemRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can add items to the Library."""
