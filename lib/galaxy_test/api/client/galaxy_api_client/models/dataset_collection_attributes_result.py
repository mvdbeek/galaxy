from dataclasses import dataclass

from .dataset_collection_attributes_result_dbkeys import DatasetCollectionAttributesResultDbkeys
from .dataset_collection_attributes_result_extensions import DatasetCollectionAttributesResultExtensions

__all__ = ["DatasetCollectionAttributesResult"]


@dataclass
class DatasetCollectionAttributesResult:
    """
    DatasetCollectionAttributesResult dataclass

    Args:
        dbkey (str)              : TODO
        dbkeys (DatasetCollectionAttributesResultDbkeys)
                                 :
        extension (str)          : The dataset file extension.
        extensions (DatasetCollectionAttributesResultExtensions)
                                 :
        model_class (str)        : The name of the database model class.
        tags (List[str])         : The collection of tags associated with an item.
    """

    dbkey: str  # TODO
    dbkeys: DatasetCollectionAttributesResultDbkeys
    extension: str  # The dataset file extension.
    extensions: DatasetCollectionAttributesResultExtensions
    model_class: str  # The name of the database model class.
    tags: list[str]  # The collection of tags associated with an item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dbkey": "dbkey",
            "dbkeys": "dbkeys",
            "extension": "extension",
            "extensions": "extensions",
            "model_class": "model_class",
            "tags": "tags",
        }
        key_transform_with_dump = {
            "dbkey": "dbkey",
            "dbkeys": "dbkeys",
            "extension": "extension",
            "extensions": "extensions",
            "model_class": "model_class",
            "tags": "tags",
        }
