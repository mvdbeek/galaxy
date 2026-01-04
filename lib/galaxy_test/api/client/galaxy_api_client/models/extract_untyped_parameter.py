from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="ExtractUntypedParameter")


@_attrs_define
class ExtractUntypedParameter:
    """
    Attributes:
        action_type (Literal['extract_untyped_parameter']):
        name (str):
        label (None | str | Unset):
        position (None | Position | Unset):
    """

    action_type: Literal["extract_untyped_parameter"]
    name: str
    label: None | str | Unset = UNSET
    position: None | Position | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.position import Position

        action_type = self.action_type

        name = self.name

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        position: dict[str, Any] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, Position):
            position = self.position.to_dict()
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position

        d = dict(src_dict)
        action_type = cast(Literal["extract_untyped_parameter"], d.pop("action_type"))
        if action_type != "extract_untyped_parameter":
            raise ValueError(f"action_type must match const 'extract_untyped_parameter', got '{action_type}'")

        name = d.pop("name")

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_position(data: object) -> None | Position | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = Position.from_dict(data)

                return position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Position | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        extract_untyped_parameter = cls(
            action_type=action_type,
            name=name,
            label=label,
            position=position,
        )

        extract_untyped_parameter.additional_properties = d
        return extract_untyped_parameter

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
