from dataclasses import dataclass

from .extra_files_path import ExtraFilesPath
from .transform import Transform

__all__ = ["DatasetSource"]


@dataclass
class DatasetSource:
    """
    DatasetSource dataclass.

    Args:
        id_ (str)                : Encoded ID of the dataset source.
        source_uri (str)         : The URI of the dataset source.
        extra_files_path (Optional[ExtraFilesPath])
                                 : The path to the extra files.
        transform (Optional[Transform])
                                 : The transformations applied to the dataset source.
    """

    id_: str  # Encoded ID of the dataset source.
    source_uri: str  # The URI of the dataset source.
    extra_files_path: ExtraFilesPath | None = None  # The path to the extra files.
    transform: Transform | None = None  # The transformations applied to the dataset source.
