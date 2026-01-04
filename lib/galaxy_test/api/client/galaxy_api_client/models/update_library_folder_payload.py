from dataclasses import dataclass

from .description import Description
from .name import Name

__all__ = ["UpdateLibraryFolderPayload"]


@dataclass
class UpdateLibraryFolderPayload:
    """
    UpdateLibraryFolderPayload dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        name (Optional[Name])    : The name of the creator.
    """

    description: Description | None = ""  # Detailed text description for this Quota.
    name: Name | None = None  # The name of the creator.
