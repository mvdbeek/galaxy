from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_concrete_object_store_model_type import UserConcreteObjectStoreModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_dict import BadgeDict
    from ..models.quota_model import QuotaModel
    from ..models.user_concrete_object_store_model_variables_type_0 import UserConcreteObjectStoreModelVariablesType0


T = TypeVar("T", bound="UserConcreteObjectStoreModel")


@_attrs_define
class UserConcreteObjectStoreModel:
    """
    Attributes:
        active (bool):
        badges (list[BadgeDict]):
        hidden (bool):
        private (bool):
        purged (bool):
        quota (QuotaModel):
        secrets (list[str]):
        template_id (str):
        template_version (int):
        type_ (UserConcreteObjectStoreModelType):
        uuid (str):
        variables (None | UserConcreteObjectStoreModelVariablesType0):
        description (None | str | Unset):
        device (None | str | Unset):
        name (None | str | Unset):
        object_expires_after_days (int | None | Unset):
        object_store_id (None | str | Unset):
    """

    active: bool
    badges: list[BadgeDict]
    hidden: bool
    private: bool
    purged: bool
    quota: QuotaModel
    secrets: list[str]
    template_id: str
    template_version: int
    type_: UserConcreteObjectStoreModelType
    uuid: str
    variables: None | UserConcreteObjectStoreModelVariablesType0
    description: None | str | Unset = UNSET
    device: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    object_expires_after_days: int | None | Unset = UNSET
    object_store_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_concrete_object_store_model_variables_type_0 import (
            UserConcreteObjectStoreModelVariablesType0,
        )

        active = self.active

        badges = []
        for badges_item_data in self.badges:
            badges_item = badges_item_data.to_dict()
            badges.append(badges_item)

        hidden = self.hidden

        private = self.private

        purged = self.purged

        quota = self.quota.to_dict()

        secrets = self.secrets

        template_id = self.template_id

        template_version = self.template_version

        type_ = self.type_.value

        uuid = self.uuid

        variables: dict[str, Any] | None
        if isinstance(self.variables, UserConcreteObjectStoreModelVariablesType0):
            variables = self.variables.to_dict()
        else:
            variables = self.variables

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        device: None | str | Unset
        if isinstance(self.device, Unset):
            device = UNSET
        else:
            device = self.device

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        object_expires_after_days: int | None | Unset
        if isinstance(self.object_expires_after_days, Unset):
            object_expires_after_days = UNSET
        else:
            object_expires_after_days = self.object_expires_after_days

        object_store_id: None | str | Unset
        if isinstance(self.object_store_id, Unset):
            object_store_id = UNSET
        else:
            object_store_id = self.object_store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "badges": badges,
                "hidden": hidden,
                "private": private,
                "purged": purged,
                "quota": quota,
                "secrets": secrets,
                "template_id": template_id,
                "template_version": template_version,
                "type": type_,
                "uuid": uuid,
                "variables": variables,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if device is not UNSET:
            field_dict["device"] = device
        if name is not UNSET:
            field_dict["name"] = name
        if object_expires_after_days is not UNSET:
            field_dict["object_expires_after_days"] = object_expires_after_days
        if object_store_id is not UNSET:
            field_dict["object_store_id"] = object_store_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge_dict import BadgeDict
        from ..models.quota_model import QuotaModel
        from ..models.user_concrete_object_store_model_variables_type_0 import (
            UserConcreteObjectStoreModelVariablesType0,
        )

        d = dict(src_dict)
        active = d.pop("active")

        badges = []
        _badges = d.pop("badges")
        for badges_item_data in _badges:
            badges_item = BadgeDict.from_dict(badges_item_data)

            badges.append(badges_item)

        hidden = d.pop("hidden")

        private = d.pop("private")

        purged = d.pop("purged")

        quota = QuotaModel.from_dict(d.pop("quota"))

        secrets = cast(list[str], d.pop("secrets"))

        template_id = d.pop("template_id")

        template_version = d.pop("template_version")

        type_ = UserConcreteObjectStoreModelType(d.pop("type"))

        uuid = d.pop("uuid")

        def _parse_variables(data: object) -> None | UserConcreteObjectStoreModelVariablesType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                variables_type_0 = UserConcreteObjectStoreModelVariablesType0.from_dict(data)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserConcreteObjectStoreModelVariablesType0, data)

        variables = _parse_variables(d.pop("variables"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_device(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_object_expires_after_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        object_expires_after_days = _parse_object_expires_after_days(d.pop("object_expires_after_days", UNSET))

        def _parse_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_store_id = _parse_object_store_id(d.pop("object_store_id", UNSET))

        user_concrete_object_store_model = cls(
            active=active,
            badges=badges,
            hidden=hidden,
            private=private,
            purged=purged,
            quota=quota,
            secrets=secrets,
            template_id=template_id,
            template_version=template_version,
            type_=type_,
            uuid=uuid,
            variables=variables,
            description=description,
            device=device,
            name=name,
            object_expires_after_days=object_expires_after_days,
            object_store_id=object_store_id,
        )

        user_concrete_object_store_model.additional_properties = d
        return user_concrete_object_store_model

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
