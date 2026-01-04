from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dataset_source_type import DatasetSourceType
from ..models.dataset_state import DatasetState
from ..models.dataset_validated_state import DatasetValidatedState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_hash import DatasetHash
    from ..models.dataset_permissions import DatasetPermissions
    from ..models.dataset_source import DatasetSource
    from ..models.display_app import DisplayApp
    from ..models.metadata_file import MetadataFile
    from ..models.visualization import Visualization


T = TypeVar("T", bound="HDACustom")


@_attrs_define
class HDACustom:
    """Can contain any serializable property of an HDA.

    Allows arbitrary custom keys to be specified in the serialization
    parameters without a particular view (predefined set of keys).

        Attributes:
            accessible (bool | None | Unset): Whether this item is accessible to the current user due to permissions.
            annotation (None | str | Unset): An annotation to provide details or to help understand the purpose and usage of
                this item.
            api_type (Literal['file'] | Unset): TODO Default: 'file'.
            copied_from_history_dataset_association_id (None | str | Unset): ID of HDA this HDA was copied from.
            copied_from_ldda_id (None | str | Unset):
            copied_from_library_dataset_dataset_association_id (None | str | Unset): ID of LDDA this HDA was copied from.
            create_time (datetime.datetime | None | Unset): The time and date this item was created.
            created_from_basename (None | str | Unset): The basename of the output that produced this dataset.
            creating_job (None | str | Unset): The encoded ID of the job that created this dataset.
            data_type (None | str | Unset): The fully qualified name of the class implementing the data type of this
                dataset.
            dataset_id (str | Unset): The encoded ID of the dataset associated with this item. Example: 0123456789ABCDEF.
            deleted (bool | None | Unset): Whether this item is marked as deleted.
            display_apps (list[DisplayApp] | None | Unset): Contains new-style display app urls.
            display_types (list[DisplayApp] | None | Unset): Contains old-style display app urls.
            download_url (None | str | Unset): The URL to download this item from the server.
            drs_id (None | str | Unset): The DRS ID of the dataset.
            extension (None | str | Unset): The extension of the dataset.
            file_ext (None | str | Unset): The extension of the file.
            file_name (None | str | Unset): The full path to the dataset file.
            file_size (int | None | Unset): The file size in bytes.
            genome_build (None | str | Unset): TODO Default: '?'.
            hashes (list[DatasetHash] | None | Unset): The list of hashes associated with this dataset.
            hda_ldda (DatasetSourceType | Unset):
            hid (int | None | Unset): The index position of this item in the History.
            history_content_type (Literal['dataset'] | None | Unset): This is always `dataset` for datasets.
            history_id (str | Unset):  Example: 0123456789ABCDEF.
            id (str | Unset):  Example: 0123456789ABCDEF.
            meta_files (list[MetadataFile] | None | Unset): Collection of metadata files associated with this dataset.
            metadata (Any | None | Unset): The metadata associated with this dataset.
            misc_blurb (None | str | Unset): TODO
            misc_info (None | str | Unset): TODO
            model_class (Literal['HistoryDatasetAssociation'] | None | Unset): The name of the database model class.
            name (None | str | Unset): The name of the item.
            object_store_id (None | str | Unset): The ID of the object store that this dataset is stored in.
            peek (None | str | Unset): A few lines of contents from the start of the file.
            permissions (DatasetPermissions | None | Unset): Role-based access and manage control permissions for the
                dataset.
            purged (bool | None | Unset): Whether this dataset has been removed from disk.
            rerunnable (bool | None | Unset): Whether the job creating this dataset can be run again.
            resubmitted (bool | None | Unset): Whether the job creating this dataset has been resubmitted.
            sources (list[DatasetSource] | None | Unset): The list of sources associated with this dataset.
            state (DatasetState | None | Unset): The current state of this dataset.
            tags (list[str] | None | Unset): The collection of tags associated with an item.
            type_ (Literal['file'] | Unset): This is always `file` for datasets. Default: 'file'.
            type_id (None | str | Unset): The type and the encoded ID of this item. Used for caching.
            update_time (datetime.datetime | None | Unset): The last time and date this item was updated.
            url (None | str | Unset): The relative URL to access this item.
            uuid (None | str | Unset):
            validated_state (DatasetValidatedState | None | Unset): The state of the datatype validation for this dataset.
            validated_state_message (None | str | Unset): The message with details about the datatype validation result for
                this dataset.
            visible (bool | None | Unset): Whether this item is visible or hidden to the user by default.
            visualizations (list[Visualization] | None | Unset): The collection of visualizations that can be applied to
                this dataset.
    """

    accessible: bool | None | Unset = UNSET
    annotation: None | str | Unset = UNSET
    api_type: Literal["file"] | Unset = "file"
    copied_from_history_dataset_association_id: None | str | Unset = UNSET
    copied_from_ldda_id: None | str | Unset = UNSET
    copied_from_library_dataset_dataset_association_id: None | str | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    created_from_basename: None | str | Unset = UNSET
    creating_job: None | str | Unset = UNSET
    data_type: None | str | Unset = UNSET
    dataset_id: str | Unset = UNSET
    deleted: bool | None | Unset = UNSET
    display_apps: list[DisplayApp] | None | Unset = UNSET
    display_types: list[DisplayApp] | None | Unset = UNSET
    download_url: None | str | Unset = UNSET
    drs_id: None | str | Unset = UNSET
    extension: None | str | Unset = UNSET
    file_ext: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    file_size: int | None | Unset = UNSET
    genome_build: None | str | Unset = "?"
    hashes: list[DatasetHash] | None | Unset = UNSET
    hda_ldda: DatasetSourceType | Unset = UNSET
    hid: int | None | Unset = UNSET
    history_content_type: Literal["dataset"] | None | Unset = UNSET
    history_id: str | Unset = UNSET
    id: str | Unset = UNSET
    meta_files: list[MetadataFile] | None | Unset = UNSET
    metadata: Any | None | Unset = UNSET
    misc_blurb: None | str | Unset = UNSET
    misc_info: None | str | Unset = UNSET
    model_class: Literal["HistoryDatasetAssociation"] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    object_store_id: None | str | Unset = UNSET
    peek: None | str | Unset = UNSET
    permissions: DatasetPermissions | None | Unset = UNSET
    purged: bool | None | Unset = UNSET
    rerunnable: bool | None | Unset = UNSET
    resubmitted: bool | None | Unset = UNSET
    sources: list[DatasetSource] | None | Unset = UNSET
    state: DatasetState | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    type_: Literal["file"] | Unset = "file"
    type_id: None | str | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    url: None | str | Unset = UNSET
    uuid: None | str | Unset = UNSET
    validated_state: DatasetValidatedState | None | Unset = UNSET
    validated_state_message: None | str | Unset = UNSET
    visible: bool | None | Unset = UNSET
    visualizations: list[Visualization] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_permissions import DatasetPermissions

        accessible: bool | None | Unset
        if isinstance(self.accessible, Unset):
            accessible = UNSET
        else:
            accessible = self.accessible

        annotation: None | str | Unset
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        api_type = self.api_type

        copied_from_history_dataset_association_id: None | str | Unset
        if isinstance(self.copied_from_history_dataset_association_id, Unset):
            copied_from_history_dataset_association_id = UNSET
        else:
            copied_from_history_dataset_association_id = self.copied_from_history_dataset_association_id

        copied_from_ldda_id: None | str | Unset
        if isinstance(self.copied_from_ldda_id, Unset):
            copied_from_ldda_id = UNSET
        else:
            copied_from_ldda_id = self.copied_from_ldda_id

        copied_from_library_dataset_dataset_association_id: None | str | Unset
        if isinstance(self.copied_from_library_dataset_dataset_association_id, Unset):
            copied_from_library_dataset_dataset_association_id = UNSET
        else:
            copied_from_library_dataset_dataset_association_id = self.copied_from_library_dataset_dataset_association_id

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        created_from_basename: None | str | Unset
        if isinstance(self.created_from_basename, Unset):
            created_from_basename = UNSET
        else:
            created_from_basename = self.created_from_basename

        creating_job: None | str | Unset
        if isinstance(self.creating_job, Unset):
            creating_job = UNSET
        else:
            creating_job = self.creating_job

        data_type: None | str | Unset
        if isinstance(self.data_type, Unset):
            data_type = UNSET
        else:
            data_type = self.data_type

        dataset_id = self.dataset_id

        deleted: bool | None | Unset
        if isinstance(self.deleted, Unset):
            deleted = UNSET
        else:
            deleted = self.deleted

        display_apps: list[dict[str, Any]] | None | Unset
        if isinstance(self.display_apps, Unset):
            display_apps = UNSET
        elif isinstance(self.display_apps, list):
            display_apps = []
            for display_apps_type_0_item_data in self.display_apps:
                display_apps_type_0_item = display_apps_type_0_item_data.to_dict()
                display_apps.append(display_apps_type_0_item)

        else:
            display_apps = self.display_apps

        display_types: list[dict[str, Any]] | None | Unset
        if isinstance(self.display_types, Unset):
            display_types = UNSET
        elif isinstance(self.display_types, list):
            display_types = []
            for display_types_type_0_item_data in self.display_types:
                display_types_type_0_item = display_types_type_0_item_data.to_dict()
                display_types.append(display_types_type_0_item)

        else:
            display_types = self.display_types

        download_url: None | str | Unset
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        drs_id: None | str | Unset
        if isinstance(self.drs_id, Unset):
            drs_id = UNSET
        else:
            drs_id = self.drs_id

        extension: None | str | Unset
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        file_ext: None | str | Unset
        if isinstance(self.file_ext, Unset):
            file_ext = UNSET
        else:
            file_ext = self.file_ext

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_size: int | None | Unset
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        genome_build: None | str | Unset
        if isinstance(self.genome_build, Unset):
            genome_build = UNSET
        else:
            genome_build = self.genome_build

        hashes: list[dict[str, Any]] | None | Unset
        if isinstance(self.hashes, Unset):
            hashes = UNSET
        elif isinstance(self.hashes, list):
            hashes = []
            for hashes_type_0_item_data in self.hashes:
                hashes_type_0_item = hashes_type_0_item_data.to_dict()
                hashes.append(hashes_type_0_item)

        else:
            hashes = self.hashes

        hda_ldda: str | Unset = UNSET
        if not isinstance(self.hda_ldda, Unset):
            hda_ldda = self.hda_ldda.value

        hid: int | None | Unset
        if isinstance(self.hid, Unset):
            hid = UNSET
        else:
            hid = self.hid

        history_content_type: Literal["dataset"] | None | Unset
        if isinstance(self.history_content_type, Unset):
            history_content_type = UNSET
        else:
            history_content_type = self.history_content_type

        history_id = self.history_id

        id = self.id

        meta_files: list[dict[str, Any]] | None | Unset
        if isinstance(self.meta_files, Unset):
            meta_files = UNSET
        elif isinstance(self.meta_files, list):
            meta_files = []
            for meta_files_type_0_item_data in self.meta_files:
                meta_files_type_0_item = meta_files_type_0_item_data.to_dict()
                meta_files.append(meta_files_type_0_item)

        else:
            meta_files = self.meta_files

        metadata: Any | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        misc_blurb: None | str | Unset
        if isinstance(self.misc_blurb, Unset):
            misc_blurb = UNSET
        else:
            misc_blurb = self.misc_blurb

        misc_info: None | str | Unset
        if isinstance(self.misc_info, Unset):
            misc_info = UNSET
        else:
            misc_info = self.misc_info

        model_class: Literal["HistoryDatasetAssociation"] | None | Unset
        if isinstance(self.model_class, Unset):
            model_class = UNSET
        else:
            model_class = self.model_class

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        object_store_id: None | str | Unset
        if isinstance(self.object_store_id, Unset):
            object_store_id = UNSET
        else:
            object_store_id = self.object_store_id

        peek: None | str | Unset
        if isinstance(self.peek, Unset):
            peek = UNSET
        else:
            peek = self.peek

        permissions: dict[str, Any] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, DatasetPermissions):
            permissions = self.permissions.to_dict()
        else:
            permissions = self.permissions

        purged: bool | None | Unset
        if isinstance(self.purged, Unset):
            purged = UNSET
        else:
            purged = self.purged

        rerunnable: bool | None | Unset
        if isinstance(self.rerunnable, Unset):
            rerunnable = UNSET
        else:
            rerunnable = self.rerunnable

        resubmitted: bool | None | Unset
        if isinstance(self.resubmitted, Unset):
            resubmitted = UNSET
        else:
            resubmitted = self.resubmitted

        sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, DatasetState):
            state = self.state.value
        else:
            state = self.state

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

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        validated_state: None | str | Unset
        if isinstance(self.validated_state, Unset):
            validated_state = UNSET
        elif isinstance(self.validated_state, DatasetValidatedState):
            validated_state = self.validated_state.value
        else:
            validated_state = self.validated_state

        validated_state_message: None | str | Unset
        if isinstance(self.validated_state_message, Unset):
            validated_state_message = UNSET
        else:
            validated_state_message = self.validated_state_message

        visible: bool | None | Unset
        if isinstance(self.visible, Unset):
            visible = UNSET
        else:
            visible = self.visible

        visualizations: list[dict[str, Any]] | None | Unset
        if isinstance(self.visualizations, Unset):
            visualizations = UNSET
        elif isinstance(self.visualizations, list):
            visualizations = []
            for visualizations_type_0_item_data in self.visualizations:
                visualizations_type_0_item = visualizations_type_0_item_data.to_dict()
                visualizations.append(visualizations_type_0_item)

        else:
            visualizations = self.visualizations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessible is not UNSET:
            field_dict["accessible"] = accessible
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if api_type is not UNSET:
            field_dict["api_type"] = api_type
        if copied_from_history_dataset_association_id is not UNSET:
            field_dict["copied_from_history_dataset_association_id"] = copied_from_history_dataset_association_id
        if copied_from_ldda_id is not UNSET:
            field_dict["copied_from_ldda_id"] = copied_from_ldda_id
        if copied_from_library_dataset_dataset_association_id is not UNSET:
            field_dict["copied_from_library_dataset_dataset_association_id"] = (
                copied_from_library_dataset_dataset_association_id
            )
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if created_from_basename is not UNSET:
            field_dict["created_from_basename"] = created_from_basename
        if creating_job is not UNSET:
            field_dict["creating_job"] = creating_job
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if display_apps is not UNSET:
            field_dict["display_apps"] = display_apps
        if display_types is not UNSET:
            field_dict["display_types"] = display_types
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if drs_id is not UNSET:
            field_dict["drs_id"] = drs_id
        if extension is not UNSET:
            field_dict["extension"] = extension
        if file_ext is not UNSET:
            field_dict["file_ext"] = file_ext
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if hda_ldda is not UNSET:
            field_dict["hda_ldda"] = hda_ldda
        if hid is not UNSET:
            field_dict["hid"] = hid
        if history_content_type is not UNSET:
            field_dict["history_content_type"] = history_content_type
        if history_id is not UNSET:
            field_dict["history_id"] = history_id
        if id is not UNSET:
            field_dict["id"] = id
        if meta_files is not UNSET:
            field_dict["meta_files"] = meta_files
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if misc_blurb is not UNSET:
            field_dict["misc_blurb"] = misc_blurb
        if misc_info is not UNSET:
            field_dict["misc_info"] = misc_info
        if model_class is not UNSET:
            field_dict["model_class"] = model_class
        if name is not UNSET:
            field_dict["name"] = name
        if object_store_id is not UNSET:
            field_dict["object_store_id"] = object_store_id
        if peek is not UNSET:
            field_dict["peek"] = peek
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if purged is not UNSET:
            field_dict["purged"] = purged
        if rerunnable is not UNSET:
            field_dict["rerunnable"] = rerunnable
        if resubmitted is not UNSET:
            field_dict["resubmitted"] = resubmitted
        if sources is not UNSET:
            field_dict["sources"] = sources
        if state is not UNSET:
            field_dict["state"] = state
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
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if validated_state is not UNSET:
            field_dict["validated_state"] = validated_state
        if validated_state_message is not UNSET:
            field_dict["validated_state_message"] = validated_state_message
        if visible is not UNSET:
            field_dict["visible"] = visible
        if visualizations is not UNSET:
            field_dict["visualizations"] = visualizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_hash import DatasetHash
        from ..models.dataset_permissions import DatasetPermissions
        from ..models.dataset_source import DatasetSource
        from ..models.display_app import DisplayApp
        from ..models.metadata_file import MetadataFile
        from ..models.visualization import Visualization

        d = dict(src_dict)

        def _parse_accessible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        accessible = _parse_accessible(d.pop("accessible", UNSET))

        def _parse_annotation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        api_type = cast(Literal["file"] | Unset, d.pop("api_type", UNSET))
        if api_type != "file" and not isinstance(api_type, Unset):
            raise ValueError(f"api_type must match const 'file', got '{api_type}'")

        def _parse_copied_from_history_dataset_association_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_history_dataset_association_id = _parse_copied_from_history_dataset_association_id(
            d.pop("copied_from_history_dataset_association_id", UNSET)
        )

        def _parse_copied_from_ldda_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_ldda_id = _parse_copied_from_ldda_id(d.pop("copied_from_ldda_id", UNSET))

        def _parse_copied_from_library_dataset_dataset_association_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        copied_from_library_dataset_dataset_association_id = _parse_copied_from_library_dataset_dataset_association_id(
            d.pop("copied_from_library_dataset_dataset_association_id", UNSET)
        )

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

        def _parse_created_from_basename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_from_basename = _parse_created_from_basename(d.pop("created_from_basename", UNSET))

        def _parse_creating_job(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        creating_job = _parse_creating_job(d.pop("creating_job", UNSET))

        def _parse_data_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_type = _parse_data_type(d.pop("data_type", UNSET))

        dataset_id = d.pop("dataset_id", UNSET)

        def _parse_deleted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted = _parse_deleted(d.pop("deleted", UNSET))

        def _parse_display_apps(data: object) -> list[DisplayApp] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                display_apps_type_0 = []
                _display_apps_type_0 = data
                for display_apps_type_0_item_data in _display_apps_type_0:
                    display_apps_type_0_item = DisplayApp.from_dict(display_apps_type_0_item_data)

                    display_apps_type_0.append(display_apps_type_0_item)

                return display_apps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DisplayApp] | None | Unset, data)

        display_apps = _parse_display_apps(d.pop("display_apps", UNSET))

        def _parse_display_types(data: object) -> list[DisplayApp] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                display_types_type_0 = []
                _display_types_type_0 = data
                for display_types_type_0_item_data in _display_types_type_0:
                    display_types_type_0_item = DisplayApp.from_dict(display_types_type_0_item_data)

                    display_types_type_0.append(display_types_type_0_item)

                return display_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DisplayApp] | None | Unset, data)

        display_types = _parse_display_types(d.pop("display_types", UNSET))

        def _parse_download_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_url = _parse_download_url(d.pop("download_url", UNSET))

        def _parse_drs_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drs_id = _parse_drs_id(d.pop("drs_id", UNSET))

        def _parse_extension(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension = _parse_extension(d.pop("extension", UNSET))

        def _parse_file_ext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_ext = _parse_file_ext(d.pop("file_ext", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_file_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_genome_build(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genome_build = _parse_genome_build(d.pop("genome_build", UNSET))

        def _parse_hashes(data: object) -> list[DatasetHash] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hashes_type_0 = []
                _hashes_type_0 = data
                for hashes_type_0_item_data in _hashes_type_0:
                    hashes_type_0_item = DatasetHash.from_dict(hashes_type_0_item_data)

                    hashes_type_0.append(hashes_type_0_item)

                return hashes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatasetHash] | None | Unset, data)

        hashes = _parse_hashes(d.pop("hashes", UNSET))

        _hda_ldda = d.pop("hda_ldda", UNSET)
        hda_ldda: DatasetSourceType | Unset
        if isinstance(_hda_ldda, Unset):
            hda_ldda = UNSET
        else:
            hda_ldda = DatasetSourceType(_hda_ldda)

        def _parse_hid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hid = _parse_hid(d.pop("hid", UNSET))

        def _parse_history_content_type(data: object) -> Literal["dataset"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            history_content_type_type_0 = cast(Literal["dataset"], data)
            if history_content_type_type_0 != "dataset":
                raise ValueError(
                    f"history_content_type_type_0 must match const 'dataset', got '{history_content_type_type_0}'"
                )
            return history_content_type_type_0
            return cast(Literal["dataset"] | None | Unset, data)

        history_content_type = _parse_history_content_type(d.pop("history_content_type", UNSET))

        history_id = d.pop("history_id", UNSET)

        id = d.pop("id", UNSET)

        def _parse_meta_files(data: object) -> list[MetadataFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                meta_files_type_0 = []
                _meta_files_type_0 = data
                for meta_files_type_0_item_data in _meta_files_type_0:
                    meta_files_type_0_item = MetadataFile.from_dict(meta_files_type_0_item_data)

                    meta_files_type_0.append(meta_files_type_0_item)

                return meta_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MetadataFile] | None | Unset, data)

        meta_files = _parse_meta_files(d.pop("meta_files", UNSET))

        def _parse_metadata(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_misc_blurb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_blurb = _parse_misc_blurb(d.pop("misc_blurb", UNSET))

        def _parse_misc_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_info = _parse_misc_info(d.pop("misc_info", UNSET))

        def _parse_model_class(data: object) -> Literal["HistoryDatasetAssociation"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            model_class_type_0 = cast(Literal["HistoryDatasetAssociation"], data)
            if model_class_type_0 != "HistoryDatasetAssociation":
                raise ValueError(
                    f"model_class_type_0 must match const 'HistoryDatasetAssociation', got '{model_class_type_0}'"
                )
            return model_class_type_0
            return cast(Literal["HistoryDatasetAssociation"] | None | Unset, data)

        model_class = _parse_model_class(d.pop("model_class", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_object_store_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_store_id = _parse_object_store_id(d.pop("object_store_id", UNSET))

        def _parse_peek(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        peek = _parse_peek(d.pop("peek", UNSET))

        def _parse_permissions(data: object) -> DatasetPermissions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permissions_type_0 = DatasetPermissions.from_dict(data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetPermissions | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_purged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        purged = _parse_purged(d.pop("purged", UNSET))

        def _parse_rerunnable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rerunnable = _parse_rerunnable(d.pop("rerunnable", UNSET))

        def _parse_resubmitted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resubmitted = _parse_resubmitted(d.pop("resubmitted", UNSET))

        def _parse_sources(data: object) -> list[DatasetSource] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = DatasetSource.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DatasetSource] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

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

        type_ = cast(Literal["file"] | Unset, d.pop("type", UNSET))
        if type_ != "file" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'file', got '{type_}'")

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

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        def _parse_validated_state(data: object) -> DatasetValidatedState | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                validated_state_type_0 = DatasetValidatedState(data)

                return validated_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasetValidatedState | None | Unset, data)

        validated_state = _parse_validated_state(d.pop("validated_state", UNSET))

        def _parse_validated_state_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validated_state_message = _parse_validated_state_message(d.pop("validated_state_message", UNSET))

        def _parse_visible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible = _parse_visible(d.pop("visible", UNSET))

        def _parse_visualizations(data: object) -> list[Visualization] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                visualizations_type_0 = []
                _visualizations_type_0 = data
                for visualizations_type_0_item_data in _visualizations_type_0:
                    visualizations_type_0_item = Visualization.from_dict(visualizations_type_0_item_data)

                    visualizations_type_0.append(visualizations_type_0_item)

                return visualizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Visualization] | None | Unset, data)

        visualizations = _parse_visualizations(d.pop("visualizations", UNSET))

        hda_custom = cls(
            accessible=accessible,
            annotation=annotation,
            api_type=api_type,
            copied_from_history_dataset_association_id=copied_from_history_dataset_association_id,
            copied_from_ldda_id=copied_from_ldda_id,
            copied_from_library_dataset_dataset_association_id=copied_from_library_dataset_dataset_association_id,
            create_time=create_time,
            created_from_basename=created_from_basename,
            creating_job=creating_job,
            data_type=data_type,
            dataset_id=dataset_id,
            deleted=deleted,
            display_apps=display_apps,
            display_types=display_types,
            download_url=download_url,
            drs_id=drs_id,
            extension=extension,
            file_ext=file_ext,
            file_name=file_name,
            file_size=file_size,
            genome_build=genome_build,
            hashes=hashes,
            hda_ldda=hda_ldda,
            hid=hid,
            history_content_type=history_content_type,
            history_id=history_id,
            id=id,
            meta_files=meta_files,
            metadata=metadata,
            misc_blurb=misc_blurb,
            misc_info=misc_info,
            model_class=model_class,
            name=name,
            object_store_id=object_store_id,
            peek=peek,
            permissions=permissions,
            purged=purged,
            rerunnable=rerunnable,
            resubmitted=resubmitted,
            sources=sources,
            state=state,
            tags=tags,
            type_=type_,
            type_id=type_id,
            update_time=update_time,
            url=url,
            uuid=uuid,
            validated_state=validated_state,
            validated_state_message=validated_state_message,
            visible=visible,
            visualizations=visualizations,
        )

        hda_custom.additional_properties = d
        return hda_custom

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
