from dataclasses import dataclass, field
from datetime import datetime

from .library_folder_details_description import LibraryFolderDetailsDescription
from .library_folder_details_genome_build import LibraryFolderDetailsGenomeBuild
from .library_folder_details_parent_id import LibraryFolderDetailsParentId

__all__ = ["LibraryFolderDetails"]


@dataclass
class LibraryFolderDetails:
    """
    LibraryFolderDetails dataclass

    Args:
        deleted (bool)           : Whether this folder is marked as deleted.
        id_ (str)                : Encoded ID of the library folder. (maps from 'id')
        item_count (int)         : A detailed description of the library folder.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the library folder.
        parent_library_id (str)  : Encoded ID of the Library this folder belongs to.
        update_time (datetime)   : The last time and date this item was updated.
        description (LibraryFolderDetailsDescription | None)
                                 : A detailed description of the library folder.
        genome_build (LibraryFolderDetailsGenomeBuild | None)
                                 : TODO
        library_path (List[str] | None)
                                 : The list of folder names composing the path to this
                                   folder.
        parent_id (LibraryFolderDetailsParentId | None)
                                 : Encoded ID of the parent folder. Empty if it's the root
                                   folder.
    """

    deleted: bool  # Whether this folder is marked as deleted.
    id_: str  # Encoded ID of the library folder. (maps from 'id')
    item_count: int  # A detailed description of the library folder.
    model_class: str  # The name of the database model class.
    name: str  # The name of the library folder.
    parent_library_id: str  # Encoded ID of the Library this folder belongs to.
    update_time: datetime  # The last time and date this item was updated.
    description: LibraryFolderDetailsDescription | None = ""  # A detailed description of the library folder.
    genome_build: LibraryFolderDetailsGenomeBuild | None = "?"  # TODO
    library_path: list[str] | None = field(
        default_factory=list
    )  # The list of folder names composing the path to this folder.
    parent_id: LibraryFolderDetailsParentId | None = (
        None  # Encoded ID of the parent folder. Empty if it's the root folder.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deleted": "deleted",
            "description": "description",
            "genome_build": "genome_build",
            "id": "id_",
            "item_count": "item_count",
            "library_path": "library_path",
            "model_class": "model_class",
            "name": "name",
            "parent_id": "parent_id",
            "parent_library_id": "parent_library_id",
            "update_time": "update_time",
        }
        key_transform_with_dump = {
            "deleted": "deleted",
            "description": "description",
            "genome_build": "genome_build",
            "id_": "id",
            "item_count": "item_count",
            "library_path": "library_path",
            "model_class": "model_class",
            "name": "name",
            "parent_id": "parent_id",
            "parent_library_id": "parent_library_id",
            "update_time": "update_time",
        }
