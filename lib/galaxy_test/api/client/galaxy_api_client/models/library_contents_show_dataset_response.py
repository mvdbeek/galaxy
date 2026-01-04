from dataclasses import dataclass

from .created_from_basename import CreatedFromBasename
from .genome_build import GenomeBuild
from .message import Message
from .misc_blurb import MiscBlurb
from .misc_info import MiscInfo
from .peek import Peek
from .tags import Tags
from .uploaded_by import UploadedBy

__all__ = ["LibraryContentsShowDatasetResponse"]


@dataclass
class LibraryContentsShowDatasetResponse:
    """
    LibraryContentsShowDatasetResponse dataclass.

    Args:
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        data_type (str)          :
        date_uploaded (str)      :
        file_ext (str)           :
        file_name (str)          :
        file_size (int)          :
        folder_id (str)          :
        genome_build (Optional[GenomeBuild])
                                 : TODO
        id_ (str)                :
        ldda_id (str)            :
        message (Optional[Message])
                                 : The optional message sent with the error report.
        misc_blurb (Optional[MiscBlurb])
                                 : TODO
        misc_info (Optional[MiscInfo])
                                 : TODO
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_library_id (str)  :
        peek (Optional[Peek])    : A few lines of contents from the start of the file.
        state (str)              :
        tags (Tags)              : The collection of tags associated with an item.
        update_time (str)        :
        uploaded_by (Optional[UploadedBy])
                                 :
        uuid_ (str)              :
    """

    created_from_basename: CreatedFromBasename | None  # The basename of the output that produced this dataset.
    data_type: str
    date_uploaded: str
    file_ext: str
    file_name: str
    file_size: int
    folder_id: str
    genome_build: GenomeBuild | None  # TODO
    id_: str
    ldda_id: str
    message: Message | None  # The optional message sent with the error report.
    misc_blurb: MiscBlurb | None  # TODO
    misc_info: MiscInfo | None  # TODO
    model_class: str  # The name of the database model class.
    name: str
    parent_library_id: str
    peek: Peek | None  # A few lines of contents from the start of the file.
    state: str
    tags: Tags  # The collection of tags associated with an item.
    update_time: str
    uploaded_by: UploadedBy | None
    uuid_: str
