from typing import TypeAlias

__all__ = ["ServerDirElementTags"]

ServerDirElementTags: TypeAlias = list[str] | None
"""Alias for Tags are a way to categorize datasets in Galaxy. They are free-form text strings that can be used to
group datasets together. Tags can be used to filter datasets in the Galaxy user interface and can be
used to search for datasets in the Galaxy API.
"""
