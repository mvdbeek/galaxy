from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position import Position


T = TypeVar("T", bound="AddInputAction")


@_attrs_define
class AddInputAction:
    """
    Attributes:
        action_type (Literal['add_input']):
        type_ (str):
        collection_type (None | str | Unset):
        default (Any | None | Unset):
        label (None | str | Unset):
        optional (bool | None | Unset):  Default: False.
        position (None | Position | Unset):
        restrict_on_connections (bool | None | Unset):
        restrictions (list[str] | None | Unset):
        suggestions (list[str] | None | Unset):
    """

    action_type: Literal["add_input"]
    type_: str
    collection_type: None | str | Unset = UNSET
    default: Any | None | Unset = UNSET
    label: None | str | Unset = UNSET
    optional: bool | None | Unset = False
    position: None | Position | Unset = UNSET
    restrict_on_connections: bool | None | Unset = UNSET
    restrictions: list[str] | None | Unset = UNSET
    suggestions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.position import Position

        action_type = self.action_type

        type_ = self.type_

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        default: Any | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        optional: bool | None | Unset
        if isinstance(self.optional, Unset):
            optional = UNSET
        else:
            optional = self.optional

        position: dict[str, Any] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, Position):
            position = self.position.to_dict()
        else:
            position = self.position

        restrict_on_connections: bool | None | Unset
        if isinstance(self.restrict_on_connections, Unset):
            restrict_on_connections = UNSET
        else:
            restrict_on_connections = self.restrict_on_connections

        restrictions: list[str] | None | Unset
        if isinstance(self.restrictions, Unset):
            restrictions = UNSET
        elif isinstance(self.restrictions, list):
            restrictions = self.restrictions

        else:
            restrictions = self.restrictions

        suggestions: list[str] | None | Unset
        if isinstance(self.suggestions, Unset):
            suggestions = UNSET
        elif isinstance(self.suggestions, list):
            suggestions = self.suggestions

        else:
            suggestions = self.suggestions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "type": type_,
            }
        )
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if default is not UNSET:
            field_dict["default"] = default
        if label is not UNSET:
            field_dict["label"] = label
        if optional is not UNSET:
            field_dict["optional"] = optional
        if position is not UNSET:
            field_dict["position"] = position
        if restrict_on_connections is not UNSET:
            field_dict["restrict_on_connections"] = restrict_on_connections
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position

        d = dict(src_dict)
        action_type = cast(Literal["add_input"], d.pop("action_type"))
        if action_type != "add_input":
            raise ValueError(f"action_type must match const 'add_input', got '{action_type}'")

        type_ = d.pop("type")

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_optional(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        optional = _parse_optional(d.pop("optional", UNSET))

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

        def _parse_restrict_on_connections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        restrict_on_connections = _parse_restrict_on_connections(d.pop("restrict_on_connections", UNSET))

        def _parse_restrictions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restrictions_type_0 = cast(list[str], data)

                return restrictions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        restrictions = _parse_restrictions(d.pop("restrictions", UNSET))

        def _parse_suggestions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggestions_type_0 = cast(list[str], data)

                return suggestions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        suggestions = _parse_suggestions(d.pop("suggestions", UNSET))

        add_input_action = cls(
            action_type=action_type,
            type_=type_,
            collection_type=collection_type,
            default=default,
            label=label,
            optional=optional,
            position=position,
            restrict_on_connections=restrict_on_connections,
            restrictions=restrictions,
            suggestions=suggestions,
        )

        add_input_action.additional_properties = d
        return add_input_action

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
