from dataclasses import dataclass

from .all_datasets import AllDatasets
from .archive_file import ArchiveFile
from .archive_source import ArchiveSource
from .archive_type import ArchiveType
from .history_id import HistoryId
from .name import Name

__all__ = ["BodyHistoriesCreate2"]


@dataclass
class BodyHistoriesCreate2:
    """
    BodyHistoriesCreate2 dataclass.

    Args:
        all_datasets (Optional[AllDatasets])
                                 :
        archive_file (Optional[ArchiveFile])
                                 :
        archive_source (Optional[ArchiveSource])
                                 :
        archive_type (Optional[ArchiveType])
                                 :
        history_id (Optional[HistoryId])
                                 : The encoded ID of the history associated with this item.
        name (Optional[Name])    : The name of the creator.
    """

    all_datasets: AllDatasets | None = True
    archive_file: ArchiveFile | None = None
    archive_source: ArchiveSource | None = None
    archive_type: ArchiveType | None = "url"
    history_id: HistoryId | None = None  # The encoded ID of the history associated with this item.
    name: Name | None = None  # The name of the creator.
