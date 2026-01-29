from dataclasses import dataclass

from .export_history_archive_payload_directory_uri import ExportHistoryArchivePayloadDirectoryUri
from .export_history_archive_payload_file_name import ExportHistoryArchivePayloadFileName
from .export_history_archive_payload_force import ExportHistoryArchivePayloadForce
from .export_history_archive_payload_gzip import ExportHistoryArchivePayloadGzip
from .export_history_archive_payload_include_deleted import ExportHistoryArchivePayloadIncludeDeleted
from .export_history_archive_payload_include_hidden import ExportHistoryArchivePayloadIncludeHidden

__all__ = ["ExportHistoryArchivePayload"]


@dataclass
class ExportHistoryArchivePayload:
    """
    ExportHistoryArchivePayload dataclass

    Args:
        directory_uri (ExportHistoryArchivePayloadDirectoryUri | None)
                                 : A writable directory destination where the history will
                                   be exported using the `galaxy.files` URI infrastructure.
        file_name (ExportHistoryArchivePayloadFileName | None)
                                 : The name of the file containing the exported history.
        force (ExportHistoryArchivePayloadForce | None)
                                 : Whether to force a rebuild of the history archive.
        gzip (ExportHistoryArchivePayloadGzip | None)
                                 : Whether to export as gzip archive.
        include_deleted (ExportHistoryArchivePayloadIncludeDeleted | None)
                                 : Whether to include deleted datasets in the exported
                                   archive.
        include_hidden (ExportHistoryArchivePayloadIncludeHidden | None)
                                 : Whether to include hidden datasets in the exported
                                   archive.
    """

    directory_uri: ExportHistoryArchivePayloadDirectoryUri | None = (
        None  # A writable directory destination where the history will be exported using the `galaxy.files` URI infrastructure.
    )
    file_name: ExportHistoryArchivePayloadFileName | None = (
        None  # The name of the file containing the exported history.
    )
    force: ExportHistoryArchivePayloadForce | None = None  # Whether to force a rebuild of the history archive.
    gzip: ExportHistoryArchivePayloadGzip | None = True  # Whether to export as gzip archive.
    include_deleted: ExportHistoryArchivePayloadIncludeDeleted | None = (
        False  # Whether to include deleted datasets in the exported archive.
    )
    include_hidden: ExportHistoryArchivePayloadIncludeHidden | None = (
        False  # Whether to include hidden datasets in the exported archive.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "directory_uri": "directory_uri",
            "file_name": "file_name",
            "force": "force",
            "gzip": "gzip",
            "include_deleted": "include_deleted",
            "include_hidden": "include_hidden",
        }
        key_transform_with_dump = {
            "directory_uri": "directory_uri",
            "file_name": "file_name",
            "force": "force",
            "gzip": "gzip",
            "include_deleted": "include_deleted",
            "include_hidden": "include_hidden",
        }
