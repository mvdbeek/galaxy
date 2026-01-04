from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_shared_item_notification_content_item_type import NewSharedItemNotificationContentItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSharedItemNotificationContent")


@_attrs_define
class NewSharedItemNotificationContent:
    """
    Attributes:
        item_name (str): The name of the shared item.
        item_type (NewSharedItemNotificationContentItemType): The type of the shared item.
        owner_name (str): The name of the owner of the shared item.
        slug (str): The slug of the shared item. Used for the link to the item.
        category (Literal['new_shared_item'] | Unset):  Default: 'new_shared_item'.
    """

    item_name: str
    item_type: NewSharedItemNotificationContentItemType
    owner_name: str
    slug: str
    category: Literal["new_shared_item"] | Unset = "new_shared_item"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_name = self.item_name

        item_type = self.item_type.value

        owner_name = self.owner_name

        slug = self.slug

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_name": item_name,
                "item_type": item_type,
                "owner_name": owner_name,
                "slug": slug,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_name = d.pop("item_name")

        item_type = NewSharedItemNotificationContentItemType(d.pop("item_type"))

        owner_name = d.pop("owner_name")

        slug = d.pop("slug")

        category = cast(Literal["new_shared_item"] | Unset, d.pop("category", UNSET))
        if category != "new_shared_item" and not isinstance(category, Unset):
            raise ValueError(f"category must match const 'new_shared_item', got '{category}'")

        new_shared_item_notification_content = cls(
            item_name=item_name,
            item_type=item_type,
            owner_name=owner_name,
            slug=slug,
            category=category,
        )

        new_shared_item_notification_content.additional_properties = d
        return new_shared_item_notification_content

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
