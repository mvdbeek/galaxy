from typing import TypeAlias

from .parsed_workbook_parse_log_item import ParsedWorkbookParseLogItem

__all__ = ["ParsedWorkbookParseLog"]

ParsedWorkbookParseLog: TypeAlias = list[ParsedWorkbookParseLogItem]
