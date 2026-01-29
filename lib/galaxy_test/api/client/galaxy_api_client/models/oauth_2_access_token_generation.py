from typing import TypeAlias

from .plugin_aspect_status import PluginAspectStatus

__all__ = ["Oauth2AccessTokenGeneration"]

Oauth2AccessTokenGeneration: TypeAlias = PluginAspectStatus | None
