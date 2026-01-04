from typing import TypeAlias

__all__ = ["ValidatedStateMessage"]

ValidatedStateMessage: TypeAlias = str | None
"""Alias for The message with details about the datatype validation result for this dataset."""
