from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.parsed_column import ParsedColumn


T = TypeVar("T", bound="InferredCollectionTypeLogEntry")


@_attrs_define
class InferredCollectionTypeLogEntry:
    """
    Attributes:
        from_columns (list[ParsedColumn]):
        message (str):
    """

    from_columns: list[ParsedColumn]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_columns = []
        for from_columns_item_data in self.from_columns:
            from_columns_item = from_columns_item_data.to_dict()
            from_columns.append(from_columns_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_columns": from_columns,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parsed_column import ParsedColumn

        d = dict(src_dict)
        from_columns = []
        _from_columns = d.pop("from_columns")
        for from_columns_item_data in _from_columns:
            from_columns_item = ParsedColumn.from_dict(from_columns_item_data)

            from_columns.append(from_columns_item)

        message = d.pop("message")

        inferred_collection_type_log_entry = cls(
            from_columns=from_columns,
            message=message,
        )

        inferred_collection_type_log_entry.additional_properties = d
        return inferred_collection_type_log_entry

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
