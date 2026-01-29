from dataclasses import dataclass

from .directory import Directory
from .format_ import Format_

__all__ = ["ToolProvidedMetadataDatasetCollection"]


@dataclass
class ToolProvidedMetadataDatasetCollection:
    """
    ToolProvidedMetadataDatasetCollection dataclass.

    Args:
        assign_primary_output (bool)
                                 :
        directory (Optional[Directory])
                                 :
        discover_via (str)       :
        format_ (Format_)        : The short name for the output datatype.
        match_relative_path (bool):
        recurse (bool)           :
        visible (bool)           :
    """

    assign_primary_output: bool
    directory: Directory | None
    discover_via: str
    format_: Format_  # The short name for the output datatype.
    match_relative_path: bool
    recurse: bool
    visible: bool
