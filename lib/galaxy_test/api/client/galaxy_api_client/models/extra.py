from typing import TypeAlias

from .share_with_extra import ShareWithExtra

__all__ = ["Extra"]

Extra: TypeAlias = ShareWithExtra | None
"""Alias for Optional extra information about this shareable resource that may be of interest. The contents of this field depend on the particular resource."""
