from typing import TypeAlias

from .sample_sheet_column_definition import SampleSheetColumnDefinition

__all__ = ["DcObjectColumnDefinitions"]

DcObjectColumnDefinitions: TypeAlias = list[SampleSheetColumnDefinition] | None
"""Alias for Column definitions for sample sheet collections."""
