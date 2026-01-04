from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fill_identifiers import FillIdentifiers


T = TypeVar("T", bound="ParseFetchWorkbook")


@_attrs_define
class ParseFetchWorkbook:
    """
    Attributes:
        content (str): The workbook content (the contents of the xlsx file) that have been base64 encoded.
        fill_identifiers (FillIdentifiers | None | Unset):
    """

    content: str
    fill_identifiers: FillIdentifiers | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fill_identifiers import FillIdentifiers

        content = self.content

        fill_identifiers: dict[str, Any] | None | Unset
        if isinstance(self.fill_identifiers, Unset):
            fill_identifiers = UNSET
        elif isinstance(self.fill_identifiers, FillIdentifiers):
            fill_identifiers = self.fill_identifiers.to_dict()
        else:
            fill_identifiers = self.fill_identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if fill_identifiers is not UNSET:
            field_dict["fill_identifiers"] = fill_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fill_identifiers import FillIdentifiers

        d = dict(src_dict)
        content = d.pop("content")

        def _parse_fill_identifiers(data: object) -> FillIdentifiers | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fill_identifiers_type_0 = FillIdentifiers.from_dict(data)

                return fill_identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FillIdentifiers | None | Unset, data)

        fill_identifiers = _parse_fill_identifiers(d.pop("fill_identifiers", UNSET))

        parse_fetch_workbook = cls(
            content=content,
            fill_identifiers=fill_identifiers,
        )

        parse_fetch_workbook.additional_properties = d
        return parse_fetch_workbook

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
