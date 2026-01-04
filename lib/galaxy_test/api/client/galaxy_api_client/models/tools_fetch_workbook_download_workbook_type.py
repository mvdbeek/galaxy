from enum import Enum


class ToolsFetchWorkbookDownloadWorkbookType(str, Enum):
    COLLECTION = "collection"
    COLLECTIONS = "collections"
    DATASETS = "datasets"

    def __str__(self) -> str:
        return str(self.value)
