from dataclasses import dataclass

from .collection_type import CollectionType
from .prefix_values import PrefixValues
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["CreateWorkbookRequest"]


@dataclass
class CreateWorkbookRequest:
    """
    CreateWorkbookRequest dataclass.

    Args:
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        prefix_columns_type (Optional[str])
                                 :
        prefix_values (Optional[PrefixValues])
                                 : An area to pre-populate URIs, etc...
        title (Optional[str])    : A short title to give the workbook.
    """

    collection_type: (
        CollectionType | None
    )  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    prefix_columns_type: str | None = "URI"
    prefix_values: PrefixValues | None = None  # An area to pre-populate URIs, etc...
    title: str | None = "Sample Sheet for Galaxy"  # A short title to give the workbook.
