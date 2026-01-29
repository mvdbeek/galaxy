from typing import TypeAlias

__all__ = ["EncodedJobDetailsUserEmail"]

EncodedJobDetailsUserEmail: TypeAlias = str | None
"""Alias for The email of the user that owns this job. Only the owner of the job and administrators can see this value."""
