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


T = TypeVar("T", bound="HDADetailed")


@_attrs_define
class HDADetailed:
    """History Dataset Association detailed information.

    Attributes:
        accessible (bool): Whether this item is accessible to the current user due to permissions.
        annotation (None | str): An annotation to provide details or to help understand the purpose and usage of this
            item.
        create_time (datetime.datetime): The time and date this item was created.
        creating_job (str): The encoded ID of the job that created this dataset.
        data_type (str): The fully qualified name of the class implementing the data type of this dataset.
        dataset_id (str): The encoded ID of the dataset associated with this item. Example: 0123456789ABCDEF.
        deleted (bool): Whether this item is marked as deleted.
        display_apps (list[DisplayApp]): Contains new-style display app urls.
        display_types (list[DisplayApp]): Contains old-style display app urls.
        download_url (str): The URL to download this item from the server.
        drs_id (str): The DRS ID of the dataset.
        extension (None | str): The extension of the dataset.
        file_ext (str): The extension of the file.
        file_size (int): The file size in bytes.
        hashes (list[DatasetHash]): The list of hashes associated with this dataset.
        hid (int): The index position of this item in the History.
        history_content_type (Literal['dataset']): This is always `dataset` for datasets.
        history_id (str):  Example: 0123456789ABCDEF.
        id (str):  Example: 0123456789ABCDEF.
        meta_files (list[MetadataFile]): Collection of metadata files associated with this dataset.
        model_class (Literal['HistoryDatasetAssociation']): The name of the database model class.
        name (None | str): The name of the item.
        permissions (DatasetPermissions): Role-based permissions for accessing and managing a dataset.
        purged (bool): Whether this dataset has been removed from disk.
        rerunnable (bool): Whether the job creating this dataset can be run again.
        resubmitted (bool): Whether the job creating this dataset has been resubmitted.
        sources (list[DatasetSource]): The list of sources associated with this dataset.
        state (DatasetState):
        tags (list[str]): The collection of tags associated with an item.
        update_time (datetime.datetime | None): The last time and date this item was updated.
        url (str): The relative URL to access this item.
        uuid (str): Universal unique identifier for this dataset.
        validated_state (DatasetValidatedState):
        visible (bool): Whether this item is visible or hidden to the user by default.
        api_type (Literal['file'] | Unset): TODO Default: 'file'.
        copied_from_history_dataset_association_id (None | str | Unset): ID of HDA this HDA was copied from.
        copied_from_ldda_id (None | str | Unset):
        copied_from_library_dataset_dataset_association_id (None | str | Unset): ID of LDDA this HDA was copied from.
        created_from_basename (None | str | Unset): The basename of the output that produced this dataset.
        file_name (None | str | Unset): The full path to the dataset file.
        genome_build (None | str | Unset): TODO Default: '?'.
        hda_ldda (DatasetSourceType | Unset):
        metadata (Any | None | Unset): The metadata associated with this dataset.
        misc_blurb (None | str | Unset): TODO
        misc_info (None | str | Unset): TODO
        object_store_id (None | str | Unset): The ID of the object store that this dataset is stored in.
        peek (None | str | Unset): A few lines of contents from the start of the file.
        type_ (Literal['file'] | Unset): This is always `file` for datasets. Default: 'file'.
        type_id (None | str | Unset): The type and the encoded ID of this item. Used for caching.
        validated_state_message (None | str | Unset): The message with details about the datatype validation result for
            this dataset.
    """

    accessible: bool
    annotation: None | str
    create_time: datetime.datetime
    creating_job: str
    data_type: str
    dataset_id: str
    deleted: bool
    display_apps: list[DisplayApp]
    display_types: list[DisplayApp]
    download_url: str
    drs_id: str
    extension: None | str
    file_ext: str
    file_size: int
    hashes: list[DatasetHash]
    hid: int
    history_content_type: Literal["dataset"]
    history_id: str
    id: str
    meta_files: list[MetadataFile]
    model_class: Literal["HistoryDatasetAssociation"]
    name: None | str
    permissions: DatasetPermissions
    purged: bool
    rerunnable: bool
    resubmitted: bool
    sources: list[DatasetSource]
    state: DatasetState
    tags: list[str]
    update_time: datetime.datetime | None
    url: str
    uuid: str
    validated_state: DatasetValidatedState
    visible: bool
    api_type: Literal["file"] | Unset = "file"
    copied_from_history_dataset_association_id: None | str | Unset = UNSET
    copied_from_ldda_id: None | str | Unset = UNSET
    copied_from_library_dataset_dataset_association_id: None | str | Unset = UNSET
    created_from_basename: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    genome_build: None | str | Unset = "?"
    hda_ldda: DatasetSourceType | Unset = UNSET
    metadata: Any | None | Unset = UNSET
    misc_blurb: None | str | Unset = UNSET
    misc_info: None | str | Unset = UNSET
    object_store_id: None | str | Unset = UNSET
    peek: None | str | Unset = UNSET
    type_: Literal["file"] | Unset = "file"
    type_id: None | str | Unset = UNSET
    validated_state_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessible = self.accessible

        annotation: None | str
        annotation = self.annotation

        create_time = self.create_time.isoformat()

        creating_job = self.creating_job

        data_type = self.data_type

        dataset_id = self.dataset_id

        deleted = self.deleted

        display_apps = []
        for display_apps_item_data in self.display_apps:
            display_apps_item = display_apps_item_data.to_dict()
            display_apps.append(display_apps_item)

        display_types = []
        for display_types_item_data in self.display_types:
            display_types_item = display_types_item_data.to_dict()
            display_types.append(display_types_item)

        download_url = self.download_url

        drs_id = self.drs_id

        extension: None | str
        extension = self.extension

        file_ext = self.file_ext

        file_size = self.file_size

        hashes = []
        for hashes_item_data in self.hashes:
            hashes_item = hashes_item_data.to_dict()
            hashes.append(hashes_item)

        hid = self.hid

        history_content_type = self.history_content_type

        history_id = self.history_id

        id = self.id

        meta_files = []
        for meta_files_item_data in self.meta_files:
            meta_files_item = meta_files_item_data.to_dict()
            meta_files.append(meta_files_item)

        model_class = self.model_class

        name: None | str
        name = self.name

        permissions = self.permissions.to_dict()

        purged = self.purged

        rerunnable = self.rerunnable

        resubmitted = self.resubmitted

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        state = self.state.value

        tags = self.tags

        update_time: None | str
        if isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        url = self.url

        uuid = self.uuid

        validated_state = self.validated_state.value

        visible = self.visible

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

        created_from_basename: None | str | Unset
        if isinstance(self.created_from_basename, Unset):
            created_from_basename = UNSET
        else:
            created_from_basename = self.created_from_basename

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        genome_build: None | str | Unset
        if isinstance(self.genome_build, Unset):
            genome_build = UNSET
        else:
            genome_build = self.genome_build

        hda_ldda: str | Unset = UNSET
        if not isinstance(self.hda_ldda, Unset):
            hda_ldda = self.hda_ldda.value

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

        type_ = self.type_

        type_id: None | str | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        validated_state_message: None | str | Unset
        if isinstance(self.validated_state_message, Unset):
            validated_state_message = UNSET
        else:
            validated_state_message = self.validated_state_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessible": accessible,
                "annotation": annotation,
                "create_time": create_time,
                "creating_job": creating_job,
                "data_type": data_type,
                "dataset_id": dataset_id,
                "deleted": deleted,
                "display_apps": display_apps,
                "display_types": display_types,
                "download_url": download_url,
                "drs_id": drs_id,
                "extension": extension,
                "file_ext": file_ext,
                "file_size": file_size,
                "hashes": hashes,
                "hid": hid,
                "history_content_type": history_content_type,
                "history_id": history_id,
                "id": id,
                "meta_files": meta_files,
                "model_class": model_class,
                "name": name,
                "permissions": permissions,
                "purged": purged,
                "rerunnable": rerunnable,
                "resubmitted": resubmitted,
                "sources": sources,
                "state": state,
                "tags": tags,
                "update_time": update_time,
                "url": url,
                "uuid": uuid,
                "validated_state": validated_state,
                "visible": visible,
            }
        )
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
        if created_from_basename is not UNSET:
            field_dict["created_from_basename"] = created_from_basename
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if genome_build is not UNSET:
            field_dict["genome_build"] = genome_build
        if hda_ldda is not UNSET:
            field_dict["hda_ldda"] = hda_ldda
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if misc_blurb is not UNSET:
            field_dict["misc_blurb"] = misc_blurb
        if misc_info is not UNSET:
            field_dict["misc_info"] = misc_info
        if object_store_id is not UNSET:
            field_dict["object_store_id"] = object_store_id
        if peek is not UNSET:
            field_dict["peek"] = peek
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if validated_state_message is not UNSET:
            field_dict["validated_state_message"] = validated_state_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_hash import DatasetHash
        from ..models.dataset_permissions import DatasetPermissions
        from ..models.dataset_source import DatasetSource
        from ..models.display_app import DisplayApp
        from ..models.metadata_file import MetadataFile

        d = dict(src_dict)
        accessible = d.pop("accessible")

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        create_time = isoparse(d.pop("create_time"))

        creating_job = d.pop("creating_job")

        data_type = d.pop("data_type")

        dataset_id = d.pop("dataset_id")

        deleted = d.pop("deleted")

        display_apps = []
        _display_apps = d.pop("display_apps")
        for display_apps_item_data in _display_apps:
            display_apps_item = DisplayApp.from_dict(display_apps_item_data)

            display_apps.append(display_apps_item)

        display_types = []
        _display_types = d.pop("display_types")
        for display_types_item_data in _display_types:
            display_types_item = DisplayApp.from_dict(display_types_item_data)

            display_types.append(display_types_item)

        download_url = d.pop("download_url")

        drs_id = d.pop("drs_id")

        def _parse_extension(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        extension = _parse_extension(d.pop("extension"))

        file_ext = d.pop("file_ext")

        file_size = d.pop("file_size")

        hashes = []
        _hashes = d.pop("hashes")
        for hashes_item_data in _hashes:
            hashes_item = DatasetHash.from_dict(hashes_item_data)

            hashes.append(hashes_item)

        hid = d.pop("hid")

        history_content_type = cast(Literal["dataset"], d.pop("history_content_type"))
        if history_content_type != "dataset":
            raise ValueError(f"history_content_type must match const 'dataset', got '{history_content_type}'")

        history_id = d.pop("history_id")

        id = d.pop("id")

        meta_files = []
        _meta_files = d.pop("meta_files")
        for meta_files_item_data in _meta_files:
            meta_files_item = MetadataFile.from_dict(meta_files_item_data)

            meta_files.append(meta_files_item)

        model_class = cast(Literal["HistoryDatasetAssociation"], d.pop("model_class"))
        if model_class != "HistoryDatasetAssociation":
            raise ValueError(f"model_class must match const 'HistoryDatasetAssociation', got '{model_class}'")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        permissions = DatasetPermissions.from_dict(d.pop("permissions"))

        purged = d.pop("purged")

        rerunnable = d.pop("rerunnable")

        resubmitted = d.pop("resubmitted")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = DatasetSource.from_dict(sources_item_data)

            sources.append(sources_item)

        state = DatasetState(d.pop("state"))

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

        uuid = d.pop("uuid")

        validated_state = DatasetValidatedState(d.pop("validated_state"))

        visible = d.pop("visible")

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

        def _parse_created_from_basename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_from_basename = _parse_created_from_basename(d.pop("created_from_basename", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_genome_build(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        genome_build = _parse_genome_build(d.pop("genome_build", UNSET))

        _hda_ldda = d.pop("hda_ldda", UNSET)
        hda_ldda: DatasetSourceType | Unset
        if isinstance(_hda_ldda, Unset):
            hda_ldda = UNSET
        else:
            hda_ldda = DatasetSourceType(_hda_ldda)

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

        def _parse_validated_state_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validated_state_message = _parse_validated_state_message(d.pop("validated_state_message", UNSET))

        hda_detailed = cls(
            accessible=accessible,
            annotation=annotation,
            create_time=create_time,
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
            file_size=file_size,
            hashes=hashes,
            hid=hid,
            history_content_type=history_content_type,
            history_id=history_id,
            id=id,
            meta_files=meta_files,
            model_class=model_class,
            name=name,
            permissions=permissions,
            purged=purged,
            rerunnable=rerunnable,
            resubmitted=resubmitted,
            sources=sources,
            state=state,
            tags=tags,
            update_time=update_time,
            url=url,
            uuid=uuid,
            validated_state=validated_state,
            visible=visible,
            api_type=api_type,
            copied_from_history_dataset_association_id=copied_from_history_dataset_association_id,
            copied_from_ldda_id=copied_from_ldda_id,
            copied_from_library_dataset_dataset_association_id=copied_from_library_dataset_dataset_association_id,
            created_from_basename=created_from_basename,
            file_name=file_name,
            genome_build=genome_build,
            hda_ldda=hda_ldda,
            metadata=metadata,
            misc_blurb=misc_blurb,
            misc_info=misc_info,
            object_store_id=object_store_id,
            peek=peek,
            type_=type_,
            type_id=type_id,
            validated_state_message=validated_state_message,
        )

        hda_detailed.additional_properties = d
        return hda_detailed

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
