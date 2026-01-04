from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_state import DatasetState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_record_data import ExportRecordData
    from ..models.state_counts import StateCounts
    from ..models.state_i_ds import StateIDs


T = TypeVar("T", bound="ArchivedHistoryDetailed")


@_attrs_define
class ArchivedHistoryDetailed:
    """
    Attributes:
        annotation (None | str): An annotation to provide details or to help understand the purpose and usage of this
            item.
        archived (bool): Whether this item has been archived and is no longer active.
        contents_url (str): The relative URL to access the contents of this History.
        count (int): The number of items in the history.
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool): Whether this item is marked as deleted.
        id (str):  Example: 0123456789ABCDEF.
        importable (bool): Whether this History can be imported by other users with a shared link.
        model_class (Literal['History']): The name of the database model class.
        name (str): The name of the history.
        published (bool): Whether this resource is currently publicly available to all users.
        purged (bool): Whether this item has been permanently removed.
        size (int): The total size of the contents of this history in bytes.
        state (DatasetState):
        state_details (StateCounts): A dictionary keyed to possible dataset states and valued with the number of
            datasets in this history that have those states.
        state_ids (StateIDs): A dictionary keyed to possible dataset states and valued with lists containing the ids of
            each HDA in that state.
        tags (list[str]): The collection of tags associated with an item.
        update_time (datetime.datetime): The last time and date this item was updated.
        url (str): The relative URL to access this item.
        export_record_data (ExportRecordData | None | Unset): The export record data associated with this archived
            history. Used to recover the history.
        genome_build (None | str | Unset): TODO Default: '?'.
        preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
            datasets in this history.
        slug (None | str | Unset): Part of the URL to uniquely identify this History by link in a readable way.
        user_id (None | str | Unset): The encoded ID of the user that owns this History.
        username (None | str | Unset): Owner of the history
        username_and_slug (None | str | Unset): The relative URL in the form of /u/{username}/h/{slug}
    """

    annotation: None | str
    archived: bool
    contents_url: str
    count: int
    create_time: datetime.datetime
    deleted: bool
    id: str
    importable: bool
    model_class: Literal["History"]
    name: str
    published: bool
    purged: bool
    size: int
    state: DatasetState
    state_details: StateCounts
    state_ids: StateIDs
    tags: list[str]
    update_time: datetime.datetime
    url: str
    export_record_data: ExportRecordData | None | Unset = UNSET
    genome_build: None | str | Unset = "?"
    preferred_object_store_id: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    username_and_slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_record_data import ExportRecordData

        annotation: None | str
        annotation = self.annotation

        archived = self.archived

        contents_url = self.contents_url

        count = self.count

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        id = self.id

        importable = self.importable

        model_class = self.model_class

        name = self.name

        published = self.published

        purged = self.purged

        size = self.size

        state = self.state.value

        state_details = self.state_details.to_dict()

        state_ids = self.state_ids.to_dict()

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

        genome_build: None | str | Unset
        if isinstance(self.genome_build, Unset):
            genome_build = UNSET
        else:
            genome_build = self.genome_build

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        username_and_slug: None | str | Unset
        if isinstance(self.username_and_slug, Unset):
            username_and_slug = UNSET
        else:
            username_and_slug = self.username_and_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "annotation": annotation,
                "archived": archived,
                "contents_url": contents_url,
                "count": count,
                "create_time": create_time,
                "deleted": deleted,
                "id": id,
                "importable": importable,
                "model_class": model_class,
                "name": name,
                "published": published,
                "purged": purged,
                "size": size,
                "state": state,
                "state_details": state_details,
                "state_ids": state_ids,
                "tags": tags,
                "update_time": update_time,
                "url": url,
            }
        )
        if export_record_data is not UNSET:
            field_dict["export_record_data"] = export_record_data
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if username_and_slug is not UNSET:
            field_dict["username_and_slug"] = username_and_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_record_data import ExportRecordData
        from ..models.state_counts import StateCounts
        from ..models.state_i_ds import StateIDs

        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        archived = d.pop("archived")

        contents_url = d.pop("contents_url")

        count = d.pop("count")

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        id = d.pop("id")

        importable = d.pop("importable")

        model_class = cast(Literal["History"], d.pop("model_class"))
        if model_class != "History":
            raise ValueError(f"model_class must match const 'History', got '{model_class}'")

        name = d.pop("name")

        published = d.pop("published")

        purged = d.pop("purged")

        size = d.pop("size")

        state = DatasetState(d.pop("state"))

        state_details = StateCounts.from_dict(d.pop("state_details"))

        state_ids = StateIDs.from_dict(d.pop("state_ids"))

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

        def _parse_genome_build(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genome_build = _parse_genome_build(d.pop("genome_build", UNSET))

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_username_and_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username_and_slug = _parse_username_and_slug(d.pop("username_and_slug", UNSET))

        archived_history_detailed = cls(
            annotation=annotation,
            archived=archived,
            contents_url=contents_url,
            count=count,
            create_time=create_time,
            deleted=deleted,
            id=id,
            importable=importable,
            model_class=model_class,
            name=name,
            published=published,
            purged=purged,
            size=size,
            state=state,
            state_details=state_details,
            state_ids=state_ids,
            tags=tags,
            update_time=update_time,
            url=url,
            export_record_data=export_record_data,
            genome_build=genome_build,
            preferred_object_store_id=preferred_object_store_id,
            slug=slug,
            user_id=user_id,
            username=username,
            username_and_slug=username_and_slug,
        )

        archived_history_detailed.additional_properties = d
        return archived_history_detailed

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
