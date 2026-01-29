from dataclasses import dataclass

from .library_contents_create_dataset_response_created_from_basename import (
    LibraryContentsCreateDatasetResponseCreatedFromBasename,
)
from .library_contents_create_dataset_response_misc_blurb import LibraryContentsCreateDatasetResponseMiscBlurb
from .library_contents_create_dataset_response_misc_info import LibraryContentsCreateDatasetResponseMiscInfo

__all__ = ["LibraryContentsCreateDatasetResponse"]


@dataclass
class LibraryContentsCreateDatasetResponse:
    """
    LibraryContentsCreateDatasetResponse dataclass

    Args:
        created_from_basename (LibraryContentsCreateDatasetResponseCreatedFromBasename)
                                 :
        data_type (str)          :
        deleted (bool)           :
        file_ext (str)           :
        file_name (str)          :
        file_size (int)          :
        genome_build (str)       :
        hda_ldda (str)           :
        id_ (str)                : Maps from 'id'
        library_dataset_id (str) :
        misc_blurb (LibraryContentsCreateDatasetResponseMiscBlurb)
                                 :
        misc_info (LibraryContentsCreateDatasetResponseMiscInfo)
                                 :
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_library_id (str)  :
        state (str)              :
        update_time (str)        :
        uuid_ (str)              : Maps from 'uuid'
        visible (bool)           :
    """

    created_from_basename: LibraryContentsCreateDatasetResponseCreatedFromBasename
    data_type: str
    deleted: bool
    file_ext: str
    file_name: str
    file_size: int
    genome_build: str
    hda_ldda: str
    id_: str  # Maps from 'id'
    library_dataset_id: str
    misc_blurb: LibraryContentsCreateDatasetResponseMiscBlurb
    misc_info: LibraryContentsCreateDatasetResponseMiscInfo
    model_class: str  # The name of the database model class.
    name: str
    parent_library_id: str
    state: str
    update_time: str
    uuid_: str  # Maps from 'uuid'
    visible: bool

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "created_from_basename": "created_from_basename",
            "data_type": "data_type",
            "deleted": "deleted",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "genome_build": "genome_build",
            "hda_ldda": "hda_ldda",
            "id": "id_",
            "library_dataset_id": "library_dataset_id",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "parent_library_id": "parent_library_id",
            "state": "state",
            "update_time": "update_time",
            "uuid": "uuid_",
            "visible": "visible",
        }
        key_transform_with_dump = {
            "created_from_basename": "created_from_basename",
            "data_type": "data_type",
            "deleted": "deleted",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "genome_build": "genome_build",
            "hda_ldda": "hda_ldda",
            "id_": "id",
            "library_dataset_id": "library_dataset_id",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "parent_library_id": "parent_library_id",
            "state": "state",
            "update_time": "update_time",
            "uuid_": "uuid",
            "visible": "visible",
        }
