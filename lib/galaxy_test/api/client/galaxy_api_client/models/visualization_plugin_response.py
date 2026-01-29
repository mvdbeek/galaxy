from dataclasses import dataclass

from .visualization_plugin_response_entry_point import VisualizationPluginResponseEntryPoint
from .visualization_plugin_response_logo import VisualizationPluginResponseLogo
from .visualization_plugin_response_settings import VisualizationPluginResponseSettings
from .visualization_plugin_response_specs import VisualizationPluginResponseSpecs
from .visualization_plugin_response_title import VisualizationPluginResponseTitle
from .visualization_plugin_response_tracks import VisualizationPluginResponseTracks

__all__ = ["VisualizationPluginResponse"]


@dataclass
class VisualizationPluginResponse:
    """
    VisualizationPluginResponse dataclass

    Args:
        description (str)        : The description of the plugin.
        embeddable (bool)        : Whether the plugin is embeddable.
        entry_point (VisualizationPluginResponseEntryPoint)
                                 : The entry point of the plugin.
        href (str)               : The href of the plugin.
        html (str)               : The HTML of the plugin.
        name (str)               : The name of the plugin.
        logo (VisualizationPluginResponseLogo | None)
                                 : The logo of the plugin.
        settings (VisualizationPluginResponseSettings | None)
                                 : The settings of the plugin.
        specs (VisualizationPluginResponseSpecs | None)
                                 : The specs of the plugin.
        title (VisualizationPluginResponseTitle | None)
                                 : The title of the plugin.
        tracks (VisualizationPluginResponseTracks | None)
                                 : The tracks of the plugin.
    """

    description: str  # The description of the plugin.
    embeddable: bool  # Whether the plugin is embeddable.
    entry_point: VisualizationPluginResponseEntryPoint  # The entry point of the plugin.
    href: str  # The href of the plugin.
    html: str  # The HTML of the plugin.
    name: str  # The name of the plugin.
    logo: VisualizationPluginResponseLogo | None = None  # The logo of the plugin.
    settings: VisualizationPluginResponseSettings | None = None  # The settings of the plugin.
    specs: VisualizationPluginResponseSpecs | None = None  # The specs of the plugin.
    title: VisualizationPluginResponseTitle | None = None  # The title of the plugin.
    tracks: VisualizationPluginResponseTracks | None = None  # The tracks of the plugin.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "embeddable": "embeddable",
            "entry_point": "entry_point",
            "href": "href",
            "html": "html",
            "logo": "logo",
            "name": "name",
            "settings": "settings",
            "specs": "specs",
            "title": "title",
            "tracks": "tracks",
        }
        key_transform_with_dump = {
            "description": "description",
            "embeddable": "embeddable",
            "entry_point": "entry_point",
            "href": "href",
            "html": "html",
            "logo": "logo",
            "name": "name",
            "settings": "settings",
            "specs": "specs",
            "title": "title",
            "tracks": "tracks",
        }
