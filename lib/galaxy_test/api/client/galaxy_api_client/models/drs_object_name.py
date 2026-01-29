from typing import TypeAlias

__all__ = ["DrsObjectName"]

DrsObjectName: TypeAlias = str | None
"""Alias for A string that can be used to name a `DrsObject`.
This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames]."""
