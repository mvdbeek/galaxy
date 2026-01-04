from dataclasses import dataclass

from .library_access_in import LibraryAccessIn
from .library_add_in import LibraryAddIn
from .library_manage_in import LibraryManageIn
from .library_modify_in import LibraryModifyIn

__all__ = ["LegacyLibraryPermissionsPayload"]


@dataclass
class LegacyLibraryPermissionsPayload:
    """
    LegacyLibraryPermissionsPayload dataclass.

    Args:
        library_access_in (Optional[LibraryAccessIn])
                                 : A list of role encoded IDs defining roles that should
                                   have access permission on the library.
        library_add_in (Optional[LibraryAddIn])
                                 : A list of role encoded IDs defining roles that should
                                   have manage permission on the library.
        library_manage_in (Optional[LibraryManageIn])
                                 : A list of role encoded IDs defining roles that should
                                   have modify permission on the library.
        library_modify_in (Optional[LibraryModifyIn])
                                 : A list of role encoded IDs defining roles that should be
                                   able to add items to the library.
    """

    library_access_in: LibraryAccessIn | None = (
        None  # A list of role encoded IDs defining roles that should have access permission on the library.
    )
    library_add_in: LibraryAddIn | None = (
        None  # A list of role encoded IDs defining roles that should have manage permission on the library.
    )
    library_manage_in: LibraryManageIn | None = (
        None  # A list of role encoded IDs defining roles that should have modify permission on the library.
    )
    library_modify_in: LibraryModifyIn | None = (
        None  # A list of role encoded IDs defining roles that should be able to add items to the library.
    )
