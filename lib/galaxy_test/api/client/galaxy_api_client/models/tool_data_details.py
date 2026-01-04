from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolDataDetails")


@_attrs_define
class ToolDataDetails:
    """
    Attributes:
        columns (list[str]): A list of column names
        model_class (str): The name of class modelling this tool data
        name (str): The name of this tool data entry
        fields (list[list[str]] | Unset):
    """

    columns: list[str]
    model_class: str
    name: str
    fields: list[list[str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns = self.columns

        model_class = self.model_class

        name = self.name

        fields: list[list[str]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data

                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "model_class": model_class,
                "name": name,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        columns = cast(list[str], d.pop("columns"))

        model_class = d.pop("model_class")

        name = d.pop("name")

        _fields = d.pop("fields", UNSET)
        fields: list[list[str]] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = cast(list[str], fields_item_data)

                fields.append(fields_item)

        tool_data_details = cls(
            columns=columns,
            model_class=model_class,
            name=name,
            fields=fields,
        )

        tool_data_details.additional_properties = d
        return tool_data_details

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
