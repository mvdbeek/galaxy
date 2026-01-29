from dataclasses import dataclass

from .library_current_permissions_access_library_role_list import LibraryCurrentPermissionsAccessLibraryRoleList
from .library_current_permissions_add_library_item_role_list import LibraryCurrentPermissionsAddLibraryItemRoleList
from .library_current_permissions_manage_library_role_list import LibraryCurrentPermissionsManageLibraryRoleList
from .library_current_permissions_modify_library_role_list import LibraryCurrentPermissionsModifyLibraryRoleList

__all__ = ["LibraryCurrentPermissions"]


@dataclass
class LibraryCurrentPermissions:
    """
    LibraryCurrentPermissions dataclass

    Args:
        access_library_role_list (LibraryCurrentPermissionsAccessLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which have access to the Library.
        add_library_item_role_list (LibraryCurrentPermissionsAddLibraryItemRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can add items to the Library.
        manage_library_role_list (LibraryCurrentPermissionsManageLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can manage the Library.
        modify_library_role_list (LibraryCurrentPermissionsModifyLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can modify the Library.
    """

    access_library_role_list: LibraryCurrentPermissionsAccessLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which have access to the Library.
    add_library_item_role_list: LibraryCurrentPermissionsAddLibraryItemRoleList  # A list containing pairs of role names and corresponding encoded IDs which can add items to the Library.
    manage_library_role_list: LibraryCurrentPermissionsManageLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which can manage the Library.
    modify_library_role_list: LibraryCurrentPermissionsModifyLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which can modify the Library.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "access_library_role_list": "access_library_role_list",
            "add_library_item_role_list": "add_library_item_role_list",
            "manage_library_role_list": "manage_library_role_list",
            "modify_library_role_list": "modify_library_role_list",
        }
        key_transform_with_dump = {
            "access_library_role_list": "access_library_role_list",
            "add_library_item_role_list": "add_library_item_role_list",
            "manage_library_role_list": "manage_library_role_list",
            "modify_library_role_list": "modify_library_role_list",
        }
