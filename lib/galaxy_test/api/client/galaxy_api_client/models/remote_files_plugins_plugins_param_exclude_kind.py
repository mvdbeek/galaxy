from typing import TypeAlias

from .plugin_kind import PluginKind

__all__ = ["RemoteFilesPluginsPluginsParamExcludeKind"]

RemoteFilesPluginsPluginsParamExcludeKind: TypeAlias = list[PluginKind] | None
"""Alias for Whether to exclude filesources of the specified kind from the list. The default is `None`, which will return all filesources. Multiple values can be specified by repeating the parameter."""
