from typing import TypeAlias

__all__ = ["FromWorkDir"]

FromWorkDir: TypeAlias = str | None
"""Alias for Relative path to a file produced by the tool in its working directory. Output’s contents are set to this file’s contents."""
