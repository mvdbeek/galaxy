from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.badge_dict_source import BadgeDictSource
from ..models.badge_dict_type_type_0 import BadgeDictTypeType0
from ..models.badge_dict_type_type_1 import BadgeDictTypeType1

T = TypeVar("T", bound="BadgeDict")


@_attrs_define
class BadgeDict:
    """
    Attributes:
        message (None | str):
        source (BadgeDictSource):
        type_ (BadgeDictTypeType0 | BadgeDictTypeType1):
    """

    message: None | str
    source: BadgeDictSource
    type_: BadgeDictTypeType0 | BadgeDictTypeType1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message: None | str
        message = self.message

        source = self.source.value

        type_: str
        if isinstance(self.type_, BadgeDictTypeType0):
            type_ = self.type_.value
        else:
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "source": source,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        message = _parse_message(d.pop("message"))

        source = BadgeDictSource(d.pop("source"))

        def _parse_type_(data: object) -> BadgeDictTypeType0 | BadgeDictTypeType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = BadgeDictTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            type_type_1 = BadgeDictTypeType1(data)

            return type_type_1

        type_ = _parse_type_(d.pop("type"))

        badge_dict = cls(
            message=message,
            source=source,
            type_=type_,
        )

        badge_dict.additional_properties = d
        return badge_dict

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
