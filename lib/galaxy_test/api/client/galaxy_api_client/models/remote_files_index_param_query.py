from typing import TypeAlias

__all__ = ["RemoteFilesIndexParamQuery"]

RemoteFilesIndexParamQuery: TypeAlias = str | None
"""Alias for Search query to filter entries by. The syntax could be different depending on the target source."""
