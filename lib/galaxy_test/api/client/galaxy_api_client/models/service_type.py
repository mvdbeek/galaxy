from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServiceType")


@_attrs_define
class ServiceType:
    """
    Attributes:
        artifact (str): Name of the API or GA4GH specification implemented. Official GA4GH types should be assigned as
            part of standards approval process. Custom artifacts are supported.
        group (str): Namespace in reverse domain name format. Use `org.ga4gh` for implementations compliant with
            official GA4GH specifications. For services with custom APIs not standardized by GA4GH, or implementations
            diverging from official GA4GH specifications, use a different namespace (e.g. your organization's reverse domain
            name).
        version (str): Version of the API or specification. GA4GH specifications use semantic versioning.
    """

    artifact: str
    group: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact = self.artifact

        group = self.group

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artifact": artifact,
                "group": group,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact = d.pop("artifact")

        group = d.pop("group")

        version = d.pop("version")

        service_type = cls(
            artifact=artifact,
            group=group,
            version=version,
        )

        service_type.additional_properties = d
        return service_type

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
