from dataclasses import dataclass

from .create_workbook_for_collection_api_prefix_values import CreateWorkbookForCollectionApiPrefixValues
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["CreateWorkbookForCollectionApi"]


@dataclass
class CreateWorkbookForCollectionApi:
    """
    CreateWorkbookForCollectionApi dataclass

    Args:
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        prefix_values (CreateWorkbookForCollectionApiPrefixValues | None)
                                 : An area to pre-populate URIs, etc...
    """

    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    prefix_values: CreateWorkbookForCollectionApiPrefixValues | None = None  # An area to pre-populate URIs, etc...

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "column_definitions": "column_definitions",
            "prefix_values": "prefix_values",
        }
        key_transform_with_dump = {
            "column_definitions": "column_definitions",
            "prefix_values": "prefix_values",
        }
