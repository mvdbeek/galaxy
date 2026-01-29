from typing import TypeAlias

from .dataset_association_roles_modify_item_roles_item import DatasetAssociationRolesModifyItemRolesItem

__all__ = ["DatasetAssociationRolesModifyItemRoles"]

DatasetAssociationRolesModifyItemRoles: TypeAlias = list[DatasetAssociationRolesModifyItemRolesItem]
"""Alias for A list of roles that can modify the library item. This is a library related permission. User with **any** of these roles can modify name, metadata, and other information about this library item."""
