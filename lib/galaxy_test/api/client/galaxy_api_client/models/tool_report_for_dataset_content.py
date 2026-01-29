from typing import TypeAlias

__all__ = ["ToolReportForDatasetContent"]

ToolReportForDatasetContent: TypeAlias = str | None
"""Alias for Text contents of the last page revision with embedded directives expanded (type dependent on content_format)."""
