from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.step_reference_by_label import StepReferenceByLabel
    from ..models.step_reference_by_order_index import StepReferenceByOrderIndex


T = TypeVar("T", bound="FillStepDefaultsAction")


@_attrs_define
class FillStepDefaultsAction:
    """
    Attributes:
        action_type (Literal['fill_step_defaults']):
        step (StepReferenceByLabel | StepReferenceByOrderIndex):
    """

    action_type: Literal["fill_step_defaults"]
    step: StepReferenceByLabel | StepReferenceByOrderIndex
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_reference_by_order_index import StepReferenceByOrderIndex

        action_type = self.action_type

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
                "step": step,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_reference_by_label import StepReferenceByLabel
        from ..models.step_reference_by_order_index import StepReferenceByOrderIndex

        d = dict(src_dict)
        action_type = cast(Literal["fill_step_defaults"], d.pop("action_type"))
        if action_type != "fill_step_defaults":
            raise ValueError(f"action_type must match const 'fill_step_defaults', got '{action_type}'")

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

        fill_step_defaults_action = cls(
            action_type=action_type,
            step=step,
        )

        fill_step_defaults_action.additional_properties = d
        return fill_step_defaults_action

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
