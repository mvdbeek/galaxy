from dataclasses import dataclass

from .body_histories_create_all_datasets import BodyHistoriesCreateAllDatasets
from .body_histories_create_archive_file import BodyHistoriesCreateArchiveFile
from .body_histories_create_archive_source import BodyHistoriesCreateArchiveSource
from .body_histories_create_archive_type import BodyHistoriesCreateArchiveType
from .body_histories_create_history_id import BodyHistoriesCreateHistoryId
from .body_histories_create_name import BodyHistoriesCreateName

__all__ = ["BodyHistoriesCreate2"]


@dataclass
class BodyHistoriesCreate2:
    """
    BodyHistoriesCreate2 dataclass

    Args:
        all_datasets (BodyHistoriesCreateAllDatasets | None)
                                 :
        archive_file (BodyHistoriesCreateArchiveFile | None)
                                 :
        archive_source (BodyHistoriesCreateArchiveSource | None)
                                 :
        archive_type (BodyHistoriesCreateArchiveType | None)
                                 :
        history_id (BodyHistoriesCreateHistoryId | None)
                                 :
        name (BodyHistoriesCreateName | None)
                                 :
    """

    all_datasets: BodyHistoriesCreateAllDatasets | None = True
    archive_file: BodyHistoriesCreateArchiveFile | None = None
    archive_source: BodyHistoriesCreateArchiveSource | None = None
    archive_type: BodyHistoriesCreateArchiveType | None = "url"
    history_id: BodyHistoriesCreateHistoryId | None = None
    name: BodyHistoriesCreateName | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "all_datasets": "all_datasets",
            "archive_file": "archive_file",
            "archive_source": "archive_source",
            "archive_type": "archive_type",
            "history_id": "history_id",
            "name": "name",
        }
        key_transform_with_dump = {
            "all_datasets": "all_datasets",
            "archive_file": "archive_file",
            "archive_source": "archive_source",
            "archive_type": "archive_type",
            "history_id": "history_id",
            "name": "name",
        }
