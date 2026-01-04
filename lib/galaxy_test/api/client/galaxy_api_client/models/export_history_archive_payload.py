from dataclasses import dataclass

from .directory_uri import DirectoryUri
from .file_name import FileName
from .force import Force
from .gzip import Gzip
from .include_deleted import IncludeDeleted
from .include_hidden import IncludeHidden

__all__ = ["ExportHistoryArchivePayload"]


@dataclass
class ExportHistoryArchivePayload:
    """
    ExportHistoryArchivePayload dataclass.

    Args:
        directory_uri (Optional[DirectoryUri])
                                 : A writable directory destination where the history will
                                   be exported using the `galaxy.files` URI infrastructure.
        file_name (Optional[FileName])
                                 : The full path to the dataset file.
        force (Optional[Force])  : Whether to force a rebuild of the history archive.
        gzip (Optional[Gzip])    : Whether to export as gzip archive.
        include_deleted (Optional[IncludeDeleted])
                                 : Whether to include deleted datasets in the exported
                                   archive.
        include_hidden (Optional[IncludeHidden])
                                 : Whether to include hidden datasets in the exported
                                   archive.
    """

    directory_uri: DirectoryUri | None = (
        None  # A writable directory destination where the history will be exported using the `galaxy.files` URI infrastructure.
    )
    file_name: FileName | None = None  # The full path to the dataset file.
    force: Force | None = None  # Whether to force a rebuild of the history archive.
    gzip: Gzip | None = True  # Whether to export as gzip archive.
    include_deleted: IncludeDeleted | None = False  # Whether to include deleted datasets in the exported archive.
    include_hidden: IncludeHidden | None = False  # Whether to include hidden datasets in the exported archive.
