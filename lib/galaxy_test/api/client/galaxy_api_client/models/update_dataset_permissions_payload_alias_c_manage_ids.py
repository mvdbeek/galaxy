from typing import TypeAlias

__all__ = ["UpdateDatasetPermissionsPayloadAliasCManageIds"]

UpdateDatasetPermissionsPayloadAliasCManageIds: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should have manage permission on the dataset."""
