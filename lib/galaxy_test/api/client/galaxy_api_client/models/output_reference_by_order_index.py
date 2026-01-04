from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputReferenceByOrderIndex")


@_attrs_define
class OutputReferenceByOrderIndex:
    """
    Attributes:
        order_index (int): The order_index of the step being referenced. The order indices of a workflow start at 0.
        output_name (None | str | Unset): The output name as defined by the workflow module corresponding to the step
            being referenced. The default is 'output', corresponding to the output defined by input step types. Default:
            'output'.
    """

    order_index: int
    output_name: None | str | Unset = "output"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_index = self.order_index

        output_name: None | str | Unset
        if isinstance(self.output_name, Unset):
            output_name = UNSET
        else:
            output_name = self.output_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_index": order_index,
            }
        )
        if output_name is not UNSET:
            field_dict["output_name"] = output_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_index = d.pop("order_index")

        def _parse_output_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_name = _parse_output_name(d.pop("output_name", UNSET))

        output_reference_by_order_index = cls(
            order_index=order_index,
            output_name=output_name,
        )

        output_reference_by_order_index.additional_properties = d
        return output_reference_by_order_index

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
