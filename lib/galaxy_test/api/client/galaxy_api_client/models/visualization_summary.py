from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VisualizationSummary")


@_attrs_define
class VisualizationSummary:
    """
    Attributes:
        create_time (datetime.datetime | None): The time and date this item was created.
        deleted (bool): Whether this Visualization has been deleted.
        id (str): Encoded ID of the Visualization. Example: 0123456789ABCDEF.
        importable (bool): Whether this Visualization can be imported.
        published (bool): Whether this Visualization has been published.
        tags (list[str] | None): A list of tags to add to this item.
        title (str): The name of the visualization.
        type_ (str): The type of the visualization.
        update_time (datetime.datetime | None): The last time and date this item was updated.
        username (str): The name of the user owning this Visualization.
        annotation (None | str | Unset): The annotation of this Visualization.
        dbkey (None | str | Unset): The database key of the visualization.
    """

    create_time: datetime.datetime | None
    deleted: bool
    id: str
    importable: bool
    published: bool
    tags: list[str] | None
    title: str
    type_: str
    update_time: datetime.datetime | None
    username: str
    annotation: None | str | Unset = UNSET
    dbkey: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: None | str
        if isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        deleted = self.deleted

        id = self.id

        importable = self.importable

        published = self.published

        tags: list[str] | None
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        title = self.title

        type_ = self.type_

        update_time: None | str
        if isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        username = self.username

        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        dbkey: None | str | Unset
        if isinstance(self.dbkey, Unset):
            dbkey = UNSET
        else:
            dbkey = self.dbkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_time": create_time,
                "deleted": deleted,
                "id": id,
                "importable": importable,
                "published": published,
                "tags": tags,
                "title": title,
                "type": type_,
                "update_time": update_time,
                "username": username,
            }
        )
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if dbkey is not UNSET:
            field_dict["dbkey"] = dbkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_create_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = isoparse(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        create_time = _parse_create_time(d.pop("create_time"))

        deleted = d.pop("deleted")

        id = d.pop("id")

        importable = d.pop("importable")

        published = d.pop("published")

        def _parse_tags(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tags = _parse_tags(d.pop("tags"))

        title = d.pop("title")

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

        username = d.pop("username")

        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        def _parse_dbkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dbkey = _parse_dbkey(d.pop("dbkey", UNSET))

        visualization_summary = cls(
            create_time=create_time,
            deleted=deleted,
            id=id,
            importable=importable,
            published=published,
            tags=tags,
            title=title,
            type_=type_,
            update_time=update_time,
            username=username,
            annotation=annotation,
            dbkey=dbkey,
        )

        visualization_summary.additional_properties = d
        return visualization_summary

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
