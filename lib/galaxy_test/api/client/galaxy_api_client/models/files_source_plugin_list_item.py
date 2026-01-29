from typing import TypeAlias

from .browsable_files_source_plugin import BrowsableFilesSourcePlugin
from .files_source_plugin import FilesSourcePlugin

__all__ = ["FilesSourcePluginListItem"]

FilesSourcePluginListItem: TypeAlias = BrowsableFilesSourcePlugin | FilesSourcePlugin
