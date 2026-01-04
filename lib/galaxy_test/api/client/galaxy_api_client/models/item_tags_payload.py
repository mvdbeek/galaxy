from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taggable_item_class import TaggableItemClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemTagsPayload")


@_attrs_define
class ItemTagsPayload:
    """
    Attributes:
        item_class (TaggableItemClass):
        item_id (str): The `encoded identifier` of the item whose tags will be updated. Example: 0123456789ABCDEF.
        item_tags (list[str] | None | Unset): The list of tags that will replace the current tags associated with the
            item.
    """

    item_class: TaggableItemClass
    item_id: str
    item_tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_class = self.item_class.value

        item_id = self.item_id

        item_tags: list[str] | None | Unset
        if isinstance(self.item_tags, Unset):
            item_tags = UNSET
        elif isinstance(self.item_tags, list):
            item_tags = self.item_tags

        else:
            item_tags = self.item_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_class": item_class,
                "item_id": item_id,
            }
        )
        if item_tags is not UNSET:
            field_dict["item_tags"] = item_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_class = TaggableItemClass(d.pop("item_class"))

        item_id = d.pop("item_id")

        def _parse_item_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                item_tags_tags = cast(list[str], data)

                return item_tags_tags
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        item_tags = _parse_item_tags(d.pop("item_tags", UNSET))

        item_tags_payload = cls(
            item_class=item_class,
            item_id=item_id,
            item_tags=item_tags,
        )

        item_tags_payload.additional_properties = d
        return item_tags_payload

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
