from typing import TypeAlias

from .failed_item import FailedItem

__all__ = ["Failed"]

Failed: TypeAlias = list[FailedItem]
