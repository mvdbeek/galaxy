from dataclasses import dataclass

from .library_folder_current_permissions_add_library_item_role_list import (
    LibraryFolderCurrentPermissionsAddLibraryItemRoleList,
)
from .library_folder_current_permissions_manage_folder_role_list import (
    LibraryFolderCurrentPermissionsManageFolderRoleList,
)
from .library_folder_current_permissions_modify_folder_role_list import (
    LibraryFolderCurrentPermissionsModifyFolderRoleList,
)

__all__ = ["LibraryFolderCurrentPermissions"]


@dataclass
class LibraryFolderCurrentPermissions:
    """
    LibraryFolderCurrentPermissions dataclass

    Args:
        add_library_item_role_list (LibraryFolderCurrentPermissionsAddLibraryItemRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can add items to the Library folder.
        manage_folder_role_list (LibraryFolderCurrentPermissionsManageFolderRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can manage the Library folder.
        modify_folder_role_list (LibraryFolderCurrentPermissionsModifyFolderRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can modify the Library folder.
    """

    add_library_item_role_list: LibraryFolderCurrentPermissionsAddLibraryItemRoleList  # A list containing pairs of role names and corresponding encoded IDs which can add items to the Library folder.
    manage_folder_role_list: LibraryFolderCurrentPermissionsManageFolderRoleList  # A list containing pairs of role names and corresponding encoded IDs which can manage the Library folder.
    modify_folder_role_list: LibraryFolderCurrentPermissionsModifyFolderRoleList  # A list containing pairs of role names and corresponding encoded IDs which can modify the Library folder.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "add_library_item_role_list": "add_library_item_role_list",
            "manage_folder_role_list": "manage_folder_role_list",
            "modify_folder_role_list": "modify_folder_role_list",
        }
        key_transform_with_dump = {
            "add_library_item_role_list": "add_library_item_role_list",
            "manage_folder_role_list": "manage_folder_role_list",
            "modify_folder_role_list": "modify_folder_role_list",
        }
