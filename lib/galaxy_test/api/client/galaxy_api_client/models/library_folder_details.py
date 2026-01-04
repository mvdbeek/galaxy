from dataclasses import dataclass
from datetime import datetime

from .description import Description
from .genome_build import GenomeBuild
from .library_path import LibraryPath
from .parent_id import ParentId

__all__ = ["LibraryFolderDetails"]


@dataclass
class LibraryFolderDetails:
    """
    LibraryFolderDetails dataclass.

    Args:
        deleted (bool)           : Whether this folder is marked as deleted.
        id_ (str)                : Encoded ID of the library folder.
        item_count (int)         : A detailed description of the library folder.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the library folder.
        parent_library_id (str)  : Encoded ID of the Library this folder belongs to.
        update_time (datetime)   : The last time and date this item was updated.
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        library_path (Optional[LibraryPath])
                                 : The list of folder names composing the path to this
                                   folder.
        parent_id (Optional[ParentId])
                                 : Encoded ID of the parent folder. Empty if it's the root
                                   folder.
    """

    deleted: bool  # Whether this folder is marked as deleted.
    id_: str  # Encoded ID of the library folder.
    item_count: int  # A detailed description of the library folder.
    model_class: str  # The name of the database model class.
    name: str  # The name of the library folder.
    parent_library_id: str  # Encoded ID of the Library this folder belongs to.
    update_time: datetime  # The last time and date this item was updated.
    description: Description | None = ""  # Detailed text description for this Quota.
    genome_build: GenomeBuild | None = "?"  # TODO
    library_path: LibraryPath | None = None  # The list of folder names composing the path to this folder.
    parent_id: ParentId | None = None  # Encoded ID of the parent folder. Empty if it's the root folder.
