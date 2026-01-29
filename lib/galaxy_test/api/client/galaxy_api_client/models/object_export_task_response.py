from dataclasses import dataclass
from datetime import datetime

from .export_metadata import ExportMetadata

__all__ = ["ObjectExportTaskResponse"]


@dataclass
class ObjectExportTaskResponse:
    """
    ObjectExportTaskResponse dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        id_ (str)                : The encoded database ID of the export request.
        preparing (bool)         : Whether the archive is currently being built or in
                                   preparation.
        ready (bool)             : Whether the export has completed successfully and the
                                   archive is ready
        task_uuid (str)          : The identifier of the task processing the export.
        up_to_date (bool)        : False, if a new export archive should be generated.
        export_metadata (Optional[ExportMetadata])
                                 :
    """

    create_time: datetime  # The time and date this item was created.
    id_: str  # The encoded database ID of the export request.
    preparing: bool  # Whether the archive is currently being built or in preparation.
    ready: bool  # Whether the export has completed successfully and the archive is ready
    task_uuid: str  # The identifier of the task processing the export.
    up_to_date: bool  # False, if a new export archive should be generated.
    export_metadata: ExportMetadata | None = None
