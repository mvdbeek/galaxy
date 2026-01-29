from dataclasses import dataclass

from .legacy_library_permissions_payload_library_access_in import LegacyLibraryPermissionsPayloadLibraryAccessIn
from .legacy_library_permissions_payload_library_add_in import LegacyLibraryPermissionsPayloadLibraryAddIn
from .legacy_library_permissions_payload_library_manage_in import LegacyLibraryPermissionsPayloadLibraryManageIn
from .legacy_library_permissions_payload_library_modify_in import LegacyLibraryPermissionsPayloadLibraryModifyIn

__all__ = ["LegacyLibraryPermissionsPayload"]


@dataclass
class LegacyLibraryPermissionsPayload:
    """
    LegacyLibraryPermissionsPayload dataclass

    Args:
        library_access_in (LegacyLibraryPermissionsPayloadLibraryAccessIn | None)
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the library. (maps from
                                   'LIBRARY_ACCESS_in')
        library_add_in (LegacyLibraryPermissionsPayloadLibraryAddIn | None)
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the library. (maps from
                                   'LIBRARY_ADD_in')
        library_manage_in (LegacyLibraryPermissionsPayloadLibraryManageIn | None)
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the library. (maps from
                                   'LIBRARY_MANAGE_in')
        library_modify_in (LegacyLibraryPermissionsPayloadLibraryModifyIn | None)
                                 : A list of role encoded IDs defining roles that should be
                                   able to add items to the library. (maps from
                                   'LIBRARY_MODIFY_in')
    """

    library_access_in: LegacyLibraryPermissionsPayloadLibraryAccessIn | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the library. (maps from 'LIBRARY_ACCESS_in')
    )
    library_add_in: LegacyLibraryPermissionsPayloadLibraryAddIn | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the library. (maps from 'LIBRARY_ADD_in')
    )
    library_manage_in: LegacyLibraryPermissionsPayloadLibraryManageIn | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the library. (maps from 'LIBRARY_MANAGE_in')
    )
    library_modify_in: LegacyLibraryPermissionsPayloadLibraryModifyIn | None = (
        None  # A list of role encoded IDs defining roles that should be able to add items to the library. (maps from 'LIBRARY_MODIFY_in')
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "LIBRARY_ACCESS_in": "library_access_in",
            "LIBRARY_ADD_in": "library_add_in",
            "LIBRARY_MANAGE_in": "library_manage_in",
            "LIBRARY_MODIFY_in": "library_modify_in",
        }
        key_transform_with_dump = {
            "library_access_in": "LIBRARY_ACCESS_in",
            "library_add_in": "LIBRARY_ADD_in",
            "library_manage_in": "LIBRARY_MANAGE_in",
            "library_modify_in": "LIBRARY_MODIFY_in",
        }
