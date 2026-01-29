from dataclasses import dataclass

from .create_workbook_request_collection_type import CreateWorkbookRequestCollectionType
from .create_workbook_request_prefix_values import CreateWorkbookRequestPrefixValues
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["CreateWorkbookRequest"]


@dataclass
class CreateWorkbookRequest:
    """
    CreateWorkbookRequest dataclass

    Args:
        collection_type (CreateWorkbookRequestCollectionType)
                                 :
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        prefix_columns_type (str | None)
                                 :
        prefix_values (CreateWorkbookRequestPrefixValues | None)
                                 :
        title (str | None)       : A short title to give the workbook.
    """

    collection_type: CreateWorkbookRequestCollectionType
    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    prefix_columns_type: str | None = "URI"
    prefix_values: CreateWorkbookRequestPrefixValues | None = None
    title: str | None = "Sample Sheet for Galaxy"  # A short title to give the workbook.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "prefix_columns_type": "prefix_columns_type",
            "prefix_values": "prefix_values",
            "title": "title",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "prefix_columns_type": "prefix_columns_type",
            "prefix_values": "prefix_values",
            "title": "title",
        }
