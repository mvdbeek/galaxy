from dataclasses import dataclass

__all__ = ["DeleteLibraryPayload"]


@dataclass
class DeleteLibraryPayload:
    """
    DeleteLibraryPayload dataclass.

    Args:
        undelete (bool)          : Whether to restore this previously deleted library.
    """

    undelete: bool  # Whether to restore this previously deleted library.
