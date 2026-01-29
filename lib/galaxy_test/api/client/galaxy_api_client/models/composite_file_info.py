from dataclasses import dataclass

from .composite_file_info_description import CompositeFileInfoDescription
from .composite_file_info_mimetype import CompositeFileInfoMimetype
from .composite_file_info_substitute_name_with_metadata import CompositeFileInfoSubstituteNameWithMetadata

__all__ = ["CompositeFileInfo"]


@dataclass
class CompositeFileInfo:
    """
    CompositeFileInfo dataclass

    Args:
        description (CompositeFileInfoDescription)
                                 : Summary description of the purpouse of this file
        is_binary (bool)         : Whether this file is a binary file
        mimetype (CompositeFileInfoMimetype)
                                 : The MIME type of this file
        name (str)               : The name of this composite file
        optional (bool)          :
        space_to_tab (bool)      :
        substitute_name_with_metadata (CompositeFileInfoSubstituteNameWithMetadata)
                                 :
        to_posix_lines (bool)    :
    """

    description: CompositeFileInfoDescription  # Summary description of the purpouse of this file
    is_binary: bool  # Whether this file is a binary file
    mimetype: CompositeFileInfoMimetype  # The MIME type of this file
    name: str  # The name of this composite file
    optional: bool
    space_to_tab: bool
    substitute_name_with_metadata: CompositeFileInfoSubstituteNameWithMetadata
    to_posix_lines: bool

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "is_binary": "is_binary",
            "mimetype": "mimetype",
            "name": "name",
            "optional": "optional",
            "space_to_tab": "space_to_tab",
            "substitute_name_with_metadata": "substitute_name_with_metadata",
            "to_posix_lines": "to_posix_lines",
        }
        key_transform_with_dump = {
            "description": "description",
            "is_binary": "is_binary",
            "mimetype": "mimetype",
            "name": "name",
            "optional": "optional",
            "space_to_tab": "space_to_tab",
            "substitute_name_with_metadata": "substitute_name_with_metadata",
            "to_posix_lines": "to_posix_lines",
        }
