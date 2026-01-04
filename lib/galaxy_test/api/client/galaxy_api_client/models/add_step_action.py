from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_step_action_tool_state_type_0 import AddStepActionToolStateType0
    from ..models.position import Position


T = TypeVar("T", bound="AddStepAction")


@_attrs_define
class AddStepAction:
    """Add a new action to the workflow.

    After the workflow is updated, an order_index will be assigned
    and this step may cause other steps to have their output_index
    adjusted.

        Attributes:
            action_type (Literal['add_step']):
            type_ (str): Module type of the step to add, see galaxy.workflow.modules for available types.
            label (None | str | Unset): A unique label for the step being added, must be distinct from the labels already
                present in the workflow.
            position (None | Position | Unset): The location of the step in the Galaxy workflow editor.
            tool_state (AddStepActionToolStateType0 | None | Unset):
    """

    action_type: Literal["add_step"]
    type_: str
    label: None | str | Unset = UNSET
    position: None | Position | Unset = UNSET
    tool_state: AddStepActionToolStateType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_step_action_tool_state_type_0 import AddStepActionToolStateType0
        from ..models.position import Position

        action_type = self.action_type

        type_ = self.type_

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

        tool_state: dict[str, Any] | None | Unset
        if isinstance(self.tool_state, Unset):
            tool_state = UNSET
        elif isinstance(self.tool_state, AddStepActionToolStateType0):
            tool_state = self.tool_state.to_dict()
        else:
            tool_state = self.tool_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "type": type_,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if position is not UNSET:
            field_dict["position"] = position
        if tool_state is not UNSET:
            field_dict["tool_state"] = tool_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_step_action_tool_state_type_0 import AddStepActionToolStateType0
        from ..models.position import Position

        d = dict(src_dict)
        action_type = cast(Literal["add_step"], d.pop("action_type"))
        if action_type != "add_step":
            raise ValueError(f"action_type must match const 'add_step', got '{action_type}'")

        type_ = d.pop("type")

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

        def _parse_tool_state(data: object) -> AddStepActionToolStateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tool_state_type_0 = AddStepActionToolStateType0.from_dict(data)

                return tool_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddStepActionToolStateType0 | None | Unset, data)

        tool_state = _parse_tool_state(d.pop("tool_state", UNSET))

        add_step_action = cls(
            action_type=action_type,
            type_=type_,
            label=label,
            position=position,
            tool_state=tool_state,
        )

        add_step_action.additional_properties = d
        return add_step_action

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
