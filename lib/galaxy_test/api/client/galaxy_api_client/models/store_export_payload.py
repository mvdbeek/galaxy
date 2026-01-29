from dataclasses import dataclass

from .model_store_format import ModelStoreFormat

__all__ = ["StoreExportPayload"]


@dataclass
class StoreExportPayload:
    """
    StoreExportPayload dataclass

    Args:
        include_deleted (bool | None)
                                 : Include file contents for deleted datasets (if
                                   include_files is True).
        include_files (bool | None)
                                 : include materialized files in export when available
        include_hidden (bool | None)
                                 : Include file contents for hidden datasets (if
                                   include_files is True).
        model_store_format (ModelStoreFormat | None)
                                 : Available types of model stores for export.
    """

    include_deleted: bool | None = False  # Include file contents for deleted datasets (if include_files is True).
    include_files: bool | None = True  # include materialized files in export when available
    include_hidden: bool | None = False  # Include file contents for hidden datasets (if include_files is True).
    model_store_format: ModelStoreFormat | None = None  # Available types of model stores for export.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
        }
        key_transform_with_dump = {
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
        }
