from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpgradeAllStepsAction")


@_attrs_define
class UpgradeAllStepsAction:
    """
    Attributes:
        action_type (Literal['upgrade_all_steps']):
    """

    action_type: Literal["upgrade_all_steps"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = cast(Literal["upgrade_all_steps"], d.pop("action_type"))
        if action_type != "upgrade_all_steps":
            raise ValueError(f"action_type must match const 'upgrade_all_steps', got '{action_type}'")

        upgrade_all_steps_action = cls(
            action_type=action_type,
        )

        upgrade_all_steps_action.additional_properties = d
        return upgrade_all_steps_action

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
