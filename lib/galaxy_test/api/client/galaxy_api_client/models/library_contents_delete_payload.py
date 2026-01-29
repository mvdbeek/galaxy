from dataclasses import dataclass

__all__ = ["LibraryContentsDeletePayload"]


@dataclass
class LibraryContentsDeletePayload:
    """
    LibraryContentsDeletePayload dataclass.

    Args:
        purge (Optional[bool])   : if True, purge the library dataset
    """

    purge: bool | None = False  # if True, purge the library dataset
