from typing import TypeAlias

__all__ = ["ArchiveExportId"]

ArchiveExportId: TypeAlias = str | None
"""Alias for The encoded ID of the export record to associate with this history archival.This is used to be able to recover the history from the export record."""
