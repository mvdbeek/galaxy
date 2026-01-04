from typing import TypeAlias

__all__ = ["AccessId"]

AccessId: TypeAlias = str | None
"""Alias for An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided."""
