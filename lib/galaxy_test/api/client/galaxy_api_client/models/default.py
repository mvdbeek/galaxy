from typing import Any, TypeAlias

__all__ = ["Default"]

Default: TypeAlias = Any
"""Alias for Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``."""
