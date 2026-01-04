from enum import Enum


class ParsedFetchWorkbookForCollectionsCollectionType(str, Enum):
    LIST = "list"
    LISTLIST = "list:list"
    LISTLISTPAIRED = "list:list:paired"
    LISTPAIRED = "list:paired"
    LISTPAIRED_OR_UNPAIRED = "list:paired_or_unpaired"

    def __str__(self) -> str:
        return str(self.value)
