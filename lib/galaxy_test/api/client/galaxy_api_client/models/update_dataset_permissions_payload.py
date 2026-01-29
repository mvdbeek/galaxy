from dataclasses import dataclass

from .access_ids import AccessIds
from .action import Action
from .manage_ids import ManageIds
from .modify_ids import ModifyIds

__all__ = ["UpdateDatasetPermissionsPayload"]


@dataclass
class UpdateDatasetPermissionsPayload:
    """
    UpdateDatasetPermissionsPayload dataclass.

    Args:
        access_ids (Optional[AccessIds])
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the dataset.
        action (Optional[Action]): Indicates what action should be performed on the dataset.
        manage_ids (Optional[ManageIds])
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the dataset.
        modify_ids (Optional[ModifyIds])
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the dataset.
    """

    access_ids: AccessIds | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the dataset.
    )
    action: Action | None = "set_permissions"  # Indicates what action should be performed on the dataset.
    manage_ids: ManageIds | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the dataset.
    )
    modify_ids: ModifyIds | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the dataset.
    )
