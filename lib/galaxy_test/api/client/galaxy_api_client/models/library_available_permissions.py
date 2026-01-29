from dataclasses import dataclass

from .basic_role_model import BasicRoleModel

__all__ = ["LibraryAvailablePermissions"]


@dataclass
class LibraryAvailablePermissions:
    """
    LibraryAvailablePermissions dataclass.

    Args:
        page (int)               : Current page.
        page_limit (int)         : Maximum number of items per page.
        roles (List[BasicRoleModel])
                                 : A list containing available roles that can be assigned to
                                   a particular permission.
        total (int)              : Total number of items
    """

    page: int  # Current page.
    page_limit: int  # Maximum number of items per page.
    roles: list[BasicRoleModel]  # A list containing available roles that can be assigned to a particular permission.
    total: int  # Total number of items
