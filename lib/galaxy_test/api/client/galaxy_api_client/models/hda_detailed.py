from dataclasses import dataclass
from datetime import datetime

from .dataset_hash import DatasetHash
from .dataset_permissions import DatasetPermissions
from .dataset_source import DatasetSource
from .dataset_source_type import DatasetSourceType
from .dataset_state import DatasetState
from .dataset_validated_state import DatasetValidatedState
from .display_app import DisplayApp
from .hda_detailed_annotation import HdaDetailedAnnotation
from .hda_detailed_copied_from_history_dataset_association_id import HdaDetailedCopiedFromHistoryDatasetAssociationId
from .hda_detailed_copied_from_ldda_id import HdaDetailedCopiedFromLddaId
from .hda_detailed_copied_from_library_dataset_dataset_association_id import (
    HdaDetailedCopiedFromLibraryDatasetDatasetAssociationId,
)
from .hda_detailed_created_from_basename import HdaDetailedCreatedFromBasename
from .hda_detailed_extension import HdaDetailedExtension
from .hda_detailed_file_name import HdaDetailedFileName
from .hda_detailed_genome_build import HdaDetailedGenomeBuild
from .hda_detailed_metadata import HdaDetailedMetadata
from .hda_detailed_misc_blurb import HdaDetailedMiscBlurb
from .hda_detailed_misc_info import HdaDetailedMiscInfo
from .hda_detailed_name import HdaDetailedName
from .hda_detailed_object_store_id import HdaDetailedObjectStoreId
from .hda_detailed_peek import HdaDetailedPeek
from .hda_detailed_type_id import HdaDetailedTypeId
from .hda_detailed_update_time import HdaDetailedUpdateTime
from .hda_detailed_validated_state_message import HdaDetailedValidatedStateMessage
from .metadata_file import MetadataFile

__all__ = ["HdaDetailed"]


