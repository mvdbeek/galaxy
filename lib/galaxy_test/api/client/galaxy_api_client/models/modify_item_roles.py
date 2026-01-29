from typing import TypeAlias

from .modify_item_roles_item import ModifyItemRolesItem

__all__ = ["ModifyItemRoles"]

ModifyItemRoles: TypeAlias = list[ModifyItemRolesItem]
"""Alias for A list of roles that can modify the library item. This is a library related permission. User with **any** of these roles can modify name, metadata, and other information about this library item."""
