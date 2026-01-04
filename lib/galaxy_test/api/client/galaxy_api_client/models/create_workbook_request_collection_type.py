from enum import Enum


class CreateWorkbookRequestCollectionType(str, Enum):
    SAMPLE_SHEET = "sample_sheet"
    SAMPLE_SHEETPAIRED = "sample_sheet:paired"
    SAMPLE_SHEETPAIRED_OR_UNPAIRED = "sample_sheet:paired_or_unpaired"
    SAMPLE_SHEETRECORD = "sample_sheet:record"

    def __str__(self) -> str:
        return str(self.value)
