from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_credential_group_payload import ServiceCredentialGroupPayload


T = TypeVar("T", bound="ServiceCredentialPayload")


@_attrs_define
class ServiceCredentialPayload:
    """
    Attributes:
        group (ServiceCredentialGroupPayload):
        name (str): The name of the service requiring credentials.
        version (str): The version of the service.
    """

    group: ServiceCredentialGroupPayload
    name: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "name": name,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_credential_group_payload import ServiceCredentialGroupPayload

        d = dict(src_dict)
        group = ServiceCredentialGroupPayload.from_dict(d.pop("group"))

        name = d.pop("name")

        version = d.pop("version")

        service_credential_payload = cls(
            group=group,
            name=name,
            version=version,
        )

        service_credential_payload.additional_properties = d
        return service_credential_payload

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
