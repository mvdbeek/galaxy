from typing import TypeAlias

__all__ = ["HistoryContentsIndexParamIds"]

HistoryContentsIndexParamIds: TypeAlias = str | None
"""Alias for A comma-separated list of encoded `HDA/HDCA` IDs. If this list is provided, only information about the specific datasets will be returned. Also, setting this value will return `all` details of the content item."""
