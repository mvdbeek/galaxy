from dataclasses import dataclass

from .access_library_role_list import AccessLibraryRoleList
from .add_library_item_role_list import AddLibraryItemRoleList
from .manage_library_role_list import ManageLibraryRoleList
from .modify_library_role_list import ModifyLibraryRoleList

__all__ = ["LibraryCurrentPermissions"]


@dataclass
class LibraryCurrentPermissions:
    """
    LibraryCurrentPermissions dataclass.

    Args:
        access_library_role_list (AccessLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which have access to the Library.
        add_library_item_role_list (AddLibraryItemRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can add items to the Library.
        manage_library_role_list (ManageLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can manage the Library.
        modify_library_role_list (ModifyLibraryRoleList)
                                 : A list containing pairs of role names and corresponding
                                   encoded IDs which can modify the Library.
    """

    access_library_role_list: AccessLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which have access to the Library.
    add_library_item_role_list: AddLibraryItemRoleList  # A list containing pairs of role names and corresponding encoded IDs which can add items to the Library.
    manage_library_role_list: ManageLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which can manage the Library.
    modify_library_role_list: ModifyLibraryRoleList  # A list containing pairs of role names and corresponding encoded IDs which can modify the Library.
