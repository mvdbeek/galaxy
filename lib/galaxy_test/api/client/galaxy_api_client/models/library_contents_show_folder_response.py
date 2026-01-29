from dataclasses import dataclass

from .library_contents_show_folder_response_genome_build import LibraryContentsShowFolderResponseGenomeBuild
from .library_contents_show_folder_response_parent_id import LibraryContentsShowFolderResponseParentId

__all__ = ["LibraryContentsShowFolderResponse"]


@dataclass
class LibraryContentsShowFolderResponse:
    """
    LibraryContentsShowFolderResponse dataclass

    Args:
        deleted (bool)           :
        description (str)        :
        genome_build (LibraryContentsShowFolderResponseGenomeBuild)
                                 :
        id_ (str)                : Maps from 'id'
        item_count (int)         :
        library_path (List[str]) :
        model_class (str)        : The name of the database model class.
        name (str)               :
        parent_id (LibraryContentsShowFolderResponseParentId)
                                 :
        parent_library_id (str)  :
        update_time (str)        :
    """

    deleted: bool
    description: str
    genome_build: LibraryContentsShowFolderResponseGenomeBuild
    id_: str  # Maps from 'id'
    item_count: int
    library_path: list[str]
    model_class: str  # The name of the database model class.
    name: str
    parent_id: LibraryContentsShowFolderResponseParentId
    parent_library_id: str
    update_time: str

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
