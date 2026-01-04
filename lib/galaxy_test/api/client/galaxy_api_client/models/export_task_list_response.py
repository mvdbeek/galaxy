from typing import TypeAlias

from .object_export_task_response import ObjectExportTaskResponse

__all__ = ["ExportTaskListResponse"]

ExportTaskListResponse: TypeAlias = list[ObjectExportTaskResponse]
