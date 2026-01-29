from typing import TypeAlias

from .metadata_file import MetadataFile

__all__ = ["HdaCustomMetaFiles"]

HdaCustomMetaFiles: TypeAlias = list[MetadataFile] | None
"""Alias for Collection of metadata files associated with this dataset."""
