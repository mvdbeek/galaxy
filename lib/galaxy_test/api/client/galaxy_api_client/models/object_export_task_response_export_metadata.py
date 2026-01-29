from typing import TypeAlias

from .export_object_metadata import ExportObjectMetadata

__all__ = ["ObjectExportTaskResponseExportMetadata"]

ObjectExportTaskResponseExportMetadata: TypeAlias = ExportObjectMetadata | None
