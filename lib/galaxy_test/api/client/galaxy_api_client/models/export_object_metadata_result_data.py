from typing import TypeAlias

from .export_object_result_metadata import ExportObjectResultMetadata

__all__ = ["ExportObjectMetadataResultData"]

ExportObjectMetadataResultData: TypeAlias = ExportObjectResultMetadata | None
