from dataclasses import dataclass

from .collection_type import CollectionType
from .prefix_columns_type import PrefixColumnsType
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["ParseWorkbook"]


@dataclass
class ParseWorkbook:
    """
    ParseWorkbook dataclass.

    Args:
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        content (str)            : The workbook content (the contents of the xlsx file) that
                                   have been base64 encoded.
        prefix_columns_type (Optional[PrefixColumnsType])
                                 :
    """

    collection_type: (
        CollectionType | None
    )  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    content: str  # The workbook content (the contents of the xlsx file) that have been base64 encoded.
    prefix_columns_type: PrefixColumnsType | None = "URI"
