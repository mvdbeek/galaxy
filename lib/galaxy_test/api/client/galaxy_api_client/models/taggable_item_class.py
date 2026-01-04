from enum import Enum


class TaggableItemClass(str, Enum):
    HISTORY = "History"
    HISTORYDATASETASSOCIATION = "HistoryDatasetAssociation"
    HISTORYDATASETCOLLECTIONASSOCIATION = "HistoryDatasetCollectionAssociation"
    LIBRARYDATASETDATASETASSOCIATION = "LibraryDatasetDatasetAssociation"
    PAGE = "Page"
    STOREDWORKFLOW = "StoredWorkflow"
    VISUALIZATION = "Visualization"

    def __str__(self) -> str:
        return str(self.value)
