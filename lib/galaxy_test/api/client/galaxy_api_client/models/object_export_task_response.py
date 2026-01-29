from dataclasses import dataclass
from datetime import datetime

from .object_export_task_response_export_metadata import ObjectExportTaskResponseExportMetadata

__all__ = ["ObjectExportTaskResponse"]


@dataclass
class ObjectExportTaskResponse:
    """
    ObjectExportTaskResponse dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : The encoded database ID of the export request. (maps from
                                   'id')
        preparing (bool)         : Whether the archive is currently being built or in
                                   preparation.
        ready (bool)             : Whether the export has completed successfully and the
                                   archive is ready
        task_uuid (str)          : The identifier of the task processing the export.
        up_to_date (bool)        : False, if a new export archive should be generated.
        export_metadata (ObjectExportTaskResponseExportMetadata | None)
                                 :
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # The encoded database ID of the export request. (maps from 'id')
    preparing: bool  # Whether the archive is currently being built or in preparation.
    ready: bool  # Whether the export has completed successfully and the archive is ready
    task_uuid: str  # The identifier of the task processing the export.
    up_to_date: bool  # False, if a new export archive should be generated.
    export_metadata: ObjectExportTaskResponseExportMetadata | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "export_metadata": "export_metadata",
            "id": "id_",
            "preparing": "preparing",
            "ready": "ready",
            "task_uuid": "task_uuid",
            "up_to_date": "up_to_date",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "export_metadata": "export_metadata",
            "id_": "id",
            "preparing": "preparing",
            "ready": "ready",
            "task_uuid": "task_uuid",
            "up_to_date": "up_to_date",
        }
