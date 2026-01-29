from dataclasses import dataclass

from .files_source_plugin_doc import FilesSourcePluginDoc
from .files_source_plugin_requires_groups import FilesSourcePluginRequiresGroups
from .files_source_plugin_requires_roles import FilesSourcePluginRequiresRoles
from .files_source_plugin_url import FilesSourcePluginUrl
from .files_source_supports import FilesSourceSupports

__all__ = ["FilesSourcePlugin"]


@dataclass
class FilesSourcePlugin:
    """
    FilesSourcePlugin dataclass

    Args:
        browsable (bool)         : Whether this file source plugin can list items.
        id_ (str)                : The `FilesSource` plugin identifier (maps from 'id')
        label (str)              : The display label for this plugin.
        type_ (str)              : The type of the plugin. (maps from 'type')
        writable (bool)          : Whether this files source plugin allows write access.
        doc (FilesSourcePluginDoc | None)
                                 : Documentation or extended description for this plugin.
        requires_groups (FilesSourcePluginRequiresGroups | None)
                                 : Only users belonging to the groups specified here can
                                   access this files source.
        requires_roles (FilesSourcePluginRequiresRoles | None)
                                 : Only users with the roles specified here can access this
                                   files source.
        supports (FilesSourceSupports | None)
                                 :
        url (FilesSourcePluginUrl | None)
                                 : Optional URL that might be provided by some plugins to
                                   link to the remote source.
    """

    browsable: bool  # Whether this file source plugin can list items.
    id_: str  # The `FilesSource` plugin identifier (maps from 'id')
    label: str  # The display label for this plugin.
    type_: str  # The type of the plugin. (maps from 'type')
    writable: bool  # Whether this files source plugin allows write access.
    doc: FilesSourcePluginDoc | None = None  # Documentation or extended description for this plugin.
    requires_groups: FilesSourcePluginRequiresGroups | None = (
        None  # Only users belonging to the groups specified here can access this files source.
    )
    requires_roles: FilesSourcePluginRequiresRoles | None = (
        None  # Only users with the roles specified here can access this files source.
    )
    supports: FilesSourceSupports | None = None
    url: FilesSourcePluginUrl | None = (
        None  # Optional URL that might be provided by some plugins to link to the remote source.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "browsable": "browsable",
            "doc": "doc",
            "id": "id_",
            "label": "label",
            "requires_groups": "requires_groups",
            "requires_roles": "requires_roles",
            "supports": "supports",
            "type": "type_",
            "url": "url",
            "writable": "writable",
        }
        key_transform_with_dump = {
            "browsable": "browsable",
            "doc": "doc",
            "id_": "id",
            "label": "label",
            "requires_groups": "requires_groups",
            "requires_roles": "requires_roles",
            "supports": "supports",
            "type_": "type",
            "url": "url",
            "writable": "writable",
        }
