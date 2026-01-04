from typing import TypeAlias

from .visualization_plugin_response import VisualizationPluginResponse

__all__ = ["Plugin"]

Plugin: TypeAlias = VisualizationPluginResponse | None
"""Alias for The plugin of this Visualization."""
