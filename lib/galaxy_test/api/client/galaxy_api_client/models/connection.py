from typing import TypeAlias

from .plugin_aspect_status import PluginAspectStatus

__all__ = ["Connection"]

Connection: TypeAlias = PluginAspectStatus | None
