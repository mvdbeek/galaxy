from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CsvDialect")


@_attrs_define
class CsvDialect:
    """
    Attributes:
        delimiter (str):
        double_quote (bool):
        escape_character (None | str):
        line_terminator (str):
        quote_character (None | str):
        skip_initial_space (bool):
    """

    delimiter: str
    double_quote: bool
    escape_character: None | str
    line_terminator: str
    quote_character: None | str
    skip_initial_space: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delimiter = self.delimiter

        double_quote = self.double_quote

        escape_character: None | str
        escape_character = self.escape_character

        line_terminator = self.line_terminator

        quote_character: None | str
        quote_character = self.quote_character

        skip_initial_space = self.skip_initial_space

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delimiter": delimiter,
                "double_quote": double_quote,
                "escape_character": escape_character,
                "line_terminator": line_terminator,
                "quote_character": quote_character,
                "skip_initial_space": skip_initial_space,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delimiter = d.pop("delimiter")

        double_quote = d.pop("double_quote")

        def _parse_escape_character(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        escape_character = _parse_escape_character(d.pop("escape_character"))

        line_terminator = d.pop("line_terminator")

        def _parse_quote_character(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        quote_character = _parse_quote_character(d.pop("quote_character"))

        skip_initial_space = d.pop("skip_initial_space")

        csv_dialect = cls(
            delimiter=delimiter,
            double_quote=double_quote,
            escape_character=escape_character,
            line_terminator=line_terminator,
            quote_character=quote_character,
            skip_initial_space=skip_initial_space,
        )

        csv_dialect.additional_properties = d
        return csv_dialect

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
