from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.csv_dialect import CsvDialect


T = TypeVar("T", bound="CsvDialectInferenceMessage")


@_attrs_define
class CsvDialectInferenceMessage:
    """
    Attributes:
        dialect (CsvDialect):
        message (str):
    """

    dialect: CsvDialect
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dialect = self.dialect.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialect": dialect,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.csv_dialect import CsvDialect

        d = dict(src_dict)
        dialect = CsvDialect.from_dict(d.pop("dialect"))

        message = d.pop("message")

        csv_dialect_inference_message = cls(
            dialect=dialect,
            message=message,
        )

        csv_dialect_inference_message.additional_properties = d
        return csv_dialect_inference_message

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
