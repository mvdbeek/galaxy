from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType
from .hda_custom_accessible import HdaCustomAccessible
from .hda_custom_annotation import HdaCustomAnnotation
from .hda_custom_copied_from_history_dataset_association_id import HdaCustomCopiedFromHistoryDatasetAssociationId
from .hda_custom_copied_from_ldda_id import HdaCustomCopiedFromLddaId
from .hda_custom_copied_from_library_dataset_dataset_association_id import (
    HdaCustomCopiedFromLibraryDatasetDatasetAssociationId,
)
from .hda_custom_create_time import HdaCustomCreateTime
from .hda_custom_created_from_basename import HdaCustomCreatedFromBasename
from .hda_custom_creating_job import HdaCustomCreatingJob
from .hda_custom_data_type import HdaCustomDataType
from .hda_custom_deleted import HdaCustomDeleted
from .hda_custom_display_apps import HdaCustomDisplayApps
from .hda_custom_display_types import HdaCustomDisplayTypes
from .hda_custom_download_url import HdaCustomDownloadUrl
from .hda_custom_drs_id import HdaCustomDrsId
from .hda_custom_extension import HdaCustomExtension
from .hda_custom_file_ext import HdaCustomFileExt
from .hda_custom_file_name import HdaCustomFileName
from .hda_custom_file_size import HdaCustomFileSize
from .hda_custom_genome_build import HdaCustomGenomeBuild
from .hda_custom_hashes import HdaCustomHashes
from .hda_custom_hid import HdaCustomHid
from .hda_custom_history_content_type import HdaCustomHistoryContentType
from .hda_custom_meta_files import HdaCustomMetaFiles
from .hda_custom_metadata import HdaCustomMetadata
from .hda_custom_misc_blurb import HdaCustomMiscBlurb
from .hda_custom_misc_info import HdaCustomMiscInfo
from .hda_custom_name import HdaCustomName
from .hda_custom_object_store_id import HdaCustomObjectStoreId
from .hda_custom_peek import HdaCustomPeek
from .hda_custom_permissions import HdaCustomPermissions
from .hda_custom_purged import HdaCustomPurged
from .hda_custom_rerunnable import HdaCustomRerunnable
from .hda_custom_resubmitted import HdaCustomResubmitted
from .hda_custom_sources import HdaCustomSources
from .hda_custom_state import HdaCustomState
from .hda_custom_tags import HdaCustomTags
from .hda_custom_type_id import HdaCustomTypeId
from .hda_custom_update_time import HdaCustomUpdateTime
from .hda_custom_url import HdaCustomUrl
from .hda_custom_validated_state import HdaCustomValidatedState
from .hda_custom_validated_state_message import HdaCustomValidatedStateMessage
from .hda_custom_visible import HdaCustomVisible
from .hda_custom_visualizations import HdaCustomVisualizations
from .uuid__5 import Uuid5

__all__ = ["HdaCustom2"]


