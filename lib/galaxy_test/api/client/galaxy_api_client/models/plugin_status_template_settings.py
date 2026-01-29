from typing import TypeAlias

from .plugin_aspect_status import PluginAspectStatus

__all__ = ["PluginStatusTemplateSettings"]

PluginStatusTemplateSettings: TypeAlias = PluginAspectStatus | None
