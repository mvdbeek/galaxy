from dataclasses import dataclass

from .description import Description
from .mimetype import Mimetype
from .substitute_name_with_metadata import SubstituteNameWithMetadata

__all__ = ["CompositeFileInfo"]


@dataclass
class CompositeFileInfo:
    """
    CompositeFileInfo dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        is_binary (bool)         : Whether this file is a binary file
        mimetype (Optional[Mimetype])
                                 : The MIME type of this file
        name (str)               : The name of this composite file
        optional (bool)          :
        space_to_tab (bool)      :
        substitute_name_with_metadata (Optional[SubstituteNameWithMetadata])
                                 :
        to_posix_lines (bool)    :
    """

    description: Description | None  # Detailed text description for this Quota.
    is_binary: bool  # Whether this file is a binary file
    mimetype: Mimetype | None  # The MIME type of this file
    name: str  # The name of this composite file
    optional: bool
    space_to_tab: bool
    substitute_name_with_metadata: SubstituteNameWithMetadata | None
    to_posix_lines: bool
