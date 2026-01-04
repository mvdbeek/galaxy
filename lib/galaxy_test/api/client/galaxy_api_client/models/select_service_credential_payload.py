from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.select_current_group_payload import SelectCurrentGroupPayload


T = TypeVar("T", bound="SelectServiceCredentialPayload")


@_attrs_define
class SelectServiceCredentialPayload:
    """
    Attributes:
        service_credentials (list[SelectCurrentGroupPayload]): List of user credentials to update with current group
            selections.
        source_id (str): The ID of the source (e.g., tool ID).
        source_type (Literal['tool']): The type of source requiring credentials.
        source_version (str): The version of the source.
    """

    service_credentials: list[SelectCurrentGroupPayload]
    source_id: str
    source_type: Literal["tool"]
    source_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_credentials = []
        for service_credentials_item_data in self.service_credentials:
            service_credentials_item = service_credentials_item_data.to_dict()
            service_credentials.append(service_credentials_item)

        source_id = self.source_id

        source_type = self.source_type

        source_version = self.source_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_credentials": service_credentials,
                "source_id": source_id,
                "source_type": source_type,
                "source_version": source_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.select_current_group_payload import SelectCurrentGroupPayload

        d = dict(src_dict)
        service_credentials = []
        _service_credentials = d.pop("service_credentials")
        for service_credentials_item_data in _service_credentials:
            service_credentials_item = SelectCurrentGroupPayload.from_dict(service_credentials_item_data)

            service_credentials.append(service_credentials_item)

        source_id = d.pop("source_id")

        source_type = cast(Literal["tool"], d.pop("source_type"))
        if source_type != "tool":
            raise ValueError(f"source_type must match const 'tool', got '{source_type}'")

        source_version = d.pop("source_version")

        select_service_credential_payload = cls(
            service_credentials=service_credentials,
            source_id=source_id,
            source_type=source_type,
            source_version=source_version,
        )

        select_service_credential_payload.additional_properties = d
        return select_service_credential_payload

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