@dataclass
class HdaCustom2:
    """
    Can contain any serializable property of an HDA.  Allows arbitrary custom keys to be
    specified in the serialization parameters without a particular view (predefined set of
    keys).

    Args:
        accessible (HdaCustomAccessible | None)
                                 : Whether this item is accessible to the current user due
                                   to permissions.
        annotation (HdaCustomAnnotation | None)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        api_type (str | None)    : TODO
        copied_from_history_dataset_association_id (HdaCustomCopiedFromHistoryDatasetAssociationId | None)
                                 : ID of HDA this HDA was copied from.
        copied_from_ldda_id (HdaCustomCopiedFromLddaId | None)
                                 :
        copied_from_library_dataset_dataset_association_id (HdaCustomCopiedFromLibraryDatasetDatasetAssociationId | None)
                                 : ID of LDDA this HDA was copied from.
        create_time (HdaCustomCreateTime | None)
                                 : The time and date this item was created.
        created_from_basename (HdaCustomCreatedFromBasename | None)
                                 : The basename of the output that produced this dataset.
        creating_job (HdaCustomCreatingJob | None)
                                 : The encoded ID of the job that created this dataset.
        data_type (HdaCustomDataType | None)
                                 : The fully qualified name of the class implementing the
                                   data type of this dataset.
        dataset_id (str | None)  : The encoded ID of the dataset associated with this item.
        deleted (HdaCustomDeleted | None)
                                 : Whether this item is marked as deleted.
        display_apps (HdaCustomDisplayApps | None)
                                 : Contains new-style display app urls.
        display_types (HdaCustomDisplayTypes | None)
                                 : Contains old-style display app urls.
        download_url (HdaCustomDownloadUrl | None)
                                 : The URL to download this item from the server.
        drs_id (HdaCustomDrsId | None)
                                 : The DRS ID of the dataset.
        extension (HdaCustomExtension | None)
                                 : The extension of the dataset.
        file_ext (HdaCustomFileExt | None)
                                 : The extension of the file.
        file_name (HdaCustomFileName | None)
                                 : The full path to the dataset file.
        file_size (HdaCustomFileSize | None)
                                 : The file size in bytes.
        genome_build (HdaCustomGenomeBuild | None)
                                 : TODO
        hashes (HdaCustomHashes | None)
                                 : The list of hashes associated with this dataset.
        hda_ldda (DatasetSourceType | None)
                                 :
        hid (HdaCustomHid | None): The index position of this item in the History.
        history_content_type (HdaCustomHistoryContentType | None)
                                 : This is always `dataset` for datasets.
        history_id (str | None)  :
        id_ (str | None)         : Maps from 'id'
        meta_files (HdaCustomMetaFiles | None)
                                 : Collection of metadata files associated with this
                                   dataset.
        metadata (HdaCustomMetadata | None)
                                 : The metadata associated with this dataset.
        misc_blurb (HdaCustomMiscBlurb | None)
                                 : TODO
        misc_info (HdaCustomMiscInfo | None)
                                 : TODO
        model_class (str | None) : The name of the database model class.
        name (HdaCustomName | None)
                                 : The name of the item.
        object_store_id (HdaCustomObjectStoreId | None)
                                 : The ID of the object store that this dataset is stored
                                   in.
        peek (HdaCustomPeek | None)
                                 : A few lines of contents from the start of the file.
        permissions (HdaCustomPermissions | None)
                                 : Role-based access and manage control permissions for the
                                   dataset.
        purged (HdaCustomPurged | None)
                                 : Whether this dataset has been removed from disk.
        rerunnable (HdaCustomRerunnable | None)
                                 : Whether the job creating this dataset can be run again.
        resubmitted (HdaCustomResubmitted | None)
                                 : Whether the job creating this dataset has been
                                   resubmitted.
        sources (HdaCustomSources | None)
                                 : The list of sources associated with this dataset.
        state (HdaCustomState | None)
                                 : The current state of this dataset.
        tags (HdaCustomTags | None)
                                 : The collection of tags associated with an item.
        type_ (str | None)       : This is always `file` for datasets. (maps from 'type')
        type_id (HdaCustomTypeId | None)
                                 : The type and the encoded ID of this item. Used for
                                   caching.
        update_time (HdaCustomUpdateTime | None)
                                 : The last time and date this item was updated.
        url (HdaCustomUrl | None): The relative URL to access this item.
        uuid_ (Uuid5 | None)     : Maps from 'uuid'
        validated_state (HdaCustomValidatedState | None)
                                 : The state of the datatype validation for this dataset.
        validated_state_message (HdaCustomValidatedStateMessage | None)
                                 : The message with details about the datatype validation
                                   result for this dataset.
        visible (HdaCustomVisible | None)
                                 : Whether this item is visible or hidden to the user by
                                   default.
        visualizations (HdaCustomVisualizations | None)
                                 : The collection of visualizations that can be applied to
                                   this dataset.
    """

    accessible: HdaCustomAccessible | None = (
        None  # Whether this item is accessible to the current user due to permissions.
    )
    annotation: HdaCustomAnnotation | None = (
        None  # An annotation to provide details or to help understand the purpose and usage of this item.
    )
    api_type: str | None = "file"  # TODO
    copied_from_history_dataset_association_id: HdaCustomCopiedFromHistoryDatasetAssociationId | None = (
        None  # ID of HDA this HDA was copied from.
    )
    copied_from_ldda_id: HdaCustomCopiedFromLddaId | None = None
    copied_from_library_dataset_dataset_association_id: HdaCustomCopiedFromLibraryDatasetDatasetAssociationId | None = (
        None  # ID of LDDA this HDA was copied from.
    )
    create_time: HdaCustomCreateTime | None = None  # The time and date this item was created.
    created_from_basename: HdaCustomCreatedFromBasename | None = (
        None  # The basename of the output that produced this dataset.
    )
    creating_job: HdaCustomCreatingJob | None = None  # The encoded ID of the job that created this dataset.
    data_type: HdaCustomDataType | None = (
        None  # The fully qualified name of the class implementing the data type of this dataset.
    )
    dataset_id: str | None = None  # The encoded ID of the dataset associated with this item.
    deleted: HdaCustomDeleted | None = None  # Whether this item is marked as deleted.
    display_apps: HdaCustomDisplayApps | None = None  # Contains new-style display app urls.
    display_types: HdaCustomDisplayTypes | None = None  # Contains old-style display app urls.
    download_url: HdaCustomDownloadUrl | None = None  # The URL to download this item from the server.
    drs_id: HdaCustomDrsId | None = None  # The DRS ID of the dataset.
    extension: HdaCustomExtension | None = None  # The extension of the dataset.
    file_ext: HdaCustomFileExt | None = None  # The extension of the file.
    file_name: HdaCustomFileName | None = None  # The full path to the dataset file.
    file_size: HdaCustomFileSize | None = None  # The file size in bytes.
    genome_build: HdaCustomGenomeBuild | None = "?"  # TODO
    hashes: HdaCustomHashes | None = None  # The list of hashes associated with this dataset.
    hda_ldda: DatasetSourceType | None = None
    hid: HdaCustomHid | None = None  # The index position of this item in the History.
    history_content_type: HdaCustomHistoryContentType | None = None  # This is always `dataset` for datasets.
    history_id: str | None = None
    id_: str | None = None  # Maps from 'id'
    meta_files: HdaCustomMetaFiles | None = None  # Collection of metadata files associated with this dataset.
    metadata: HdaCustomMetadata | None = None  # The metadata associated with this dataset.
    misc_blurb: HdaCustomMiscBlurb | None = None  # TODO
    misc_info: HdaCustomMiscInfo | None = None  # TODO
    model_class: str | None = None  # The name of the database model class.
    name: HdaCustomName | None = None  # The name of the item.
    object_store_id: HdaCustomObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
    peek: HdaCustomPeek | None = None  # A few lines of contents from the start of the file.
    permissions: HdaCustomPermissions | None = None  # Role-based access and manage control permissions for the dataset.
    purged: HdaCustomPurged | None = None  # Whether this dataset has been removed from disk.
    rerunnable: HdaCustomRerunnable | None = None  # Whether the job creating this dataset can be run again.
    resubmitted: HdaCustomResubmitted | None = None  # Whether the job creating this dataset has been resubmitted.
    sources: HdaCustomSources | None = None  # The list of sources associated with this dataset.
    state: HdaCustomState | None = None  # The current state of this dataset.
    tags: HdaCustomTags | None = None  # The collection of tags associated with an item.
    type_: str | None = "file"  # This is always `file` for datasets. (maps from 'type')
    type_id: HdaCustomTypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    update_time: HdaCustomUpdateTime | None = None  # The last time and date this item was updated.
    url: HdaCustomUrl | None = None  # The relative URL to access this item.
    uuid_: Uuid5 | None = None  # Maps from 'uuid'
    validated_state: HdaCustomValidatedState | None = None  # The state of the datatype validation for this dataset.
    validated_state_message: HdaCustomValidatedStateMessage | None = (
        None  # The message with details about the datatype validation result for this dataset.
    )
    visible: HdaCustomVisible | None = None  # Whether this item is visible or hidden to the user by default.
    visualizations: HdaCustomVisualizations | None = (
        None  # The collection of visualizations that can be applied to this dataset.
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
            "visualizations": "visualizations",
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
            "visualizations": "visualizations",
        }
