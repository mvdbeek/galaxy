from typing import TypeAlias

__all__ = ["DatatypeDetailsDisplayBehavior"]

DatatypeDetailsDisplayBehavior: TypeAlias = str | None
"""Alias for How this datatype behaves when displayed with preview=True: 'inline' (can be displayed in browser) or 'download' (triggers download)"""
