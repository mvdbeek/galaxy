from dataclasses import dataclass

from .composite_files import CompositeFiles
from .description import Description
from .description_url import DescriptionUrl
from .display_behavior import DisplayBehavior
from .upload_warning import UploadWarning

__all__ = ["DatatypeDetails"]


@dataclass
class DatatypeDetails:
    """
    DatatypeDetails dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        description_url (Optional[DescriptionUrl])
                                 : The URL to a detailed description for this datatype
        extension (str)          : The data type’s Dataset file extension
        composite_files (Optional[CompositeFiles])
                                 : A collection of files composing this data type
        display_behavior (Optional[DisplayBehavior])
                                 : How this datatype behaves when displayed with
                                   preview=True: 'inline' (can be displayed in browser) or
                                   'download' (triggers download)
        display_in_upload (Optional[bool])
                                 : If True, the associated file extension will be displayed
                                   in the `File Format` select list in the `Upload File from
                                   your computer` tool in the `Get Data` tool section of the
                                   tool panel
        upload_warning (Optional[UploadWarning])
                                 : End-user information regarding potential pitfalls with
                                   this upload type.
    """

    description: Description | None  # Detailed text description for this Quota.
    description_url: DescriptionUrl | None  # The URL to a detailed description for this datatype
    extension: str  # The data type’s Dataset file extension
    composite_files: CompositeFiles | None = None  # A collection of files composing this data type
    display_behavior: DisplayBehavior | None = (
        None  # How this datatype behaves when displayed with preview=True: 'inline' (can be displayed in browser) or 'download' (triggers download)
    )
    display_in_upload: bool | None = (
        False  # If True, the associated file extension will be displayed in the `File Format` select list in the `Upload File from your computer` tool in the `Get Data` tool section of the tool panel
    )
    upload_warning: UploadWarning | None = (
        None  # End-user information regarding potential pitfalls with this upload type.
    )
