from typing import TypeAlias

__all__ = ["RemoteFilesIndexParamWriteIntent2"]

RemoteFilesIndexParamWriteIntent2: TypeAlias = bool | None
"""Alias for Whether the query is made with the intention of writing to the source. If set to True, only entries that can be written to will be returned."""
