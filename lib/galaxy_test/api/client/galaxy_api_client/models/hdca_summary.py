from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_collection_populated_state import DatasetCollectionPopulatedState
from ..models.job_source_type import JobSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elements_states_dict import ElementsStatesDict
    from ..models.hdc_job_state_summary import HDCJobStateSummary
    from ..models.oldest_create_time_by_object_store_id import OldestCreateTimeByObjectStoreId


T = TypeVar("T", bound="HDCASummary")


@_attrs_define
class HDCASummary:
    """History Dataset Collection Association summary information.

    Attributes:
        collection_id (str):  Example: 0123456789ABCDEF.
        collection_type (str): The type of the collection, can be `list`, `paired`, or define subcollections using `:`
            as separator like `list:paired` or `list:list`.
        contents_url (str): The relative URL to access the contents of this History.
        create_time (datetime.datetime): The time and date this item was created.
        deleted (bool): Whether this item is marked as deleted.
        elements_datatypes (list[str]): A set containing all the different element datatypes in the collection.
        elements_deleted (int): The number of elements in the collection that are marked as deleted.
        elements_states (ElementsStatesDict):
        hid (int): The index position of this item in the History.
        history_content_type (Literal['dataset_collection']): This is always `dataset_collection` for dataset
            collections.
        history_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        model_class (Literal['HistoryDatasetCollectionAssociation']): The name of the database model class.
        name (None | str): The name of the item.
        populated_state (DatasetCollectionPopulatedState):
        tags (list[str]): The collection of tags associated with an item.
        update_time (datetime.datetime | None): The last time and date this item was updated.
        url (str): The relative URL to access this item.
        visible (bool): Whether this item is visible or hidden to the user by default.
        element_count (int | None | Unset): The number of elements contained in the dataset collection. It may be None
            or undefined if the collection could not be populated.
        job_source_id (None | str | Unset): The encoded ID of the Job that produced this dataset collection. Used to
            track the state of the job.
        job_source_type (JobSourceType | None | Unset): The type of job (model class) that produced this dataset
            collection. Used to track the state of the job.
        job_state_summary (HDCJobStateSummary | None | Unset): Overview of the job states working inside the dataset
            collection.
        populated_state_message (None | str | Unset): Optional message with further information in case the population
            of the dataset collection failed.
        store_times_summary (list[OldestCreateTimeByObjectStoreId] | None | Unset): A list of objects containing the
            object store ID and the oldest creation time of the datasets stored in that object store for this
            collection.This is used to determine the age of the datasets in the collection when the object store is short-
            lived.
        type_ (Literal['collection'] | Unset): This is always `collection` for dataset collections. Default:
            'collection'.
        type_id (None | str | Unset): The type and the encoded ID of this item. Used for caching.
    """

    collection_id: str
    collection_type: str
    contents_url: str
    create_time: datetime.datetime
    deleted: bool
    elements_datatypes: list[str]
    elements_deleted: int
    elements_states: ElementsStatesDict
    hid: int
    history_content_type: Literal["dataset_collection"]
    history_id: str
    id: str
    model_class: Literal["HistoryDatasetCollectionAssociation"]
    name: None | str
    populated_state: DatasetCollectionPopulatedState
    tags: list[str]
    update_time: datetime.datetime | None
    url: str
    visible: bool
    element_count: int | None | Unset = UNSET
    job_source_id: None | str | Unset = UNSET
    job_source_type: JobSourceType | None | Unset = UNSET
    job_state_summary: HDCJobStateSummary | None | Unset = UNSET
    populated_state_message: None | str | Unset = UNSET
    store_times_summary: list[OldestCreateTimeByObjectStoreId] | None | Unset = UNSET
    type_: Literal["collection"] | Unset = "collection"
    type_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hdc_job_state_summary import HDCJobStateSummary

        collection_id = self.collection_id

        collection_type = self.collection_type

        contents_url = self.contents_url

        create_time = self.create_time.isoformat()

        deleted = self.deleted

        elements_datatypes = self.elements_datatypes

        elements_deleted = self.elements_deleted

        elements_states = self.elements_states.to_dict()

        hid = self.hid

        history_content_type = self.history_content_type

        history_id = self.history_id

        id = self.id

        model_class = self.model_class

        name: None | str
        name = self.name

        populated_state = self.populated_state.value

        tags = self.tags

        update_time: None | str
        if isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        url = self.url

        visible = self.visible

        element_count: int | None | Unset
        if isinstance(self.element_count, Unset):
            element_count = UNSET
        else:
            element_count = self.element_count

        job_source_id: None | str | Unset
        if isinstance(self.job_source_id, Unset):
            job_source_id = UNSET
        else:
            job_source_id = self.job_source_id

        job_source_type: None | str | Unset
        if isinstance(self.job_source_type, Unset):
            job_source_type = UNSET
        elif isinstance(self.job_source_type, JobSourceType):
            job_source_type = self.job_source_type.value
        else:
            job_source_type = self.job_source_type

        job_state_summary: dict[str, Any] | None | Unset
        if isinstance(self.job_state_summary, Unset):
            job_state_summary = UNSET
        elif isinstance(self.job_state_summary, HDCJobStateSummary):
            job_state_summary = self.job_state_summary.to_dict()
        else:
            job_state_summary = self.job_state_summary

        populated_state_message: None | str | Unset
        if isinstance(self.populated_state_message, Unset):
            populated_state_message = UNSET
        else:
            populated_state_message = self.populated_state_message

        store_times_summary: list[dict[str, Any]] | None | Unset
        if isinstance(self.store_times_summary, Unset):
            store_times_summary = UNSET
        elif isinstance(self.store_times_summary, list):
            store_times_summary = []
            for store_times_summary_type_0_item_data in self.store_times_summary:
                store_times_summary_type_0_item = store_times_summary_type_0_item_data.to_dict()
                store_times_summary.append(store_times_summary_type_0_item)

        else:
            store_times_summary = self.store_times_summary

        type_ = self.type_

        type_id: None | str | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "collection_type": collection_type,
                "contents_url": contents_url,
                "create_time": create_time,
                "deleted": deleted,
                "elements_datatypes": elements_datatypes,
                "elements_deleted": elements_deleted,
                "elements_states": elements_states,
                "hid": hid,
                "history_content_type": history_content_type,
                "history_id": history_id,
                "id": id,
                "model_class": model_class,
                "name": name,
                "populated_state": populated_state,
                "tags": tags,
                "update_time": update_time,
                "url": url,
                "visible": visible,
            }
        )
        if element_count is not UNSET:
            field_dict["element_count"] = element_count
        if job_source_id is not UNSET:
            field_dict["job_source_id"] = job_source_id
        if job_source_type is not UNSET:
            field_dict["job_source_type"] = job_source_type
        if job_state_summary is not UNSET:
            field_dict["job_state_summary"] = job_state_summary
        if populated_state_message is not UNSET:
            field_dict["populated_state_message"] = populated_state_message
        if store_times_summary is not UNSET:
            field_dict["store_times_summary"] = store_times_summary
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_id is not UNSET:
            field_dict["type_id"] = type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.elements_states_dict import ElementsStatesDict
        from ..models.hdc_job_state_summary import HDCJobStateSummary
        from ..models.oldest_create_time_by_object_store_id import OldestCreateTimeByObjectStoreId

        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        collection_type = d.pop("collection_type")

        contents_url = d.pop("contents_url")

        create_time = isoparse(d.pop("create_time"))

        deleted = d.pop("deleted")

        elements_datatypes = cast(list[str], d.pop("elements_datatypes"))

        elements_deleted = d.pop("elements_deleted")

        elements_states = ElementsStatesDict.from_dict(d.pop("elements_states"))

        hid = d.pop("hid")

        history_content_type = cast(Literal["dataset_collection"], d.pop("history_content_type"))
        if history_content_type != "dataset_collection":
            raise ValueError(
                f"history_content_type must match const 'dataset_collection', got '{history_content_type}'"
            )

        history_id = d.pop("history_id")

        id = d.pop("id")

        model_class = cast(Literal["HistoryDatasetCollectionAssociation"], d.pop("model_class"))
        if model_class != "HistoryDatasetCollectionAssociation":
            raise ValueError(f"model_class must match const 'HistoryDatasetCollectionAssociation', got '{model_class}'")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        populated_state = DatasetCollectionPopulatedState(d.pop("populated_state"))

        tags = cast(list[str], d.pop("tags"))

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

        def _parse_element_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        element_count = _parse_element_count(d.pop("element_count", UNSET))

        def _parse_job_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_source_id = _parse_job_source_id(d.pop("job_source_id", UNSET))

        def _parse_job_source_type(data: object) -> JobSourceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_source_type_type_0 = JobSourceType(data)

                return job_source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobSourceType | None | Unset, data)

        job_source_type = _parse_job_source_type(d.pop("job_source_type", UNSET))

        def _parse_job_state_summary(data: object) -> HDCJobStateSummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_state_summary_type_0 = HDCJobStateSummary.from_dict(data)

                return job_state_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HDCJobStateSummary | None | Unset, data)

        job_state_summary = _parse_job_state_summary(d.pop("job_state_summary", UNSET))

        def _parse_populated_state_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        populated_state_message = _parse_populated_state_message(d.pop("populated_state_message", UNSET))

        def _parse_store_times_summary(data: object) -> list[OldestCreateTimeByObjectStoreId] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                store_times_summary_type_0 = []
                _store_times_summary_type_0 = data
                for store_times_summary_type_0_item_data in _store_times_summary_type_0:
                    store_times_summary_type_0_item = OldestCreateTimeByObjectStoreId.from_dict(
                        store_times_summary_type_0_item_data
                    )

                    store_times_summary_type_0.append(store_times_summary_type_0_item)

                return store_times_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OldestCreateTimeByObjectStoreId] | None | Unset, data)

        store_times_summary = _parse_store_times_summary(d.pop("store_times_summary", UNSET))

        type_ = cast(Literal["collection"] | Unset, d.pop("type", UNSET))
        if type_ != "collection" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'collection', got '{type_}'")

        def _parse_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_id = _parse_type_id(d.pop("type_id", UNSET))

        hdca_summary = cls(
            collection_id=collection_id,
            collection_type=collection_type,
            contents_url=contents_url,
            create_time=create_time,
            deleted=deleted,
            elements_datatypes=elements_datatypes,
            elements_deleted=elements_deleted,
            elements_states=elements_states,
            hid=hid,
            history_content_type=history_content_type,
            history_id=history_id,
            id=id,
            model_class=model_class,
            name=name,
            populated_state=populated_state,
            tags=tags,
            update_time=update_time,
            url=url,
            visible=visible,
            element_count=element_count,
            job_source_id=job_source_id,
            job_source_type=job_source_type,
            job_state_summary=job_state_summary,
            populated_state_message=populated_state_message,
            store_times_summary=store_times_summary,
            type_=type_,
            type_id=type_id,
        )

        hdca_summary.additional_properties = d
        return hdca_summary

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
