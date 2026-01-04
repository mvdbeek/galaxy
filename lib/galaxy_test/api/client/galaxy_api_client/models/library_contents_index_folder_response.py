from dataclasses import dataclass

__all__ = ["LibraryContentsIndexFolderResponse"]


@dataclass
class LibraryContentsIndexFolderResponse:
    """
    LibraryContentsIndexFolderResponse dataclass.

    Args:
        id_ (str)                :
        name (str)               :
        type_ (str)              :
        url (str)                :
    """

    id_: str
    name: str
    type_: str
    url: str
