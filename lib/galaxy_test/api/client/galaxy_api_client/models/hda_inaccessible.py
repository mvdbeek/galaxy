from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_state import DatasetState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HDAInaccessible")


@_attrs_define
class HDAInaccessible:
    """History Dataset Association information when the user can not access it.

    Attributes:
        accessible (bool):
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool): Whether this item is marked as deleted.
        hid (int): The index position of this item in the History.
        history_content_type (Literal['dataset']): This is always `dataset` for datasets.
        history_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        name (None | str): The name of the item.
        state (DatasetState):
        tags (list[str]): The collection of tags associated with an item.
        type_ (str): The type of this item.
        update_time (datetime.datetime | None): The last time and date this item was updated.
        url (str): The relative URL to access this item.
        visible (bool): Whether this item is visible or hidden to the user by default.
        copied_from_ldda_id (None | str | Unset):
        type_id (None | str | Unset): The type and the encoded ID of this item. Used for caching.
    """

    accessible: bool
    create_time: datetime.datetime
    deleted: bool
    hid: int
    history_content_type: Literal["dataset"]
    history_id: str
    id: str
    name: None | str
    state: DatasetState
    tags: list[str]
    type_: str
    update_time: datetime.datetime | None
    url: str
    visible: bool
    copied_from_ldda_id: None | str | Unset = UNSET
    type_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessible = self.accessible

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        hid = self.hid

        history_content_type = self.history_content_type

        history_id = self.history_id

        id = self.id

        name: None | str
        name = self.name

        state = self.state.value

        tags = self.tags

        type_ = self.type_

        update_time: None | str
        if isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        url = self.url

        visible = self.visible

        copied_from_ldda_id: None | str | Unset
        if isinstance(self.copied_from_ldda_id, Unset):
            copied_from_ldda_id = UNSET
        else:
            copied_from_ldda_id = self.copied_from_ldda_id

        type_id: None | str | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessible": accessible,
                "create_time": create_time,
                "deleted": deleted,
                "hid": hid,
                "history_content_type": history_content_type,
                "history_id": history_id,
                "id": id,
                "name": name,
                "state": state,
                "tags": tags,
                "type": type_,
                "update_time": update_time,
                "url": url,
                "visible": visible,
            }
        )
        if copied_from_ldda_id is not UNSET:
            field_dict["copied_from_ldda_id"] = copied_from_ldda_id
        if type_id is not UNSET:
            field_dict["type_id"] = type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accessible = d.pop("accessible")

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        hid = d.pop("hid")

        history_content_type = cast(Literal["dataset"], d.pop("history_content_type"))
        if history_content_type != "dataset":
            raise ValueError(f"history_content_type must match const 'dataset', got '{history_content_type}'")

        history_id = d.pop("history_id")

        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        state = DatasetState(d.pop("state"))

        tags = cast(list[str], d.pop("tags"))

        type_ = d.pop("type")

        def _parse_update_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = isoparse(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        update_time = _parse_update_time(d.pop("update_time"))

        url = d.pop("url")

        visible = d.pop("visible")

        def _parse_copied_from_ldda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_ldda_id = _parse_copied_from_ldda_id(d.pop("copied_from_ldda_id", UNSET))

        def _parse_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_id = _parse_type_id(d.pop("type_id", UNSET))

        hda_inaccessible = cls(
            accessible=accessible,
            create_time=create_time,
            deleted=deleted,
            hid=hid,
            history_content_type=history_content_type,
            history_id=history_id,
            id=id,
            name=name,
            state=state,
            tags=tags,
            type_=type_,
            update_time=update_time,
            url=url,
            visible=visible,
            copied_from_ldda_id=copied_from_ldda_id,
            type_id=type_id,
        )

        hda_inaccessible.additional_properties = d
        return hda_inaccessible

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
