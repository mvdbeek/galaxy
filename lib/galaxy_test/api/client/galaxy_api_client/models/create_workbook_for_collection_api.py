from dataclasses import dataclass

from .prefix_values import PrefixValues
from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["CreateWorkbookForCollectionApi"]


@dataclass
class CreateWorkbookForCollectionApi:
    """
    CreateWorkbookForCollectionApi dataclass.

    Args:
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        prefix_values (Optional[PrefixValues])
                                 : An area to pre-populate URIs, etc...
    """

    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    prefix_values: PrefixValues | None = None  # An area to pre-populate URIs, etc...
