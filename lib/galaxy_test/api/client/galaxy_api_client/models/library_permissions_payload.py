from dataclasses import dataclass

from .library_permissions_payload_access_ids import LibraryPermissionsPayloadAccessIds
from .library_permissions_payload_action import LibraryPermissionsPayloadAction
from .library_permissions_payload_add_ids import LibraryPermissionsPayloadAddIds
from .library_permissions_payload_manage_ids import LibraryPermissionsPayloadManageIds
from .library_permissions_payload_modify_ids import LibraryPermissionsPayloadModifyIds

__all__ = ["LibraryPermissionsPayload"]


@dataclass
class LibraryPermissionsPayload:
    """
    LibraryPermissionsPayload dataclass

    Args:
        access_ids (LibraryPermissionsPayloadAccessIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the library. (maps from
                                   'access_ids[]')
        action (LibraryPermissionsPayloadAction | None)
                                 : Indicates what action should be performed on the Library.
        add_ids (LibraryPermissionsPayloadAddIds | None)
                                 : A list of role encoded IDs defining roles that should be
                                   able to add items to the library. (maps from 'add_ids[]')
        manage_ids (LibraryPermissionsPayloadManageIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the library. (maps from
                                   'manage_ids[]')
        modify_ids (LibraryPermissionsPayloadModifyIds | None)
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the library. (maps from
                                   'modify_ids[]')
    """

    access_ids: LibraryPermissionsPayloadAccessIds | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the library. (maps from 'access_ids[]')
    )
    action: LibraryPermissionsPayloadAction | None = None  # Indicates what action should be performed on the Library.
    add_ids: LibraryPermissionsPayloadAddIds | None = (
        None  # A list of role encoded IDs defining roles that should be able to add items to the library. (maps from 'add_ids[]')
    )
    manage_ids: LibraryPermissionsPayloadManageIds | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the library. (maps from 'manage_ids[]')
    )
    modify_ids: LibraryPermissionsPayloadModifyIds | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the library. (maps from 'modify_ids[]')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_ids[]": "access_ids",
            "action": "action",
            "add_ids[]": "add_ids",
            "manage_ids[]": "manage_ids",
            "modify_ids[]": "modify_ids",
        }
        key_transform_with_dump = {
            "access_ids": "access_ids[]",
            "action": "action",
            "add_ids": "add_ids[]",
            "manage_ids": "manage_ids[]",
            "modify_ids": "modify_ids[]",
        }
