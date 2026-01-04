from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.refactor_action_execution_message_type_enum import RefactorActionExecutionMessageTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RefactorActionExecutionMessage")


@_attrs_define
class RefactorActionExecutionMessage:
    """
    Attributes:
        message (str):
        message_type (RefactorActionExecutionMessageTypeEnum):
        from_order_index (int | None | Unset): For dropped connections these optional attributes refer to the output
            side of the connection that was dropped.
        from_step_label (None | str | Unset): For dropped connections these optional attributes refer to the output
            side of the connection that was dropped.
        input_name (None | str | Unset): If this message is about an input to a step,
            this field describes the target input name. $The input name as defined by the workflow module corresponding to
            the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g.
            'cond|repeat_0|input').
        order_index (int | None | Unset): Reference to the step the message refers to. $

            Messages don't have to be bound to a step, but if they are they will
            have a step_label and order_index included in the execution message.
            These are the label and order_index before applying the refactoring,
            the result of applying the action may change one or both of these.
            If connections are dropped this step reference will refer to the
            step with the previously connected input.
        output_label (None | str | Unset): If the message_type is workflow_output_drop_forced, this is the output label
            dropped.
        output_name (None | str | Unset): If this message is about an output to a step,
            this field describes the target output name. The output name as defined by the workflow module corresponding to
            the step being referenced.
        step_label (None | str | Unset): Reference to the step the message refers to. $

            Messages don't have to be bound to a step, but if they are they will
            have a step_label and order_index included in the execution message.
            These are the label and order_index before applying the refactoring,
            the result of applying the action may change one or both of these.
            If connections are dropped this step reference will refer to the
            step with the previously connected input.
    """

    message: str
    message_type: RefactorActionExecutionMessageTypeEnum
    from_order_index: int | None | Unset = UNSET
    from_step_label: None | str | Unset = UNSET
    input_name: None | str | Unset = UNSET
    order_index: int | None | Unset = UNSET
    output_label: None | str | Unset = UNSET
    output_name: None | str | Unset = UNSET
    step_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        message_type = self.message_type.value

        from_order_index: int | None | Unset
        if isinstance(self.from_order_index, Unset):
            from_order_index = UNSET
        else:
            from_order_index = self.from_order_index

        from_step_label: None | str | Unset
        if isinstance(self.from_step_label, Unset):
            from_step_label = UNSET
        else:
            from_step_label = self.from_step_label

        input_name: None | str | Unset
        if isinstance(self.input_name, Unset):
            input_name = UNSET
        else:
            input_name = self.input_name

        order_index: int | None | Unset
        if isinstance(self.order_index, Unset):
            order_index = UNSET
        else:
            order_index = self.order_index

        output_label: None | str | Unset
        if isinstance(self.output_label, Unset):
            output_label = UNSET
        else:
            output_label = self.output_label

        output_name: None | str | Unset
        if isinstance(self.output_name, Unset):
            output_name = UNSET
        else:
            output_name = self.output_name

        step_label: None | str | Unset
        if isinstance(self.step_label, Unset):
            step_label = UNSET
        else:
            step_label = self.step_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "message_type": message_type,
            }
        )
        if from_order_index is not UNSET:
            field_dict["from_order_index"] = from_order_index
        if from_step_label is not UNSET:
            field_dict["from_step_label"] = from_step_label
        if input_name is not UNSET:
            field_dict["input_name"] = input_name
        if order_index is not UNSET:
            field_dict["order_index"] = order_index
        if output_label is not UNSET:
            field_dict["output_label"] = output_label
        if output_name is not UNSET:
            field_dict["output_name"] = output_name
        if step_label is not UNSET:
            field_dict["step_label"] = step_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        message_type = RefactorActionExecutionMessageTypeEnum(d.pop("message_type"))

        def _parse_from_order_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        from_order_index = _parse_from_order_index(d.pop("from_order_index", UNSET))

        def _parse_from_step_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_step_label = _parse_from_step_label(d.pop("from_step_label", UNSET))

        def _parse_input_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_name = _parse_input_name(d.pop("input_name", UNSET))

        def _parse_order_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order_index = _parse_order_index(d.pop("order_index", UNSET))

        def _parse_output_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_label = _parse_output_label(d.pop("output_label", UNSET))

        def _parse_output_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_name = _parse_output_name(d.pop("output_name", UNSET))

        def _parse_step_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_label = _parse_step_label(d.pop("step_label", UNSET))

        refactor_action_execution_message = cls(
            message=message,
            message_type=message_type,
            from_order_index=from_order_index,
            from_step_label=from_step_label,
            input_name=input_name,
            order_index=order_index,
            output_label=output_label,
            output_name=output_name,
            step_label=step_label,
        )

        refactor_action_execution_message.additional_properties = d
        return refactor_action_execution_message

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
