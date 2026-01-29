from enum import Enum, unique

__all__ = ["CreateWorkbookRequestCollectionType"]


@unique
class CreateWorkbookRequestCollectionType(str, Enum):
    """
    CreateWorkbookRequestCollectionType Enum

    Args:
        sample_sheet (str)       : Value for SAMPLE_SHEET
        sample_sheet:paired (str): Value for SAMPLE_SHEETPAIRED
        sample_sheet:paired_or_unpaired (str)
                                 : Value for SAMPLE_SHEETPAIRED_OR_UNPAIRED
        sample_sheet:record (str): Value for SAMPLE_SHEETRECORD
    """

    SAMPLE_SHEET = "sample_sheet"
    SAMPLE_SHEETPAIRED = "sample_sheet:paired"
    SAMPLE_SHEETPAIRED_OR_UNPAIRED = "sample_sheet:paired_or_unpaired"
    SAMPLE_SHEETRECORD = "sample_sheet:record"
