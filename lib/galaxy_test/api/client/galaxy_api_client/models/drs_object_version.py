from typing import TypeAlias

__all__ = ["DrsObjectVersion"]

DrsObjectVersion: TypeAlias = str | None
"""Alias for A string representing a version.
(Some systems may use checksum, a RFC3339 timestamp, or an incrementing version number.)"""
