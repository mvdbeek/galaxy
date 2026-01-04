from typing import TypeAlias

__all__ = ["Info"]

Info: TypeAlias = str | None
"""Alias for Free text field that can be used to store arbitrary information about the dataset. This used to be prominently
displayed in the Galaxy user interface, but now is largely unused.
"""
