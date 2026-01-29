from dataclasses import dataclass

from .import_tool_data_bundle_source_src_enum import ImportToolDataBundleSourceSrcEnum

__all__ = ["ImportToolDataBundleDatasetSource"]


@dataclass
class ImportToolDataBundleDatasetSource:
    """
    ImportToolDataBundleDatasetSource dataclass

    Args:
        id_ (str)                : Maps from 'id'
        src (ImportToolDataBundleSourceSrcEnum)
                                 : Indicates that the tool data should be resolved from a
                                   dataset.
    """

    id_: str  # Maps from 'id'
    src: ImportToolDataBundleSourceSrcEnum  # Indicates that the tool data should be resolved from a dataset.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "src": "src",
        }
        key_transform_with_dump = {
            "id_": "id",
            "src": "src",
        }
