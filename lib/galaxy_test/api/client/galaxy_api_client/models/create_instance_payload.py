from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secrets import Secrets
    from ..models.variables import Variables


T = TypeVar("T", bound="CreateInstancePayload")


@_attrs_define
class CreateInstancePayload:
    """
    Attributes:
        name (str):
        secrets (Secrets):
        template_id (str):
        template_version (int):
        variables (Variables):
        description (None | str | Unset):
        uuid (None | str | Unset):
    """

    name: str
    secrets: Secrets
    template_id: str
    template_version: int
    variables: Variables
    description: None | str | Unset = UNSET
    uuid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secrets = self.secrets.to_dict()

        template_id = self.template_id

        template_version = self.template_version

        variables = self.variables.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "secrets": secrets,
                "template_id": template_id,
                "template_version": template_version,
                "variables": variables,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secrets import Secrets
        from ..models.variables import Variables

        d = dict(src_dict)
        name = d.pop("name")

        secrets = Secrets.from_dict(d.pop("secrets"))

        template_id = d.pop("template_id")

        template_version = d.pop("template_version")

        variables = Variables.from_dict(d.pop("variables"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        create_instance_payload = cls(
            name=name,
            secrets=secrets,
            template_id=template_id,
            template_version=template_version,
            variables=variables,
            description=description,
            uuid=uuid,
        )

        create_instance_payload.additional_properties = d
        return create_instance_payload

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
