from typing import TypeAlias

from .library_folder_current_permissions_manage_folder_role_list_item import (
    LibraryFolderCurrentPermissionsManageFolderRoleListItem,
)

__all__ = ["LibraryFolderCurrentPermissionsManageFolderRoleList"]

LibraryFolderCurrentPermissionsManageFolderRoleList: TypeAlias = list[
    LibraryFolderCurrentPermissionsManageFolderRoleListItem
]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can manage the Library folder."""
