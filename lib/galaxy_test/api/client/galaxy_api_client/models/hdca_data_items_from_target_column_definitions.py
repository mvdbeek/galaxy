from typing import TypeAlias

from .sample_sheet_column_definition import SampleSheetColumnDefinition

__all__ = ["HdcaDataItemsFromTargetColumnDefinitions"]

HdcaDataItemsFromTargetColumnDefinitions: TypeAlias = list[SampleSheetColumnDefinition] | None
