from dataclasses import dataclass

from .extra_files_entry_class import ExtraFilesEntryClass

__all__ = ["ExtraFileEntry"]


@dataclass
class ExtraFileEntry:
    """
    ExtraFileEntry dataclass.

    Args:
        class_ (ExtraFilesEntryClass)
                                 :
        path (str)               : Relative path to the file or directory.
    """

    class_: ExtraFilesEntryClass
    path: str  # Relative path to the file or directory.
