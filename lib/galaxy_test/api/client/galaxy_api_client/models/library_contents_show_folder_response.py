from dataclasses import dataclass

from .genome_build import GenomeBuild
from .library_path import LibraryPath
from .parent_id import ParentId

__all__ = ["LibraryContentsShowFolderResponse"]


@dataclass
class LibraryContentsShowFolderResponse:
    """
    LibraryContentsShowFolderResponse dataclass.

    Args:
        deleted (bool)           :
        description (str)        :
        genome_build (Optional[GenomeBuild])
                                 : TODO
        id_ (str)                :
        item_count (int)         :
        library_path (LibraryPath):
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_id (Optional[ParentId])
                                 : Encoded ID of the parent folder. Empty if it's the root
                                   folder.
        parent_library_id (str)  :
        update_time (str)        :
    """

    deleted: bool
    description: str
    genome_build: GenomeBuild | None  # TODO
    id_: str
    item_count: int
    library_path: LibraryPath
    model_class: str  # The name of the database model class.
    name: str
    parent_id: ParentId | None  # Encoded ID of the parent folder. Empty if it's the root folder.
    parent_library_id: str
    update_time: str
