from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCreatorAction")


@_attrs_define
class UpdateCreatorAction:
    """
    Attributes:
        action_type (Literal['update_creator']):
        creator (Any | Unset):
    """

    action_type: Literal["update_creator"]
    creator: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        creator = self.creator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
            }
        )
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = cast(Literal["update_creator"], d.pop("action_type"))
        if action_type != "update_creator":
            raise ValueError(f"action_type must match const 'update_creator', got '{action_type}'")

        creator = d.pop("creator", UNSET)

        update_creator_action = cls(
            action_type=action_type,
            creator=creator,
        )

        update_creator_action.additional_properties = d
        return update_creator_action

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
