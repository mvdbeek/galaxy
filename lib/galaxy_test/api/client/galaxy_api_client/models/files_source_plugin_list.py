from typing import TypeAlias

from .files_source_plugin_list_item import FilesSourcePluginListItem

__all__ = ["FilesSourcePluginList"]

FilesSourcePluginList: TypeAlias = list[FilesSourcePluginListItem]
