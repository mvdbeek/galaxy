from typing import TypeAlias

from .export_object_metadata import ExportObjectMetadata

__all__ = ["ExportMetadata"]

ExportMetadata: TypeAlias = ExportObjectMetadata | None
