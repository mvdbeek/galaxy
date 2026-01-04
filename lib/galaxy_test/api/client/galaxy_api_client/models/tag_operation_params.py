from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TagOperationParams")


@_attrs_define
class TagOperationParams:
    """
    Attributes:
        tags (list[str]):
        type_ (Literal['add_tags'] | Literal['remove_tags']):
    """

    tags: list[str]
    type_: Literal["add_tags"] | Literal["remove_tags"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        type_: Literal["add_tags"] | Literal["remove_tags"]
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tags = cast(list[str], d.pop("tags"))

        def _parse_type_(data: object) -> Literal["add_tags"] | Literal["remove_tags"]:
            type_type_0 = cast(Literal["add_tags"], data)
            if type_type_0 != "add_tags":
                raise ValueError(f"type_type_0 must match const 'add_tags', got '{type_type_0}'")
            return type_type_0
            type_type_1 = cast(Literal["remove_tags"], data)
            if type_type_1 != "remove_tags":
                raise ValueError(f"type_type_1 must match const 'remove_tags', got '{type_type_1}'")
            return type_type_1

        type_ = _parse_type_(d.pop("type"))

        tag_operation_params = cls(
            tags=tags,
            type_=type_,
        )

        tag_operation_params.additional_properties = d
        return tag_operation_params

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