@dataclass
class HdaDetailed:
    """
    History Dataset Association detailed information.

    Args:
        accessible (bool)        : Whether this item is accessible to the current user due
                                   to permissions.
        annotation (HdaDetailedAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        create_time (datetime)   : The time and date this item was created.
        creating_job (str)       : The encoded ID of the job that created this dataset.
        data_type (str)          : The fully qualified name of the class implementing the
                                   data type of this dataset.
        dataset_id (str)         : The encoded ID of the dataset associated with this item.
        deleted (bool)           : Whether this item is marked as deleted.
        display_apps (List[DisplayApp])
                                 : Contains new-style display app urls.
        display_types (List[DisplayApp])
                                 : Contains old-style display app urls.
        download_url (str)       : The URL to download this item from the server.
        drs_id (str)             : The DRS ID of the dataset.
        extension (HdaDetailedExtension)
                                 : The extension of the dataset.
        file_ext (str)           : The extension of the file.
        file_size (int)          : The file size in bytes.
        hashes (List[DatasetHash]): The list of hashes associated with this dataset.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                : Maps from 'id'
        meta_files (List[MetadataFile])
                                 : Collection of metadata files associated with this
                                   dataset.
        model_class (str)        : The name of the database model class.
        name (HdaDetailedName)   : The name of the item.
        permissions (DatasetPermissions)
                                 : Role-based permissions for accessing and managing a
                                   dataset.
        purged (bool)            : Whether this dataset has been removed from disk.
        rerunnable (bool)        : Whether the job creating this dataset can be run again.
        resubmitted (bool)       : Whether the job creating this dataset has been
                                   resubmitted.
        sources (List[DatasetSource])
                                 : The list of sources associated with this dataset.
        state (DatasetState)     :
        tags (List[str])         : The collection of tags associated with an item.
        update_time (HdaDetailedUpdateTime)
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        uuid_ (str)              : Universal unique identifier for this dataset. (maps from
                                   'uuid')
        validated_state (DatasetValidatedState)
                                 :
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        api_type (str | None)    : TODO
        copied_from_history_dataset_association_id (HdaDetailedCopiedFromHistoryDatasetAssociationId | None)
                                 : ID of HDA this HDA was copied from.
        copied_from_ldda_id (HdaDetailedCopiedFromLddaId | None)
                                 :
        copied_from_library_dataset_dataset_association_id (HdaDetailedCopiedFromLibraryDatasetDatasetAssociationId | None)
                                 : ID of LDDA this HDA was copied from.
        created_from_basename (HdaDetailedCreatedFromBasename | None)
                                 : The basename of the output that produced this dataset.
        file_name (HdaDetailedFileName | None)
                                 : The full path to the dataset file.
        genome_build (HdaDetailedGenomeBuild | None)
                                 : TODO
        hda_ldda (DatasetSourceType | None)
                                 :
        metadata (HdaDetailedMetadata | None)
                                 : The metadata associated with this dataset.
        misc_blurb (HdaDetailedMiscBlurb | None)
                                 : TODO
        misc_info (HdaDetailedMiscInfo | None)
                                 : TODO
        object_store_id (HdaDetailedObjectStoreId | None)
                                 : The ID of the object store that this dataset is stored
                                   in.
        peek (HdaDetailedPeek | None)
                                 : A few lines of contents from the start of the file.
        type_ (str | None)       : This is always `file` for datasets. (maps from 'type')
        type_id (HdaDetailedTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
        validated_state_message (HdaDetailedValidatedStateMessage | None)
                                 : The message with details about the datatype validation
                                   result for this dataset.
    """

    accessible: bool  # Whether this item is accessible to the current user due to permissions.
    annotation: HdaDetailedAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    create_time: datetime  # The time and date this item was created.
    creating_job: str  # The encoded ID of the job that created this dataset.
    data_type: str  # The fully qualified name of the class implementing the data type of this dataset.
    dataset_id: str  # The encoded ID of the dataset associated with this item.
    deleted: bool  # Whether this item is marked as deleted.
    display_apps: list[DisplayApp]  # Contains new-style display app urls.
    display_types: list[DisplayApp]  # Contains old-style display app urls.
    download_url: str  # The URL to download this item from the server.
    drs_id: str  # The DRS ID of the dataset.
    extension: HdaDetailedExtension  # The extension of the dataset.
    file_ext: str  # The extension of the file.
    file_size: int  # The file size in bytes.
    hashes: list[DatasetHash]  # The list of hashes associated with this dataset.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str  # Maps from 'id'
    meta_files: list[MetadataFile]  # Collection of metadata files associated with this dataset.
    model_class: str  # The name of the database model class.
    name: HdaDetailedName  # The name of the item.
    permissions: DatasetPermissions  # Role-based permissions for accessing and managing a dataset.
    purged: bool  # Whether this dataset has been removed from disk.
    rerunnable: bool  # Whether the job creating this dataset can be run again.
    resubmitted: bool  # Whether the job creating this dataset has been resubmitted.
    sources: list[DatasetSource]  # The list of sources associated with this dataset.
    state: DatasetState
    tags: list[str]  # The collection of tags associated with an item.
    update_time: HdaDetailedUpdateTime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    uuid_: str  # Universal unique identifier for this dataset. (maps from 'uuid')
    validated_state: DatasetValidatedState
    visible: bool  # Whether this item is visible or hidden to the user by default.
    api_type: str | None = "file"  # TODO
    copied_from_history_dataset_association_id: HdaDetailedCopiedFromHistoryDatasetAssociationId | None = (
        None  # ID of HDA this HDA was copied from.
    )
    copied_from_ldda_id: HdaDetailedCopiedFromLddaId | None = None
    copied_from_library_dataset_dataset_association_id: (
        HdaDetailedCopiedFromLibraryDatasetDatasetAssociationId | None
    ) = None  # ID of LDDA this HDA was copied from.
    created_from_basename: HdaDetailedCreatedFromBasename | None = (
        None  # The basename of the output that produced this dataset.
    )
    file_name: HdaDetailedFileName | None = None  # The full path to the dataset file.
    genome_build: HdaDetailedGenomeBuild | None = "?"  # TODO
    hda_ldda: DatasetSourceType | None = None
    metadata: HdaDetailedMetadata | None = None  # The metadata associated with this dataset.
    misc_blurb: HdaDetailedMiscBlurb | None = None  # TODO
    misc_info: HdaDetailedMiscInfo | None = None  # TODO
    object_store_id: HdaDetailedObjectStoreId | None = (
        None  # The ID of the object store that this dataset is stored in.
    )
    peek: HdaDetailedPeek | None = None  # A few lines of contents from the start of the file.
    type_: str | None = "file"  # This is always `file` for datasets. (maps from 'type')
    type_id: HdaDetailedTypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    validated_state_message: HdaDetailedValidatedStateMessage | None = (
        None  # The message with details about the datatype validation result for this dataset.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "accessible": "accessible",
            "annotation": "annotation",
            "api_type": "api_type",
            "copied_from_history_dataset_association_id": "copied_from_history_dataset_association_id",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "copied_from_library_dataset_dataset_association_id": "copied_from_library_dataset_dataset_association_id",
            "create_time": "create_time",
            "created_from_basename": "created_from_basename",
            "creating_job": "creating_job",
            "data_type": "data_type",
            "dataset_id": "dataset_id",
            "deleted": "deleted",
            "display_apps": "display_apps",
            "display_types": "display_types",
            "download_url": "download_url",
            "drs_id": "drs_id",
            "extension": "extension",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "genome_build": "genome_build",
            "hashes": "hashes",
            "hda_ldda": "hda_ldda",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id": "id_",
            "meta_files": "meta_files",
            "metadata": "metadata",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "object_store_id": "object_store_id",
            "peek": "peek",
            "permissions": "permissions",
            "purged": "purged",
            "rerunnable": "rerunnable",
            "resubmitted": "resubmitted",
            "sources": "sources",
            "state": "state",
            "tags": "tags",
            "type": "type_",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "uuid": "uuid_",
            "validated_state": "validated_state",
            "validated_state_message": "validated_state_message",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "accessible": "accessible",
            "annotation": "annotation",
            "api_type": "api_type",
            "copied_from_history_dataset_association_id": "copied_from_history_dataset_association_id",
            "copied_from_ldda_id": "copied_from_ldda_id",
            "copied_from_library_dataset_dataset_association_id": "copied_from_library_dataset_dataset_association_id",
            "create_time": "create_time",
            "created_from_basename": "created_from_basename",
            "creating_job": "creating_job",
            "data_type": "data_type",
            "dataset_id": "dataset_id",
            "deleted": "deleted",
            "display_apps": "display_apps",
            "display_types": "display_types",
            "download_url": "download_url",
            "drs_id": "drs_id",
            "extension": "extension",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "genome_build": "genome_build",
            "hashes": "hashes",
            "hda_ldda": "hda_ldda",
            "hid": "hid",
            "history_content_type": "history_content_type",
            "history_id": "history_id",
            "id_": "id",
            "meta_files": "meta_files",
            "metadata": "metadata",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "object_store_id": "object_store_id",
            "peek": "peek",
            "permissions": "permissions",
            "purged": "purged",
            "rerunnable": "rerunnable",
            "resubmitted": "resubmitted",
            "sources": "sources",
            "state": "state",
            "tags": "tags",
            "type_": "type",
            "type_id": "type_id",
            "update_time": "update_time",
            "url": "url",
            "uuid_": "uuid",
            "validated_state": "validated_state",
            "validated_state_message": "validated_state_message",
            "visible": "visible",
        }
