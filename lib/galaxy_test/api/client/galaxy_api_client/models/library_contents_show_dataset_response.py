from dataclasses import dataclass

from .library_contents_show_dataset_response_created_from_basename import (
    LibraryContentsShowDatasetResponseCreatedFromBasename,
)
from .library_contents_show_dataset_response_genome_build import LibraryContentsShowDatasetResponseGenomeBuild
from .library_contents_show_dataset_response_message import LibraryContentsShowDatasetResponseMessage
from .library_contents_show_dataset_response_misc_blurb import LibraryContentsShowDatasetResponseMiscBlurb
from .library_contents_show_dataset_response_misc_info import LibraryContentsShowDatasetResponseMiscInfo
from .library_contents_show_dataset_response_peek import LibraryContentsShowDatasetResponsePeek
from .library_contents_show_dataset_response_uploaded_by import LibraryContentsShowDatasetResponseUploadedBy

__all__ = ["LibraryContentsShowDatasetResponse"]


@dataclass
class LibraryContentsShowDatasetResponse:
    """
    LibraryContentsShowDatasetResponse dataclass

    Args:
        created_from_basename (LibraryContentsShowDatasetResponseCreatedFromBasename)
                                 :
        data_type (str)          :
        date_uploaded (str)      :
        file_ext (str)           :
        file_name (str)          :
        file_size (int)          :
        folder_id (str)          :
        genome_build (LibraryContentsShowDatasetResponseGenomeBuild)
                                 :
        id_ (str)                : Maps from 'id'
        ldda_id (str)            :
        message (LibraryContentsShowDatasetResponseMessage)
                                 :
        misc_blurb (LibraryContentsShowDatasetResponseMiscBlurb)
                                 :
        misc_info (LibraryContentsShowDatasetResponseMiscInfo)
                                 :
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_library_id (str)  :
        peek (LibraryContentsShowDatasetResponsePeek)
                                 :
        state (str)              :
        tags (List[str])         : The collection of tags associated with an item.
        update_time (str)        :
        uploaded_by (LibraryContentsShowDatasetResponseUploadedBy)
                                 :
        uuid_ (str)              : Maps from 'uuid'
    """

    created_from_basename: LibraryContentsShowDatasetResponseCreatedFromBasename
    data_type: str
    date_uploaded: str
    file_ext: str
    file_name: str
    file_size: int
    folder_id: str
    genome_build: LibraryContentsShowDatasetResponseGenomeBuild
    id_: str  # Maps from 'id'
    ldda_id: str
    message: LibraryContentsShowDatasetResponseMessage
    misc_blurb: LibraryContentsShowDatasetResponseMiscBlurb
    misc_info: LibraryContentsShowDatasetResponseMiscInfo
    model_class: str  # The name of the database model class.
    name: str
    parent_library_id: str
    peek: LibraryContentsShowDatasetResponsePeek
    state: str
    tags: list[str]  # The collection of tags associated with an item.
    update_time: str
    uploaded_by: LibraryContentsShowDatasetResponseUploadedBy
    uuid_: str  # Maps from 'uuid'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "created_from_basename": "created_from_basename",
            "data_type": "data_type",
            "date_uploaded": "date_uploaded",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "folder_id": "folder_id",
            "genome_build": "genome_build",
            "id": "id_",
            "ldda_id": "ldda_id",
            "message": "message",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "parent_library_id": "parent_library_id",
            "peek": "peek",
            "state": "state",
            "tags": "tags",
            "update_time": "update_time",
            "uploaded_by": "uploaded_by",
            "uuid": "uuid_",
        }
        key_transform_with_dump = {
            "created_from_basename": "created_from_basename",
            "data_type": "data_type",
            "date_uploaded": "date_uploaded",
            "file_ext": "file_ext",
            "file_name": "file_name",
            "file_size": "file_size",
            "folder_id": "folder_id",
            "genome_build": "genome_build",
            "id_": "id",
            "ldda_id": "ldda_id",
            "message": "message",
            "misc_blurb": "misc_blurb",
            "misc_info": "misc_info",
            "model_class": "model_class",
            "name": "name",
            "parent_library_id": "parent_library_id",
            "peek": "peek",
            "state": "state",
            "tags": "tags",
            "update_time": "update_time",
            "uploaded_by": "uploaded_by",
            "uuid_": "uuid",
        }
