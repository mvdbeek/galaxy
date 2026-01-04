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
    from ..models.dce_summary import DCESummary
    from ..models.elements_states_dict import ElementsStatesDict
    from ..models.hdc_job_state_summary import HDCJobStateSummary
    from ..models.oldest_create_time_by_object_store_id import OldestCreateTimeByObjectStoreId
    from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition


T = TypeVar("T", bound="HDCACustom")


@_attrs_define
class HDCACustom:
    """Can contain any serializable property of an HDCA.

    Allows arbitrary custom keys to be specified in the serialization
    parameters without a particular view (predefined set of keys).

        Attributes:
            collection_id (str | Unset):  Example: 0123456789ABCDEF.
            collection_type (None | str | Unset): The type of the collection, can be `list`, `paired`, or define
                subcollections using `:` as separator like `list:paired` or `list:list`.
            column_definitions (list[SampleSheetColumnDefinition] | None | Unset): Column data associated with each element
                of this collection.
            contents_url (None | str | Unset): The relative URL to access the contents of this History.
            create_time (datetime.datetime | None | Unset): The time and date this item was created.
            deleted (bool | None | Unset): Whether this item is marked as deleted.
            element_count (int | None | Unset): The number of elements contained in the dataset collection. It may be None
                or undefined if the collection could not be populated.
            elements (list[DCESummary] | Unset): The summary information of each of the elements inside the dataset
                collection.
            elements_datatypes (list[str] | None | Unset): A set containing all the different element datatypes in the
                collection.
            elements_deleted (int | None | Unset): The number of elements in the collection that are marked as deleted.
            elements_states (ElementsStatesDict | None | Unset): A dictionary containing counts for each dataset state in
                the collection.
            hid (int | None | Unset): The index position of this item in the History.
            history_content_type (Literal['dataset_collection'] | None | Unset): This is always `dataset_collection` for
                dataset collections.
            history_id (str | Unset):  Example: 0123456789ABCDEF.
            id (str | Unset):  Example: 0123456789ABCDEF.
            implicit_collection_jobs_id (None | str | Unset): Encoded ID for the ICJ object describing the collection of
                jobs corresponding to this collection
            job_source_id (None | str | Unset): The encoded ID of the Job that produced this dataset collection. Used to
                track the state of the job.
            job_source_type (JobSourceType | None | Unset): The type of job (model class) that produced this dataset
                collection. Used to track the state of the job.
            job_state_summary (HDCJobStateSummary | None | Unset): Overview of the job states working inside the dataset
                collection.
            model_class (Literal['HistoryDatasetCollectionAssociation'] | None | Unset): The name of the database model
                class.
            name (None | str | Unset): The name of the item.
            populated (bool | Unset): Whether the dataset collection elements (and any subcollections elements) were
                successfully populated.
            populated_state (DatasetCollectionPopulatedState | None | Unset): Indicates the general state of the elements in
                the dataset collection:- 'new': new dataset collection, unpopulated elements.- 'ok': collection elements
                populated (HDAs may or may not have errors).- 'failed': some problem populating, won't be populated.
            populated_state_message (None | str | Unset): Optional message with further information in case the population
                of the dataset collection failed.
            store_times_summary (list[OldestCreateTimeByObjectStoreId] | None | Unset): A list of objects containing the
                object store ID and the oldest creation time of the datasets stored in that object store for this
                collection.This is used to determine the age of the datasets in the collection when the object store is short-
                lived.
            tags (list[str] | None | Unset): The collection of tags associated with an item.
            type_ (Literal['collection'] | Unset): This is always `collection` for dataset collections. Default:
                'collection'.
            type_id (None | str | Unset): The type and the encoded ID of this item. Used for caching.
            update_time (datetime.datetime | None | Unset): The last time and date this item was updated.
            url (None | str | Unset): The relative URL to access this item.
            visible (bool | None | Unset): Whether this item is visible or hidden to the user by default.
    """

    collection_id: str | Unset = UNSET
    collection_type: None | str | Unset = UNSET
    column_definitions: list[SampleSheetColumnDefinition] | None | Unset = UNSET
    contents_url: None | str | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    deleted: bool | None | Unset = UNSET
    element_count: int | None | Unset = UNSET
    elements: list[DCESummary] | Unset = UNSET
    elements_datatypes: list[str] | None | Unset = UNSET
    elements_deleted: int | None | Unset = UNSET
    elements_states: ElementsStatesDict | None | Unset = UNSET
    hid: int | None | Unset = UNSET
    history_content_type: Literal["dataset_collection"] | None | Unset = UNSET
    history_id: str | Unset = UNSET
    id: str | Unset = UNSET
    implicit_collection_jobs_id: None | str | Unset = UNSET
    job_source_id: None | str | Unset = UNSET
    job_source_type: JobSourceType | None | Unset = UNSET
    job_state_summary: HDCJobStateSummary | None | Unset = UNSET
    model_class: Literal["HistoryDatasetCollectionAssociation"] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    populated: bool | Unset = UNSET
    populated_state: DatasetCollectionPopulatedState | None | Unset = UNSET
    populated_state_message: None | str | Unset = UNSET
    store_times_summary: list[OldestCreateTimeByObjectStoreId] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    type_: Literal["collection"] | Unset = "collection"
    type_id: None | str | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    url: None | str | Unset = UNSET
    visible: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.elements_states_dict import ElementsStatesDict
        from ..models.hdc_job_state_summary import HDCJobStateSummary

        collection_id = self.collection_id

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        column_definitions: list[dict[str, Any]] | None | Unset
        if isinstance(self.column_definitions, Unset):
            column_definitions = UNSET
        elif isinstance(self.column_definitions, list):
            column_definitions = []
            for column_definitions_type_0_item_data in self.column_definitions:
                column_definitions_type_0_item = column_definitions_type_0_item_data.to_dict()
                column_definitions.append(column_definitions_type_0_item)

        else:
            column_definitions = self.column_definitions

        contents_url: None | str | Unset
        if isinstance(self.contents_url, Unset):
            contents_url = UNSET
        else:
            contents_url = self.contents_url

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

        element_count: int | None | Unset
        if isinstance(self.element_count, Unset):
            element_count = UNSET
        else:
            element_count = self.element_count

        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        elements_datatypes: list[str] | None | Unset
        if isinstance(self.elements_datatypes, Unset):
            elements_datatypes = UNSET
        elif isinstance(self.elements_datatypes, list):
            elements_datatypes = self.elements_datatypes

        else:
            elements_datatypes = self.elements_datatypes

        elements_deleted: int | None | Unset
        if isinstance(self.elements_deleted, Unset):
            elements_deleted = UNSET
        else:
            elements_deleted = self.elements_deleted

        elements_states: dict[str, Any] | None | Unset
        if isinstance(self.elements_states, Unset):
            elements_states = UNSET
        elif isinstance(self.elements_states, ElementsStatesDict):
            elements_states = self.elements_states.to_dict()
        else:
            elements_states = self.elements_states

        hid: int | None | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        history_content_type: Literal["dataset_collection"] | None | Unset
        if isinstance(self.history_content_type, Unset):
            history_content_type = UNSET
        else:
            history_content_type = self.history_content_type

        history_id = self.history_id

        id = self.id

        implicit_collection_jobs_id: None | str | Unset
        if isinstance(self.implicit_collection_jobs_id, Unset):
            implicit_collection_jobs_id = UNSET
        else:
            implicit_collection_jobs_id = self.implicit_collection_jobs_id

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

        model_class: Literal["HistoryDatasetCollectionAssociation"] | None | Unset
        if isinstance(self.model_class, Unset):
            model_class = UNSET
        else:
            model_class = self.model_class

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        populated = self.populated

        populated_state: None | str | Unset
        if isinstance(self.populated_state, Unset):
            populated_state = UNSET
        elif isinstance(self.populated_state, DatasetCollectionPopulatedState):
            populated_state = self.populated_state.value
        else:
            populated_state = self.populated_state

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

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        type_ = self.type_

        type_id: None | str | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

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

        visible: bool | None | Unset
        if isinstance(self.visible, Unset):
            visible = UNSET
        else:
            visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if column_definitions is not UNSET:
            field_dict["column_definitions"] = column_definitions
        if contents_url is not UNSET:
            field_dict["contents_url"] = contents_url
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if element_count is not UNSET:
            field_dict["element_count"] = element_count
        if elements is not UNSET:
            field_dict["elements"] = elements
        if elements_datatypes is not UNSET:
            field_dict["elements_datatypes"] = elements_datatypes
        if elements_deleted is not UNSET:
            field_dict["elements_deleted"] = elements_deleted
        if elements_states is not UNSET:
            field_dict["elements_states"] = elements_states
        if hid is not UNSET:
            field_dict["hid"] = hid
        if history_content_type is not UNSET:
            field_dict["history_content_type"] = history_content_type
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if id is not UNSET:
            field_dict["id"] = id
        if implicit_collection_jobs_id is not UNSET:
            field_dict["implicit_collection_jobs_id"] = implicit_collection_jobs_id
        if job_source_id is not UNSET:
            field_dict["job_source_id"] = job_source_id
        if job_source_type is not UNSET:
            field_dict["job_source_type"] = job_source_type
        if job_state_summary is not UNSET:
            field_dict["job_state_summary"] = job_state_summary
        if model_class is not UNSET:
            field_dict["model_class"] = model_class
        if name is not UNSET:
            field_dict["name"] = name
        if populated is not UNSET:
            field_dict["populated"] = populated
        if populated_state is not UNSET:
            field_dict["populated_state"] = populated_state
        if populated_state_message is not UNSET:
            field_dict["populated_state_message"] = populated_state_message
        if store_times_summary is not UNSET:
            field_dict["store_times_summary"] = store_times_summary
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if url is not UNSET:
            field_dict["url"] = url
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dce_summary import DCESummary
        from ..models.elements_states_dict import ElementsStatesDict
        from ..models.hdc_job_state_summary import HDCJobStateSummary
        from ..models.oldest_create_time_by_object_store_id import OldestCreateTimeByObjectStoreId
        from ..models.sample_sheet_column_definition import SampleSheetColumnDefinition

        d = dict(src_dict)
        collection_id = d.pop("collection_id", UNSET)

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        def _parse_column_definitions(data: object) -> list[SampleSheetColumnDefinition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                column_definitions_type_0 = []
                _column_definitions_type_0 = data
                for column_definitions_type_0_item_data in _column_definitions_type_0:
                    column_definitions_type_0_item = SampleSheetColumnDefinition.from_dict(
                        column_definitions_type_0_item_data
                    )

                    column_definitions_type_0.append(column_definitions_type_0_item)

                return column_definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SampleSheetColumnDefinition] | None | Unset, data)

        column_definitions = _parse_column_definitions(d.pop("column_definitions", UNSET))

        def _parse_contents_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contents_url = _parse_contents_url(d.pop("contents_url", UNSET))

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

        def _parse_element_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        element_count = _parse_element_count(d.pop("element_count", UNSET))

        _elements = d.pop("elements", UNSET)
        elements: list[DCESummary] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = DCESummary.from_dict(elements_item_data)

                elements.append(elements_item)

        def _parse_elements_datatypes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                elements_datatypes_type_0 = cast(list[str], data)

                return elements_datatypes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        elements_datatypes = _parse_elements_datatypes(d.pop("elements_datatypes", UNSET))

        def _parse_elements_deleted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        elements_deleted = _parse_elements_deleted(d.pop("elements_deleted", UNSET))

        def _parse_elements_states(data: object) -> ElementsStatesDict | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                elements_states_type_0 = ElementsStatesDict.from_dict(data)

                return elements_states_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ElementsStatesDict | None | Unset, data)

        elements_states = _parse_elements_states(d.pop("elements_states", UNSET))

        def _parse_hid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        def _parse_history_content_type(data: object) -> Literal["dataset_collection"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            history_content_type_type_0 = cast(Literal["dataset_collection"], data)
            if history_content_type_type_0 != "dataset_collection":
                raise ValueError(
                    f"history_content_type_type_0 must match const 'dataset_collection', got '{history_content_type_type_0}'"
                )
            return history_content_type_type_0
            return cast(Literal["dataset_collection"] | None | Unset, data)

        history_content_type = _parse_history_content_type(d.pop("history_content_type", UNSET))

        history_id = d.pop("history_id", UNSET)

        id = d.pop("id", UNSET)

        def _parse_implicit_collection_jobs_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        implicit_collection_jobs_id = _parse_implicit_collection_jobs_id(d.pop("implicit_collection_jobs_id", UNSET))

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

        def _parse_model_class(data: object) -> Literal["HistoryDatasetCollectionAssociation"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            model_class_type_0 = cast(Literal["HistoryDatasetCollectionAssociation"], data)
            if model_class_type_0 != "HistoryDatasetCollectionAssociation":
                raise ValueError(
                    f"model_class_type_0 must match const 'HistoryDatasetCollectionAssociation', got '{model_class_type_0}'"
                )
            return model_class_type_0
            return cast(Literal["HistoryDatasetCollectionAssociation"] | None | Unset, data)

        model_class = _parse_model_class(d.pop("model_class", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        populated = d.pop("populated", UNSET)

        def _parse_populated_state(data: object) -> DatasetCollectionPopulatedState | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                populated_state_type_0 = DatasetCollectionPopulatedState(data)

                return populated_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetCollectionPopulatedState | None | Unset, data)

        populated_state = _parse_populated_state(d.pop("populated_state", UNSET))

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

        def _parse_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible = _parse_visible(d.pop("visible", UNSET))

        hdca_custom = cls(
            collection_id=collection_id,
            collection_type=collection_type,
            column_definitions=column_definitions,
            contents_url=contents_url,
            create_time=create_time,
            deleted=deleted,
            element_count=element_count,
            elements=elements,
            elements_datatypes=elements_datatypes,
            elements_deleted=elements_deleted,
            elements_states=elements_states,
            hid=hid,
            history_content_type=history_content_type,
            history_id=history_id,
            id=id,
            implicit_collection_jobs_id=implicit_collection_jobs_id,
            job_source_id=job_source_id,
            job_source_type=job_source_type,
            job_state_summary=job_state_summary,
            model_class=model_class,
            name=name,
            populated=populated,
            populated_state=populated_state,
            populated_state_message=populated_state_message,
            store_times_summary=store_times_summary,
            tags=tags,
            type_=type_,
            type_id=type_id,
            update_time=update_time,
            url=url,
            visible=visible,
        )

        hdca_custom.additional_properties = d
        return hdca_custom

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
