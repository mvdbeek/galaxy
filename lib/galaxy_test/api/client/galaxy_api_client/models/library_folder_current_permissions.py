from dataclasses import dataclass

from .add_library_item_role_list import AddLibraryItemRoleList
from .manage_folder_role_list import ManageFolderRoleList
from .modify_folder_role_list import ModifyFolderRoleList

__all__ = ["LibraryFolderCurrentPermissions"]


@dataclass
class LibraryFolderCurrentPermissions:
    """
    LibraryFolderCurrentPermissions dataclass.

    Args:
        add_library_item_role_list (AddLibraryItemRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can add items to the Library folder.
        manage_folder_role_list (ManageFolderRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can manage the Library folder.
        modify_folder_role_list (ModifyFolderRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can modify the Library folder.
    """

    add_library_item_role_list: AddLibraryItemRoleList  # A list containing pairs of role names and corresponding encoded IDs which can add items to the Library folder.
    manage_folder_role_list: ManageFolderRoleList  # A list containing pairs of role names and corresponding encoded IDs which can manage the Library folder.
    modify_folder_role_list: ModifyFolderRoleList  # A list containing pairs of role names and corresponding encoded IDs which can modify the Library folder.
