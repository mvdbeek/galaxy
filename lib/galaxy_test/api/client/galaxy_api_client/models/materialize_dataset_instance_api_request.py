from dataclasses import dataclass

from .dataset_source_type import DatasetSourceType

__all__ = ["MaterializeDatasetInstanceApiRequest"]


@dataclass
class MaterializeDatasetInstanceApiRequest:
    """
    MaterializeDatasetInstanceApiRequest dataclass

    Args:
        content (str)            : Depending on the `source` it can be: - The encoded id of
                                   the source library dataset - The encoded id of the HDA
        source (DatasetSourceType):
    """

    content: str  # Depending on the `source` it can be: - The encoded id of the source library dataset - The encoded id of the HDA
    source: DatasetSourceType

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "source": "source",
        }
        key_transform_with_dump = {
            "content": "content",
            "source": "source",
        }
