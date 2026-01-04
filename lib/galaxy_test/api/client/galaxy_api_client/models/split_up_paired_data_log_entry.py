from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parsed_column import ParsedColumn


T = TypeVar("T", bound="SplitUpPairedDataLogEntry")


@_attrs_define
class SplitUpPairedDataLogEntry:
    """
    Attributes:
        message (str):
        new_paired_status_column (int):
        old_forward_column (ParsedColumn):
        old_reverse_column (ParsedColumn):
    """

    message: str
    new_paired_status_column: int
    old_forward_column: ParsedColumn
    old_reverse_column: ParsedColumn
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        new_paired_status_column = self.new_paired_status_column

        old_forward_column = self.old_forward_column.to_dict()

        old_reverse_column = self.old_reverse_column.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "new_paired_status_column": new_paired_status_column,
                "old_forward_column": old_forward_column,
                "old_reverse_column": old_reverse_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_column import ParsedColumn

        d = dict(src_dict)
        message = d.pop("message")

        new_paired_status_column = d.pop("new_paired_status_column")

        old_forward_column = ParsedColumn.from_dict(d.pop("old_forward_column"))

        old_reverse_column = ParsedColumn.from_dict(d.pop("old_reverse_column"))

        split_up_paired_data_log_entry = cls(
            message=message,
            new_paired_status_column=new_paired_status_column,
            old_forward_column=old_forward_column,
            old_reverse_column=old_reverse_column,
        )

        split_up_paired_data_log_entry.additional_properties = d
        return split_up_paired_data_log_entry

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
