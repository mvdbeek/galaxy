from dataclasses import dataclass

__all__ = ["LicenseMetadataModel"]


@dataclass
class LicenseMetadataModel:
    """
    LicenseMetadataModel dataclass

    Args:
        details_url (str)        : URL to the SPDX json details for this license (maps from
                                   'detailsUrl')
        is_deprecated_license_id (bool)
                                 : True if the entire license is deprecated (maps from
                                   'isDeprecatedLicenseId')
        is_osi_approved (bool)   : Indicates if the [OSI](https://opensource.org/) has
                                   approved the license (maps from 'isOsiApproved')
        license_id (str)         : SPDX Identifier (maps from 'licenseId')
        name (str)               : Full name of the license
        recommended (bool)       : True if this license is recommended to be used
        reference (str)          : Reference to the HTML format for the license file
        reference_number (int)   : *Deprecated* - this field is generated and is no longer
                                   in use (maps from 'referenceNumber')
        see_also (List[str])     : Cross reference URL pointing to additional copies of the
                                   license (maps from 'seeAlso')
        spdx_url (str)           : Maps from 'spdxUrl'
        url (str)                : License URL
    """

    details_url: str  # URL to the SPDX json details for this license (maps from 'detailsUrl')
    is_deprecated_license_id: bool  # True if the entire license is deprecated (maps from 'isDeprecatedLicenseId')
    is_osi_approved: (
        bool  # Indicates if the [OSI](https://opensource.org/) has approved the license (maps from 'isOsiApproved')
    )
    license_id: str  # SPDX Identifier (maps from 'licenseId')
    name: str  # Full name of the license
    recommended: bool  # True if this license is recommended to be used
    reference: str  # Reference to the HTML format for the license file
    reference_number: (
        int  # *Deprecated* - this field is generated and is no longer in use (maps from 'referenceNumber')
    )
    see_also: list[str]  # Cross reference URL pointing to additional copies of the license (maps from 'seeAlso')
    spdx_url: str  # Maps from 'spdxUrl'
    url: str  # License URL

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "detailsUrl": "details_url",
            "isDeprecatedLicenseId": "is_deprecated_license_id",
            "isOsiApproved": "is_osi_approved",
            "licenseId": "license_id",
            "name": "name",
            "recommended": "recommended",
            "reference": "reference",
            "referenceNumber": "reference_number",
            "seeAlso": "see_also",
            "spdxUrl": "spdx_url",
            "url": "url",
        }
        key_transform_with_dump = {
            "details_url": "detailsUrl",
            "is_deprecated_license_id": "isDeprecatedLicenseId",
            "is_osi_approved": "isOsiApproved",
            "license_id": "licenseId",
            "name": "name",
            "recommended": "recommended",
            "reference": "reference",
            "reference_number": "referenceNumber",
            "see_also": "seeAlso",
            "spdx_url": "spdxUrl",
            "url": "url",
        }
