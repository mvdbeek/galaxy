from typing import TypeAlias

from .job_export_history_archive_model import JobExportHistoryArchiveModel

__all__ = ["JobExportHistoryArchiveListResponse"]

JobExportHistoryArchiveListResponse: TypeAlias = list[JobExportHistoryArchiveModel]
