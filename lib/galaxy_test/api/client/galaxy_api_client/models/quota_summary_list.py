from typing import TypeAlias

from .quota_summary import QuotaSummary

__all__ = ["QuotaSummaryList"]

QuotaSummaryList: TypeAlias = list[QuotaSummary]
