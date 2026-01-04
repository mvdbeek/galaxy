from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_reference_by_label import OutputReferenceByLabel
    from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex


T = TypeVar("T", bound="UpdateOutputLabelAction")


@_attrs_define
class UpdateOutputLabelAction:
    """
    Attributes:
        action_type (Literal['update_output_label']):
        output (OutputReferenceByLabel | OutputReferenceByOrderIndex):
        output_label (str):
    """

    action_type: Literal["update_output_label"]
    output: OutputReferenceByLabel | OutputReferenceByOrderIndex
    output_label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex

        action_type = self.action_type

        output: dict[str, Any]
        if isinstance(self.output, OutputReferenceByOrderIndex):
            output = self.output.to_dict()
        else:
            output = self.output.to_dict()

        output_label = self.output_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "output": output,
                "output_label": output_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_reference_by_label import OutputReferenceByLabel
        from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex

        d = dict(src_dict)
        action_type = cast(Literal["update_output_label"], d.pop("action_type"))
        if action_type != "update_output_label":
            raise ValueError(f"action_type must match const 'update_output_label', got '{action_type}'")

        def _parse_output(data: object) -> OutputReferenceByLabel | OutputReferenceByOrderIndex:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_type_0 = OutputReferenceByOrderIndex.from_dict(data)

                return output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            output_type_1 = OutputReferenceByLabel.from_dict(data)

            return output_type_1

        output = _parse_output(d.pop("output"))

        output_label = d.pop("output_label")

        update_output_label_action = cls(
            action_type=action_type,
            output=output,
            output_label=output_label,
        )

        update_output_label_action.additional_properties = d
        return update_output_label_action

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
