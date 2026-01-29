from dataclasses import dataclass

from .description import Description

__all__ = ["CreateLibraryFolderPayload"]


@dataclass
class CreateLibraryFolderPayload:
    """
    CreateLibraryFolderPayload dataclass.

    Args:
        name (str)               : The name of the library folder.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
    """

    name: str  # The name of the library folder.
    description: Description | None = ""  # Detailed text description for this Quota.
