from dataclasses import dataclass

from .dataset_source_extra_files_path import DatasetSourceExtraFilesPath
from .dataset_source_transform import DatasetSourceTransform

__all__ = ["DatasetSource"]


@dataclass
class DatasetSource:
    """
    DatasetSource dataclass

    Args:
        id_ (str)                : Encoded ID of the dataset source. (maps from 'id')
        source_uri (str)         : The URI of the dataset source.
        extra_files_path (DatasetSourceExtraFilesPath | None)
                                 : The path to the extra files.
        transform (DatasetSourceTransform | None)
                                 : The transformations applied to the dataset source.
    """

    id_: str  # Encoded ID of the dataset source. (maps from 'id')
    source_uri: str  # The URI of the dataset source.
    extra_files_path: DatasetSourceExtraFilesPath | None = None  # The path to the extra files.
    transform: DatasetSourceTransform | None = None  # The transformations applied to the dataset source.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "extra_files_path": "extra_files_path",
            "id": "id_",
            "source_uri": "source_uri",
            "transform": "transform",
        }
        key_transform_with_dump = {
            "extra_files_path": "extra_files_path",
            "id_": "id",
            "source_uri": "source_uri",
            "transform": "transform",
        }
