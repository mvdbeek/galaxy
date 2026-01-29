from dataclasses import dataclass

from .tool_output_collection_structure_collection_type import ToolOutputCollectionStructureCollectionType
from .tool_output_collection_structure_collection_type_from_rules import (
    ToolOutputCollectionStructureCollectionTypeFromRules,
)
from .tool_output_collection_structure_collection_type_source import ToolOutputCollectionStructureCollectionTypeSource
from .tool_output_collection_structure_discover_datasets import ToolOutputCollectionStructureDiscoverDatasets
from .tool_output_collection_structure_structured_like import ToolOutputCollectionStructureStructuredLike

__all__ = ["ToolOutputCollectionStructure"]


@dataclass
class ToolOutputCollectionStructure:
    """
    ToolOutputCollectionStructure dataclass

    Args:
        collection_type (ToolOutputCollectionStructureCollectionType | None)
                                 :
        collection_type_from_rules (ToolOutputCollectionStructureCollectionTypeFromRules | None)
                                 :
        collection_type_source (ToolOutputCollectionStructureCollectionTypeSource | None)
                                 :
        discover_datasets (ToolOutputCollectionStructureDiscoverDatasets | None)
                                 :
        structured_like (ToolOutputCollectionStructureStructuredLike | None)
                                 :
    """

    collection_type: ToolOutputCollectionStructureCollectionType | None = None
    collection_type_from_rules: ToolOutputCollectionStructureCollectionTypeFromRules | None = None
    collection_type_source: ToolOutputCollectionStructureCollectionTypeSource | None = None
    discover_datasets: ToolOutputCollectionStructureDiscoverDatasets | None = None
    structured_like: ToolOutputCollectionStructureStructuredLike | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "collection_type_from_rules": "collection_type_from_rules",
            "collection_type_source": "collection_type_source",
            "discover_datasets": "discover_datasets",
            "structured_like": "structured_like",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "collection_type_from_rules": "collection_type_from_rules",
            "collection_type_source": "collection_type_source",
            "discover_datasets": "discover_datasets",
            "structured_like": "structured_like",
        }
