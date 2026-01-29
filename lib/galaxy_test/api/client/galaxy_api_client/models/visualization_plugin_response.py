from dataclasses import dataclass

from .logo import Logo
from .settings import Settings
from .specs import Specs
from .title import Title
from .tracks import Tracks
from .visualization_plugin_response_entry_point import VisualizationPluginResponseEntryPoint

__all__ = ["VisualizationPluginResponse"]


@dataclass
class VisualizationPluginResponse:
    """
    VisualizationPluginResponse dataclass.

    Args:
        description (str)        : The description of the plugin.
        embeddable (bool)        : Whether the plugin is embeddable.
        entry_point (VisualizationPluginResponseEntryPoint)
                                 : The entry point of the plugin.
        href (str)               : The href of the plugin.
        html (str)               : The HTML of the plugin.
        name (str)               : The name of the plugin.
        logo (Optional[Logo])    : The logo of the plugin.
        settings (Optional[Settings])
                                 : The settings of the plugin.
        specs (Optional[Specs])  : The specs of the plugin.
        title (Optional[Title])  : The name of the visualization.
        tracks (Optional[Tracks]): The tracks of the plugin.
    """

    description: str  # The description of the plugin.
    embeddable: bool  # Whether the plugin is embeddable.
    entry_point: VisualizationPluginResponseEntryPoint  # The entry point of the plugin.
    href: str  # The href of the plugin.
    html: str  # The HTML of the plugin.
    name: str  # The name of the plugin.
    logo: Logo | None = None  # The logo of the plugin.
    settings: Settings | None = None  # The settings of the plugin.
    specs: Specs | None = None  # The specs of the plugin.
    title: Title | None = "Untitled Visualization"  # The name of the visualization.
    tracks: Tracks | None = None  # The tracks of the plugin.
