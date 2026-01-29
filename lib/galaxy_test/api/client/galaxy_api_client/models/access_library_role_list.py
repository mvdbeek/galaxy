from typing import TypeAlias

from .access_library_role_list_item import AccessLibraryRoleListItem

__all__ = ["AccessLibraryRoleList"]

AccessLibraryRoleList: TypeAlias = list[AccessLibraryRoleListItem]
"""Alias for A list containing pairs of role names and corresponding encoded IDs which have access to the Library."""
