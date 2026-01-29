from typing import TypeAlias

__all__ = ["PastedDataElementPasteContent"]

PastedDataElementPasteContent: TypeAlias = str | int | float | bool
"""Alias for This is the text of the content to import if the 'src' of the item is 'pasted'.
"""
