from typing import TypeAlias

__all__ = ["PasteContent"]

PasteContent: TypeAlias = bool | float | int | str
"""Alias for This is the text of the content to import if the 'src' of the item is 'pasted'.
"""
