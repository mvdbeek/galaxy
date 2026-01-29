from typing import TypeAlias

from .add_library_item_role_list_item import AddLibraryItemRoleListItem

__all__ = ["AddLibraryItemRoleList"]

AddLibraryItemRoleList: TypeAlias = list[AddLibraryItemRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which can add items to the Library."""
