from dataclasses import dataclass

from .description import Description
from .synopsis import Synopsis

__all__ = ["CreateLibraryPayload"]


@dataclass
class CreateLibraryPayload:
    """
    CreateLibraryPayload dataclass.

    Args:
        name (str)               : The name of the Library.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        synopsis (Optional[Synopsis])
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    name: str  # The name of the Library.
    description: Description | None = ""  # Detailed text description for this Quota.
    synopsis: Synopsis | None = (
        ""  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )
