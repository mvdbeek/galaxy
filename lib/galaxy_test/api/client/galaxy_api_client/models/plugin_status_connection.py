from typing import TypeAlias

from .plugin_aspect_status import PluginAspectStatus

__all__ = ["PluginStatusConnection"]

PluginStatusConnection: TypeAlias = PluginAspectStatus | None
