from enum import Enum, unique

__all__ = ["ParsedFetchWorkbookForCollectionsCollectionType"]


@unique
class ParsedFetchWorkbookForCollectionsCollectionType(str, Enum):
    """
    ParsedFetchWorkbookForCollectionsCollectionType Enum

    Args:
        list (str)               : Value for LIST
        list:paired (str)        : Value for LISTPAIRED
        list:list (str)          : Value for LISTLIST
        list:list:paired (str)   : Value for LISTLISTPAIRED
        list:paired_or_unpaired (str)
                                 : Value for LISTPAIRED_OR_UNPAIRED
    """

    LIST = "list"
    LISTPAIRED = "list:paired"
    LISTLIST = "list:list"
    LISTLISTPAIRED = "list:list:paired"
    LISTPAIRED_OR_UNPAIRED = "list:paired_or_unpaired"
