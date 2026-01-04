from typing import TypeAlias

from .dataset_error_message import DatasetErrorMessage

__all__ = ["Errors"]

Errors: TypeAlias = list[DatasetErrorMessage] | None
"""Alias for Collection of messages indicating that the resource was not shared with some (or all users) due to an error."""
