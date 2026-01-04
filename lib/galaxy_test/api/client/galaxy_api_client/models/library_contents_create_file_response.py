from dataclasses import dataclass

__all__ = ["LibraryContentsCreateFileResponse"]


@dataclass
class LibraryContentsCreateFileResponse:
    """
    LibraryContentsCreateFileResponse dataclass.

    Args:
        id_ (str)                :
        name (str)               :
        url (str)                :
    """

    id_: str
    name: str
    url: str
