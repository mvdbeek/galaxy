from typing import TypeAlias

from .sample_sheet_column_definition import SampleSheetColumnDefinition

__all__ = ["CreateHistoryContentPayloadColumnDefinitions"]

CreateHistoryContentPayloadColumnDefinitions: TypeAlias = list[SampleSheetColumnDefinition] | None
"""Alias for Specify definitions for row data if collection_type is sample_sheet"""
