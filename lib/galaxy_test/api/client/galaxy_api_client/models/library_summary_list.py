from typing import TypeAlias

from .library_summary import LibrarySummary

__all__ = ["LibrarySummaryList"]

LibrarySummaryList: TypeAlias = list[LibrarySummary]
