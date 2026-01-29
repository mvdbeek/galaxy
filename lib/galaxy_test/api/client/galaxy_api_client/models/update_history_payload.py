from dataclasses import dataclass

from .annotation import Annotation
from .deleted import Deleted
from .genome_build import GenomeBuild
from .importable import Importable
from .name import Name
from .preferred_object_store_id import PreferredObjectStoreId
from .published import Published
from .purged import Purged
from .tags import Tags

__all__ = ["UpdateHistoryPayload"]


@dataclass
class UpdateHistoryPayload:
    """
    UpdateHistoryPayload dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        deleted (Optional[Deleted])
                                 : Whether this Visualization has been deleted.
        genome_build (Optional[GenomeBuild])
                                 : TODO
        importable (Optional[Importable])
                                 : Indicates if the workflow is importable by the current
                                   user.
        name (Optional[Name])    : The name of the creator.
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        published (Optional[Published])
                                 : Whether this resource is currently publicly available to
                                   all users.
        purged (Optional[Purged]): Whether this dataset has been removed from disk.
        tags (Optional[Tags])    : The collection of tags associated with an item.
    """

    annotation: Annotation | None = None  # The annotation of this Visualization.
    deleted: Deleted | None = False  # Whether this Visualization has been deleted.
    genome_build: GenomeBuild | None = "?"  # TODO
    importable: Importable | None = None  # Indicates if the workflow is importable by the current user.
    name: Name | None = None  # The name of the creator.
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    published: Published | None = None  # Whether this resource is currently publicly available to all users.
    purged: Purged | None = None  # Whether this dataset has been removed from disk.
    tags: Tags | None = None  # The collection of tags associated with an item.
