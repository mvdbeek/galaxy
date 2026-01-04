from typing import TypeAlias

from .access_dataset_roles_item import AccessDatasetRolesItem

__all__ = ["AccessDatasetRoles"]

AccessDatasetRoles: TypeAlias = list[AccessDatasetRolesItem]
"""Alias for A list of roles that can access the dataset. The user has to **have all these roles** in order to access this dataset. Users without access permission **cannot** have other permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**."""
