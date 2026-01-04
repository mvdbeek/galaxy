from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_file_source_model_type import UserFileSourceModelType

if TYPE_CHECKING:
    from ..models.user_file_source_model_variables_type_0 import UserFileSourceModelVariablesType0


T = TypeVar("T", bound="UserFileSourceModel")


@_attrs_define
class UserFileSourceModel:
    """
    Attributes:
        active (bool):
        description (None | str):
        hidden (bool):
        name (str):
        purged (bool):
        secrets (list[str]):
        template_id (str):
        template_version (int):
        type_ (UserFileSourceModelType):
        uri_root (str):
        uuid (str):
        variables (None | UserFileSourceModelVariablesType0):
    """

    active: bool
    description: None | str
    hidden: bool
    name: str
    purged: bool
    secrets: list[str]
    template_id: str
    template_version: int
    type_: UserFileSourceModelType
    uri_root: str
    uuid: str
    variables: None | UserFileSourceModelVariablesType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_file_source_model_variables_type_0 import UserFileSourceModelVariablesType0

        active = self.active

        description: None | str
        description = self.description

        hidden = self.hidden

        name = self.name

        purged = self.purged

        secrets = self.secrets

        template_id = self.template_id

        template_version = self.template_version

        type_ = self.type_.value

        uri_root = self.uri_root

        uuid = self.uuid

        variables: dict[str, Any] | None
        if isinstance(self.variables, UserFileSourceModelVariablesType0):
            variables = self.variables.to_dict()
        else:
            variables = self.variables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "description": description,
                "hidden": hidden,
                "name": name,
                "purged": purged,
                "secrets": secrets,
                "template_id": template_id,
                "template_version": template_version,
                "type": type_,
                "uri_root": uri_root,
                "uuid": uuid,
                "variables": variables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_file_source_model_variables_type_0 import UserFileSourceModelVariablesType0

        d = dict(src_dict)
        active = d.pop("active")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        hidden = d.pop("hidden")

        name = d.pop("name")

        purged = d.pop("purged")

        secrets = cast(list[str], d.pop("secrets"))

        template_id = d.pop("template_id")

        template_version = d.pop("template_version")

        type_ = UserFileSourceModelType(d.pop("type"))

        uri_root = d.pop("uri_root")

        uuid = d.pop("uuid")

        def _parse_variables(data: object) -> None | UserFileSourceModelVariablesType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                variables_type_0 = UserFileSourceModelVariablesType0.from_dict(data)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserFileSourceModelVariablesType0, data)

        variables = _parse_variables(d.pop("variables"))

        user_file_source_model = cls(
            active=active,
            description=description,
            hidden=hidden,
            name=name,
            purged=purged,
            secrets=secrets,
            template_id=template_id,
            template_version=template_version,
            type_=type_,
            uri_root=uri_root,
            uuid=uuid,
            variables=variables,
        )

        user_file_source_model.additional_properties = d
        return user_file_source_model

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
