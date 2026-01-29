from typing import TypeAlias

from .library_folder_current_permissions_add_library_item_role_list_item import (
    LibraryFolderCurrentPermissionsAddLibraryItemRoleListItem,
)

__all__ = ["LibraryFolderCurrentPermissionsAddLibraryItemRoleList"]

LibraryFolderCurrentPermissionsAddLibraryItemRoleList: TypeAlias = list[
    LibraryFolderCurrentPermissionsAddLibraryItemRoleListItem
]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can add items to the Library folder."""
