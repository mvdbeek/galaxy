from dataclasses import dataclass
from uuid import UUID

from .model_store_format import ModelStoreFormat
from .short_term_store_export_payload_duration import ShortTermStoreExportPayloadDuration

__all__ = ["ShortTermStoreExportPayload"]


@dataclass
class ShortTermStoreExportPayload:
    """
    ShortTermStoreExportPayload dataclass

    Args:
        short_term_storage_request_id (UUID)
                                 :
        duration (ShortTermStoreExportPayloadDuration | None)
                                 :
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

    short_term_storage_request_id: UUID
    duration: ShortTermStoreExportPayloadDuration | None = None
    include_deleted: bool | None = False  # Include file contents for deleted datasets (if include_files is True).
    include_files: bool | None = True  # include materialized files in export when available
    include_hidden: bool | None = False  # Include file contents for hidden datasets (if include_files is True).
    model_store_format: ModelStoreFormat | None = None  # Available types of model stores for export.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "duration": "duration",
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
            "short_term_storage_request_id": "short_term_storage_request_id",
        }
        key_transform_with_dump = {
            "duration": "duration",
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
            "short_term_storage_request_id": "short_term_storage_request_id",
        }
