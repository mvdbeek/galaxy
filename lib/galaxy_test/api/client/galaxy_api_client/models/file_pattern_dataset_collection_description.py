from dataclasses import dataclass

from .file_pattern_dataset_collection_description_directory import FilePatternDatasetCollectionDescriptionDirectory
from .file_pattern_dataset_collection_description_sort_comp import FilePatternDatasetCollectionDescriptionSortComp
from .file_pattern_dataset_collection_description_sort_key import FilePatternDatasetCollectionDescriptionSortKey
from .format__2 import Format2

__all__ = ["FilePatternDatasetCollectionDescription"]


@dataclass
class FilePatternDatasetCollectionDescription:
    """
    FilePatternDatasetCollectionDescription dataclass

    Args:
        assign_primary_output (bool)
                                 :
        directory (FilePatternDatasetCollectionDescriptionDirectory)
                                 :
        discover_via (str)       :
        format_ (Format2 | None) : Maps from 'format'
        match_relative_path (bool):
        pattern (str)            :
        recurse (bool)           :
        sort_comp (FilePatternDatasetCollectionDescriptionSortComp)
                                 :
        sort_key (FilePatternDatasetCollectionDescriptionSortKey)
                                 :
        visible (bool)           :
        sort_reverse (bool | None):
    """

    assign_primary_output: bool
    directory: FilePatternDatasetCollectionDescriptionDirectory
    discover_via: str
    format_: Format2 | None  # Maps from 'format'
    match_relative_path: bool
    pattern: str
    recurse: bool
    sort_comp: FilePatternDatasetCollectionDescriptionSortComp
    sort_key: FilePatternDatasetCollectionDescriptionSortKey
    visible: bool
    sort_reverse: bool | None = False

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "assign_primary_output": "assign_primary_output",
            "directory": "directory",
            "discover_via": "discover_via",
            "format": "format_",
            "match_relative_path": "match_relative_path",
            "pattern": "pattern",
            "recurse": "recurse",
            "sort_comp": "sort_comp",
            "sort_key": "sort_key",
            "sort_reverse": "sort_reverse",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "assign_primary_output": "assign_primary_output",
            "directory": "directory",
            "discover_via": "discover_via",
            "format_": "format",
            "match_relative_path": "match_relative_path",
            "pattern": "pattern",
            "recurse": "recurse",
            "sort_comp": "sort_comp",
            "sort_key": "sort_key",
            "sort_reverse": "sort_reverse",
            "visible": "visible",
        }
