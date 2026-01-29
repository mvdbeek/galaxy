from dataclasses import dataclass

from .archive_history_request_payload_archive_export_id import ArchiveHistoryRequestPayloadArchiveExportId

__all__ = ["ArchiveHistoryRequestPayload"]


@dataclass
class ArchiveHistoryRequestPayload:
    """
    ArchiveHistoryRequestPayload dataclass

    Args:
        archive_export_id (ArchiveHistoryRequestPayloadArchiveExportId | None)
                                 : The encoded ID of the export record to associate with
                                   this history archival.This is used to be able to recover
                                   the history from the export record.
        purge_history (bool | None)
                                 : Whether to purge the history after archiving it. It
                                   requires an `archive_export_id` to be set.
    """

    archive_export_id: ArchiveHistoryRequestPayloadArchiveExportId | None = (
        None  # The encoded ID of the export record to associate with this history archival.This is used to be able to recover the history from the export record.
    )
    purge_history: bool | None = (
        False  # Whether to purge the history after archiving it. It requires an `archive_export_id` to be set.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "archive_export_id": "archive_export_id",
            "purge_history": "purge_history",
        }
        key_transform_with_dump = {
            "archive_export_id": "archive_export_id",
            "purge_history": "purge_history",
        }
