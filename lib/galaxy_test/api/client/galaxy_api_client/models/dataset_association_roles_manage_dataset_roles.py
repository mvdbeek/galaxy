from typing import TypeAlias

from .dataset_association_roles_manage_dataset_roles_item import DatasetAssociationRolesManageDatasetRolesItem

__all__ = ["DatasetAssociationRolesManageDatasetRoles"]

DatasetAssociationRolesManageDatasetRoles: TypeAlias = list[DatasetAssociationRolesManageDatasetRolesItem]
"""Alias for A list of roles that can manage permissions on the dataset. Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose the ability to manage this dataset unless you are an admin."""
