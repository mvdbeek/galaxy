from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position import Position
    from ..models.step_reference_by_label import StepReferenceByLabel
    from ..models.step_reference_by_order_index import StepReferenceByOrderIndex


T = TypeVar("T", bound="UpdateStepPositionAction")


@_attrs_define
class UpdateStepPositionAction:
    """
    Attributes:
        action_type (Literal['update_step_position']):
        position_shift (Position):
        step (StepReferenceByLabel | StepReferenceByOrderIndex): The target step for this action.
    """

    action_type: Literal["update_step_position"]
    position_shift: Position
    step: StepReferenceByLabel | StepReferenceByOrderIndex
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_reference_by_order_index import StepReferenceByOrderIndex

        action_type = self.action_type

        position_shift = self.position_shift.to_dict()

        step: dict[str, Any]
        if isinstance(self.step, StepReferenceByOrderIndex):
            step = self.step.to_dict()
        else:
            step = self.step.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "position_shift": position_shift,
                "step": step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position
        from ..models.step_reference_by_label import StepReferenceByLabel
        from ..models.step_reference_by_order_index import StepReferenceByOrderIndex

        d = dict(src_dict)
        action_type = cast(Literal["update_step_position"], d.pop("action_type"))
        if action_type != "update_step_position":
            raise ValueError(f"action_type must match const 'update_step_position', got '{action_type}'")

        position_shift = Position.from_dict(d.pop("position_shift"))

        def _parse_step(data: object) -> StepReferenceByLabel | StepReferenceByOrderIndex:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_type_0 = StepReferenceByOrderIndex.from_dict(data)

                return step_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            step_type_1 = StepReferenceByLabel.from_dict(data)

            return step_type_1

        step = _parse_step(d.pop("step"))

        update_step_position_action = cls(
            action_type=action_type,
            position_shift=position_shift,
            step=step,
        )

        update_step_position_action.additional_properties = d
        return update_step_position_action

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
