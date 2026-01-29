from dataclasses import dataclass

from .format__3 import Format3
from .tool_provided_metadata_dataset_collection_directory import ToolProvidedMetadataDatasetCollectionDirectory

__all__ = ["ToolProvidedMetadataDatasetCollection"]


@dataclass
class ToolProvidedMetadataDatasetCollection:
    """
    ToolProvidedMetadataDatasetCollection dataclass

    Args:
        assign_primary_output (bool)
                                 :
        directory (ToolProvidedMetadataDatasetCollectionDirectory)
                                 :
        discover_via (str)       :
        format_ (Format3 | None) : Maps from 'format'
        match_relative_path (bool):
        recurse (bool)           :
        visible (bool)           :
    """

    assign_primary_output: bool
    directory: ToolProvidedMetadataDatasetCollectionDirectory
    discover_via: str
    format_: Format3 | None  # Maps from 'format'
    match_relative_path: bool
    recurse: bool
    visible: bool

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "assign_primary_output": "assign_primary_output",
            "directory": "directory",
            "discover_via": "discover_via",
            "format": "format_",
            "match_relative_path": "match_relative_path",
            "recurse": "recurse",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "assign_primary_output": "assign_primary_output",
            "directory": "directory",
            "discover_via": "discover_via",
            "format_": "format",
            "match_relative_path": "match_relative_path",
            "recurse": "recurse",
            "visible": "visible",
        }
