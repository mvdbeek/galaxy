from typing import TypeAlias

from .library_available_permissions import LibraryAvailablePermissions
from .library_folder_current_permissions import LibraryFolderCurrentPermissions

__all__ = ["DataLibrariesFoldersPermissionsGetPermissions200Response"]

DataLibrariesFoldersPermissionsGetPermissions200Response: TypeAlias = (
    LibraryFolderCurrentPermissions | LibraryAvailablePermissions
)
