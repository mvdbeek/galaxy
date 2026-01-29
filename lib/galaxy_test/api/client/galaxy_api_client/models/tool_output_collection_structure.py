from dataclasses import dataclass

from .collection_type import CollectionType
from .collection_type_from_rules import CollectionTypeFromRules
from .collection_type_source import CollectionTypeSource
from .discover_datasets import DiscoverDatasets
from .structured_like import StructuredLike

__all__ = ["ToolOutputCollectionStructure"]


@dataclass
class ToolOutputCollectionStructure:
    """
    ToolOutputCollectionStructure dataclass.

    Args:
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        collection_type_from_rules (Optional[CollectionTypeFromRules])
                                 :
        collection_type_source (Optional[CollectionTypeSource])
                                 :
        discover_datasets (Optional[DiscoverDatasets])
                                 :
        structured_like (Optional[StructuredLike])
                                 :
    """

    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    collection_type_from_rules: CollectionTypeFromRules | None = None
    collection_type_source: CollectionTypeSource | None = None
    discover_datasets: DiscoverDatasets | None = None
    structured_like: StructuredLike | None = None
