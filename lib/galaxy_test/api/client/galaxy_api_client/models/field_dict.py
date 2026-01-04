from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.field_dict_type_type_0 import FieldDictTypeType0
from ..models.field_dict_type_type_1_item import FieldDictTypeType1Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldDict")


@_attrs_define
class FieldDict:
    """
    Attributes:
        name (str):
        type_ (FieldDictTypeType0 | list[FieldDictTypeType1Item]):
        format_ (None | str | Unset):
    """

    name: str
    type_: FieldDictTypeType0 | list[FieldDictTypeType1Item]
    format_: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: list[str] | str
        if isinstance(self.type_, FieldDictTypeType0):
            type_ = self.type_.value
        else:
            type_ = []
            for type_type_1_item_data in self.type_:
                type_type_1_item = type_type_1_item_data.value
                type_.append(type_type_1_item)

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_type_(data: object) -> FieldDictTypeType0 | list[FieldDictTypeType1Item]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = FieldDictTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            type_type_1 = []
            _type_type_1 = data
            for type_type_1_item_data in _type_type_1:
                type_type_1_item = FieldDictTypeType1Item(type_type_1_item_data)

                type_type_1.append(type_type_1_item)

            return type_type_1

        type_ = _parse_type_(d.pop("type"))

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        field_dict = cls(
            name=name,
            type_=type_,
            format_=format_,
        )

        return field_dict
