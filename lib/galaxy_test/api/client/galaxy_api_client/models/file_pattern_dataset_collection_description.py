from dataclasses import dataclass

from .directory import Directory
from .format_ import Format_
from .sort_comp import SortComp
from .sort_key import SortKey

__all__ = ["FilePatternDatasetCollectionDescription"]


@dataclass
class FilePatternDatasetCollectionDescription:
    """
    FilePatternDatasetCollectionDescription dataclass.

    Args:
        assign_primary_output (bool)
                                 :
        directory (Optional[Directory])
                                 :
        discover_via (str)       :
        format_ (Format_)        : The short name for the output datatype.
        match_relative_path (bool):
        pattern (str)            :
        recurse (bool)           :
        sort_comp (SortComp)     :
        sort_key (SortKey)       :
        visible (bool)           :
        sort_reverse (Optional[bool])
                                 :
    """

    assign_primary_output: bool
    directory: Directory | None
    discover_via: str
    format_: Format_  # The short name for the output datatype.
    match_relative_path: bool
    pattern: str
    recurse: bool
    sort_comp: SortComp
    sort_key: SortKey
    visible: bool
    sort_reverse: bool | None = False
