from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parsed_column import ParsedColumn


T = TypeVar("T", bound="InferredColumnMapping")


@_attrs_define
class InferredColumnMapping:
    """
    Attributes:
        column_index (int):
        column_title (str):
        parsed_column (ParsedColumn):
    """

    column_index: int
    column_title: str
    parsed_column: ParsedColumn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_index = self.column_index

        column_title = self.column_title

        parsed_column = self.parsed_column.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column_index": column_index,
                "column_title": column_title,
                "parsed_column": parsed_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_column import ParsedColumn

        d = dict(src_dict)
        column_index = d.pop("column_index")

        column_title = d.pop("column_title")

        parsed_column = ParsedColumn.from_dict(d.pop("parsed_column"))

        inferred_column_mapping = cls(
            column_index=column_index,
            column_title=column_title,
            parsed_column=parsed_column,
        )

        inferred_column_mapping.additional_properties = d
        return inferred_column_mapping

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
