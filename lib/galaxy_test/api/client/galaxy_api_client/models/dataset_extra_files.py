from typing import TypeAlias

from .extra_file_entry import ExtraFileEntry

__all__ = ["DatasetExtraFiles"]

DatasetExtraFiles: TypeAlias = list[ExtraFileEntry]
"""Alias for A list of extra files associated with a dataset."""
