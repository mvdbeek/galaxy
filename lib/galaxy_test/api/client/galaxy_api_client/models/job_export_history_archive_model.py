from dataclasses import dataclass

__all__ = ["JobExportHistoryArchiveModel"]


@dataclass
class JobExportHistoryArchiveModel:
    """
    JobExportHistoryArchiveModel dataclass

    Args:
        download_url (str)       : Relative API URL to download the exported history
                                   archive.
        external_download_latest_url (str)
                                 : Fully qualified URL to download the latests version of
                                   the exported history archive.
        external_download_permanent_url (str)
                                 : Fully qualified URL to download this particular version
                                   of the exported history archive.
        id_ (str)                : The encoded database ID of the export request. (maps from
                                   'id')
        job_id (str)             : The encoded database ID of the job that generated this
                                   history export archive.
        preparing (bool)         : Whether the archive is currently being built or in
                                   preparation.
        ready (bool)             : Whether the export has completed successfully and the
                                   archive is ready
        up_to_date (bool)        : False, if a new export archive should be generated.
    """

    download_url: str  # Relative API URL to download the exported history archive.
    external_download_latest_url: (
        str  # Fully qualified URL to download the latests version of the exported history archive.
    )
    external_download_permanent_url: (
        str  # Fully qualified URL to download this particular version of the exported history archive.
    )
    id_: str  # The encoded database ID of the export request. (maps from 'id')
    job_id: str  # The encoded database ID of the job that generated this history export archive.
    preparing: bool  # Whether the archive is currently being built or in preparation.
    ready: bool  # Whether the export has completed successfully and the archive is ready
    up_to_date: bool  # False, if a new export archive should be generated.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "download_url": "download_url",
            "external_download_latest_url": "external_download_latest_url",
            "external_download_permanent_url": "external_download_permanent_url",
            "id": "id_",
            "job_id": "job_id",
            "preparing": "preparing",
            "ready": "ready",
            "up_to_date": "up_to_date",
        }
        key_transform_with_dump = {
            "download_url": "download_url",
            "external_download_latest_url": "external_download_latest_url",
            "external_download_permanent_url": "external_download_permanent_url",
            "id_": "id",
            "job_id": "job_id",
            "preparing": "preparing",
            "ready": "ready",
            "up_to_date": "up_to_date",
        }
