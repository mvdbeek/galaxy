from typing import TypeAlias

from .job_export_history_archive_model import JobExportHistoryArchiveModel
from .job_id_response import JobIdResponse

__all__ = ["HistoriesExportsArchiveExport200Response"]

HistoriesExportsArchiveExport200Response: TypeAlias = JobExportHistoryArchiveModel | JobIdResponse
