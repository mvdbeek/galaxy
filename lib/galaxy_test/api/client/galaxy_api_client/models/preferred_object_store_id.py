from typing import TypeAlias

__all__ = ["PreferredObjectStoreId"]

PreferredObjectStoreId: TypeAlias = str | None
"""Alias for The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences"""
