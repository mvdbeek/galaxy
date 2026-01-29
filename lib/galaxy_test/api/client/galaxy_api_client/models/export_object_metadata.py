from dataclasses import dataclass

from .export_object_metadata_result_data import ExportObjectMetadataResultData
from .export_object_request_metadata import ExportObjectRequestMetadata

__all__ = ["ExportObjectMetadata"]


@dataclass
class ExportObjectMetadata:
    """
    ExportObjectMetadata dataclass

    Args:
        request_data (ExportObjectRequestMetadata)
                                 :
        result_data (ExportObjectMetadataResultData | None)
                                 :
    """

    request_data: ExportObjectRequestMetadata
    result_data: ExportObjectMetadataResultData | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "request_data": "request_data",
            "result_data": "result_data",
        }
        key_transform_with_dump = {
            "request_data": "request_data",
            "result_data": "result_data",
        }
