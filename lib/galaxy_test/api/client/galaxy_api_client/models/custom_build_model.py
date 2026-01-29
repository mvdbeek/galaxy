from dataclasses import dataclass

from .count import Count
from .fasta import Fasta
from .linecount import Linecount

__all__ = ["CustomBuildModel"]


@dataclass
class CustomBuildModel:
    """
    CustomBuildModel dataclass.

    Args:
        id_ (str)                : The ID of the custom build.
        len_ (str)               : The primary id of the len file.
        name (str)               : The name of the custom build.
        count (Optional[Count])  : The number of items in the history.
        fasta (Optional[Fasta])  : The primary id of the fasta file from a history.
        linecount (Optional[Linecount])
                                 : The primary id of a linecount dataset.
    """

    id_: str  # The ID of the custom build.
    len_: str  # The primary id of the len file.
    name: str  # The name of the custom build.
    count: Count | None = None  # The number of items in the history.
    fasta: Fasta | None = None  # The primary id of the fasta file from a history.
    linecount: Linecount | None = None  # The primary id of a linecount dataset.
