from dataclasses import dataclass

from .sample_sheet_column_definition_model import SampleSheetColumnDefinitionModel

__all__ = ["ParseWorkbookForCollectionApi"]


@dataclass
class ParseWorkbookForCollectionApi:
    """
    ParseWorkbookForCollectionApi dataclass.

    Args:
        column_definitions (List[SampleSheetColumnDefinitionModel])
                                 : A description of the columns expected in the workbook
                                   after the first columns described by
                                   'prefix_columns_type'
        content (str)            : The workbook content (the contents of the xlsx file) that
                                   have been base64 encoded.
    """

    column_definitions: list[
        SampleSheetColumnDefinitionModel
    ]  # A description of the columns expected in the workbook after the first columns described by 'prefix_columns_type'
    content: str  # The workbook content (the contents of the xlsx file) that have been base64 encoded.
