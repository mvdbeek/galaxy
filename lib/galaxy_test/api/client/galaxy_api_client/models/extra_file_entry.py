from dataclasses import dataclass

from .extra_files_entry_class import ExtraFilesEntryClass

__all__ = ["ExtraFileEntry"]


@dataclass
class ExtraFileEntry:
    """
    ExtraFileEntry dataclass

    Args:
        class_ (ExtraFilesEntryClass)
                                 : Maps from 'class'
        path (str)               : Relative path to the file or directory.
    """

    class_: ExtraFilesEntryClass  # Maps from 'class'
    path: str  # Relative path to the file or directory.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "class": "class_",
            "path": "path",
        }
        key_transform_with_dump = {
            "class_": "class",
            "path": "path",
        }
