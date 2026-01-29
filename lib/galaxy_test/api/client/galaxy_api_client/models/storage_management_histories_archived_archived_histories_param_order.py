from typing import TypeAlias

from .stored_item_order_by import StoredItemOrderBy

__all__ = ["StorageManagementHistoriesArchivedArchivedHistoriesParamOrder"]

StorageManagementHistoriesArchivedArchivedHistoriesParamOrder: TypeAlias = StoredItemOrderBy | None
"""Alias for String containing one of the valid ordering attributes followed by '-asc' or '-dsc' for ascending and descending order respectively."""
