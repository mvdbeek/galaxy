from dataclasses import dataclass

__all__ = ["LibraryContentsDeleteResponse"]


@dataclass
class LibraryContentsDeleteResponse:
    """
    LibraryContentsDeleteResponse dataclass.

    Args:
        deleted (bool)           :
        id_ (str)                :
    """

    deleted: bool
    id_: str
