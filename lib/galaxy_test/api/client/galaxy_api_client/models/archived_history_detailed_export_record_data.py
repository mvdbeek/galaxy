from typing import TypeAlias

from .export_record_data import ExportRecordData

__all__ = ["ArchivedHistoryDetailedExportRecordData"]

ArchivedHistoryDetailedExportRecordData: TypeAlias = ExportRecordData | None
"""Alias for The export record data associated with this archived history. Used to recover the history."""
