from dataclasses import dataclass

from .library_folder_permissions_payload_action import LibraryFolderPermissionsPayloadAction
from .library_folder_permissions_payload_add_ids import LibraryFolderPermissionsPayloadAddIds
from .library_folder_permissions_payload_manage_ids import LibraryFolderPermissionsPayloadManageIds
from .library_folder_permissions_payload_modify_ids import LibraryFolderPermissionsPayloadModifyIds

__all__ = ["LibraryFolderPermissionsPayload"]


@dataclass
class LibraryFolderPermissionsPayload:
    """
    LibraryFolderPermissionsPayload dataclass

    Args:
        action (LibraryFolderPermissionsPayloadAction | None)
                                 : Indicates what action should be performed on the library
                                   folder.
        add_ids (LibraryFolderPermissionsPayloadAddIds | None)
                                 : A list of role encoded IDs defining roles that should be
                                   able to add items to the library. (maps from 'add_ids[]')
        manage_ids (LibraryFolderPermissionsPayloadManageIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the library. (maps from
                                   'manage_ids[]')
        modify_ids (LibraryFolderPermissionsPayloadModifyIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the library. (maps from
                                   'modify_ids[]')
    """

    action: LibraryFolderPermissionsPayloadAction | None = (
        None  # Indicates what action should be performed on the library folder.
    )
    add_ids: LibraryFolderPermissionsPayloadAddIds | None = (
        None  # A list of role encoded IDs defining roles that should be able to add items to the library. (maps from 'add_ids[]')
    )
    manage_ids: LibraryFolderPermissionsPayloadManageIds | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the library. (maps from 'manage_ids[]')
    )
    modify_ids: LibraryFolderPermissionsPayloadModifyIds | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the library. (maps from 'modify_ids[]')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action": "action",
            "add_ids[]": "add_ids",
            "manage_ids[]": "manage_ids",
            "modify_ids[]": "modify_ids",
        }
        key_transform_with_dump = {
            "action": "action",
            "add_ids": "add_ids[]",
            "manage_ids": "manage_ids[]",
            "modify_ids": "modify_ids[]",
        }
