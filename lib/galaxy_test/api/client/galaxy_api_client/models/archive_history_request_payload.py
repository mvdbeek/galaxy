from dataclasses import dataclass

from .archive_export_id import ArchiveExportId

__all__ = ["ArchiveHistoryRequestPayload"]


@dataclass
class ArchiveHistoryRequestPayload:
    """
    ArchiveHistoryRequestPayload dataclass.

    Args:
        archive_export_id (Optional[ArchiveExportId])
                                 : The encoded ID of the export record to associate with
                                   this history archival.This is used to be able to recover
                                   the history from the export record.
        purge_history (Optional[bool])
                                 : Whether to purge the history after archiving it. It
                                   requires an `archive_export_id` to be set.
    """

    archive_export_id: ArchiveExportId | None = (
        None  # The encoded ID of the export record to associate with this history archival.This is used to be able to recover the history from the export record.
    )
    purge_history: bool | None = (
        False  # Whether to purge the history after archiving it. It requires an `archive_export_id` to be set.
    )
