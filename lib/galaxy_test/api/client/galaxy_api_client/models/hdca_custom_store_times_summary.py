from typing import TypeAlias

from .oldest_create_time_by_object_store_id import OldestCreateTimeByObjectStoreId

__all__ = ["HdcaCustomStoreTimesSummary"]

HdcaCustomStoreTimesSummary: TypeAlias = list[OldestCreateTimeByObjectStoreId] | None
"""Alias for A list of objects containing the object store ID and the oldest creation time of the datasets stored in that object store for this collection.This is used to determine the age of the datasets in the collection when the object store is short-lived."""
