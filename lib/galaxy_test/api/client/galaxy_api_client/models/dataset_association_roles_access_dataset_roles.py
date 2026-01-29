from typing import TypeAlias

from .dataset_association_roles_access_dataset_roles_item import DatasetAssociationRolesAccessDatasetRolesItem

__all__ = ["DatasetAssociationRolesAccessDatasetRoles"]

DatasetAssociationRolesAccessDatasetRoles: TypeAlias = list[DatasetAssociationRolesAccessDatasetRolesItem]
"""Alias for A list of roles that can access the dataset. The user has to **have all these roles** in order to access this dataset. Users without access permission **cannot** have other permissions on this dataset. If there are no access roles set on the dataset it is considered **unrestricted**."""
