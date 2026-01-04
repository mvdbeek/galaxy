from dataclasses import dataclass

__all__ = ["LibraryFolderDestination"]


@dataclass
class LibraryFolderDestination:
    """
    LibraryFolderDestination dataclass.

    Args:
        library_folder_id (str)  :
        type_ (str)              :
    """

    library_folder_id: str
    type_: str
