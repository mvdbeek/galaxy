from typing import TypeAlias

from .parsed_workbook_for_collection_parse_log_item import ParsedWorkbookForCollectionParseLogItem

__all__ = ["ParsedWorkbookForCollectionParseLog"]

ParsedWorkbookForCollectionParseLog: TypeAlias = list[ParsedWorkbookForCollectionParseLogItem]
