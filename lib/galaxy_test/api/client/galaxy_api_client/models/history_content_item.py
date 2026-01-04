from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.history_content_type import HistoryContentType

T = TypeVar("T", bound="HistoryContentItem")


@_attrs_define
class HistoryContentItem:
    """
    Attributes:
        history_content_type (HistoryContentType): Available types of History contents.
        id (str):  Example: 0123456789ABCDEF.
    """

    history_content_type: HistoryContentType
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_content_type = self.history_content_type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history_content_type": history_content_type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        history_content_type = HistoryContentType(d.pop("history_content_type"))

        id = d.pop("id")

        history_content_item = cls(
            history_content_type=history_content_type,
            id=id,
        )

        history_content_item.additional_properties = d
        return history_content_item

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
