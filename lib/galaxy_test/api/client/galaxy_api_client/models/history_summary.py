from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HistorySummary")


@_attrs_define
class HistorySummary:
    """History summary information.

    Attributes:
        annotation (None | str): An annotation to provide details or to help understand the purpose and usage of this
            item.
        archived (bool): Whether this item has been archived and is no longer active.
        count (int): The number of items in the history.
        deleted (bool): Whether this item is marked as deleted.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['History']): The name of the database model class.
        name (str): The name of the history.
        published (bool): Whether this resource is currently publicly available to all users.
        purged (bool): Whether this item has been permanently removed.
        tags (list[str]): The collection of tags associated with an item.
        update_time (datetime.datetime): The last time and date this item was updated.
        url (str): The relative URL to access this item.
        preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
            datasets in this history.
    """

    annotation: None | str
    archived: bool
    count: int
    deleted: bool
    id: str
    model_class: Literal["History"]
    name: str
    published: bool
    purged: bool
    tags: list[str]
    update_time: datetime.datetime
    url: str
    preferred_object_store_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation: None | str
        annotation = self.annotation

        archived = self.archived

        count = self.count

        deleted = self.deleted

        id = self.id

        model_class = self.model_class

        name = self.name

        published = self.published

        purged = self.purged

        tags = self.tags

        update_time = self.update_time.isoformat()

        url = self.url

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotation": annotation,
                "archived": archived,
                "count": count,
                "deleted": deleted,
                "id": id,
                "model_class": model_class,
                "name": name,
                "published": published,
                "purged": purged,
                "tags": tags,
                "update_time": update_time,
                "url": url,
            }
        )
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        archived = d.pop("archived")

        count = d.pop("count")

        deleted = d.pop("deleted")

        id = d.pop("id")

        model_class = cast(Literal["History"], d.pop("model_class"))
        if model_class != "History":
            raise ValueError(f"model_class must match const 'History', got '{model_class}'")

        name = d.pop("name")

        published = d.pop("published")

        purged = d.pop("purged")

        tags = cast(list[str], d.pop("tags"))

        update_time = isoparse(d.pop("update_time"))

        url = d.pop("url")

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        history_summary = cls(
            annotation=annotation,
            archived=archived,
            count=count,
            deleted=deleted,
            id=id,
            model_class=model_class,
            name=name,
            published=published,
            purged=purged,
            tags=tags,
            update_time=update_time,
            url=url,
            preferred_object_store_id=preferred_object_store_id,
        )

        history_summary.additional_properties = d
        return history_summary

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
