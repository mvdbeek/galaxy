from dataclasses import dataclass

from .created_from_basename import CreatedFromBasename
from .misc_blurb import MiscBlurb
from .misc_info import MiscInfo

__all__ = ["LibraryContentsCreateDatasetResponse"]


@dataclass
class LibraryContentsCreateDatasetResponse:
    """
    LibraryContentsCreateDatasetResponse dataclass.

    Args:
        created_from_basename (Optional[CreatedFromBasename])
                                 : The basename of the output that produced this dataset.
        data_type (str)          :
        deleted (bool)           :
        file_ext (str)           :
        file_name (str)          :
        file_size (int)          :
        genome_build (str)       :
        hda_ldda (str)           :
        id_ (str)                :
        library_dataset_id (str) :
        misc_blurb (Optional[MiscBlurb])
                                 : TODO
        misc_info (Optional[MiscInfo])
                                 : TODO
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_library_id (str)  :
        state (str)              :
        update_time (str)        :
        uuid_ (str)              :
        visible (bool)           :
    """

    created_from_basename: CreatedFromBasename | None  # The basename of the output that produced this dataset.
    data_type: str
    deleted: bool
    file_ext: str
    file_name: str
    file_size: int
    genome_build: str
    hda_ldda: str
    id_: str
    library_dataset_id: str
    misc_blurb: MiscBlurb | None  # TODO
    misc_info: MiscInfo | None  # TODO
    model_class: str  # The name of the database model class.
    name: str
    parent_library_id: str
    state: str
    update_time: str
    uuid_: str
    visible: bool
