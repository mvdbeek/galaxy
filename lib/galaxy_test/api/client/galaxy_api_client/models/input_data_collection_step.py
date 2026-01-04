from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_steps import InputSteps


T = TypeVar("T", bound="InputDataCollectionStep")


@_attrs_define
class InputDataCollectionStep:
    """
    Attributes:
        annotation (None | str): An annotation to provide details or to help understand the purpose and usage of this
            item.
        id (int): The identifier of the step. It matches the index order of the step inside the workflow.
        input_steps (InputSteps): A dictionary containing information about the inputs connected to this workflow step.
        type_ (Literal['data_collection_input']):
        when (None | str):
        tool_id (None | str | Unset): The unique name of the tool associated with this step.
        tool_inputs (Any | Unset): TODO
        tool_uuid (None | str | Unset): The universal unique identifier of the tool associated with this step. Takes
            precedence over tool_id if set.
        tool_version (None | str | Unset): The version of the tool associated with this step.
    """

    annotation: None | str
    id: int
    input_steps: InputSteps
    type_: Literal["data_collection_input"]
    when: None | str
    tool_id: None | str | Unset = UNSET
    tool_inputs: Any | Unset = UNSET
    tool_uuid: None | str | Unset = UNSET
    tool_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation: None | str
        annotation = self.annotation

        id = self.id

        input_steps = self.input_steps.to_dict()

        type_ = self.type_

        when: None | str
        when = self.when

        tool_id: None | str | Unset
        if isinstance(self.tool_id, Unset):
            tool_id = UNSET
        else:
            tool_id = self.tool_id

        tool_inputs = self.tool_inputs

        tool_uuid: None | str | Unset
        if isinstance(self.tool_uuid, Unset):
            tool_uuid = UNSET
        else:
            tool_uuid = self.tool_uuid

        tool_version: None | str | Unset
        if isinstance(self.tool_version, Unset):
            tool_version = UNSET
        else:
            tool_version = self.tool_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotation": annotation,
                "id": id,
                "input_steps": input_steps,
                "type": type_,
                "when": when,
            }
        )
        if tool_id is not UNSET:
            field_dict["tool_id"] = tool_id
        if tool_inputs is not UNSET:
            field_dict["tool_inputs"] = tool_inputs
        if tool_uuid is not UNSET:
            field_dict["tool_uuid"] = tool_uuid
        if tool_version is not UNSET:
            field_dict["tool_version"] = tool_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_steps import InputSteps

        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        id = d.pop("id")

        input_steps = InputSteps.from_dict(d.pop("input_steps"))

        type_ = cast(Literal["data_collection_input"], d.pop("type"))
        if type_ != "data_collection_input":
            raise ValueError(f"type must match const 'data_collection_input', got '{type_}'")

        def _parse_when(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        when = _parse_when(d.pop("when"))

        def _parse_tool_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_id = _parse_tool_id(d.pop("tool_id", UNSET))

        tool_inputs = d.pop("tool_inputs", UNSET)

        def _parse_tool_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_uuid = _parse_tool_uuid(d.pop("tool_uuid", UNSET))

        def _parse_tool_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_version = _parse_tool_version(d.pop("tool_version", UNSET))

        input_data_collection_step = cls(
            annotation=annotation,
            id=id,
            input_steps=input_steps,
            type_=type_,
            when=when,
            tool_id=tool_id,
            tool_inputs=tool_inputs,
            tool_uuid=tool_uuid,
            tool_version=tool_version,
        )

        input_data_collection_step.additional_properties = d
        return input_data_collection_step

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
