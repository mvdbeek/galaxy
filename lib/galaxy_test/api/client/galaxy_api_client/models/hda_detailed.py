from dataclasses import dataclass
from datetime import datetime

from .annotation import Annotation
from .copied_from_history_dataset_association_id import CopiedFromHistoryDatasetAssociationId
from .copied_from_ldda_id import CopiedFromLddaId
from .copied_from_library_dataset_dataset_association_id import CopiedFromLibraryDatasetDatasetAssociationId
from .created_from_basename import CreatedFromBasename
from .dataset_hash import DatasetHash
from .dataset_permissions import DatasetPermissions
from .dataset_source import DatasetSource
from .dataset_source_type import DatasetSourceType
from .dataset_state import DatasetState
from .dataset_validated_state import DatasetValidatedState
from .display_app import DisplayApp
from .extension import Extension
from .file_name import FileName
from .genome_build import GenomeBuild
from .metadata import Metadata
from .metadata_file import MetadataFile
from .misc_blurb import MiscBlurb
from .misc_info import MiscInfo
from .name import Name
from .object_store_id import ObjectStoreId
from .peek import Peek
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime
from .validated_state_message import ValidatedStateMessage

__all__ = ["HdaDetailed"]


@dataclass
class HdaDetailed:
    """
    History Dataset Association detailed information.

    Args:
        accessible (bool)        : Whether this item is accessible to the current user due
                                   to permissions.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
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
        extension (Optional[Extension])
                                 : The extension of the dataset.
        file_ext (str)           : The extension of the file.
        file_size (int)          : The file size in bytes.
        hashes (List[DatasetHash]): The list of hashes associated with this dataset.
        hid (int)                : The index position of this item in the History.
        history_content_type (str): This is always `dataset` for datasets.
        history_id (str)         :
        id_ (str)                :
        meta_files (List[MetadataFile])
                                 : Collection of metadata files associated with this
                                   dataset.
        model_class (str)        : The name of the database model class.
        name (Optional[Name])    : The name of the creator.
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
        tags (Tags)              : The collection of tags associated with an item.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        uuid_ (str)              : Universal unique identifier for this dataset.
        validated_state (DatasetValidatedState)
                                 :
        visible (bool)           : Whether this item is visible or hidden to the user by
                                   default.
        api_type (Optional[str]) : TODO
        copied_from_history_dataset_association_id (Optional[CopiedFromHistoryDatasetAssociationId])
                                 : ID of HDA this HDA was copied from.
        copied_from_ldda_id (Optional[CopiedFromLddaId])
                                 :
        copied_from_library_dataset_dataset_association_id (Optional[CopiedFromLibraryDatasetDatasetAssociationId])
                                 : ID of LDDA this HDA was copied from.
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        file_name (Optional[FileName])
                                 : The full path to the dataset file.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        hda_ldda (Optional[DatasetSourceType])
                                 :
        metadata (Optional[Metadata])
                                 : The metadata associated with this dataset.
        misc_blurb (Optional[MiscBlurb])
                                 : TODO
        misc_info (Optional[MiscInfo])
                                 : TODO
        object_store_id (Optional[ObjectStoreId])
                                 : The ID of the object store that this dataset is stored
                                   in.
        peek (Optional[Peek])    : A few lines of contents from the start of the file.
        type_ (Optional[str])    : This is always `file` for datasets.
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
        validated_state_message (Optional[ValidatedStateMessage])
                                 : The message with details about the datatype validation
                                   result for this dataset.
    """

    accessible: bool  # Whether this item is accessible to the current user due to permissions.
    annotation: Annotation | None  # The annotation of this Visualization.
    create_time: datetime  # The time and date this item was created.
    creating_job: str  # The encoded ID of the job that created this dataset.
    data_type: str  # The fully qualified name of the class implementing the data type of this dataset.
    dataset_id: str  # The encoded ID of the dataset associated with this item.
    deleted: bool  # Whether this item is marked as deleted.
    display_apps: list[DisplayApp]  # Contains new-style display app urls.
    display_types: list[DisplayApp]  # Contains old-style display app urls.
    download_url: str  # The URL to download this item from the server.
    drs_id: str  # The DRS ID of the dataset.
    extension: Extension | None  # The extension of the dataset.
    file_ext: str  # The extension of the file.
    file_size: int  # The file size in bytes.
    hashes: list[DatasetHash]  # The list of hashes associated with this dataset.
    hid: int  # The index position of this item in the History.
    history_content_type: str  # This is always `dataset` for datasets.
    history_id: str
    id_: str
    meta_files: list[MetadataFile]  # Collection of metadata files associated with this dataset.
    model_class: str  # The name of the database model class.
    name: Name | None  # The name of the creator.
    permissions: DatasetPermissions  # Role-based permissions for accessing and managing a dataset.
    purged: bool  # Whether this dataset has been removed from disk.
    rerunnable: bool  # Whether the job creating this dataset can be run again.
    resubmitted: bool  # Whether the job creating this dataset has been resubmitted.
    sources: list[DatasetSource]  # The list of sources associated with this dataset.
    state: DatasetState
    tags: Tags  # The collection of tags associated with an item.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    uuid_: str  # Universal unique identifier for this dataset.
    validated_state: DatasetValidatedState
    visible: bool  # Whether this item is visible or hidden to the user by default.
    api_type: str | None = "file"  # TODO
    copied_from_history_dataset_association_id: CopiedFromHistoryDatasetAssociationId | None = (
        None  # ID of HDA this HDA was copied from.
    )
    copied_from_ldda_id: CopiedFromLddaId | None = None
    copied_from_library_dataset_dataset_association_id: CopiedFromLibraryDatasetDatasetAssociationId | None = (
        None  # ID of LDDA this HDA was copied from.
    )
    created_from_basename: CreatedFromBasename | None = None  # The basename of the output that produced this dataset.
    file_name: FileName | None = None  # The full path to the dataset file.
    genome_build: GenomeBuild | None = "?"  # TODO
    hda_ldda: DatasetSourceType | None = None
    metadata: Metadata | None = None  # The metadata associated with this dataset.
    misc_blurb: MiscBlurb | None = None  # TODO
    misc_info: MiscInfo | None = None  # TODO
    object_store_id: ObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
    peek: Peek | None = None  # A few lines of contents from the start of the file.
    type_: str | None = "file"  # This is always `file` for datasets.
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    validated_state_message: ValidatedStateMessage | None = (
        None  # The message with details about the datatype validation result for this dataset.
    )
