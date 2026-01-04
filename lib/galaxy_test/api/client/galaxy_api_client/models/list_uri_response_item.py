from typing import TypeAlias

from .remote_directory import RemoteDirectory
from .remote_file import RemoteFile

__all__ = ["ListUriResponseItem"]

ListUriResponseItem: TypeAlias = RemoteDirectory | RemoteFile
