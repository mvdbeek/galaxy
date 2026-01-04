from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_record_data import ExportRecordData


T = TypeVar("T", bound="ArchivedHistorySummary")


@_attrs_define
class ArchivedHistorySummary:
    """
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
        export_record_data (ExportRecordData | None | Unset): The export record data associated with this archived
            history. Used to recover the history.
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
    export_record_data: ExportRecordData | None | Unset = UNSET
    preferred_object_store_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_record_data import ExportRecordData

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

        export_record_data: dict[str, Any] | None | Unset
        if isinstance(self.export_record_data, Unset):
            export_record_data = UNSET
        elif isinstance(self.export_record_data, ExportRecordData):
            export_record_data = self.export_record_data.to_dict()
        else:
            export_record_data = self.export_record_data

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
        if export_record_data is not UNSET:
            field_dict["export_record_data"] = export_record_data
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_record_data import ExportRecordData

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

        def _parse_export_record_data(data: object) -> ExportRecordData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                export_record_data_type_0 = ExportRecordData.from_dict(data)

                return export_record_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportRecordData | None | Unset, data)

        export_record_data = _parse_export_record_data(d.pop("export_record_data", UNSET))

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        archived_history_summary = cls(
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
            export_record_data=export_record_data,
            preferred_object_store_id=preferred_object_store_id,
        )

        archived_history_summary.additional_properties = d
        return archived_history_summary

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
