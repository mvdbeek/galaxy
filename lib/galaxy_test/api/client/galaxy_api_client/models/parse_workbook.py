from dataclasses import dataclass

from .parse_workbook_collection_type import ParseWorkbookCollectionType
from .parse_workbook_prefix_columns_type import ParseWorkbookPrefixColumnsType
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["ParseWorkbook"]


@dataclass
class ParseWorkbook:
    """
    ParseWorkbook dataclass

    Args:
        collection_type (ParseWorkbookCollectionType)
                                 :
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        content (str)            : The workbook content (the contents of the xlsx file) that
                                   have been base64 encoded.
        prefix_columns_type (ParseWorkbookPrefixColumnsType | None)
                                 :
    """

    collection_type: ParseWorkbookCollectionType
    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    content: str  # The workbook content (the contents of the xlsx file) that have been base64 encoded.
    prefix_columns_type: ParseWorkbookPrefixColumnsType | None = "URI"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "content": "content",
            "prefix_columns_type": "prefix_columns_type",
        }
        key_transform_with_dump = {
            "collection_type": "collection_type",
            "column_definitions": "column_definitions",
            "content": "content",
            "prefix_columns_type": "prefix_columns_type",
        }
