from typing import TypeAlias

__all__ = ["RemoteFilesIndexParamRecursive"]

RemoteFilesIndexParamRecursive: TypeAlias = bool | None
"""Alias for Whether to recursively lists all sub-directories. This will be `True` by default depending on the `target`."""
