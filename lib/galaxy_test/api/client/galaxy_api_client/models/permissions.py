from typing import TypeAlias

from .dataset_permissions import DatasetPermissions

__all__ = ["Permissions"]

Permissions: TypeAlias = DatasetPermissions | None
"""Alias for Role-based access and manage control permissions for the dataset."""
