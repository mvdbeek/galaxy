from typing import TypeAlias

__all__ = ["RemoteFilesPluginsPluginsParamBrowsableOnly"]

RemoteFilesPluginsPluginsParamBrowsableOnly: TypeAlias = bool | None
"""Alias for Whether to return browsable filesources only. The default is `True`, which will omit filesourceslike `http` and `base64` that do not implement a list method."""
