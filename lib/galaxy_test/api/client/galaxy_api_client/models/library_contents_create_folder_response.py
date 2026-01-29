from dataclasses import dataclass

__all__ = ["LibraryContentsCreateFolderResponse"]


@dataclass
class LibraryContentsCreateFolderResponse:
    """
    LibraryContentsCreateFolderResponse dataclass.

    Args:
        id_ (str)                :
        name (str)               :
        url (str)                :
    """

    id_: str
    name: str
    url: str
