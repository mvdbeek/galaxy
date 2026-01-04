from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InputReferenceByLabel")


@_attrs_define
class InputReferenceByLabel:
    """
    Attributes:
        input_name (str): The input name as defined by the workflow module corresponding to the step being referenced.
            For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').
        label (str): The unique label of the step being referenced.
    """

    input_name: str
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_name = self.input_name

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_name": input_name,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_name = d.pop("input_name")

        label = d.pop("label")

        input_reference_by_label = cls(
            input_name=input_name,
            label=label,
        )

        input_reference_by_label.additional_properties = d
        return input_reference_by_label

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
