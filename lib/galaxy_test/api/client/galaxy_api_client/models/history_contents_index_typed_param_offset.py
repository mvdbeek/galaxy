from typing import TypeAlias

__all__ = ["HistoryContentsIndexTypedParamOffset"]

HistoryContentsIndexTypedParamOffset: TypeAlias = int | None
"""Alias for Starts at the beginning skip the first ( offset - 1 ) items and begin returning at the Nth item"""
