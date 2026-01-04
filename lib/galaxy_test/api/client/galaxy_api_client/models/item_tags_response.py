from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemTagsResponse")


@_attrs_define
class ItemTagsResponse:
    """Response schema for showing an item tag.

    Attributes:
        id (str):  Example: 0123456789ABCDEF.
        model_class (str):
        user_tname (str):
        user_value (None | str | Unset):
    """

    id: str
    model_class: str
    user_tname: str
    user_value: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_class = self.model_class

        user_tname = self.user_tname

        user_value: None | str | Unset
        if isinstance(self.user_value, Unset):
            user_value = UNSET
        else:
            user_value = self.user_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model_class": model_class,
                "user_tname": user_tname,
            }
        )
        if user_value is not UNSET:
            field_dict["user_value"] = user_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        model_class = d.pop("model_class")

        user_tname = d.pop("user_tname")

        def _parse_user_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_value = _parse_user_value(d.pop("user_value", UNSET))

        item_tags_response = cls(
            id=id,
            model_class=model_class,
            user_tname=user_tname,
            user_value=user_value,
        )

        item_tags_response.additional_properties = d
        return item_tags_response

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
