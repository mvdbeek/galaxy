from typing import TypeAlias

__all__ = ["RemoteFilesIndexParamDisable"]

RemoteFilesIndexParamDisable: TypeAlias = str | None
"""Alias for (This only applies when `format` is `jstree`) The value can be either `folders` or `files` and it will disable the corresponding nodes of the tree."""
