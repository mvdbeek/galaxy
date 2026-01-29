from dataclasses import dataclass

from .description import Description
from .name import Name
from .synopsis import Synopsis

__all__ = ["UpdateLibraryPayload"]


@dataclass
class UpdateLibraryPayload:
    """
    UpdateLibraryPayload dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        name (Optional[Name])    : The name of the creator.
        synopsis (Optional[Synopsis])
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    description: Description | None = ""  # Detailed text description for this Quota.
    name: Name | None = None  # The name of the creator.
    synopsis: Synopsis | None = (
        ""  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )
