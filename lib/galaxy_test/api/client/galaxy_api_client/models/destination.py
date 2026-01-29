from typing import TypeAlias

from .hda_destination import HdaDestination
from .library_destination import LibraryDestination
from .library_folder_destination import LibraryFolderDestination

__all__ = ["Destination"]

Destination: TypeAlias = HdaDestination | LibraryDestination | LibraryFolderDestination
