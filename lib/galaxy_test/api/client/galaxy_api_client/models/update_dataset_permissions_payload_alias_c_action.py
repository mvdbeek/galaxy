from typing import TypeAlias

from .dataset_permission_action import DatasetPermissionAction

__all__ = ["UpdateDatasetPermissionsPayloadAliasCAction"]

UpdateDatasetPermissionsPayloadAliasCAction: TypeAlias = DatasetPermissionAction | None
"""Alias for Indicates what action should be performed on the dataset."""
