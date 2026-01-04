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
    from ..models.custom_archived_history_view_contents_states_type_0 import (
        CustomArchivedHistoryViewContentsStatesType0,
    )
    from ..models.custom_archived_history_view_state_details_type_0 import CustomArchivedHistoryViewStateDetailsType0
    from ..models.custom_archived_history_view_state_ids_type_0 import CustomArchivedHistoryViewStateIdsType0
    from ..models.export_record_data import ExportRecordData
    from ..models.history_active_content_counts import HistoryActiveContentCounts


T = TypeVar("T", bound="CustomArchivedHistoryView")


@_attrs_define
class CustomArchivedHistoryView:
    """Archived History Response with all optional fields.

    It is used for serializing only specific attributes using the "keys"
    query parameter.

        Attributes:
            annotation (None | str | Unset): An annotation to provide details or to help understand the purpose and usage of
                this item.
            archived (bool | None | Unset): Whether this item has been archived and is no longer active.
            contents_active (HistoryActiveContentCounts | None | Unset): Contains the number of active, deleted or hidden
                items in a History.
            contents_states (CustomArchivedHistoryViewContentsStatesType0 | None | Unset): A dictionary keyed to possible
                dataset states and valued with the number of datasets in this history that have those states.
            contents_url (None | str | Unset): The relative URL to access the contents of this History.
            count (int | None | Unset): The number of items in the history.
            create_time (datetime.datetime | None | Unset): The time and date this item was created.
            deleted (bool | None | Unset): Whether this item is marked as deleted.
            export_record_data (ExportRecordData | None | Unset): The export record data associated with this archived
                history. Used to recover the history.
            genome_build (None | str | Unset): TODO Default: '?'.
            id (str | Unset):  Example: 0123456789ABCDEF.
            importable (bool | None | Unset): Whether this History can be imported by other users with a shared link.
            model_class (Literal['History'] | None | Unset): The name of the database model class.
            name (None | str | Unset): The name of the history.
            nice_size (None | str | Unset): The total size of the contents of this history in a human-readable format.
            preferred_object_store_id (None | str | Unset): The ID of the object store that should be used to store new
                datasets in this history.
            published (bool | None | Unset): Whether this resource is currently publicly available to all users.
            purged (bool | None | Unset): Whether this item has been permanently removed.
            size (int | None | Unset): The total size of the contents of this history in bytes.
            slug (None | str | Unset): Part of the URL to uniquely identify this History by link in a readable way.
            state (DatasetState | None | Unset): The current state of the History based on the states of the datasets it
                contains.
            state_details (CustomArchivedHistoryViewStateDetailsType0 | None | Unset): A dictionary keyed to possible
                dataset states and valued with the number of datasets in this history that have those states.
            state_ids (CustomArchivedHistoryViewStateIdsType0 | None | Unset): A dictionary keyed to possible dataset states
                and valued with lists containing the ids of each HDA in that state.
            tags (list[str] | None | Unset): The collection of tags associated with an item.
            update_time (datetime.datetime | None | Unset): The last time and date this item was updated.
            url (None | str | Unset): The relative URL to access this item.
            user_id (None | str | Unset): The encoded ID of the user that owns this History.
            username (None | str | Unset): Owner of the history
            username_and_slug (None | str | Unset): The relative URL in the form of /u/{username}/h/{slug}
    """

    annotation: None | str | Unset = UNSET
    archived: bool | None | Unset = UNSET
    contents_active: HistoryActiveContentCounts | None | Unset = UNSET
    contents_states: CustomArchivedHistoryViewContentsStatesType0 | None | Unset = UNSET
    contents_url: None | str | Unset = UNSET
    count: int | None | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    deleted: bool | None | Unset = UNSET
    export_record_data: ExportRecordData | None | Unset = UNSET
    genome_build: None | str | Unset = "?"
    id: str | Unset = UNSET
    importable: bool | None | Unset = UNSET
    model_class: Literal["History"] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    nice_size: None | str | Unset = UNSET
    preferred_object_store_id: None | str | Unset = UNSET
    published: bool | None | Unset = UNSET
    purged: bool | None | Unset = UNSET
    size: int | None | Unset = UNSET
    slug: None | str | Unset = UNSET
    state: DatasetState | None | Unset = UNSET
    state_details: CustomArchivedHistoryViewStateDetailsType0 | None | Unset = UNSET
    state_ids: CustomArchivedHistoryViewStateIdsType0 | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    url: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    username_and_slug: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_archived_history_view_contents_states_type_0 import (
            CustomArchivedHistoryViewContentsStatesType0,
        )
        from ..models.custom_archived_history_view_state_details_type_0 import (
            CustomArchivedHistoryViewStateDetailsType0,
        )
        from ..models.custom_archived_history_view_state_ids_type_0 import CustomArchivedHistoryViewStateIdsType0
        from ..models.export_record_data import ExportRecordData
        from ..models.history_active_content_counts import HistoryActiveContentCounts

        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        contents_active: dict[str, Any] | None | Unset
        if isinstance(self.contents_active, Unset):
            contents_active = UNSET
        elif isinstance(self.contents_active, HistoryActiveContentCounts):
            contents_active = self.contents_active.to_dict()
        else:
            contents_active = self.contents_active

        contents_states: dict[str, Any] | None | Unset
        if isinstance(self.contents_states, Unset):
            contents_states = UNSET
        elif isinstance(self.contents_states, CustomArchivedHistoryViewContentsStatesType0):
            contents_states = self.contents_states.to_dict()
        else:
            contents_states = self.contents_states

        contents_url: None | str | Unset
        if isinstance(self.contents_url, Unset):
            contents_url = UNSET
        else:
            contents_url = self.contents_url

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

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

        id = self.id

        importable: bool | None | Unset
        if isinstance(self.importable, Unset):
            importable = UNSET
        else:
            importable = self.importable

        model_class: Literal["History"] | None | Unset
        if isinstance(self.model_class, Unset):
            model_class = UNSET
        else:
            model_class = self.model_class

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        nice_size: None | str | Unset
        if isinstance(self.nice_size, Unset):
            nice_size = UNSET
        else:
            nice_size = self.nice_size

        preferred_object_store_id: None | str | Unset
        if isinstance(self.preferred_object_store_id, Unset):
            preferred_object_store_id = UNSET
        else:
            preferred_object_store_id = self.preferred_object_store_id

        published: bool | None | Unset
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        purged: bool | None | Unset
        if isinstance(self.purged, Unset):
            purged = UNSET
        else:
            purged = self.purged

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, DatasetState):
            state = self.state.value
        else:
            state = self.state

        state_details: dict[str, Any] | None | Unset
        if isinstance(self.state_details, Unset):
            state_details = UNSET
        elif isinstance(self.state_details, CustomArchivedHistoryViewStateDetailsType0):
            state_details = self.state_details.to_dict()
        else:
            state_details = self.state_details

        state_ids: dict[str, Any] | None | Unset
        if isinstance(self.state_ids, Unset):
            state_ids = UNSET
        elif isinstance(self.state_ids, CustomArchivedHistoryViewStateIdsType0):
            state_ids = self.state_ids.to_dict()
        else:
            state_ids = self.state_ids

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

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
        field_dict.update({})
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if archived is not UNSET:
            field_dict["archived"] = archived
        if contents_active is not UNSET:
            field_dict["contents_active"] = contents_active
        if contents_states is not UNSET:
            field_dict["contents_states"] = contents_states
        if contents_url is not UNSET:
            field_dict["contents_url"] = contents_url
        if count is not UNSET:
            field_dict["count"] = count
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if export_record_data is not UNSET:
            field_dict["export_record_data"] = export_record_data
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if id is not UNSET:
            field_dict["id"] = id
        if importable is not UNSET:
            field_dict["importable"] = importable
        if model_class is not UNSET:
            field_dict["model_class"] = model_class
        if name is not UNSET:
            field_dict["name"] = name
        if nice_size is not UNSET:
            field_dict["nice_size"] = nice_size
        if preferred_object_store_id is not UNSET:
            field_dict["preferred_object_store_id"] = preferred_object_store_id
        if published is not UNSET:
            field_dict["published"] = published
        if purged is not UNSET:
            field_dict["purged"] = purged
        if size is not UNSET:
            field_dict["size"] = size
        if slug is not UNSET:
            field_dict["slug"] = slug
        if state is not UNSET:
            field_dict["state"] = state
        if state_details is not UNSET:
            field_dict["state_details"] = state_details
        if state_ids is not UNSET:
            field_dict["state_ids"] = state_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if username_and_slug is not UNSET:
            field_dict["username_and_slug"] = username_and_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_archived_history_view_contents_states_type_0 import (
            CustomArchivedHistoryViewContentsStatesType0,
        )
        from ..models.custom_archived_history_view_state_details_type_0 import (
            CustomArchivedHistoryViewStateDetailsType0,
        )
        from ..models.custom_archived_history_view_state_ids_type_0 import CustomArchivedHistoryViewStateIdsType0
        from ..models.export_record_data import ExportRecordData
        from ..models.history_active_content_counts import HistoryActiveContentCounts

        d = dict(src_dict)

        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        def _parse_contents_active(data: object) -> HistoryActiveContentCounts | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contents_active_type_0 = HistoryActiveContentCounts.from_dict(data)

                return contents_active_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HistoryActiveContentCounts | None | Unset, data)

        contents_active = _parse_contents_active(d.pop("contents_active", UNSET))

        def _parse_contents_states(data: object) -> CustomArchivedHistoryViewContentsStatesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contents_states_type_0 = CustomArchivedHistoryViewContentsStatesType0.from_dict(data)

                return contents_states_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomArchivedHistoryViewContentsStatesType0 | None | Unset, data)

        contents_states = _parse_contents_states(d.pop("contents_states", UNSET))

        def _parse_contents_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_url = _parse_contents_url(d.pop("contents_url", UNSET))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = isoparse(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("create_time", UNSET))

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

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

        id = d.pop("id", UNSET)

        def _parse_importable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        importable = _parse_importable(d.pop("importable", UNSET))

        def _parse_model_class(data: object) -> Literal["History"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            model_class_type_0 = cast(Literal["History"], data)
            if model_class_type_0 != "History":
                raise ValueError(f"model_class_type_0 must match const 'History', got '{model_class_type_0}'")
            return model_class_type_0
            return cast(Literal["History"] | None | Unset, data)

        model_class = _parse_model_class(d.pop("model_class", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_nice_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nice_size = _parse_nice_size(d.pop("nice_size", UNSET))

        def _parse_preferred_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_object_store_id = _parse_preferred_object_store_id(d.pop("preferred_object_store_id", UNSET))

        def _parse_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published = _parse_published(d.pop("published", UNSET))

        def _parse_purged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        purged = _parse_purged(d.pop("purged", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_state(data: object) -> DatasetState | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = DatasetState(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetState | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_state_details(data: object) -> CustomArchivedHistoryViewStateDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_details_type_0 = CustomArchivedHistoryViewStateDetailsType0.from_dict(data)

                return state_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomArchivedHistoryViewStateDetailsType0 | None | Unset, data)

        state_details = _parse_state_details(d.pop("state_details", UNSET))

        def _parse_state_ids(data: object) -> CustomArchivedHistoryViewStateIdsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_ids_type_0 = CustomArchivedHistoryViewStateIdsType0.from_dict(data)

                return state_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomArchivedHistoryViewStateIdsType0 | None | Unset, data)

        state_ids = _parse_state_ids(d.pop("state_ids", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = isoparse(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

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

        custom_archived_history_view = cls(
            annotation=annotation,
            archived=archived,
            contents_active=contents_active,
            contents_states=contents_states,
            contents_url=contents_url,
            count=count,
            create_time=create_time,
            deleted=deleted,
            export_record_data=export_record_data,
            genome_build=genome_build,
            id=id,
            importable=importable,
            model_class=model_class,
            name=name,
            nice_size=nice_size,
            preferred_object_store_id=preferred_object_store_id,
            published=published,
            purged=purged,
            size=size,
            slug=slug,
            state=state,
            state_details=state_details,
            state_ids=state_ids,
            tags=tags,
            update_time=update_time,
            url=url,
            user_id=user_id,
            username=username,
            username_and_slug=username_and_slug,
        )

        custom_archived_history_view.additional_properties = d
        return custom_archived_history_view

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
