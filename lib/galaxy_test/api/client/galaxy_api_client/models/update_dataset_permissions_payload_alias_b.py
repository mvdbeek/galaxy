from dataclasses import dataclass

from .access import Access
from .action import Action
from .manage import Manage
from .modify import Modify

__all__ = ["UpdateDatasetPermissionsPayloadAliasB"]


@dataclass
class UpdateDatasetPermissionsPayloadAliasB:
    """
    UpdateDatasetPermissionsPayloadAliasB dataclass.

    Args:
        access (Optional[Access]): A list of role encoded IDs defining roles that should
                                   have access permission on the dataset.
        action (Optional[Action]): Indicates what action should be performed on the dataset.
        manage (Optional[Manage]): A list of role encoded IDs defining roles that should
                                   have manage permission on the dataset.
        modify (Optional[Modify]): A list of role encoded IDs defining roles that should
                                   have modify permission on the dataset.
    """

    access: Access | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the dataset.
    )
    action: Action | None = "set_permissions"  # Indicates what action should be performed on the dataset.
    manage: Manage | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the dataset.
    )
    modify: Modify | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the dataset.
    )
