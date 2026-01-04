from typing import TypeAlias

from .manage_library_role_list_item import ManageLibraryRoleListItem

__all__ = ["ManageLibraryRoleList"]

ManageLibraryRoleList: TypeAlias = list[ManageLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can manage the Library."""
