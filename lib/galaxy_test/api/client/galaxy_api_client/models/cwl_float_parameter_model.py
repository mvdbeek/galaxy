from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CwlFloatParameterModel")


@_attrs_define
class CwlFloatParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        parameter_type (Literal['cwl_float'] | Unset):  Default: 'cwl_float'.
    """

    name: str
    parameter_type: Literal["cwl_float"] | Unset = "cwl_float"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parameter_type = self.parameter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        parameter_type = cast(Literal["cwl_float"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "cwl_float" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'cwl_float', got '{parameter_type}'")

        cwl_float_parameter_model = cls(
            name=name,
            parameter_type=parameter_type,
        )

        cwl_float_parameter_model.additional_properties = d
        return cwl_float_parameter_model

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
