from typing import TypeAlias

from .remote_files_format import RemoteFilesFormat

__all__ = ["RemoteFilesIndexParamFormat2"]

RemoteFilesIndexParamFormat2: TypeAlias = RemoteFilesFormat | None
"""Alias for The requested format of returned data. Either `flat` to simply list all the files, `jstree` to get a tree representation of the files, or the default `uri` to list files and directories by their URI."""
