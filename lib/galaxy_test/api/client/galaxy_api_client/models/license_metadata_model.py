from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LicenseMetadataModel")


@_attrs_define
class LicenseMetadataModel:
    """
    Attributes:
        details_url (str): URL to the SPDX json details for this license
        is_deprecated_license_id (bool): True if the entire license is deprecated
        is_osi_approved (bool): Indicates if the [OSI](https://opensource.org/) has approved the license
        license_id (str): SPDX Identifier
        name (str): Full name of the license
        recommended (bool): True if this license is recommended to be used
        reference (str): Reference to the HTML format for the license file
        reference_number (int): *Deprecated* - this field is generated and is no longer in use
        see_also (list[str]): Cross reference URL pointing to additional copies of the license
        spdx_url (str):
        url (str): License URL
    """

    details_url: str
    is_deprecated_license_id: bool
    is_osi_approved: bool
    license_id: str
    name: str
    recommended: bool
    reference: str
    reference_number: int
    see_also: list[str]
    spdx_url: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details_url = self.details_url

        is_deprecated_license_id = self.is_deprecated_license_id

        is_osi_approved = self.is_osi_approved

        license_id = self.license_id

        name = self.name

        recommended = self.recommended

        reference = self.reference

        reference_number = self.reference_number

        see_also = self.see_also

        spdx_url = self.spdx_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detailsUrl": details_url,
                "isDeprecatedLicenseId": is_deprecated_license_id,
                "isOsiApproved": is_osi_approved,
                "licenseId": license_id,
                "name": name,
                "recommended": recommended,
                "reference": reference,
                "referenceNumber": reference_number,
                "seeAlso": see_also,
                "spdxUrl": spdx_url,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details_url = d.pop("detailsUrl")

        is_deprecated_license_id = d.pop("isDeprecatedLicenseId")

        is_osi_approved = d.pop("isOsiApproved")

        license_id = d.pop("licenseId")

        name = d.pop("name")

        recommended = d.pop("recommended")

        reference = d.pop("reference")

        reference_number = d.pop("referenceNumber")

        see_also = cast(list[str], d.pop("seeAlso"))

        spdx_url = d.pop("spdxUrl")

        url = d.pop("url")

        license_metadata_model = cls(
            details_url=details_url,
            is_deprecated_license_id=is_deprecated_license_id,
            is_osi_approved=is_osi_approved,
            license_id=license_id,
            name=name,
            recommended=recommended,
            reference=reference,
            reference_number=reference_number,
            see_also=see_also,
            spdx_url=spdx_url,
            url=url,
        )

        license_metadata_model.additional_properties = d
        return license_metadata_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
