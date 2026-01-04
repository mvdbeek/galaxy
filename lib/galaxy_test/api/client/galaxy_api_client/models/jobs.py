from typing import Any, TypeAlias

__all__ = ["Jobs"]

Jobs: TypeAlias = dict[str, Any] | None
"""Alias for Jobs associated with the invocation."""
