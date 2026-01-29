from typing import TypeAlias

from .export_history_archive_payload import ExportHistoryArchivePayload

__all__ = ["HistoriesExportsArchiveExportRequestBody"]

HistoriesExportsArchiveExportRequestBody: TypeAlias = ExportHistoryArchivePayload | None
