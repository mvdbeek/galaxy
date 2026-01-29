from dataclasses import dataclass

from .dbkeys import Dbkeys
from .extensions import Extensions
from .tags import Tags

__all__ = ["DatasetCollectionAttributesResult"]


@dataclass
class DatasetCollectionAttributesResult:
    """
    DatasetCollectionAttributesResult dataclass.

    Args:
        dbkey (str)              : TODO
        dbkeys (Optional[Dbkeys]):
        extension (str)          : The dataset file extension.
        extensions (Extensions)  : Limit inputs to datasets with these extensions. Use
                                   'data' to allow all input datasets.
        model_class (str)        : The name of the database model class.
        tags (Tags)              : The collection of tags associated with an item.
    """

    dbkey: str  # TODO
    dbkeys: Dbkeys | None
    extension: str  # The dataset file extension.
    extensions: Extensions  # Limit inputs to datasets with these extensions. Use 'data' to allow all input datasets.
    model_class: str  # The name of the database model class.
    tags: Tags  # The collection of tags associated with an item.
