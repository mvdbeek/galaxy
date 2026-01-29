from typing import TypeAlias

from .manage_dataset_roles_item import ManageDatasetRolesItem

__all__ = ["ManageDatasetRoles"]

ManageDatasetRoles: TypeAlias = list[ManageDatasetRolesItem]
"""Alias for A list of roles that can manage permissions on the dataset. Users with **any** of these roles can manage permissions of this dataset. If you remove yourself you will lose the ability to manage this dataset unless you are an admin."""
