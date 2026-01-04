from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="JavascriptRequirement")


@_attrs_define
class JavascriptRequirement:
    """
    Attributes:
        expression_lib (list[str] | None):
        type_ (Literal['javascript']):
    """

    expression_lib: list[str] | None
    type_: Literal["javascript"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expression_lib: list[str] | None
        if isinstance(self.expression_lib, list):
            expression_lib = self.expression_lib

        else:
            expression_lib = self.expression_lib

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression_lib": expression_lib,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expression_lib(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                expression_lib_type_0 = cast(list[str], data)

                return expression_lib_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        expression_lib = _parse_expression_lib(d.pop("expression_lib"))

        type_ = cast(Literal["javascript"], d.pop("type"))
        if type_ != "javascript":
            raise ValueError(f"type must match const 'javascript', got '{type_}'")

        javascript_requirement = cls(
            expression_lib=expression_lib,
            type_=type_,
        )

        javascript_requirement.additional_properties = d
        return javascript_requirement

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
