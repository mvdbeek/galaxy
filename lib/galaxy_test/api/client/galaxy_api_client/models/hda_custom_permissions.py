from typing import TypeAlias

from .dataset_permissions import DatasetPermissions

__all__ = ["HdaCustomPermissions"]

HdaCustomPermissions: TypeAlias = DatasetPermissions | None
"""Alias for Role-based access and manage control permissions for the dataset."""
