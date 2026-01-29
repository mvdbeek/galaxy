from dataclasses import dataclass

from .accessible import Accessible
from .annotation import Annotation
from .copied_from_history_dataset_association_id import CopiedFromHistoryDatasetAssociationId
from .copied_from_ldda_id import CopiedFromLddaId
from .copied_from_library_dataset_dataset_association_id import CopiedFromLibraryDatasetDatasetAssociationId
from .create_time import CreateTime
from .created_from_basename import CreatedFromBasename
from .creating_job import CreatingJob
from .data_type import DataType
from .dataset_source_type import DatasetSourceType
from .deleted import Deleted
from .display_apps import DisplayApps
from .display_types import DisplayTypes
from .download_url import DownloadUrl
from .drs_id import DrsId
from .extension import Extension
from .file_ext import FileExt
from .file_name import FileName
from .file_size import FileSize
from .genome_build import GenomeBuild
from .hashes import Hashes
from .hid import Hid
from .history_content_type import HistoryContentType
from .meta_files import MetaFiles
from .metadata import Metadata
from .misc_blurb import MiscBlurb
from .misc_info import MiscInfo
from .model_class import ModelClass
from .name import Name
from .object_store_id import ObjectStoreId
from .peek import Peek
from .permissions import Permissions
from .purged import Purged
from .rerunnable import Rerunnable
from .resubmitted import Resubmitted
from .sources import Sources
from .state import State
from .tags import Tags
from .type_id import TypeId
from .update_time import UpdateTime
from .url import Url
from .uuid_ import Uuid_
from .validated_state import ValidatedState
from .validated_state_message import ValidatedStateMessage
from .visible import Visible
from .visualizations import Visualizations

__all__ = ["HdaCustom"]


