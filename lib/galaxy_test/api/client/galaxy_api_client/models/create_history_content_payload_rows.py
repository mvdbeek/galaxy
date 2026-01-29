from typing import Any, TypeAlias

__all__ = ["CreateHistoryContentPayloadRows"]

CreateHistoryContentPayloadRows: TypeAlias = dict[str, Any] | None
"""Alias for Specify rows of metadata data corresponding to an identifier if collection_type is sample_sheet"""
