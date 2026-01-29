from typing import TypeAlias

from .export_object_result_metadata import ExportObjectResultMetadata

__all__ = ["ResultData"]

ResultData: TypeAlias = ExportObjectResultMetadata | None
