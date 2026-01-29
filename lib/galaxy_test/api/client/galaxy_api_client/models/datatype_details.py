from dataclasses import dataclass

from .datatype_details_composite_files import DatatypeDetailsCompositeFiles
from .datatype_details_description import DatatypeDetailsDescription
from .datatype_details_description_url import DatatypeDetailsDescriptionUrl
from .datatype_details_display_behavior import DatatypeDetailsDisplayBehavior
from .datatype_details_upload_warning import DatatypeDetailsUploadWarning

__all__ = ["DatatypeDetails"]


@dataclass
class DatatypeDetails:
    """
    DatatypeDetails dataclass

    Args:
        description (DatatypeDetailsDescription)
                                 : A summary description for this data type
        description_url (DatatypeDetailsDescriptionUrl)
                                 : The URL to a detailed description for this datatype
        extension (str)          : The data type’s Dataset file extension
        composite_files (DatatypeDetailsCompositeFiles | None)
                                 : A collection of files composing this data type
        display_behavior (DatatypeDetailsDisplayBehavior | None)
                                 : How this datatype behaves when displayed with
                                   preview=True: 'inline' (can be displayed in browser) or
                                   'download' (triggers download)
        display_in_upload (bool | None)
                                 : If True, the associated file extension will be displayed
                                   in the `File Format` select list in the `Upload File from
                                   your computer` tool in the `Get Data` tool section of the
                                   tool panel
        upload_warning (DatatypeDetailsUploadWarning | None)
                                 : End-user information regarding potential pitfalls with
                                   this upload type.
    """

    description: DatatypeDetailsDescription  # A summary description for this data type
    description_url: DatatypeDetailsDescriptionUrl  # The URL to a detailed description for this datatype
    extension: str  # The data type’s Dataset file extension
    composite_files: DatatypeDetailsCompositeFiles | None = None  # A collection of files composing this data type
    display_behavior: DatatypeDetailsDisplayBehavior | None = (
        None  # How this datatype behaves when displayed with preview=True: 'inline' (can be displayed in browser) or 'download' (triggers download)
    )
    display_in_upload: bool | None = (
        False  # If True, the associated file extension will be displayed in the `File Format` select list in the `Upload File from your computer` tool in the `Get Data` tool section of the tool panel
    )
    upload_warning: DatatypeDetailsUploadWarning | None = (
        None  # End-user information regarding potential pitfalls with this upload type.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "composite_files": "composite_files",
            "description": "description",
            "description_url": "description_url",
            "display_behavior": "display_behavior",
            "display_in_upload": "display_in_upload",
            "extension": "extension",
            "upload_warning": "upload_warning",
        }
        key_transform_with_dump = {
            "composite_files": "composite_files",
            "description": "description",
            "description_url": "description_url",
            "display_behavior": "display_behavior",
            "display_in_upload": "display_in_upload",
            "extension": "extension",
            "upload_warning": "upload_warning",
        }
