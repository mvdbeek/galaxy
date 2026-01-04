from typing import TypeAlias

from .plugin_kind import PluginKind

__all__ = ["RemoteFilesPluginsPluginsParamIncludeKind"]

RemoteFilesPluginsPluginsParamIncludeKind: TypeAlias = list[PluginKind] | None
"""Alias for Whether to return **only** filesources of the specified kind. The default is `None`, which will return all filesources. Multiple values can be specified by repeating the parameter."""
