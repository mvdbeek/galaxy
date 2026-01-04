from dataclasses import dataclass

from .description import Description
from .synopsis import Synopsis

__all__ = ["LibraryDestination"]


@dataclass
class LibraryDestination:
    """
    LibraryDestination dataclass.

    Args:
        name (str)               : Must specify a library name
        type_ (str)              :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        synopsis (Optional[Synopsis])
                                 : A short text describing the contents of the Library.
                                   Leave unset to keep the existing.
    """

    name: str  # Must specify a library name
    type_: str
    description: Description | None = ""  # Detailed text description for this Quota.
    synopsis: Synopsis | None = (
        ""  # A short text describing the contents of the Library. Leave unset to keep the existing.
    )
