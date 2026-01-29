from dataclasses import dataclass

from .browsable_files_source_plugin_doc import BrowsableFilesSourcePluginDoc
from .browsable_files_source_plugin_requires_groups import BrowsableFilesSourcePluginRequiresGroups
from .browsable_files_source_plugin_requires_roles import BrowsableFilesSourcePluginRequiresRoles
from .browsable_files_source_plugin_url import BrowsableFilesSourcePluginUrl
from .files_source_supports import FilesSourceSupports

__all__ = ["BrowsableFilesSourcePlugin"]


@dataclass
class BrowsableFilesSourcePlugin:
    """
    BrowsableFilesSourcePlugin dataclass

    Args:
        browsable (bool)         :
        id_ (str)                : The `FilesSource` plugin identifier (maps from 'id')
        label (str)              : The display label for this plugin.
        type_ (str)              : The type of the plugin. (maps from 'type')
        uri_root (str)           : The URI root used by this type of plugin.
        writable (bool)          : Whether this files source plugin allows write access.
        doc (BrowsableFilesSourcePluginDoc | None)
                                 : Documentation or extended description for this plugin.
        requires_groups (BrowsableFilesSourcePluginRequiresGroups | None)
                                 : Only users belonging to the groups specified here can
                                   access this files source.
        requires_roles (BrowsableFilesSourcePluginRequiresRoles | None)
                                 : Only users with the roles specified here can access this
                                   files source.
        supports (FilesSourceSupports | None)
                                 :
        url (BrowsableFilesSourcePluginUrl | None)
                                 : Optional URL that might be provided by some plugins to
                                   link to the remote source.
    """

    browsable: bool
    id_: str  # The `FilesSource` plugin identifier (maps from 'id')
    label: str  # The display label for this plugin.
    type_: str  # The type of the plugin. (maps from 'type')
    uri_root: str  # The URI root used by this type of plugin.
    writable: bool  # Whether this files source plugin allows write access.
    doc: BrowsableFilesSourcePluginDoc | None = None  # Documentation or extended description for this plugin.
    requires_groups: BrowsableFilesSourcePluginRequiresGroups | None = (
        None  # Only users belonging to the groups specified here can access this files source.
    )
    requires_roles: BrowsableFilesSourcePluginRequiresRoles | None = (
        None  # Only users with the roles specified here can access this files source.
    )
    supports: FilesSourceSupports | None = None
    url: BrowsableFilesSourcePluginUrl | None = (
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
            "uri_root": "uri_root",
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
            "uri_root": "uri_root",
            "url": "url",
            "writable": "writable",
        }
