from typing import TypeAlias

__all__ = ["AccessUrlHeaders"]

AccessUrlHeaders: TypeAlias = list[str] | None
"""Alias for An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes."""
