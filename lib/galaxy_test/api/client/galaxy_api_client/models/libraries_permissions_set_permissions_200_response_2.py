from typing import TypeAlias

from .library_current_permissions import LibraryCurrentPermissions
from .library_legacy_summary import LibraryLegacySummary

__all__ = ["LibrariesPermissionsSetPermissions200Response2"]

LibrariesPermissionsSetPermissions200Response2: TypeAlias = LibraryCurrentPermissions | LibraryLegacySummary
