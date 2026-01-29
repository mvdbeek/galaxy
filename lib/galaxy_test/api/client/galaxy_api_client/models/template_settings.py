from typing import TypeAlias

from .plugin_aspect_status import PluginAspectStatus

__all__ = ["TemplateSettings"]

TemplateSettings: TypeAlias = PluginAspectStatus | None
