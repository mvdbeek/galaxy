from dataclasses import dataclass

from .export_object_result_metadata_error import ExportObjectResultMetadataError
from .export_object_result_metadata_uri import ExportObjectResultMetadataUri

__all__ = ["ExportObjectResultMetadata"]


@dataclass
class ExportObjectResultMetadata:
    """
    ExportObjectResultMetadata dataclass

    Args:
        success (bool)           :
        error (ExportObjectResultMetadataError | None)
                                 :
        uri (ExportObjectResultMetadataUri | None)
                                 :
    """

    success: bool
    error: ExportObjectResultMetadataError | None = None
    uri: ExportObjectResultMetadataUri | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "error": "error",
            "success": "success",
            "uri": "uri",
        }
        key_transform_with_dump = {
            "error": "error",
            "success": "success",
            "uri": "uri",
        }
