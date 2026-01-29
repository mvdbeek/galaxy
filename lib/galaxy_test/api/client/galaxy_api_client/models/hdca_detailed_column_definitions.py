from typing import TypeAlias

from .sample_sheet_column_definition import SampleSheetColumnDefinition

__all__ = ["HdcaDetailedColumnDefinitions"]

HdcaDetailedColumnDefinitions: TypeAlias = list[SampleSheetColumnDefinition] | None
"""Alias for Column data associated with each element of this collection."""
