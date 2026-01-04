from dataclasses import dataclass

from .access_ids import AccessIds
from .action import Action
from .add_ids import AddIds
from .manage_ids import ManageIds
from .modify_ids import ModifyIds

__all__ = ["LibraryPermissionsPayload"]


@dataclass
class LibraryPermissionsPayload:
    """
    LibraryPermissionsPayload dataclass.

    Args:
        access_ids (Optional[AccessIds])
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the dataset.
        action (Optional[Action]): Indicates what action should be performed on the dataset.
        add_ids (Optional[AddIds]): A list of role encoded IDs defining roles that should be
                                    able to add items to the library.
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
    add_ids: AddIds | None = (
        None  # A list of role encoded IDs defining roles that should be able to add items to the library.
    )
    manage_ids: ManageIds | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the dataset.
    )
    modify_ids: ModifyIds | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the dataset.
    )
