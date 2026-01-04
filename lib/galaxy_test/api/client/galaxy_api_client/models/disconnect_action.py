from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.input_reference_by_label import InputReferenceByLabel
    from ..models.input_reference_by_order_index import InputReferenceByOrderIndex
    from ..models.output_reference_by_label import OutputReferenceByLabel
    from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex


T = TypeVar("T", bound="DisconnectAction")


@_attrs_define
class DisconnectAction:
    """
    Attributes:
        action_type (Literal['disconnect']):
        input_ (InputReferenceByLabel | InputReferenceByOrderIndex):
        output (OutputReferenceByLabel | OutputReferenceByOrderIndex):
    """

    action_type: Literal["disconnect"]
    input_: InputReferenceByLabel | InputReferenceByOrderIndex
    output: OutputReferenceByLabel | OutputReferenceByOrderIndex
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_reference_by_order_index import InputReferenceByOrderIndex
        from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex

        action_type = self.action_type

        input_: dict[str, Any]
        if isinstance(self.input_, InputReferenceByOrderIndex):
            input_ = self.input_.to_dict()
        else:
            input_ = self.input_.to_dict()

        output: dict[str, Any]
        if isinstance(self.output, OutputReferenceByOrderIndex):
            output = self.output.to_dict()
        else:
            output = self.output.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "input": input_,
                "output": output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_reference_by_label import InputReferenceByLabel
        from ..models.input_reference_by_order_index import InputReferenceByOrderIndex
        from ..models.output_reference_by_label import OutputReferenceByLabel
        from ..models.output_reference_by_order_index import OutputReferenceByOrderIndex

        d = dict(src_dict)
        action_type = cast(Literal["disconnect"], d.pop("action_type"))
        if action_type != "disconnect":
            raise ValueError(f"action_type must match const 'disconnect', got '{action_type}'")

        def _parse_input_(data: object) -> InputReferenceByLabel | InputReferenceByOrderIndex:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_type_0 = InputReferenceByOrderIndex.from_dict(data)

                return input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            input_type_1 = InputReferenceByLabel.from_dict(data)

            return input_type_1

        input_ = _parse_input_(d.pop("input"))

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

        disconnect_action = cls(
            action_type=action_type,
            input_=input_,
            output=output,
        )

        disconnect_action.additional_properties = d
        return disconnect_action

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
