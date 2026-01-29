from dataclasses import dataclass

__all__ = ["LibraryContentsIndexDatasetResponse"]


@dataclass
class LibraryContentsIndexDatasetResponse:
    """
    LibraryContentsIndexDatasetResponse dataclass.

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
