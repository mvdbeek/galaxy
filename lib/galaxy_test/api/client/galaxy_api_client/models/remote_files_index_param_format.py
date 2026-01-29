from typing import TypeAlias

__all__ = ["RemoteFilesIndexParamFormat"]

RemoteFilesIndexParamFormat: TypeAlias = str | None
"""Alias for The requested format of returned data. Either `flat` to simply list all the files, `jstree` to get a tree representation of the files, or the default `uri` to list files and directories by their URI."""
