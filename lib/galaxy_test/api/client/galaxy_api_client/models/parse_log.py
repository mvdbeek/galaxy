from typing import TypeAlias

from .parse_log_item import ParseLogItem

__all__ = ["ParseLog"]

ParseLog: TypeAlias = list[ParseLogItem]
