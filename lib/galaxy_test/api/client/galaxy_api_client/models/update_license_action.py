from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateLicenseAction")


@_attrs_define
class UpdateLicenseAction:
    """
    Attributes:
        action_type (Literal['update_license']):
        license_ (str):
    """

    action_type: Literal["update_license"]
    license_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        license_ = self.license_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "license": license_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = cast(Literal["update_license"], d.pop("action_type"))
        if action_type != "update_license":
            raise ValueError(f"action_type must match const 'update_license', got '{action_type}'")

        license_ = d.pop("license")

        update_license_action = cls(
            action_type=action_type,
            license_=license_,
        )

        update_license_action.additional_properties = d
        return update_license_action

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
