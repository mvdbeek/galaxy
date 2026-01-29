from typing import TypeAlias

from .library_folder_current_permissions_modify_folder_role_list_item import (
    LibraryFolderCurrentPermissionsModifyFolderRoleListItem,
)

__all__ = ["LibraryFolderCurrentPermissionsModifyFolderRoleList"]

LibraryFolderCurrentPermissionsModifyFolderRoleList: TypeAlias = list[
    LibraryFolderCurrentPermissionsModifyFolderRoleListItem
]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can modify the Library folder."""
