from typing import TypeAlias

from .remote_files_disable_mode import RemoteFilesDisableMode

__all__ = ["RemoteFilesIndexParamDisable2"]

RemoteFilesIndexParamDisable2: TypeAlias = RemoteFilesDisableMode | None
"""Alias for (This only applies when `format` is `jstree`) The value can be either `folders` or `files` and it will disable the corresponding nodes of the tree."""
