from typing import TypeAlias

from .modify_folder_role_list_item import ModifyFolderRoleListItem

__all__ = ["ModifyFolderRoleList"]

ModifyFolderRoleList: TypeAlias = list[ModifyFolderRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can modify the Library folder."""
