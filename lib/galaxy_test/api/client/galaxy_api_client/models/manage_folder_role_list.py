from typing import TypeAlias

from .manage_folder_role_list_item import ManageFolderRoleListItem

__all__ = ["ManageFolderRoleList"]

ManageFolderRoleList: TypeAlias = list[ManageFolderRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can manage the Library folder."""
