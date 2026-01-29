from dataclasses import dataclass

from .doc import Doc
from .files_source_supports import FilesSourceSupports
from .requires_groups import RequiresGroups
from .requires_roles import RequiresRoles
from .url import Url

__all__ = ["FilesSourcePlugin"]


@dataclass
class FilesSourcePlugin:
    """
    FilesSourcePlugin dataclass.

    Args:
        browsable (bool)         : Whether this file source plugin can list items.
        id_ (str)                : The `FilesSource` plugin identifier
        label (str)              : The display label for this plugin.
        type_ (str)              : The type of the plugin.
        writable (bool)          : Whether this files source plugin allows write access.
        doc (Optional[Doc])      : Documentation or extended description for this plugin.
        requires_groups (Optional[RequiresGroups])
                                 : Only users belonging to the groups specified here can
                                   access this files source.
        requires_roles (Optional[RequiresRoles])
                                 : Only users with the roles specified here can access this
                                   files source.
        supports (Optional[FilesSourceSupports])
                                 :
        url (Optional[Url])      : The relative URL to access this item.
    """

    browsable: bool  # Whether this file source plugin can list items.
    id_: str  # The `FilesSource` plugin identifier
    label: str  # The display label for this plugin.
    type_: str  # The type of the plugin.
    writable: bool  # Whether this files source plugin allows write access.
    doc: Doc | None = None  # Documentation or extended description for this plugin.
    requires_groups: RequiresGroups | None = (
        None  # Only users belonging to the groups specified here can access this files source.
    )
    requires_roles: RequiresRoles | None = (
        None  # Only users with the roles specified here can access this files source.
    )
    supports: FilesSourceSupports | None = None
    url: Url | None = None  # The relative URL to access this item.
