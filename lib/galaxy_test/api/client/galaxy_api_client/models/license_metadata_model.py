from dataclasses import dataclass

from .see_also import SeeAlso

__all__ = ["LicenseMetadataModel"]


@dataclass
class LicenseMetadataModel:
    """
    LicenseMetadataModel dataclass.

    Args:
        details_url (str)        : URL to the SPDX json details for this license
        is_deprecated_license_id (bool)
                                 : True if the entire license is deprecated
        is_osi_approved (bool)   : Indicates if the [OSI](https://opensource.org/) has
                                   approved the license
        license_id (str)         : SPDX Identifier
        name (str)               : Full name of the license
        recommended (bool)       : True if this license is recommended to be used
        reference (str)          : Reference to the HTML format for the license file
        reference_number (int)   : *Deprecated* - this field is generated and is no longer
                                   in use
        see_also (SeeAlso)       : Cross reference URL pointing to additional copies of the
                                   license
        spdx_url (str)           :
        url (str)                : License URL
    """

    details_url: str  # URL to the SPDX json details for this license
    is_deprecated_license_id: bool  # True if the entire license is deprecated
    is_osi_approved: bool  # Indicates if the [OSI](https://opensource.org/) has approved the license
    license_id: str  # SPDX Identifier
    name: str  # Full name of the license
    recommended: bool  # True if this license is recommended to be used
    reference: str  # Reference to the HTML format for the license file
    reference_number: int  # *Deprecated* - this field is generated and is no longer in use
    see_also: SeeAlso  # Cross reference URL pointing to additional copies of the license
    spdx_url: str
    url: str  # License URL