@dataclass
class HdaCustom:
    """
    Can contain any serializable property of an HDA.  Allows arbitrary custom keys to be
    specified in the serialization parameters without a particular view (predefined set of
    keys).

    Args:
        accessible (Optional[Accessible])
                                 : Whether this item is accessible to the current user due
                                   to permissions.
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        api_type (Optional[str]) : TODO
        copied_from_history_dataset_association_id (Optional[CopiedFromHistoryDatasetAssociationId])
                                 : ID of HDA this HDA was copied from.
        copied_from_ldda_id (Optional[CopiedFromLddaId])
                                 :
        copied_from_library_dataset_dataset_association_id (Optional[CopiedFromLibraryDatasetDatasetAssociationId])
                                 : ID of LDDA this HDA was copied from.
        create_time (Optional[CreateTime])
                                 : The time and date this item was created.
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        creating_job (Optional[CreatingJob])
                                 : The encoded ID of the job that created this dataset.
        data_type (Optional[DataType])
                                 : The fully qualified name of the class implementing the
                                   data type of this dataset.
        dataset_id (Optional[str]): The encoded ID of the dataset associated with this item.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        display_apps (Optional[DisplayApps])
                                 : Contains new-style display app urls.
        display_types (Optional[DisplayTypes])
                                 : Contains old-style display app urls.
        download_url (Optional[DownloadUrl])
                                 : The URL to download this item from the server.
        drs_id (Optional[DrsId]) : The DRS ID of the dataset.
        extension (Optional[Extension])
                                 : The extension of the dataset.
        file_ext (Optional[FileExt])
                                 : The extension of the file.
        file_name (Optional[FileName])
                                 : The full path to the dataset file.
        file_size (Optional[FileSize])
                                 : The file size in bytes.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        hashes (Optional[Hashes]): List of precomputed hashes for the file, if available.
        hda_ldda (Optional[DatasetSourceType])
                                 :
        hid (Optional[Hid])      : The index position of this item in the History.
        history_content_type (Optional[HistoryContentType])
                                 : This is always `dataset_collection` for dataset
                                   collections.
        history_id (Optional[str]):
        id_ (Optional[str])      :
        meta_files (Optional[MetaFiles])
                                 : Collection of metadata files associated with this
                                   dataset.
        metadata (Optional[Metadata])
                                 : The metadata associated with this dataset.
        misc_blurb (Optional[MiscBlurb])
                                 : TODO
        misc_info (Optional[MiscInfo])
                                 : TODO
        model_class (Optional[ModelClass])
                                 : The name of the database model class.
        name (Optional[Name])    : The name of the creator.
        object_store_id (Optional[ObjectStoreId])
                                 : The ID of the object store that this dataset is stored
                                   in.
        peek (Optional[Peek])    : A few lines of contents from the start of the file.
        permissions (Optional[Permissions])
                                 : Role-based access and manage control permissions for the
                                   dataset.
        purged (Optional[Purged]): Whether this dataset has been removed from disk.
        rerunnable (Optional[Rerunnable])
                                 : Whether the job creating this dataset can be run again.
        resubmitted (Optional[Resubmitted])
                                 : Whether the job creating this dataset has been
                                   resubmitted.
        sources (Optional[Sources])
                                 : The list of sources associated with this dataset.
        state (Optional[State])  : Current state of the job.
        tags (Optional[Tags])    : The collection of tags associated with an item.
        type_ (Optional[str])    : This is always `file` for datasets.
        type_id (Optional[TypeId]): The type and the encoded ID of this item. Used for
                                    caching.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        url (Optional[Url])      : The relative URL to access this item.
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
        validated_state (Optional[ValidatedState])
                                 : The state of the datatype validation for this dataset.
        validated_state_message (Optional[ValidatedStateMessage])
                                 : The message with details about the datatype validation
                                   result for this dataset.
        visible (Optional[Visible])
                                 : Whether this item is visible in the history.
        visualizations (Optional[Visualizations])
                                 : The collection of visualizations that can be applied to
                                   this dataset.
    """

    accessible: Accessible | None = None  # Whether this item is accessible to the current user due to permissions.
    annotation: Annotation | None = None  # The annotation of this Visualization.
    api_type: str | None = "file"  # TODO
    copied_from_history_dataset_association_id: CopiedFromHistoryDatasetAssociationId | None = (
        None  # ID of HDA this HDA was copied from.
    )
    copied_from_ldda_id: CopiedFromLddaId | None = None
    copied_from_library_dataset_dataset_association_id: CopiedFromLibraryDatasetDatasetAssociationId | None = (
        None  # ID of LDDA this HDA was copied from.
    )
    create_time: CreateTime | None = None  # The time and date this item was created.
    created_from_basename: CreatedFromBasename | None = None  # The basename of the output that produced this dataset.
    creating_job: CreatingJob | None = None  # The encoded ID of the job that created this dataset.
    data_type: DataType | None = (
        None  # The fully qualified name of the class implementing the data type of this dataset.
    )
    dataset_id: str | None = None  # The encoded ID of the dataset associated with this item.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    display_apps: DisplayApps | None = None  # Contains new-style display app urls.
    display_types: DisplayTypes | None = None  # Contains old-style display app urls.
    download_url: DownloadUrl | None = None  # The URL to download this item from the server.
    drs_id: DrsId | None = None  # The DRS ID of the dataset.
    extension: Extension | None = None  # The extension of the dataset.
    file_ext: FileExt | None = None  # The extension of the file.
    file_name: FileName | None = None  # The full path to the dataset file.
    file_size: FileSize | None = None  # The file size in bytes.
    genome_build: GenomeBuild | None = "?"  # TODO
    hashes: Hashes | None = None  # List of precomputed hashes for the file, if available.
    hda_ldda: DatasetSourceType | None = None
    hid: Hid | None = None  # The index position of this item in the History.
    history_content_type: HistoryContentType | None = (
        None  # This is always `dataset_collection` for dataset collections.
    )
    history_id: str | None = None
    id_: str | None = None
    meta_files: MetaFiles | None = None  # Collection of metadata files associated with this dataset.
    metadata: Metadata | None = None  # The metadata associated with this dataset.
    misc_blurb: MiscBlurb | None = None  # TODO
    misc_info: MiscInfo | None = None  # TODO
    model_class: ModelClass | None = None  # The name of the database model class.
    name: Name | None = None  # The name of the creator.
    object_store_id: ObjectStoreId | None = None  # The ID of the object store that this dataset is stored in.
    peek: Peek | None = None  # A few lines of contents from the start of the file.
    permissions: Permissions | None = None  # Role-based access and manage control permissions for the dataset.
    purged: Purged | None = None  # Whether this dataset has been removed from disk.
    rerunnable: Rerunnable | None = None  # Whether the job creating this dataset can be run again.
    resubmitted: Resubmitted | None = None  # Whether the job creating this dataset has been resubmitted.
    sources: Sources | None = None  # The list of sources associated with this dataset.
    state: State | None = None  # Current state of the job.
    tags: Tags | None = None  # The collection of tags associated with an item.
    type_: str | None = "file"  # This is always `file` for datasets.
    type_id: TypeId | None = None  # The type and the encoded ID of this item. Used for caching.
    update_time: UpdateTime | None = None  # The last time and date this item was updated.
    url: Url | None = None  # The relative URL to access this item.
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
    validated_state: ValidatedState | None = None  # The state of the datatype validation for this dataset.
    validated_state_message: ValidatedStateMessage | None = (
        None  # The message with details about the datatype validation result for this dataset.
    )
    visible: Visible | None = None  # Whether this item is visible in the history.
    visualizations: Visualizations | None = (
        None  # The collection of visualizations that can be applied to this dataset.
    )
