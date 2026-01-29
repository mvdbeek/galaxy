from enum import Enum, unique

__all__ = ["TaggableItemClass"]


@unique
class TaggableItemClass(str, Enum):
    """
    TaggableItemClass Enum

    Args:
        History (str)            : Value for HISTORY
        HistoryDatasetAssociation (str)
                                 : Value for HISTORYDATASETASSOCIATION
        HistoryDatasetCollectionAssociation (str)
                                 : Value for HISTORYDATASETCOLLECTIONASSOCIATION
        LibraryDatasetDatasetAssociation (str)
                                 : Value for LIBRARYDATASETDATASETASSOCIATION
        Page (str)               : Value for PAGE
        StoredWorkflow (str)     : Value for STOREDWORKFLOW
        Visualization (str)      : Value for VISUALIZATION
    """

    HISTORY = "History"
    HISTORYDATASETASSOCIATION = "HistoryDatasetAssociation"
    HISTORYDATASETCOLLECTIONASSOCIATION = "HistoryDatasetCollectionAssociation"
    LIBRARYDATASETDATASETASSOCIATION = "LibraryDatasetDatasetAssociation"
    PAGE = "Page"
    STOREDWORKFLOW = "StoredWorkflow"
    VISUALIZATION = "Visualization"
