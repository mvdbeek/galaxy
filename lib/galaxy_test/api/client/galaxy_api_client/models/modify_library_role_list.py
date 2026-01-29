from typing import TypeAlias

from .modify_library_role_list_item import ModifyLibraryRoleListItem

__all__ = ["ModifyLibraryRoleList"]

ModifyLibraryRoleList: TypeAlias = list[ModifyLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can modify the Library."""
